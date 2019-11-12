# standard library imports
import asyncio
import datetime as dt
import io
import json
import logging
import time

# 3rd party library imports
import lxml.etree
import requests
from schema_org.so_core import SchemaDotOrgHarvester
from pythonjsonlogger import jsonlogger
import d1_scimeta.validate

# local imports
from openapi_server.models.log_entry import LogEntry
from openapi_server.models.robots_file import RobotsFile
from openapi_server.models.sitemap import Sitemap
from openapi_server.models.sci_metadata import SCIMetadata
from openapi_server.models.so_metadata import SOMetadata


# Common keyword arguments to always be fed to the SchemaDotOrg processor.
_KWARGS = {
    'no_harvest': True,
    'ignore_harvest_time': True,
}


def get_current_utc_timestamp():
    """
    Utility for creating a timestamp that is usable by javascript / JSON.
    """
    return dt.datetime.utcnow() \
             .replace(tzinfo=dt.timezone.utc) \
             .isoformat(timespec='milliseconds')


def get_validate_metadata(url, formatid):
    """Retrieve and validate a science metadata XML document

    Given a url referencing an XML metadata document, retrieve and validate the
    XML.  This corresponds to the /scimeta GET endpoint.

    Parameters
    ----------
    url : str
        URL referencing a science metadata XML document to retrieve and
        validate.
    formatid : str
        The DataONE formatId of the XML to test for validity.

    Returns
    -------
    SCIMetadata, HTTP status_code
    """
    date = get_current_utc_timestamp()
    logobj = CustomJsonLogger()

    obj = SchemaDotOrgHarvester(logger=logobj.logger, **_KWARGS)

    kwargs = {
        'url': url,
        'evaluated_date': date,
        'log': None,
        'metadata': None,
    }
    # Try to get the document
    try:
        content = asyncio.run(obj.retrieve_url(url))
    except Exception as e:

        logobj.logger.error(str(e))
        logs = logobj.get_log_messages()

        kwargs['log'] = logs
        scimetadata = SCIMetadata(**kwargs)

        # The error status is most likely a 404?
        if hasattr(e, 'message') and hasattr(e, 'status'):
            return_status = 404
        else:
            return_status = 400
        return scimetadata, return_status

    # Decode the document.
    try:
        doc = lxml.etree.parse(io.BytesIO(content))
    except Exception as e:
        logobj.logger.error(str(e))
        logs = logobj.get_log_messages()
        kwargs['log'] = logs
        scimetadata = SCIMetadata(**kwargs)
        return scimetadata, 400
    else:
        # So we know we have a valid XML document now.
        kwargs['metadata'] = lxml.etree.tostring(doc).decode('utf-8')

    # And finally, validate.
    try:
        d1_scimeta.validate.assert_valid(formatid, doc)
    except Exception as e:
        logobj.logger.error(str(e))
        return_status = 400
    finally:
        kwargs['log'] = logobj.get_log_messages()
        scimetadata = SCIMetadata(**kwargs)
        return_status = 200
        return scimetadata, return_status


def validate_so(body, type_=None):
    """
    Business logic for validating a (hopefully) dataone Schema.org JSON-LD
    document.

    Returns
    -------
    SOMetadata, HTTP status code
    """
    date = get_current_utc_timestamp()
    j = body['metadata']

    logobj = CustomJsonLogger()

    if type_ != 'Dataset':
        msg = f"Unsupported SO JSON-LD type \"{type_}\""
        logobj.logger.error(msg)
        logs = logobj.get_log_messages()
    else:
        obj = SchemaDotOrgHarvester(sitemap_url=None, logger=logobj.logger,
                                    **_KWARGS)

        try:
            obj.validate_dataone_so_jsonld(j)
        except Exception as e:
            # Log the exception.
            obj.logger.error(str(e))
            return_status = 400
        else:
            return_status = 200
        finally:
            # Always retrieve the logs no matter what.
            logs = logobj.get_log_messages()

    kwargs = {
        'url': None,
        'evaluated_date': date,
        'log': logs,
        'metadata': j,
    }
    so_metadata = SOMetadata(**kwargs)

    return so_metadata, return_status


def get_validate_so(url, type_=None):
    """
    Business logic for using schema_org to parse a landing page.

    Returns
    -------
    SOMetadata, HTTP status code
    """
    logobj = CustomJsonLogger()
    date = get_current_utc_timestamp()
    jsonld = None

    if type_ != 'Dataset':

        msg = f'Unsupported SO JSON-LD type {type_}.'
        logobj.logger.error(msg)
        logs = logobj.get_log_messages()
        return_status = 400

    else:

        obj = SchemaDotOrgHarvester(sitemap_url=url, logger=logobj.logger,
                                    **_KWARGS)

        try:
            doc = asyncio.run(obj.retrieve_landing_page_content(url))
            jsonld = obj.get_jsonld(doc)
            obj.validate_dataone_so_jsonld(jsonld)

        except Exception as e:

            # Log the exception.
            obj.logger.error(str(e))

            # JSON-LD cannot be retrieved if the landing page cannot be
            # retrieved.
            jsonld = None

            # Try to get the return status from the exception.  Possibly 400?
            # Possibly 404?
            if hasattr(e, 'message') and hasattr(e, 'status'):
                return_status = e.status
            else:
                # Some other exception?
                return_status = 500

        else:
            return_status = 200
        finally:

            # Always retrieve the logs no matter what.
            logs = logobj.get_log_messages()

    kwargs = {
        'url': url,
        'evaluated_date': date,
        'log': logs,
        'metadata': jsonld,
    }
    so_metadata = SOMetadata(**kwargs)

    return so_metadata, return_status


