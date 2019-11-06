# coding: utf-8

from __future__ import absolute_import
import importlib.resources as ir
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.robots_file import RobotsFile  # noqa: E501
from openapi_server.models.so_metadata import SOMetadata  # noqa: E501
from openapi_server.models.sitemap import Sitemap  # noqa: E501
from openapi_server.test import BaseTestCase
from .test_core import MockRequestsGet, WillItSyncTestCase


class TestUsersController(WillItSyncTestCase):
    """UsersController integration test stubs"""

    def test_parse_langingpage(self):
        """Test case for parse_langingpage

        Extract schema.org metadata
        """
        testfile = 'valid_schema_dot_org.json'
        text = ir.read_text('openapi_server.test.data', testfile)
        data = json.loads(text)
        self.setup_so_patcher(jsonld=data)

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

    def test_parse_langingpage_400(self):
        """Test case for parse_langingpage where an exception is thrown.

        EXPECTED RESULT:  400 error
        """
        self.setup_so_patcher(jsonld=RuntimeError('bad stuff happened'))

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
        self.assert400(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_parse_langingpage_404(self):
        """Test case for parse_langingpage where the URL doesn't exist

        EXPECTED RESULT:  404 error
        """
        e = Exception()
        e.message = 'bad stuff happened'
        e.status = 404
        self.setup_so_patcher(content=e)

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
        self.assert404(response,
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
