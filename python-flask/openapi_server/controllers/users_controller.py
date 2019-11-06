import connexion
import requests
import six

from openapi_server.models.robots_file import RobotsFile  # noqa: E501
from openapi_server.models.so_metadata import SOMetadata  # noqa: E501
from openapi_server.models.sitemap import Sitemap  # noqa: E501
from openapi_server import util

# local imports
from . import business_logic as bl


def parse_landing_page(url):  # noqa: E501
    """Extract schema.org metadata

    Parses landing page to extract schema.org metadata  # noqa: E501

    :param url: URL pointing to landing page to be parsed 
    :type url: str

    :rtype: SOMetadata
    """
    try:
        date, jsonld, logs = bl.parse_landing_page(url)
    except Exception as e:  # noqa:  F841
        if hasattr(e, 'message') and hasattr(e, 'status'):
            # It looks like a requests/aiohttp exception
            return e.message, e.status

        # Anything else, return a 400
        return str(e), 400

    kwargs = {
        'url': url,
        'evaluated_date': date,
        'log': logs,
        'metadata': jsonld,
    }
    so_obj = SOMetadata(**kwargs)
    return so_obj.to_dict(), 200


def parse_robots(url):  # noqa: E501
    """Parses robots.txt to find sitemap(s)

    Given a robots.txt file, parse, and retrieve referenced sitemap documents.

    :param url: URL pointing to a robots.txt file
    :type url: str

    :rtype: RobotsFile
    """
    try:
        date, sitemaps = bl.parse_robots(url)
    except Exception as e:
        return e.response.text, e.response.status_code
    else:
        r = RobotsFile(url, sitemaps=sitemaps, evaluated_date=date)
        j = [r.to_dict()]
        return j, 200


def parse_sitemap(url, maxlocs=None):  # noqa: E501
    """Parses sitemap.xml

    Parses a sitemap to retrieve entries. # noqa: E501

    :param url: URL pointing to a sitemap xml document.
    :type url: str
    :param maxlocs: Maximum number of sitemap locations to return (100) 
    :type maxlocs: int

    :rtype: Sitemap
    """
    return 'do some magic!'
