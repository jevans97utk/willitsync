"""
"""
import sys
import logging
import click
import click_log
import openapi_client

logger = logging.getLogger(__name__)
click_log.basic_config(logger)

@click.group()
@click_log.simple_verbosity_option(logger)
def main():
    logger.debug("in main()")
    pass


@main.command()
@click.option('-u','--url', required=True, help='Url to try')
def robot(url):
    logger.debug("Calling robot with url = " + str(url))
    print("Robot, url=" + url)


@main.command()
@click.option('-u','--url', required=True, help='Url to try')
@click.option('-x','--maxentries', default=100, help='Maximum number of entries to show')
def sitemap(url, maxentries):
    logger.debug(f'calling sitemap with url={url} and maxentries={maxentries}')


if __name__ == "__main__":
    sys.exit(main())
