import datetime as dt
import io
import json

import connexion
import six
import requests
from reppy.robots import Robots
import lxml.etree

from openapi_server.models.robots_file import RobotsFile  # noqa: E501
from openapi_server.models.so_metadata import SOMetadata  # noqa: E501
from openapi_server.models.sitemap import Sitemap  # noqa: E501
from openapi_server import util


def parse_langingpage(url):  # noqa: E501
    """Extract schema.org metadata

    Parses landing page to extract schema.org metadata  # noqa: E501

    :param url: URL pointing to landing page to be parsed 
    :type url: str

    :rtype: SOMetadata
    """
    date = dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

    jsonld = extract_jsonld(url)

    kwargs = {
        'url': url,
        'evaluated_date': date,
        'log': None, 
        'metadata': None,
    }
    so_obj = SOMetadata(**kwargs)
    return so_obj.to_dict()


def extract_jsonld(url):
    r = requests.get(url)
    doc = lxml.etree.HTML(r.text)
    path = './/script[@type="application/ld+json"]'
    scripts = doc.xpath(path)

    jsonld = None
    for script in scripts:
        j = json.loads(script.text)
        if '@type' in j and j['@type'] == 'Dataset':
            jsonld = j

    return jsonld


def parse_robots(url):  # noqa: E501
    """Parses robots.txt to find sitemap(s)

    Given a robots.txt file, parse, and retrieve referenced sitemap documents.  # noqa: E501

    :param url: URL pointing to a robots.txt file
    :type url: str

    :rtype: RobotsFile
    """
    date = dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

    robots = Robots.fetch(url)

    r = RobotsFile(url, sitemaps=robots.sitemaps, evaluated_date=date)
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
