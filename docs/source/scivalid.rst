===================================
Validating an XML Metadata Document
===================================

An XML document may be validated via either a ``GET`` operation if the document is available via a URL, or perhaps more conveniently with a ``POST`` operation if the document is available on a local filesystem.

*****
Usage
*****

::

    $ willitsync get-scivalid --help
    Usage: willitsync get-scivalid [OPTIONS]
    
    Options:
      -u, --url TEXT       Url to try  [required]
      -f, --formatid TEXT  ID for metadata standard
      --help               Show this message and exit.

*******
Example
*******

Suppose we try with a URL, but incorrectly use the landing page URL instead of the URL for the metadata document.  The response body
will show the log messages at the INFO level::

    $ willitsync get-scivalid -u https://www.archive.arm.gov/metadata/adc/html/wsacrcrcal.html -f http://www.isotc211.org/2005/gmd
    Traceback (most recent call last):
    .
    .
    .
    [traceback omitted]
    .
    .
    .
    openapi_client.exceptions.ApiException: (400)
    Reason: BAD REQUEST
    HTTP response headers: HTTPHeaderDict({'Content-Type': 'application/json', 'Content-Length': '505', 'Server': 'Werkzeug/0.16.0 Python/3.7.3', 'Date': 'Tue, 10 Dec 2019 15:51:03 GMT'})
    HTTP response body: {
      "evaluated_date": "2019-12-10T15:51:03.192+00:00",
      "log": [
        {
          "level": 20,
          "msg": "Retrieving URL https://www.archive.arm.gov/metadata/adc/html/wsacrcrcal.html",
          "timestamp": "2019-12-10 15:51:03.193Z"
        },
        {
          "level": 40,
          "msg": "Opening and ending tag mismatch: meta line 73 and head, line 75, column 12 (<string>, line 75)",
          "timestamp": "2019-12-10 15:51:03.324Z"
        }
      ],
      "url": "https://www.archive.arm.gov/metadata/adc/html/wsacrcrcal.html"
    }


    $ echo $?
    1

Invoking with the correct XML document can yield even larger STDOUT (suppressed here), so we show only the exit status here.

    $ willitsync johnevans$ willitsync get-scivalid -u https://www.archive.arm.gov/metadata/adc/xml/wsacrcrcal.xml > /dev/null
    $ echo $?
    0


The corresponding ``POST`` operation would be::

    $ willitsync scivalid --file wsacrcrcal.xml --formatid http://www.isotc211.org/2005/gmd > /dev/null
    $ echo $?
    0
