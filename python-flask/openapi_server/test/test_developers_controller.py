# coding: utf-8

from __future__ import absolute_import
import importlib.resources as ir
import io
import unittest

from flask import json
import requests_mock
from six import BytesIO

from openapi_server.models.robots_file import RobotsFile  # noqa: E501
from openapi_server.test import BaseTestCase
from .test_core import WillItSyncTestCase


class TestDevelopersController(WillItSyncTestCase):
    """DevelopersController integration test stubs"""

    def test_get_validate_so__bad_type(self):
        """
        SCENARIO:  We are given a GET request for a schema.org landing page
        that has valid JSON-LD, but an invalid type argument is given.

        EXPECTED RESULT:  A 400 status code
        """
        data = ir.read_binary('openapi_server.test.data.arm',
                              'nsanimfraod1michC2.c1.html')
        self.setup_requests_patcher(200, data)

        url = 'https://www.archive.arm.gov/metadata/adc/html/nsanimfraod1michC2.c1.html'
        query_string = [('url', url), ('type', 'Wrong')]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/jevans97utk/willitsync/1.0.2/sovalid',
            method='GET',
            headers=headers,
            query_string=query_string)

        text = response.data.decode('utf-8')
        self.assert400(response, 'Response body is : ' + text)

        self.assertIn('Invalid type parameter', text)

    def test_get_validate_so__no_type(self):
        """
        SCENARIO:  We are given a GET request for a schema.org landing page
        that has valid JSON-LD.  No type argument is given.

        EXPECTED RESULT:  The schema.org metadata is returned in the body
        of the response with a 200 status code.
        """
        data = ir.read_binary('openapi_server.test.data.arm',
                              'nsanimfraod1michC2.c1.html')
        self.setup_requests_patcher(200, data)

        url = 'https://www.archive.arm.gov/metadata/adc/html/nsanimfraod1michC2.c1.html'
        # query_string = [('url', url), ('type', 'Dataset')]
        query_string = [('url', url)]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/jevans97utk/willitsync/1.0.2/sovalid',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        j = json.load(io.BytesIO(response.data))
        self.assertTrue(True)

    def test_parse_robots(self):
        """
        SCENARIO:  parse a robots.txt file from NYTIMES

        EXPECTED RESPONSE:  200 status code, 6 sitemaps in an array
        """
        data = ir.read_binary('openapi_server.test.data.nytimes',
                              'robots.txt')
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

        expected = [
            "https://www.nytimes.com/sitemaps/www.nytimes.com/sitemap.xml.gz",
            "https://www.nytimes.com/sitemaps/new/news.xml.gz",
            "https://www.nytimes.com/sitemaps/sitemap_video/sitemap.xml.gz",
            "https://www.nytimes.com/sitemaps/www.nytimes.com_realestate/sitemap.xml.gz",
            "https://www.nytimes.com/sitemaps/www.nytimes.com/2016_election_sitemap.xml.gz",
            "https://www.nytimes.com/elections/2018/sitemap",
        ]
        actual = json.load(io.BytesIO(response.data))
        self.assertEqual(expected, actual['sitemaps'])



if __name__ == '__main__':
    unittest.main()
