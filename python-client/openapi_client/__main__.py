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
    configuration.host = "http://localhost:8080/jevans97utk/willitsync/1.0.2"
    client = openapi_client.ApiClient(configuration)
    ctx.obj['client'] = openapi_client.DevelopersApi(client)


@main.command()
@click.pass_context
@click.option('-u','--url', required=True, help='Url to try')
def robot(ctx, url):
    logger.debug("Calling robot with url = " + str(url))
    result = ctx.obj['client'].parse_robots(url)
    pprint(result)
    


@main.command()
@click.pass_context
@click.option('-u','--url', required=True, help='Url to try')
@click.option('-x','--maxentries', default=100, help='Maximum number of entries to show')
def sitemap(ctx, url, maxentries):
    logger.debug(f'calling sitemap with url={url} and maxentries={maxentries}')


if __name__ == "__main__":
    res = main(obj={})
    print(f"RESULT = {res}")
    sys.exit(res)
