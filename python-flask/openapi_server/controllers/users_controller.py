import datetime as dt
import json

import connexion
import requests
import six
from reppy.robots import Robots

from openapi_server.models.robots_file import RobotsFile  # noqa: E501
from openapi_server.models.so_metadata import SOMetadata  # noqa: E501
from openapi_server.models.sitemap import Sitemap  # noqa: E501
from openapi_server import util


def parse_landing_page(url):  # noqa: E501
    """Extract schema.org metadata

    Parses landing page to extract schema.org metadata  # noqa: E501

    :param url: URL pointing to landing page to be parsed 
    :type url: str

    :rtype: SOMetadata
    """
    return 'do some magic!'


def parse_robots(url):  # noqa: E501
    """Parses robots.txt to find sitemap(s)

    Given a robots.txt file, parse, and retrieve referenced sitemap documents.

    :param url: URL pointing to a robots.txt file
    :type url: str

    :rtype: RobotsFile
    """
    date = dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

    r = requests.get(url)
    if r.status_code == 400:
        return 'Bad request', 400
    elif r.status_code == 404:
        return 'Document not found', 404

    robots = Robots.fetch(url)

    r = RobotsFile(url, sitemaps=robots.sitemaps, evaluated_date=date)
    j = [ r.to_dict() ]
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
