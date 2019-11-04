# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class SitemapUrlset(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, url=None, lastmod=None):  # noqa: E501
        """SitemapUrlset - a model defined in OpenAPI

        :param url: The url of this SitemapUrlset.  # noqa: E501
        :type url: str
        :param lastmod: The lastmod of this SitemapUrlset.  # noqa: E501
        :type lastmod: datetime
        """
        self.openapi_types = {
            'url': str,
            'lastmod': datetime
        }

        self.attribute_map = {
            'url': 'url',
            'lastmod': 'lastmod'
        }

        self._url = url
        self._lastmod = lastmod

    @classmethod
    def from_dict(cls, dikt) -> 'SitemapUrlset':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Sitemap_urlset of this SitemapUrlset.  # noqa: E501
        :rtype: SitemapUrlset
        """
        return util.deserialize_model(dikt, cls)

    @property
    def url(self):
        """Gets the url of this SitemapUrlset.

        The value of the url element of a loc entry in a sitemap.   # noqa: E501

        :return: The url of this SitemapUrlset.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SitemapUrlset.

        The value of the url element of a loc entry in a sitemap.   # noqa: E501

        :param url: The url of this SitemapUrlset.
        :type url: str
        """

        self._url = url

    @property
    def lastmod(self):
        """Gets the lastmod of this SitemapUrlset.

        The value of the lastmod element of the loc entry.   # noqa: E501

        :return: The lastmod of this SitemapUrlset.
        :rtype: datetime
        """
        return self._lastmod

    @lastmod.setter
    def lastmod(self, lastmod):
        """Sets the lastmod of this SitemapUrlset.

        The value of the lastmod element of the loc entry.   # noqa: E501

        :param lastmod: The lastmod of this SitemapUrlset.
        :type lastmod: datetime
        """

        self._lastmod = lastmod
