"""
"""
import sys
import logging
import click
import click_log
import openapi_client
from pprint import pprint

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
def get_validate_metadata(ctx, url, formatid):
    msg = (
        f"Calling get_validate_metadata with url = {url} and with "
        f"format ID = {formatid}."
    )
    logger.debug(msg)
    result = ctx.obj['client'].get_validate_metadata(url, formatid)
    pprint(result)


@main.command()
@click.pass_context
@click.option('-u', '--url', required=True, help='Url to try')
@click.option('-s', '--sotype', required=False, default="Dataset",
              help="The name of the schema.org type to test for validity.")
def get_validate_so(ctx, url, sotype):
    msg = (
        f"Calling get_validate_so with url = {url} and with "
        f"sotype = {sotype}."
    )
    logger.debug(msg)
    result = ctx.obj['client'].get_validate_so(url, sotype=sotype)
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
@click.option('-u', '--url', required=True, help='URL of landing page to try')
def so(ctx, url):
    logger.debug(f'Calling so with url = {url}')
    result = ctx.obj['client'].parse_landingpage(url)
    pprint(result)


@main.command()
@click.pass_context
@click.option('-u', '--url', required=True, help='Url to try')
def sovalid(ctx, url):
    logger.debug(f'Calling so with url = {url}')
    result = ctx.obj['client'].get_validate_so(url)
    pprint(result)


if __name__ == "__main__":
    res = main(obj={})
    print(f"RESULT = {res}")
    sys.exit(res)
