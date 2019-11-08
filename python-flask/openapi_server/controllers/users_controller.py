import connexion  # noqa : F401
import six  # noqa : F401

from openapi_server.models.sci_metadata import SCIMetadata  # noqa: E501, F401
from openapi_server import util  # noqa : F401

# local imports


def get_validate_metadata(url, formatid):  # noqa: E501
    """Retrieve and validate a science metadata XML document

    Given a url referencing an XML metadata document, retrieve and validate the XML.  # noqa: E501

    :param url: URL referencing a science metadata XML document to retrieve  and validate.
    :type url: str
    :param formatid: The DataONE formatId of the XML to test for validity.
    :type formatid: str

    :rtype: SCIMetadata
    """
    return 'do some magic!'


def get_validate_so(url, type=None, _type=None, type_=None):  # noqa: E501
    """Retrieve and validate a schema.org JSON-LD document

    Given a url referencing a schema.org JSON-LD document, verify that  the structure matches expected model indicated in the type parameter.  # noqa: E501

    :param url: URL referencing a schema.org JSON-LD document to retrieve and validate.
    :type url: str
    :param type: The name of the schema.org type to test for validity.
    :type type: str

    :rtype: SOMetadata
    """
    return 'do some magic!'


def parse_landing_page(url):  # noqa: E501
    """Extract schema.org metadata

    Parses landing page to extract schema.org metadata  # noqa: E501

    :param url: URL pointing to landing page to be parsed
    :type url: str

    :rtype: SOMetadata
    """
    return 'do some magic!'


def parse_robots(url):  # noqa: E501
    """Parses robots.txt to find sitemap(s)

    Given a robots.txt file, parse, and retrieve referenced sitemap documents.

    :param url: URL pointing to a robots.txt file
    :type url: str

    :rtype: RobotsFile
    """
    return 'do some magic!'


def parse_sitemap(url, maxlocs=None):  # noqa: E501
    """Parses sitemap.xml

    Parses a sitemap to retrieve entries. # noqa: E501

    :param url: URL pointing to a sitemap xml document.
    :type url: str
    :param maxlocs: Maximum number of sitemap locations to return (100)
    :type maxlocs: int

    :rtype: Sitemap
    """
    return 'do some magic!'


def validate_metadata(formatid, body):  # noqa: E501
    """Validate provided schema.org JSON-LD document

    Given an XML metadata document, validate the XML.  # noqa: E501

    :param formatid: The DataONE formatId of the XML to test for validity.
    :type formatid: str
    :param body: Science metadata XML document to validate.
    :type body: str

    :rtype: SCIMetadata
    """
    return 'do some magic!'


def validate_so(body, type=None):  # noqa: E501
    """Validate provided schema.org JSON-LD document

    Given a schema.org JSON-LD document, verify that the structure  matches expected model indicated in the type parameter.  # noqa: E501

    :param body: Schema.org JSON-LD to validate.
    :type body:
    :param type: The name of the schema.org type to test for validity.
    :type type: str

    :rtype: SOMetadata
    """
    return 'do some magic!'
