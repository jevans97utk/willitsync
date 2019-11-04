import datetime as dt
import json
import urllib.robotparser

import connexion
import six

from openapi_server.models.robots_file import RobotsFile  # noqa: E501
from openapi_server.models.so_metadata import SOMetadata  # noqa: E501
from openapi_server.models.sitemap import Sitemap  # noqa: E501
from openapi_server import util


def parse_langingpage(url):  # noqa: E501
    """Extract schema.org metadata

    Parses landing page to extract schema.org metadata  # noqa: E501

    :param url: URL pointing to langing page to be parsed 
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

    parser = urllib.robotparser.RobotFileParser()
    parser.set_url(url)
    parser.read()

    r = RobotsFile(url, sitemaps=parser.sitemaps, evaluated_date=date)
    j = [ r.to_dict() ]
    return j


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
