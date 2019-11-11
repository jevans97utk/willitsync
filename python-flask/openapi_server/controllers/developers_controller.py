# Standard library imports

# import connexion
# import six

# from openapi_server.models.log_entry import LogEntry
from openapi_server.models.robots_file import RobotsFile
# from openapi_server.models.sci_metadata import SCIMetadata
from openapi_server.models.sitemap import Sitemap
# from openapi_server import util

from . import business_logic as bl


def get_validate_metadata(url, formatid):  # noqa: E501
    """Retrieve and validate a science metadata XML document

    Given a url referencing an XML metadata document, retrieve and validate the
    XML.

    Parameters
    ----------
    url : str
        URL referencing a science metadata XML document to retrieve and
        validate.
    formatid : str
        The DataONE formatId of the XML to test for validity.

    Returns
    -------
    SCIMetadata
    """
    return 'do some magic!'


def get_validate_so(url, **kwargs):  # noqa: E501
    """Retrieve and validate a schema.org JSON-LD document

    Given a url referencing a schema.org JSON-LD document, verify that
    the structure matches expected model indicated in the type parameter.  This
    corresponds to the /sovalid endpoint.

    Parameters
    ----------
    url : str
        URL referencing a schema.org JSON-LD document to retrieve and validate.
    type : str
        The name of the schema.org type to test for validity.

    Returns
    -------
    SOMetadata
    """
    type = 'Dataset'
    for key in kwargs:
        if 'type' in key:
            type = kwargs[key]

    if type != 'Dataset':
        return 'Invalid type parameter', 400

    so_obj, status = bl.get_validate_so(url, type=type)
    return so_obj, 200


def parse_langingpage(url):  # noqa: E501
    """Extract schema.org metadata

    Parses landing page to extract schema.org metadata  # noqa: E501

    :param url: URL pointing to landing page to be parsed
    :type url: str

    :rtype: SOMetadata
    """
    return bl.parse_landing_page(url)


def parse_robots(url):
    """
    Parses robots.txt to find sitemap(s).  This corresponds to the /robots
    endpoint.

    Given a robots.txt file, parse, and retrieve referenced sitemap documents.

    :param url: URL pointing to a robots.txt file
    :type url: str

    :rtype: RobotsFile
    """
    robots_file, status = bl.parse_robots(url)
    return robots_file, status


def parse_sitemap(url, maxlocs=None):  # noqa: E501
    """Parses sitemap.xml

    Parses a sitemap to retrieve entries.

    Parameters
    ----------
    url : str
        URL pointing to a sitemap xml document.
    maxlocs : int
        Maximum number of sitemap locations to return (100)

    Returns
    -------
    Sitemap, HTTP status code
    """
    sitemap, status_code = bl.parse_sitemap(url, maxlocs=maxlocs)
    return sitemap, status_code

    try:
        sitemaps, date, logs, urlset = bl.parse_sitemap(url)
    except Exception as e:
        return e.response.text, e.response.status_code
    else:
        kwargs = {
            'sitemaps': sitemaps,
            'evaluated_date': date,
            'log': logs,
            'urlset': urlset,
        }
        s = Sitemap(**kwargs)
        return s, 200


def validate_metadata(formatid, body):
    """Validate provided schema.org JSON-LD document

    Given an XML metadata document, validate the XML.  # noqa: E501

    :param formatid: The DataONE formatId of the XML to test for validity.
    :type formatid: str
    :param body: Science metadata XML document to validate.
    :type body: str

    :rtype: SCIMetadata
    """
    return 'do some magic!'


def validate_so(body, type=None):  # noqa: E501
    """Validate provided schema.org JSON-LD document

    Given a schema.org JSON-LD document, verify that the structure
    matches expected model indicated in the type parameter.

    :param body: Schema.org JSON-LD to validate.
    :type body:
    :param type: The name of the schema.org type to test for validity.
    :type type: str

    :rtype: SOMetadata
    """
    return 'do some magic!'
