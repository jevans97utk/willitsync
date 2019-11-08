# coding: utf-8

from __future__ import absolute_import
import datetime as dt
import importlib.resources as ir
import io
import json
import unittest

import dateutil.parser
import dateutil.tz
# from flask import json
# from six import BytesIO

# from openapi_server.models.robots_file import RobotsFile  # noqa: E501
# from openapi_server.models.so_metadata import SOMetadata  # noqa: E501
# from openapi_server.models.sitemap import Sitemap  # noqa: E501
# from openapi_server.test import BaseTestCase
from .test_core import WillItSyncTestCase


class TestUsersController(WillItSyncTestCase):
    """UsersController integration test stubs"""


if __name__ == '__main__':
    unittest.main()
