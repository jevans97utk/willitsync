# standard library imports
import unittest

# local imports
from openapi_server.controllers.business_logic import CustomJsonLogger


class TestSuite(unittest.TestCase):

    def test_return_status_200(self):
        """
        SCENARIO:  The logger does not record an error.

        EXPECTED RESULT:  The get_return_status routine returns 200.
        """

        logobj = CustomJsonLogger()

        logobj.logger.info('Testing...')

        self.assertEqual(logobj.get_return_status(), 200)

    def test_return_status_400(self):
        """
        SCENARIO:  The logger records an error.

        EXPECTED RESULT:  The get_return_status routine returns 400.
        """

        logobj = CustomJsonLogger()

        logobj.logger.info('Testing...')
        logobj.logger.error('something bad happened')

        self.assertEqual(logobj.get_return_status(), 400)
