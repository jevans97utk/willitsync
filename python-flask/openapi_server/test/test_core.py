# Standard library imports
from unittest.mock import patch

# 3rd party library imports
import requests
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


class WillItSyncTestCase(BaseTestCase):
    """
    Both the developers and users controller test cases use the same test
    setup and teardown code.
    """

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
