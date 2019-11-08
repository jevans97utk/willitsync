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


class SOMetadata(object):
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
        'url': 'str',
        'evaluated_date': 'datetime',
        'log': 'list[LogEntry]',
        'metadata': 'object'
    }

    attribute_map = {
        'url': 'url',
        'evaluated_date': 'evaluated_date',
        'log': 'log',
        'metadata': 'metadata'
    }

    def __init__(self, url=None, evaluated_date=None, log=None, metadata=None):  # noqa: E501
        """SOMetadata - a model defined in OpenAPI"""  # noqa: E501

        self._url = None
        self._evaluated_date = None
        self._log = None
        self._metadata = None
        self.discriminator = None

        self.url = url
        self.evaluated_date = evaluated_date
        self.log = log
        self.metadata = metadata

    @property
    def url(self):
        """Gets the url of this SOMetadata.  # noqa: E501

        URL of the content that was parsed. If a redirection occurs, then this is the final URL that was used to retrieve the content.   # noqa: E501

        :return: The url of this SOMetadata.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SOMetadata.

        URL of the content that was parsed. If a redirection occurs, then this is the final URL that was used to retrieve the content.   # noqa: E501

        :param url: The url of this SOMetadata.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def evaluated_date(self):
        """Gets the evaluated_date of this SOMetadata.  # noqa: E501

        The timestamp for when the evaluation the landing page was initiated.   # noqa: E501

        :return: The evaluated_date of this SOMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._evaluated_date

    @evaluated_date.setter
    def evaluated_date(self, evaluated_date):
        """Sets the evaluated_date of this SOMetadata.

        The timestamp for when the evaluation the landing page was initiated.   # noqa: E501

        :param evaluated_date: The evaluated_date of this SOMetadata.  # noqa: E501
        :type: datetime
        """
        if evaluated_date is None:
            raise ValueError("Invalid value for `evaluated_date`, must not be `None`")  # noqa: E501

        self._evaluated_date = evaluated_date

    @property
    def log(self):
        """Gets the log of this SOMetadata.  # noqa: E501


        :return: The log of this SOMetadata.  # noqa: E501
        :rtype: list[LogEntry]
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this SOMetadata.


        :param log: The log of this SOMetadata.  # noqa: E501
        :type: list[LogEntry]
        """
        if log is None:
            raise ValueError("Invalid value for `log`, must not be `None`")  # noqa: E501

        self._log = log

    @property
    def metadata(self):
        """Gets the metadata of this SOMetadata.  # noqa: E501

        The schema.org metadata that was retrieved.   # noqa: E501

        :return: The metadata of this SOMetadata.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this SOMetadata.

        The schema.org metadata that was retrieved.   # noqa: E501

        :param metadata: The metadata of this SOMetadata.  # noqa: E501
        :type: object
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata

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
        if not isinstance(other, SOMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
