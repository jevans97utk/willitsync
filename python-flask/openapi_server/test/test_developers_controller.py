# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.robots_file import RobotsFile  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDevelopersController(BaseTestCase):
    """DevelopersController integration test stubs"""

    def test_parse_robots(self):
        """Test case for parse_robots

        Parses robots.txt to find sitemap(s)
        """
        query_string = [('url', 'url_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/datadavev/willitsync/1.0.0/robots',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
