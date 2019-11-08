# coding: utf-8

"""
    WillItSync

    Sitemap Checker  # noqa: E501

    The version of the OpenAPI document: 1.1.1
    Contact: jevans97@utk.edu
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Sitemap(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'sitemaps': 'list[str]',
        'evaluated_date': 'datetime',
        'log': 'list[LogEntry]',
        'urlset': 'list[SitemapUrlset]'
    }

    attribute_map = {
        'sitemaps': 'sitemaps',
        'evaluated_date': 'evaluated_date',
        'log': 'log',
        'urlset': 'urlset'
    }

    def __init__(self, sitemaps=None, evaluated_date=None, log=None, urlset=None):  # noqa: E501
        """Sitemap - a model defined in OpenAPI"""  # noqa: E501

        self._sitemaps = None
        self._evaluated_date = None
        self._log = None
        self._urlset = None
        self.discriminator = None

        self.sitemaps = sitemaps
        self.evaluated_date = evaluated_date
        self.log = log
        self.urlset = urlset

    @property
    def sitemaps(self):
        """Gets the sitemaps of this Sitemap.  # noqa: E501

        List of sitemap URLs that were examined. The zeroth item is always the URL provided in the request.   # noqa: E501

        :return: The sitemaps of this Sitemap.  # noqa: E501
        :rtype: list[str]
        """
        return self._sitemaps

    @sitemaps.setter
    def sitemaps(self, sitemaps):
        """Sets the sitemaps of this Sitemap.

        List of sitemap URLs that were examined. The zeroth item is always the URL provided in the request.   # noqa: E501

        :param sitemaps: The sitemaps of this Sitemap.  # noqa: E501
        :type: list[str]
        """
        if sitemaps is None:
            raise ValueError("Invalid value for `sitemaps`, must not be `None`")  # noqa: E501

        self._sitemaps = sitemaps

    @property
    def evaluated_date(self):
        """Gets the evaluated_date of this Sitemap.  # noqa: E501

        The timestamp for when the evaluation of sitemaps.xml was initiated.   # noqa: E501

        :return: The evaluated_date of this Sitemap.  # noqa: E501
        :rtype: datetime
        """
        return self._evaluated_date

    @evaluated_date.setter
    def evaluated_date(self, evaluated_date):
        """Sets the evaluated_date of this Sitemap.

        The timestamp for when the evaluation of sitemaps.xml was initiated.   # noqa: E501

        :param evaluated_date: The evaluated_date of this Sitemap.  # noqa: E501
        :type: datetime
        """
        if evaluated_date is None:
            raise ValueError("Invalid value for `evaluated_date`, must not be `None`")  # noqa: E501

        self._evaluated_date = evaluated_date

    @property
    def log(self):
        """Gets the log of this Sitemap.  # noqa: E501


        :return: The log of this Sitemap.  # noqa: E501
        :rtype: list[LogEntry]
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this Sitemap.


        :param log: The log of this Sitemap.  # noqa: E501
        :type: list[LogEntry]
        """
        if log is None:
            raise ValueError("Invalid value for `log`, must not be `None`")  # noqa: E501

        self._log = log

    @property
    def urlset(self):
        """Gets the urlset of this Sitemap.  # noqa: E501

        A list of location entries retieved from the sitemap. Includes locations obtained from referenced sitemaps, if any.   # noqa: E501

        :return: The urlset of this Sitemap.  # noqa: E501
        :rtype: list[SitemapUrlset]
        """
        return self._urlset

    @urlset.setter
    def urlset(self, urlset):
        """Sets the urlset of this Sitemap.

        A list of location entries retieved from the sitemap. Includes locations obtained from referenced sitemaps, if any.   # noqa: E501

        :param urlset: The urlset of this Sitemap.  # noqa: E501
        :type: list[SitemapUrlset]
        """
        if urlset is None:
            raise ValueError("Invalid value for `urlset`, must not be `None`")  # noqa: E501

        self._urlset = urlset

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Sitemap):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
