# standard library imports
import asyncio
import datetime as dt

# 3rd party library imports
import requests
from schema_org.so_core import SchemaDotOrgHarvester

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


def parse_landing_page(url):

    date = dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    jsonld, logs = extract_jsonld(url)
    return date, jsonld, logs


def extract_jsonld(url):
    """
    Given a URL of a landing page, extract an existing JSON-LD element if it
    exists.

    Returns
    -------
    jsonld : object
        deserialized JSON object
    logs
    """
    obj = SchemaDotOrgHarvester(log_to_string=True, log_to_stdout=False)
    doc = asyncio.run(obj.retrieve_landing_page_content(url))
    jsonld = obj.extract_jsonld_from_landing_page(doc)
    obj.jsonld_validator.check(jsonld)

    logs = obj.extract_log_messages()

    return jsonld, logs


