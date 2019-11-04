# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.log_entry import LogEntry
from openapi_server import util

from openapi_server.models.log_entry import LogEntry  # noqa: E501

class SOMetadata(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, url=None, evaluated_date=None, log=None, metadata=None):  # noqa: E501
        """SOMetadata - a model defined in OpenAPI

        :param url: The url of this SOMetadata.  # noqa: E501
        :type url: str
        :param evaluated_date: The evaluated_date of this SOMetadata.  # noqa: E501
        :type evaluated_date: datetime
        :param log: The log of this SOMetadata.  # noqa: E501
        :type log: List[LogEntry]
        :param metadata: The metadata of this SOMetadata.  # noqa: E501
        :type metadata: object
        """
        self.openapi_types = {
            'url': str,
            'evaluated_date': datetime,
            'log': List[LogEntry],
            'metadata': object
        }

        self.attribute_map = {
            'url': 'url',
            'evaluated_date': 'evaluated_date',
            'log': 'log',
            'metadata': 'metadata'
        }

        self._url = url
        self._evaluated_date = evaluated_date
        self._log = log
        self._metadata = metadata

    @classmethod
    def from_dict(cls, dikt) -> 'SOMetadata':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SOMetadata of this SOMetadata.  # noqa: E501
        :rtype: SOMetadata
        """
        return util.deserialize_model(dikt, cls)

    @property
    def url(self):
        """Gets the url of this SOMetadata.

        URL of the landing page that was parsed. If a redirection occurs, then this is the final URL that was used to retrieve the landing page.   # noqa: E501

        :return: The url of this SOMetadata.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SOMetadata.

        URL of the landing page that was parsed. If a redirection occurs, then this is the final URL that was used to retrieve the landing page.   # noqa: E501

        :param url: The url of this SOMetadata.
        :type url: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def evaluated_date(self):
        """Gets the evaluated_date of this SOMetadata.

        The timestamp for when the evaluation the landing page was initiated.   # noqa: E501

        :return: The evaluated_date of this SOMetadata.
        :rtype: datetime
        """
        return self._evaluated_date

    @evaluated_date.setter
    def evaluated_date(self, evaluated_date):
        """Sets the evaluated_date of this SOMetadata.

        The timestamp for when the evaluation the landing page was initiated.   # noqa: E501

        :param evaluated_date: The evaluated_date of this SOMetadata.
        :type evaluated_date: datetime
        """
        if evaluated_date is None:
            raise ValueError("Invalid value for `evaluated_date`, must not be `None`")  # noqa: E501

        self._evaluated_date = evaluated_date

    @property
    def log(self):
        """Gets the log of this SOMetadata.


        :return: The log of this SOMetadata.
        :rtype: List[LogEntry]
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this SOMetadata.


        :param log: The log of this SOMetadata.
        :type log: List[LogEntry]
        """
        if log is None:
            raise ValueError("Invalid value for `log`, must not be `None`")  # noqa: E501

        self._log = log

    @property
    def metadata(self):
        """Gets the metadata of this SOMetadata.

        The schema.org metadata that was retrieved form the landing page   # noqa: E501

        :return: The metadata of this SOMetadata.
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this SOMetadata.

        The schema.org metadata that was retrieved form the landing page   # noqa: E501

        :param metadata: The metadata of this SOMetadata.
        :type metadata: object
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata
