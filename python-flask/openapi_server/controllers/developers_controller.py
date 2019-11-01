import datetime as dt                                                              
import json                                                                        
import urllib.robotparser   

import connexion
import six

from openapi_server.models.robots_file import RobotsFile  # noqa: E501
from openapi_server import util


def parse_robots(url):  # noqa: E501
    """Parses robots.txt to find sitemap(s)

    By passing in the appropriate options, you can search for available inventory in the system  # noqa: E501

    :param url: URL pointing to a robots.txt file
    :type url: str

    :rtype: List[RobotsFile]
    """
    date = dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

    parser = urllib.robotparser.RobotFileParser()
    parser.set_url(url)
    parser.read()

    r = RobotsFile(url, sitemaps=parser.sitemaps, evaluated_date=date)
    j = [ r.to_dict() ]
    return j
