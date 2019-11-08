# standard library imports
import asyncio
import datetime as dt
import json
import logging

# 3rd party library imports
import requests
from schema_org.so_core import SchemaDotOrgHarvester

# local imports
from openapi_server.models.log_entry import LogEntry
from openapi_server.models.so_metadata import SOMetadata


# Common keyword arguments to always be fed to the SchemaDotOrg processor.
_KWARGS = {
    'log_to_string': True,
    'log_to_stdout': False,
    'log_to_json': True,
    'no_harvest': True,
    'ignore_harvest_time': True,
}


def get_current_utc_timestamp():
    return dt.datetime.utcnow() \
             .replace(tzinfo=dt.timezone.utc) \
             .isoformat(timespec='milliseconds')


def get_validate_so(url, type='Dataset'):
    """
    Business logic for using schema.org to validate a landing page.

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

    Returns
    -------
    SOMetadata, HTTP status code
    """
    so_obj, status = parse_landing_page(url)
    return so_obj, status


def parse_sitemap(url):
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

    obj = SchemaDotOrgHarvester(sitemap_url=url, **_KWARGS)
    asyncio.run(obj.run())

    sitemaps = obj.get_sitemaps()
    urlset = obj.get_sitemaps_urlset()
    logs = obj.get_log_messages()

    return sitemaps, date, logs, urlset


def parse_robots(url):
    """
    Parses robots.txt to find sitemap(s)

    Given a robots.txt file, parse, and retrieve referenced sitemap documents.

    Parameters
    ----------
    url : str
        URL pointing to a robots.txt file
    """
    date = get_current_utc_timestamp()

    r = requests.get(url)
    r.raise_for_status()

    sitemaps = []
    for line in r.text.splitlines():
        if 'Sitemap:' in line:
            sitemaps.append(line.split(': ')[1])

    return date, sitemaps


def parse_landing_page(url):
    """
    Business logic for using schema_org to parse a landing page.

    Returns
    -------
    SOMetadata, HTTP status code
    """
    # Assume a 200 status code until we know otherwise.
    return_status = 200

    date = get_current_utc_timestamp()

    obj = SchemaDotOrgHarvester(sitemap_url=url, **_KWARGS)

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
        logs = obj.get_log_messages()
        logs = _post_process_logs(logs)

    kwargs = {
        'url': url,
        'evaluated_date': date,
        'log': logs,
        'metadata': jsonld,
    }
    so_metadata = SOMetadata(**kwargs)

    return so_metadata, return_status


def _post_process_logs(logs):
    """
    Put the already-JSON-formatted log entries into the expected form.

    Parameters
    ----------
    logs : str
        Single string of log entries.

    Returns
    -------
    array of LogEntry objects
    """
    log_items = json.loads(logs)

    logs = []
    for entry in log_items:

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
