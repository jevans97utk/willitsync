# standard library imports
import asyncio
import datetime as dt

# 3rd party library imports
import requests
from schema_org.so_core import SchemaDotOrgHarvester


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
    """
    date, jsonld, logs = parse_landing_page(url)
    return date, jsonld, logs


def parse_sitemap(url):
    """
    Business logic for using schema_org to process sitemaps.

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

    kwargs = {
        'log_to_string': True,
        'log_to_stdout': False,
        'no_harvest': True,
        'ignore_harvest_time': True,
        'sitemap_url': url,
    }
    obj = SchemaDotOrgHarvester(**kwargs)
    asyncio.run(obj.run())

    sitemaps = obj.get_sitemaps()
    urlset = obj.get_sitemaps_urlset()

    logs = obj.extract_log_messages()

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
    date
        datetime of this request
    jsonld
        JSON corresonding to JSON-LD script element
    logs
        list of log entries for this operation
    """
    date = get_current_utc_timestamp()

    obj = SchemaDotOrgHarvester(log_to_string=True, log_to_stdout=False)
    doc = asyncio.run(obj.retrieve_landing_page_content(url))
    jsonld = obj.get_jsonld(doc)

    logs = obj.extract_log_messages()

    return date, jsonld, logs