def parse_sitemap(url, maxlocs=None):
    """
    Business logic for using schema_org to process sitemaps.

    Parameters
    ----------
    url : str
        URL pointing to a sitemap

    Returns
    -------
    sitemaps
        list of all sitemap URLs on the web site
    date
        datetime of this request
    logs
        list of log entries for this operation
    urlset
        list of tuples consisting of a landing page URL and the last modified
        time of the landing page
    """
    date = get_current_utc_timestamp()
    logobj = CustomJsonLogger()

    obj = SchemaDotOrgHarvester(sitemap_url=url, logger=logobj.logger,
                                num_documents=maxlocs, **_KWARGS)
    asyncio.run(obj.run())

    sitemaps = obj.get_sitemaps()
    urlset = obj.get_sitemaps_urlset()

    logs = logobj.get_log_messages()
    return_status = logobj.get_return_status()

    kwargs = {
        'sitemaps': sitemaps,
        'evaluated_date': date,
        'log': logs,
        'urlset': urlset,
    }
    s = Sitemap(**kwargs)
    return s, return_status


def parse_robots(url):
    """
    Parses robots.txt to find sitemap(s)

    Given a robots.txt file, parse, and retrieve referenced sitemap documents.

    Parameters
    ----------
    url : str
        URL pointing to a robots.txt file
    """
    # Setup default values
    sitemaps = None
    return_status = 200

    logobj = CustomJsonLogger()
    logobj.logger.info('parse_robots:...')

    date = get_current_utc_timestamp()

    r = requests.get(url)

    try:
        r.raise_for_status()
    except Exception as e:
        logobj.logger.error(str(e))
        return_status = r.status_code
    else:
        sitemaps = []
        for line in r.text.splitlines():
            if 'Sitemap:' in line:
                sitemaps.append(line.split(': ')[1])
    finally:
        log = logobj.get_log_messages()

    r = RobotsFile(url, sitemaps=sitemaps, log=log, evaluated_date=date)
    return r, return_status


def parse_landing_page(url):
    """
    Business logic for using schema_org to parse a landing page.

    Returns
    -------
    SOMetadata, HTTP status code
    """
    # Assume a 200 status code until we know otherwise.
    return_status = 200
    logobj = CustomJsonLogger()

    date = get_current_utc_timestamp()

    obj = SchemaDotOrgHarvester(sitemap_url=url, logger=logobj.logger,
                                **_KWARGS)

    try:
        doc = asyncio.run(obj.retrieve_landing_page_content(url))

    except Exception as e:

        # Log the exception.
        obj.logger.error(str(e))

        # JSON-LD cannot be retrieved if the landing page cannot be retrieved.
        jsonld = None

        # Try to get the return status from the exception.  Possibly 400?
        # Possibly 404?
        if hasattr(e, 'message') and hasattr(e, 'status'):
            return_status = e.status
        else:
            # Some other exception?
            return_status = 500

    else:

        jsonld = obj.get_jsonld(doc)

    finally:

        # Always retrieve the logs no matter what.
        logs = logobj.get_log_messages()

    kwargs = {
        'url': url,
        'evaluated_date': date,
        'log': logs,
        'metadata': jsonld,
    }
    so_metadata = SOMetadata(**kwargs)

    return so_metadata, return_status


class CustomJsonLogger(object):
    """
    The SchemaDotOrg harvester has a logger, but we don't use it for all
    operations, so we use a simplified version here.
    """

    def __init__(self):

        self._json_formatted_log_items = None

        self.logger = logging.getLogger('dataone')
        self.logger.setLevel(logging.INFO)

        self.logstrings = io.StringIO()
        stream = logging.StreamHandler(self.logstrings)

        format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = jsonlogger.JsonFormatter(format)

        # Use UTC, and fix the millisecond format so that javaScript can use
        # it
        formatter.default_msec_format = '%s.%03d'
        formatter.converter = time.gmtime

        stream.setFormatter(formatter)

        self.logger.addHandler(stream)

    def post_process(self):
        """
        If log_to_string was specified as a constructor keyword argument, all
        the log entries are stored in the "_logstrings" attribute, making them
        recoverable.

        Returns
        -------
        JSON array of log entries
        """
        s = self.logstrings.getvalue()

        # Right now it is single string whose log entries are
        # newline-terminated.  Change that to
        # comma-and-then-newline-terminated.
        log_entries = s.splitlines()
        s = f"[{','.join(log_entries)}]"

        # Turn into actual JSON and massage into the proper form.
        self._json_formatted_log_items = json.loads(s)

    def get_log_messages(self):
        """
        If log_to_string was specified as a constructor keyword argument, all
        the log entries are stored in the "_logstrings" attribute, making them
        recoverable.

        Returns
        -------
        JSON array of log entries
        """
        if self._json_formatted_log_items is None:
            self.post_process()

        logs = []
        for entry in self._json_formatted_log_items:

            # "msg" instead of "message"
            entry['msg'] = entry.pop('message')

            # "level" is an int
            entry['level'] = getattr(logging, entry.pop('levelname'))

            # "timestamp" instead of "asctime" with Z tacked onto the end to
            # designate UTC.
            entry['timestamp'] = f"{entry.pop('asctime')}Z"

            # Get rid of the name of the logger.
            entry.pop('name')

            logs.append(LogEntry(**entry))

        return logs

    def get_return_status(self):
        """
        Go thru the list of log entries.  If any of the 'levelname' values
        are ERROR, set the return status to 400.
        """
        if self._json_formatted_log_items is None:
            self.post_process()

        # Assume all is ok until we know otherwise.
        return_status = 200

        for log_entry in self._json_formatted_log_items:
            if log_entry['levelname'] == 'ERROR':
                return_status = 400
        return return_status
