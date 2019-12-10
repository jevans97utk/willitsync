=============================
Validating Schema.org JSON-LD
=============================

You may validate Schema.org JSON-LD with the ``sovalid`` endpoints.

*********
GET Usage
*********

Schema.org JSON-LD content already available on a website may be verified with a ``GET`` operation.

::

    Usage: willitsync get-sovalid [OPTIONS]

    Options:
      -u, --url TEXT  Url to try  [required]
      --help          Show this message and exit.


***********
GET Example
***********


::
    
    $ willitsync get-sovalid -u https://www.archive.arm.gov/metadata/adc/html/wsacrcrcal.html > /dev/null
    $ echo $?
    0
    

**********
POST Usage
**********

To validate a document that is available on a local filesystem instead of a website, the corresponding ``POST`` subcommand ``sovalid`` may be used::

    $ willitsync sovalid --file wsacrcrcal.html > /dev/null
    $ echo $?
    0
