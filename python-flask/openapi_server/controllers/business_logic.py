# standard library imports
import datetime as dt

# 3rd party library imports
import requests


def parse_robots(url):
    """Parses robots.txt to find sitemap(s)

    Given a robots.txt file, parse, and retrieve referenced sitemap documents.

    :param url: URL pointing to a robots.txt file
    :type url: str
    """
    date = dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

    r = requests.get(url)
    r.raise_for_status()

    sitemaps = []
    for line in r.text.splitlines():
        if 'Sitemap:' in line:
            sitemaps.append(line.split(': ')[0])

    return date, sitemaps
