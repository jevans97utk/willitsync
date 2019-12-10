"""
"""
# Standard library imports
import datetime as dt
import json
import sys
import logging
from pprint import pprint

# 3rd party library imports
import click
import click_log
import lxml.etree
import openapi_client

# Local imports
from schema_org.so_core import SchemaDotOrgHarvester

logger = logging.getLogger(__name__)
click_log.basic_config(logger)


@click.group()
@click.pass_context
@click_log.simple_verbosity_option(logger)
def main(ctx):
    logger.debug("in main()")
    ctx.ensure_object(dict)
    configuration = openapi_client.configuration.Configuration()
    configuration.host = "http://localhost:8080/willitsync/1.1.1"
    client = openapi_client.ApiClient(configuration)
    ctx.obj['client'] = openapi_client.DevelopersApi(client)


@main.command()
@click.pass_context
@click.option('-u', '--url', required=True, help='Url to try')
@click.option('-f', '--formatid', required=False,
              default="http://www.isotc211.org/2005/gmd",
              help="ID for metadata standard")
def get_scivalid(ctx, url, formatid):
    msg = (
        f"Calling get_validate_metadata with url = {url} and with "
        f"format ID = {formatid}."
    )
    logger.debug(msg)
    result = ctx.obj['client'].get_validate_metadata(url, formatid)
    pprint(result)


@main.command()
@click.pass_context
@click.option('--file', type=click.Path(exists=True), required=True,
              help='Path to local file (landing page)')
@click.option('--formatid', required=True,
              help="ID for metadata standard")
def scivalid(ctx, file, formatid):
    msg = (
        f"Calling validate_metadata with file = {file} and with "
        f"format ID = {formatid}."
    )
    logger.debug(msg)

    with open(file, mode='rt') as f:
        txt = f.read()

    result = ctx.obj['client'].validate_metadata(formatid, txt)
    pprint(result)


@main.command()
@click.pass_context
@click.option('-u', '--url', required=True,
              help='URL of landing page to try')
def get_so(ctx, url):
    msg = f"Calling parse_landing_page with url = {url}"
    logger.debug(msg)
    result = ctx.obj['client'].parse_landingpage(url)
    pprint(result)


@main.command()
@click.pass_context
@click.option('-u', '--url', required=True, help='Url to try')
def robot(ctx, url):
    logger.debug("Calling robot with url = " + str(url))
    result = ctx.obj['client'].parse_robots(url)
    pprint(result)


@main.command()
@click.pass_context
@click.option('-u', '--url', required=True, help='Url to try')
@click.option('-x', '--maxentries', default=100,
              help=(
                  'Maximum number of entries to show, default is 100, '
                  'use -1 to retrieve all.'
              ))
def sitemap(ctx, url, maxentries):
    logger.debug(f'calling sitemap with url={url} and maxentries={maxentries}')
    result = ctx.obj['client'].parse_sitemap(url, maxlocs=maxentries)
    pprint(result)


@main.command()
@click.pass_context
@click.option('-u', '--url', required=True, help='Url to try')
def get_sovalid(ctx, url):
    logger.debug(f'Calling so with url = {url}')
    result = ctx.obj['client'].get_validate_so(url)
    pprint(result)


@main.command()
@click.pass_context
@click.option('-f', '--file', type=click.Path(exists=True), required=True,
              help='Path to local file (landing page or JSON-LD')
@click.option('-s', '--sotype', required=False, default="Dataset",
              help=(
                  "The name of the schema.org type to test for validity "
                  "(default is \"Dataset\")"
              ))
def sovalid(ctx, file, sotype):
    msg = (
        f"Calling validate_so with file = {file} and with "
        f"sotype = {sotype}."
    )
    logger.debug(msg)


    with open(file, mode='rt') as f:
        text = f.read()

    try:
        data = json.loads(text)
    except:
        # Assume it is HTML.
        data = text

    body = {
        'evaluated_date': dt.datetime.now(),
        'log': None,
        'url': '',
        'metadata': data,
    }
    result = ctx.obj['client'].validate_so(body, type=sotype)
    pprint(result)




if __name__ == "__main__":
    res = main(obj={})
    print(f"RESULT = {res}")
    sys.exit(res)
