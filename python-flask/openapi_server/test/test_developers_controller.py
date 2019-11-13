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
import requests_mock
import dateutil.parser

# Local imports
from openapi_server.models.robots_file import RobotsFile
from openapi_server.models.sci_metadata import SCIMetadata
from openapi_server.models.so_metadata import SOMetadata
from .test_core import WillItSyncTestCase


class TestDevelopersController(WillItSyncTestCase):
    """DevelopersController integration test stubs"""

    def test_get_validate_metadata(self):
        """
        SCENARIO:  We are given a valid URL leading to a valid metadata
        document, along with aa valid formatID.

        EXPECTED RESULT:  A 200 status code.  We can load the response body
        into a SCIMetadata object.
        """
        url = 'https://www.archive.arm.gov/metadata/adc/html/nsaqcrad1longC2.c2.xml'  # noqa : E501

        content = ir.read_binary('openapi_server.test.data.arm',
                                 'nsaqcrad1longC2.c2.xml')

        query_string = [
            ('url', url),
            ('formatid', 'http://www.isotc211.org/2005/gmd')
        ]

        request_headers = {
            'Accept': 'application/json',
        }

        with aioresponses() as m:
            response_headers = {'Content-Type': 'text/xml'}
            m.get(url, body=content, headers=response_headers, status=200)

            response = self.client.open(
                '/jevans97utk/willitsync/1.0.2/scivalid',
                method='GET',
                headers=request_headers,
                query_string=query_string)

        text = response.data.decode('utf-8')
        self.assert200(response, 'Response body is : ' + text)

        # Verify that we can form an SOMetadata object out of the reponse
        j = json.loads(text)
        SCIMetadata(*j)
        self.assertTrue(True)

    def test_get_validate_metadata_404(self):
        """
        SCENARIO:  We are given an invalid URL for the XML metadata document.

        EXPECTED RESULT:  A 404 status code.  We can load the response body
        into a SCIMetadata object.
        """
        url = 'https://www.archive.arm.gov/metadata/adc/html/nsaqcrad1longC2.c2.xml'  # noqa : E501

        content = ir.read_binary('openapi_server.test.data.arm',
                                 'nsaqcrad1longC2.c2.xml')

        query_string = [
            ('url', url),
            ('formatid', 'http://www.isotc211.org/2005/gmd')
        ]

        headers = {
            'Accept': 'application/json',
        }

        with aioresponses() as m:
            m.get(url, status=404)

            response = self.client.open(
                '/jevans97utk/willitsync/1.0.2/scivalid',
                method='GET',
                headers=headers,
                query_string=query_string)

        text = response.data.decode('utf-8')
        self.assert404(response, 'Response body is : ' + text)

        # Verify that we can form an SOMetadata object out of the reponse
        j = json.loads(text)
        SCIMetadata(*j)
        self.assertTrue(True)

    def test_get_validate_metadata__invalid_xml__400(self):
        """
        SCENARIO:  We are given a valid URL for an invalid XML metadata
        document.

        EXPECTED RESULT:  A 400 status code.  We can load the response body
        into a SCIMetadata object.
        """
        url = 'https://www.archive.arm.gov/metadata/adc/html/nsaqcrad1longC2.c2.xml'  # noqa : E501

        content = ir.read_binary('openapi_server.test.data.arm',
                                 'nsaqcrad1longC2.c2.invalid.xml')

        query_string = [
            ('url', url),
            ('formatid', 'http://www.isotc211.org/2005/gmd')
        ]

        headers = {
            'Accept': 'application/json',
        }

        with aioresponses() as m:
            m.get(url, body=content, status=200)

            response = self.client.open(
                '/jevans97utk/willitsync/1.0.2/scivalid',
                method='GET',
                headers=headers,
                query_string=query_string)

        text = response.data.decode('utf-8')
        self.assert400(response, 'Response body is : ' + text)

        # Verify that we can form an SOMetadata object out of the reponse
        j = json.loads(text)
        SCIMetadata(*j)
        self.assertTrue(True)

    def test_get_validate_metadata__invalid_format_id__400(self):
        """
        SCENARIO:  We are given a valid URL for an XML metadata document that
        is not valid for the given ID.

        EXPECTED RESULT:  A 400 status code.  We can load the response body
        into a SCIMetadata object.
        """
        url = 'https://www.archive.arm.gov/metadata/adc/html/nsaqcrad1longC2.c2.xml'  # noqa : E501

        content = ir.read_binary('openapi_server.test.data.dryad.v3p1',
                                 'example.xml')

        query_string = [
            ('url', url),
            ('formatid', 'http://www.isotc211.org/2005/gmd')
        ]

        headers = {
            'Accept': 'application/json',
        }

        with aioresponses() as m:
            m.get(url, body=content, status=200)

            response = self.client.open(
                '/jevans97utk/willitsync/1.0.2/scivalid',
                method='GET',
                headers=headers,
                query_string=query_string)

        text = response.data.decode('utf-8')
        self.assert400(response, 'Response body is : ' + text)

        # Verify that we can form an SOMetadata object out of the reponse
        j = json.loads(text)
        SCIMetadata(*j)
        self.assertTrue(True)

    def test_get_validate_so__bad_type(self):
        """
        SCENARIO:  We are given a GET request for a schema.org landing page
        that has valid JSON-LD, but an invalid type argument is given.

        EXPECTED RESULT:  A 400 status code and an SOMetadata object in the
        reponse body.
        """
        data = ir.read_binary('openapi_server.test.data.arm',
                              'nsanimfraod1michC2.c1.html')
        self.setup_requests_patcher(200, data)

        url = 'https://www.archive.arm.gov/metadata/adc/html/nsanimfraod1michC2.c1.html'  # noqa : E501
        query_string = [('url', url), ('type', 'Wrong')]
        request_headers = {
            'Accept': 'application/json',
        }

        with aioresponses() as m:
            response_headers = {'Content-Type': 'text/html'}
            m.get(url, headers=response_headers, status=404)

            response = self.client.open(
                '/jevans97utk/willitsync/1.0.2/sovalid',
                method='GET',
                headers=request_headers,
                query_string=query_string)

        text = response.data.decode('utf-8')
        self.assert400(response, 'Response body is : ' + text)

        # Verify that we can form an SOMetadata object out of the reponse
        j = json.loads(text)
        SOMetadata(*j)
        self.assertTrue(True)

    def test_get_validate_so__json__no_type(self):
        """
        SCENARIO:  We are given a GET request for a schema.org JSON-LD
        document that is valid.  No type is given.

        EXPECTED RESULT:  The schema.org metadata is returned in the body
        of the response with a 200 status code.
        """
        data = ir.read_binary('openapi_server.test.data.arm',
                              'nsanimfraod1michC2.c1.json')

        url = (
            'https://www.archive.arm.gov'
            '/metadata/adc/json/nsanimfraod1michC2.c1.json'
        )
        query_string = [('url', url)]
        headers = {
            'Accept': 'application/json',
        }

        with aioresponses() as m:
            response_headers = {'Content-type': 'application/json'}
            m.get(url, body=data, headers=response_headers, status=200)

            response = self.client.open(
                '/jevans97utk/willitsync/1.0.2/sovalid',
                method='GET',
                headers=headers,
                query_string=query_string)

        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        json.load(io.BytesIO(response.data))
        self.assertTrue(True)

    def test_get_validate_so__json__404(self):
        """
        SCENARIO:  We are given a GET request for a schema.org JSON-LD
        document that is not present.  No type is given.

        EXPECTED RESULT:   404 status code.
        """
        data = ir.read_binary('openapi_server.test.data.arm',
                              'nsanimfraod1michC2.c1.json')

        url = (
            'https://www.archive.arm.gov'
            '/metadata/adc/json/nsanimfraod1michC2.c1.json'
        )
        query_string = [('url', url)]
        headers = {
            'Accept': 'application/json',
        }

        with aioresponses() as m:
            m.get(url, body=data, status=404)

            response = self.client.open(
                '/jevans97utk/willitsync/1.0.2/sovalid',
                method='GET',
                headers=headers,
                query_string=query_string)

        self.assert404(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        json.load(io.BytesIO(response.data))
        self.assertTrue(True)

    def test_get_validate_so__json__not_jsonld__no_type(self):
        """
        SCENARIO:  We are given a GET request for a JSON-LD document that is 
        not SO JSON-LDv.  No type is given.

        EXPECTED RESULT:  The JSON document is returned in the body of the
        response with a 400 status code.
        """
        j = ['foo', {'bar': ['baz', None, 1.0, 2]}]
        s = json.dumps(j)
        data = s.encode('utf-8')

        url = (
            'https://www.archive.arm.gov'
            '/metadata/adc/json/nsanimfraod1michC2.c1.json'
        )
        query_string = [('url', url)]
        headers = {
            'Accept': 'application/json',
        }

        with aioresponses() as m:
            response_headers = {'Content-type': 'application/json'}
            m.get(url, body=data, headers=response_headers, status=200)

            response = self.client.open(
                '/jevans97utk/willitsync/1.0.2/sovalid',
                method='GET',
                headers=headers,
                query_string=query_string)

        self.assert400(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        # Make sure that the returned content is the same as what was sent.
        actual = json.load(io.BytesIO(response.data))
        self.assertEqual(actual['metadata'], j)

    def test_get_validate_so__html__no_type(self):
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
        query_string = [('url', url)]
        headers = {
            'Accept': 'application/json',
        }

        with aioresponses() as m:
            response_headers = {'Content-type': 'text/html'}
            m.get(url, body=data, headers=response_headers, status=200)

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

    def test_post_validate__type_is_bad(self):
        """
        SCENARIO:  We are given a POST request for a valid schema.org JSON-LD
        object, but the type parameter is bad.

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
                              'nsanimfraod1michC2.c1.json')
        metadata = json.load(io.BytesIO(data))
        payload['metadata'] = metadata

        self.setup_requests_patcher(200, data)

        headers = {
            'Accept': 'application/json',
            'Content-type': 'application/json',
        }
        query_string = [('type', 'Wrong')]
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

    def test_post_validate__content_not_json__400(self):
        """
        SCENARIO:  We are given a POST request with a body that is not JSON.

        EXPECTED RESULT:  The metadata field is empty.  The response is a 400.
        """
        payload = {}
        payload['url'] = 'http://somewhere.out.there.com'
        payload['evaluated_date'] = dt.datetime \
                                      .utcnow() \
                                      .replace(tzinfo=dt.timezone.utc) \
                                      .isoformat()
        payload['log'] = None

        # The metadata is not JSON.
        data = '<stuff>wrong</stuff>'
        payload['metadata'] = '<stuff>wrong</stuff>'

        self.setup_requests_patcher(200, data)

        # We'll try to fake JSON, though.
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

    def test_post_validate__invalid_so__400(self):
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

        EXPECTED RESULT:  The response code is 200 and the response body is
        SOmetadata.
        """
        data = ir.read_binary('openapi_server.test.data.arm',
                              'pghnoaaaosM1.b1.html')

        # This is the landing page supposedly to be parsed.
        url = 'https://www.archive.arm.gov/metadata/html/pghnoaaaosM1.b1.html'
        query_string = [('url', url)]
        headers = {
            'Accept': 'application/json',
        }

        with aioresponses() as m:
            response_headers = {'Content-Type': 'text/html'}
            m.get(url, body=data, headers=response_headers, status=200)

            response = self.client.open(
                '/jevans97utk/willitsync/1.0.2/so',
                method='GET',
                headers=headers,
                query_string=query_string)

            msg = f"Response body is : {response.data.decode('utf-8')}"
            self.assert200(response, msg)

        data = json.load(io.BytesIO(response.data))

        self.assertEqual(url, data['url'])

        # can we parse the date?
        dateutil.parser.parse(data['evaluated_date'])

        self.assertTrue('log' in data)

        # can we dump the metadata?
        json.dumps(data['metadata'])

    def test_parse_landing_page_no_jsonld(self):
        """
        SCENARIO:  A landing page without valid JSON-LD is to be parsed.

        EXPECTED RESULT:  The response code is 200 and the response body is
        SOmetadata but there is no metadata.
        """
        data = ir.read_binary('openapi_server.test.data.arm',
                              'nsanimfraod1michC2.c1.no_jsonld.html')

        # This is the landing page supposedly to be parsed.
        url = 'https://www.archive.arm.gov/metadata/html/nsanimfraod1michC2.c1.html'
        query_string = [('url', url)]
        headers = {
            'Accept': 'application/json',
        }

        with aioresponses() as m:
            response_headers = {'Content-Type': 'text/html'}
            m.get(url, body=data, headers=response_headers, status=200)

            response = self.client.open(
                '/jevans97utk/willitsync/1.0.2/so',
                method='GET',
                headers=headers,
                query_string=query_string)

            msg = f"Response body is : {response.data.decode('utf-8')}"
            self.assert400(response, msg)

        data = json.load(io.BytesIO(response.data))

        self.assertEqual(url, data['url'])

        # can we parse the date?
        dateutil.parser.parse(data['evaluated_date'])

        self.assertTrue('log' in data)

        # No metadata is returned, because there was no JSON-LD.
        self.assertFalse('metadata' in data)

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
        SCENARIO: We are given a URL that does not exist.

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

    def test_parse_landing_page__uknown_binary(self):
        """
        SCENARIO: We are given a URL that returns PNG binary content.

        EXPECTED RESULT:  LXML errors out, causing a 400 error.  There is no
        metadata returned.
        """

        url = 'https://www.archive.arm.gov/metadata/html/pghnoaaaosM1.b1.html'
        query_string = [('url', url)]
        headers = {
            'Accept': 'application/json',
        }

        with aioresponses() as m:
            body = b'\x89\x00P\x00N\x00G\x00\r\x00\n\x00\x1a\x00\n\x00'
            m.get(url, body=body, status=200)

            response = self.client.open(
                '/jevans97utk/willitsync/1.0.2/so',
                method='GET',
                headers=headers,
                query_string=query_string)

        message = f"Response body is : {response.data.decode('utf-8')}"
        self.assert400(response, message)

        data = response.data.decode('utf-8')
        j = json.loads(data)
        self.assertFalse('metadata' in j)

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
