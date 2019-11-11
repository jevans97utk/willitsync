# coding: utf-8

# standard library imports
from __future__ import absolute_import
import datetime as dt
import importlib.resources as ir
import io
import json
import unittest

# 3rd party library imports
from aioresponses import aioresponses
import dateutil.parser

# Local imports
from openapi_server.models.robots_file import RobotsFile  # noqa: E501, F401
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

        url = 'https://www.archive.arm.gov/metadata/adc/html/nsanimfraod1michC2.c1.html'  # noqa : E501
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

        url = (
            'https://www.archive.arm.gov'
            '/metadata/adc/html/nsanimfraod1michC2.c1.html'
        )
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

        json.load(io.BytesIO(response.data))
        self.assertTrue(True)

    def test_post_validate(self):
        """
        SCENARIO:  We are given a POST request for a valid schema.org JSON-LD
        object.

        EXPECTED RESULT:  The schema.org metadata is returned in the body
        of the response with a 200 status code.
        """
        payload = {}
        payload['url'] = 'http://somewhere.out.there.com'
        payload['evaluated_date'] = dt.datetime \
                                      .utcnow() \
                                      .replace(tzinfo=dt.timezone.utc) \
                                      .isoformat()
        payload['log'] = None
        data = ir.read_binary('openapi_server.test.data.arm',
                              'nsanimfraod1michC2.c1.json')
        metadata = json.load(io.BytesIO(data))
        payload['metadata'] = metadata

        self.setup_requests_patcher(200, data)

        headers = {
            'Accept': 'application/json',
            'Content-type': 'application/json',
        }
        response = self.client.open(
            '/jevans97utk/willitsync/1.0.2/sovalid',
            method='POST',
            headers=headers,
            data=json.dumps(payload),
            content_type='application/json')

        
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        actual = json.load(io.BytesIO(response.data))
        self.assertEqual(actual['metadata'], payload['metadata'])

    def test_post_validate_400(self):
        """
        SCENARIO:  We are given a POST request for an invalid schema.org
        JSON-LD object.

        EXPECTED RESULT:  The schema.org metadata is returned in the body
        of the response with a 400 status code.
        """
        payload = {}
        payload['url'] = 'http://somewhere.out.there.com'
        payload['evaluated_date'] = dt.datetime \
                                      .utcnow() \
                                      .replace(tzinfo=dt.timezone.utc) \
                                      .isoformat()
        payload['log'] = None
        data = ir.read_binary('openapi_server.test.data.arm',
                              'nsanimfraod1michC2.c1.invalid.json')
        metadata = json.load(io.BytesIO(data))
        payload['metadata'] = metadata

        self.setup_requests_patcher(200, data)

        headers = {
            'Accept': 'application/json',
            'Content-type': 'application/json',
        }
        response = self.client.open(
            '/jevans97utk/willitsync/1.0.2/sovalid',
            method='POST',
            headers=headers,
            data=json.dumps(payload),
            content_type='application/json')

        self.assert400(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        actual = json.load(io.BytesIO(response.data))
        self.assertEqual(actual['metadata'], payload['metadata'])

    def test_post_validate__400__invalid_parameter(self):
        """
        SCENARIO:  We are given a POST request for a valid schema.org JSON-LD
        object with an invalid type parameter.

        EXPECTED RESULT:  The schema.org metadata is returned in the body
        of the response with a 400 status code.
        """
        payload = {}
        payload['url'] = 'http://somewhere.out.there.com'
        payload['evaluated_date'] = dt.datetime \
                                      .utcnow() \
                                      .replace(tzinfo=dt.timezone.utc) \
                                      .isoformat()
        payload['log'] = None
        data = ir.read_binary('openapi_server.test.data.arm',
                              'nsanimfraod1michC2.c1.invalid.json')
        metadata = json.load(io.BytesIO(data))
        payload['metadata'] = metadata

        query_string = [('type_', 'notadataset')]

        headers = {
            'Accept': 'application/json',
            'Content-type': 'application/json',
        }
        response = self.client.open(
            '/jevans97utk/willitsync/1.0.2/sovalid',
            method='POST',
            headers=headers,
            data=json.dumps(payload),
            query_string=query_string,
            content_type='application/json')

        self.assert400(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        actual = json.load(io.BytesIO(response.data))
        self.assertEqual(actual['metadata'], payload['metadata'])

    def test_parse_landing_page(self):
        """
        SCENARIO:  A landing page with valid JSON-LD is to be parsed.

        EXPECTED RESULT:  The response body is SOmetadata.
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

        data = json.load(io.BytesIO(response.data))

        self.assertEqual(url, data['url'])

        # can we parse the date?
        dateutil.parser.parse(data['evaluated_date'])

        self.assertTrue('log' in data)

        # can we dump the metadata?
        json.dumps(data['metadata'])

    def test_parse_landing_page_400(self):
        """
        SCENARIO: The SO harvester issues a 400 error when we attempt to
        extract the JSON-LD from the landing page.

        EXPECTED RESULT:  400 error
        """

        url = 'https://www.archive.arm.gov/metadata/html/pghnoaaaosM1.b1.html'
        query_string = [('url', url)]
        headers = {
            'Accept': 'application/json',
        }

        with aioresponses() as m:
            m.get(url, status=400)

            response = self.client.open(
                '/jevans97utk/willitsync/1.0.2/so',
                method='GET',
                headers=headers,
                query_string=query_string)

            message = f"Response body is : {response.data.decode('utf-8')}"
            self.assert400(response, message)

    def test_parse_landing_page_404(self):
        """
        SCENARIO: The SO harvester issues a 404 error when we attempt to

        EXPECTED RESULT:  404 error
        """

        url = 'https://www.archive.arm.gov/metadata/html/pghnoaaaosM1.b1.html'
        query_string = [('url', url)]
        headers = {
            'Accept': 'application/json',
        }

        with aioresponses() as m:
            m.get(url, status=404)

            response = self.client.open(
                '/jevans97utk/willitsync/1.0.2/so',
                method='GET',
                headers=headers,
                query_string=query_string)

            message = f"Response body is : {response.data.decode('utf-8')}"
            self.assert404(response, message)

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

        prefix = "https://www.nytimes.com"
        expected = [
            f"{prefix}/sitemaps/www.nytimes.com/sitemap.xml.gz",
            f"{prefix}/sitemaps/new/news.xml.gz",
            f"{prefix}/sitemaps/sitemap_video/sitemap.xml.gz",
            f"{prefix}/sitemaps/www.nytimes.com_realestate/sitemap.xml.gz",
            f"{prefix}/sitemaps/www.nytimes.com/2016_election_sitemap.xml.gz",
            f"{prefix}/elections/2018/sitemap",
        ]
        actual = json.load(io.BytesIO(response.data))
        self.assertEqual(expected, actual['sitemaps'])

    def test_parse_robots_empty(self):
        """
        SCENARIO:  parse a robots.txt file from NYTIMES that has no sitemaps

        EXPECTED RESPONSE:  200 status code, no sitemaps in an array
        """
        data = ir.read_binary('openapi_server.test.data.nytimes',
                              'robots_no_sitemaps.txt')
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

        expected = []
        actual = json.load(io.BytesIO(response.data))
        self.assertEqual(expected, actual['sitemaps'])

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

        # Setup the mocked return values
        sitemaps = ['https://nytimes.com/sitemap.xml']
        now = dt.datetime.utcnow().replace(tzinfo=dt.timezone.utc)
        sitemaps_urlset = [
            ('https://www.nytimes.com/stuff_happened.html', now),
            ('https://www.nytimes.com/and_then_some.html', now)
        ]
        self.setup_so_patcher(sitemaps=sitemaps,
                              sitemaps_urlset=sitemaps_urlset)

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

        j = json.loads(response.data.decode('utf-8'))

        expected = sitemaps
        self.assertEqual(j['sitemaps'], sitemaps)

        expected = [
            [item[0], item[1].isoformat()] for item in sitemaps_urlset
        ]
        self.assertEqual(j['urlset'], expected)


if __name__ == '__main__':
    unittest.main()
