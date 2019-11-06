# coding: utf-8

from __future__ import absolute_import
import importlib.resources as ir
import unittest
from unittest.mock import patch

from flask import json
from six import BytesIO

from openapi_server.models.robots_file import RobotsFile  # noqa: E501
from openapi_server.models.so_metadata import SOMetadata  # noqa: E501
from openapi_server.models.sitemap import Sitemap  # noqa: E501
from openapi_server.test import BaseTestCase


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
        if self.status_code != 200:
            raise requests.HTTPError('bad url')


class TestUsersController(BaseTestCase):
    """UsersController integration test stubs"""

    def tearDown(self):

        if hasattr(self, 'requests_patcher'):
            self.requests_patcher.stop()

    def setup_requests_patcher(self, status_code, content):

        side_effect = [
            MockRequestsGet(content=content, status_code=status_code)
        ]

        patchee = 'openapi_server.controllers.users_controller.requests.get'
        self.requests_patcher = patch(patchee, side_effect=side_effect)

        self.requests_patcher.start()

    def test_parse_langingpage(self):
        """Test case for parse_langingpage

        Extract schema.org metadata
        """
        url = 'https://www.archive.arm.gov/metadata/html/pghnoaaaosM1.b1.html'
        query_string = [('url', url)]
        headers = {
            'Accept': 'application/json',
        }

        response = self.client.open(
            '/jevans97utk/willitsync/1.0.2/so',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_parse_robots(self):
        """Test case for parse_robots

        Parses robots.txt to find sitemap(s)
        """
        data = ir.read_binary('openapi_server.test.data', 'robots_nytimes.txt')
        self.setup_requests_patcher(200, data)

        query_string = [('url', 'https://nytimes.com/robots.txt')]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/jevans97utk/willitsync/1.0.2/robots',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_parse_robots_400(self):
        """Test case for parse_robots when the robots file does not exist.
        """
        self.setup_requests_patcher(400, b'')

        query_string = [('url', 'https://nytimes.com/robots.txt')]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/jevans97utk/willitsync/1.0.2/robots',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert400(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_parse_robots_404(self):
        """Test case for parse_robots when the robots file does not exist.
        """
        self.setup_requests_patcher(404, b'')

        query_string = [('url', 'https://nytimes.com/robots.txt')]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/jevans97utk/willitsync/1.0.2/robots',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert404(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_parse_sitemap(self):
        """Test case for parse_sitemap

        Parses sitemap.xml
        """
        query_string = [('url', 'url_example'),
                        ('maxlocs', 56)]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/jevans97utk/willitsync/1.0.2/sitemap',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
