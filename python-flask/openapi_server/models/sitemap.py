# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.log_entry import LogEntry
from openapi_server.models.sitemap_urlset import SitemapUrlset
from openapi_server import util

from openapi_server.models.log_entry import LogEntry  # noqa: E501
from openapi_server.models.sitemap_urlset import SitemapUrlset  # noqa: E501

class Sitemap(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, sitemaps=None, evaluated_date=None, log=None, urlset=None):  # noqa: E501
        """Sitemap - a model defined in OpenAPI

        :param sitemaps: The sitemaps of this Sitemap.  # noqa: E501
        :type sitemaps: List[str]
        :param evaluated_date: The evaluated_date of this Sitemap.  # noqa: E501
        :type evaluated_date: datetime
        :param log: The log of this Sitemap.  # noqa: E501
        :type log: List[LogEntry]
        :param urlset: The urlset of this Sitemap.  # noqa: E501
        :type urlset: List[SitemapUrlset]
        """
        self.openapi_types = {
            'sitemaps': List[str],
            'evaluated_date': datetime,
            'log': List[LogEntry],
            'urlset': List[SitemapUrlset]
        }

        self.attribute_map = {
            'sitemaps': 'sitemaps',
            'evaluated_date': 'evaluated_date',
            'log': 'log',
            'urlset': 'urlset'
        }

        self._sitemaps = sitemaps
        self._evaluated_date = evaluated_date
        self._log = log
        self._urlset = urlset

    @classmethod
    def from_dict(cls, dikt) -> 'Sitemap':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Sitemap of this Sitemap.  # noqa: E501
        :rtype: Sitemap
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sitemaps(self):
        """Gets the sitemaps of this Sitemap.

        List of sitemap URLs that were examined. The zeroth item is always the URL provided in the request.   # noqa: E501

        :return: The sitemaps of this Sitemap.
        :rtype: List[str]
        """
        return self._sitemaps

    @sitemaps.setter
    def sitemaps(self, sitemaps):
        """Sets the sitemaps of this Sitemap.

        List of sitemap URLs that were examined. The zeroth item is always the URL provided in the request.   # noqa: E501

        :param sitemaps: The sitemaps of this Sitemap.
        :type sitemaps: List[str]
        """
        if sitemaps is None:
            raise ValueError("Invalid value for `sitemaps`, must not be `None`")  # noqa: E501

        self._sitemaps = sitemaps

    @property
    def evaluated_date(self):
        """Gets the evaluated_date of this Sitemap.

        The timestamp for when the evaluation of sitemaps.xml was initiated.   # noqa: E501

        :return: The evaluated_date of this Sitemap.
        :rtype: datetime
        """
        return self._evaluated_date

    @evaluated_date.setter
    def evaluated_date(self, evaluated_date):
        """Sets the evaluated_date of this Sitemap.

        The timestamp for when the evaluation of sitemaps.xml was initiated.   # noqa: E501

        :param evaluated_date: The evaluated_date of this Sitemap.
        :type evaluated_date: datetime
        """
        if evaluated_date is None:
            raise ValueError("Invalid value for `evaluated_date`, must not be `None`")  # noqa: E501

        self._evaluated_date = evaluated_date

    @property
    def log(self):
        """Gets the log of this Sitemap.


        :return: The log of this Sitemap.
        :rtype: List[LogEntry]
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this Sitemap.


        :param log: The log of this Sitemap.
        :type log: List[LogEntry]
        """
        if log is None:
            raise ValueError("Invalid value for `log`, must not be `None`")  # noqa: E501

        self._log = log

    @property
    def urlset(self):
        """Gets the urlset of this Sitemap.

        A list of location entries retieved from the sitemap. Includes locations obtained from referenced sitemaps, if any.   # noqa: E501

        :return: The urlset of this Sitemap.
        :rtype: List[SitemapUrlset]
        """
        return self._urlset

    @urlset.setter
    def urlset(self, urlset):
        """Sets the urlset of this Sitemap.

        A list of location entries retieved from the sitemap. Includes locations obtained from referenced sitemaps, if any.   # noqa: E501

        :param urlset: The urlset of this Sitemap.
        :type urlset: List[SitemapUrlset]
        """
        if urlset is None:
            raise ValueError("Invalid value for `urlset`, must not be `None`")  # noqa: E501

        self._urlset = urlset