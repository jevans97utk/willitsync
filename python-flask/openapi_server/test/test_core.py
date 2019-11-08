# Standard library imports
import collections
from unittest.mock import patch

# 3rd party library imports
import requests
from openapi_server.test import BaseTestCase

Response = collections.namedtuple('Response', ['status_code', 'text'])


class MockRequestsGet(object):
    """
    Mock out the actions of the response of a requests.get operation.

    Attributes
    ----------
    content, text, status_code
        These correspond to the same items in a requests.Response object
    """
    def __init__(self, content=None, status_code=200):
        """
        Parameters
        ----------
        content
            binary sequence
        """

        self.content = content

        try:
            self.text = content.decode('utf-8')
        except (AttributeError, UnicodeDecodeError):
            self.text = ''

        self.status_code = status_code

    def raise_for_status(self):
        """
        Mock out the following sequence of events.

        >>> r = requests.get(bad url)
        >>> r.raise_for_status()
        """
        if self.status_code == 200:
            return
        else:
            response = Response(self.status_code, 'something went wrong')
            raise requests.HTTPError(response=response)


class MockSchemaDotOrgHarvester(object):
    def __init__(self, content=None, jsonld=None, logs=None, sitemaps=None,
                 sitemaps_urlset=None):
        self.content = content
        self.jsonld = jsonld
        self.logs = logs
        self.sitemaps = sitemaps
        self.sitemaps_urlset = sitemaps_urlset

    def get_sitemaps(self):
        """
        Corresponds to get_sitemaps method in SchemaDotOrgHarvester
        """
        if self.sitemaps is None:
            return []
        else:
            return self.sitemaps

    def get_sitemaps_urlset(self):
        """
        Corresponds to get_sitemaps_urlset method in SchemaDotOrgHarvester
        """
        if self.sitemaps_urlset is None:
            return []
        else:
            return self.sitemaps_urlset

    def get_log_messages(self):
        if self.logs is None:
            return ['Stuff happened']
        else:
            return self.logs

    def get_jsonld(self, url):
        if isinstance(self.jsonld, Exception):
            raise self.jsonld

        return self.jsonld

    async def retrieve_landing_page_content(self, url):
        if isinstance(self.content, Exception):
            raise self.content

        return self.content

    async def run(self):
        pass


class WillItSyncTestCase(BaseTestCase):
    """
    Both the developers and users controller test cases use the same test
    setup and teardown code.
    """

    def startUp(self):

        if hasattr(self, 'requests_patcher'):
            self.requests_patcher.stop()

        if hasattr(self, 'so_patcher'):
            self.so_patcher.stop()

    def tearDown(self):

        if hasattr(self, 'requests_patcher'):
            self.requests_patcher.stop()

        if hasattr(self, 'so_patcher'):
            self.so_patcher.stop()

    def setup_requests_patcher(self, status_code, content):

        side_effect = [
            MockRequestsGet(content=content, status_code=status_code)
        ]

        patchee = 'openapi_server.controllers.business_logic.requests.get'
        self.requests_patcher = patch(patchee, side_effect=side_effect)

        self.requests_patcher.start()

    def setup_so_patcher(self, **kwargs):
        """
        Setup the schema.org patcher.

        Parameters
        ----------
        jsonld
            JSON to be returned by get_jsonld method
        content : binary sequene
            binary content to be returned by retrieve_landing_page_content
            method
        sitemaps : list
            List of leaf sitemap URLs assumed visited by the harvester
        sitemaps_urlset : list
            List of landing pages and lastmod times assumed to be harvested.
        """

        side_effect = [
            MockSchemaDotOrgHarvester(**kwargs)
        ]

        patchee = 'openapi_server.controllers.business_logic.SchemaDotOrgHarvester'  # noqa : E501
        self.so_patcher = patch(patchee, side_effect=side_effect)

        self.so_patcher.start()
