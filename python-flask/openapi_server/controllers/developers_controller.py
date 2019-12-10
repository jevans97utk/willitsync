import connexion
import six

from openapi_server.models.robots_file import RobotsFile  # noqa: E501
from openapi_server.models.sci_metadata import SCIMetadata  # noqa: E501
from openapi_server.models.so_metadata import SOMetadata  # noqa: E501
from openapi_server.models.sitemap import Sitemap  # noqa: E501
from openapi_server import util
from . import business_logic as bl


def get_validate_metadata(url, formatid):  # noqa: E501
    """Retrieve and validate a science metadata XML document

    Given a URL referencing an XML metadata document, retrieve and validate the XML.  # noqa: E501

    :param url: URL referencing a science metadata XML document to retrieve  and validate. 
    :type url: str
    :param formatid: The DataONE formatId of the XML to test for validity. 
    :type formatid: str

    :rtype: SCIMetadata
    """
    return bl.get_validate_metadata(url, formatid)


def get_validate_so(url, sotype=None):  # noqa: E501
    """Retrieve and validate a schema.org JSON-LD document

    Given a URL referencing a schema.org JSON-LD document, verify that  the structure matches expected model indicated in the type parameter.  # noqa: E501

    :param url: URL referencing a schema.org JSON-LD document or a landing page containing schema.org JSON-LD to retrieve and validate. 
    :type url: str
    :param sotype: The name of the schema.org type to test for validity. 
    :type sotype: str

    :rtype: SOMetadata
    """
    return bl.get_validate_so(url, sotype=sotype)


def parse_landingpage(url):  # noqa: E501
    """Extract schema.org metadata from web page

    Parses landing page to extract schema.org JSON-LD metadata  # noqa: E501

    :param url: URL pointing to langing page to be parsed 
    :type url: str

    :rtype: SOMetadata
    """
    return bl.parse_landing_page(url)


def parse_robots(url):  # noqa: E501
    """Retrieve sitemap references from a robots.txt file

    Given a robots.txt file, parse, and retrieve referenced sitemap locations.  # noqa: E501

    :param url: URL pointing to a robots.txt file
    :type url: str

    :rtype: RobotsFile
    """
    return bl.parse_robots(url)


def parse_sitemap(url, maxlocs=None):  # noqa: E501
    """Get locatiosn from a sitemap.

    Parses a sitemap to retrieve location entries.  # noqa: E501

    :param url: URL pointing to a sitemap xml document
    :type url: str
    :param maxlocs: Maximum number of sitemap locations to return 
    :type maxlocs: int

    :rtype: Sitemap
    """
    return bl.parse_sitemap(url, maxlocs=maxlocs)


def validate_metadata(formatid, body):  # noqa: E501
    """Validate provided science metadata XML document

    Given an XML metadata document, validate the XML.  # noqa: E501

    :param formatid: The DataONE formatId of the XML to test for validity. 
    :type formatid: str
    :param body: Science metadata XML document to validate. 
    :type body: str

    :rtype: SCIMetadata
    """
    return bl.validate_metadata(formatid, body)



def validate_so(body, type_=None):  # noqa: E501
    """Validate provided schema.org JSON-LD document

    Given a schema.org JSON-LD document, verify that the structure  matches expected model indicated in the type parameter.  # noqa: E501

    :param body: Schema.org JSON-LD to validate. 
    :type body: 
    :param type: The name of the schema.org type to test for validity. 
    :type type: str

    :rtype: SOMetadata
    """
    return bl.validate_so(body, type_=type_)
