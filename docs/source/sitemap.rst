========================
Retrieve Sitemap Entries
========================

Entries from a sitemap may be retrieve using the ``sitemap`` subcommand.  The set of entries might span all nested sitemaps.

*****
Usage
*****

::

    Usage: willitsync sitemap [OPTIONS]

    Options:
      -u, --url TEXT            Url to try  [required]
      -x, --maxentries INTEGER  Maximum number of entries to show, default is 100,
                                use -1 to retrieve all.
      --help                    Show this message and exit.

*******
Example
*******

::

    $ willitsync sitemap -u https://www.archive.arm.gov/metadata/adc/sitemap.xml --maxentries 3
    {'evaluated_date': datetime.datetime(2019, 12, 10, 19, 10, 23, 17000, tzinfo=tzutc()),
     'log': [{'level': 20,
              'msg': 'Requesting sitemap document from '
                     'https://www.archive.arm.gov/metadata/adc/sitemap.xml',
              'timestamp': datetime.datetime(2019, 12, 10, 19, 10, 23, 18000, tzinfo=tzutc())},
             {'level': 20,
              'msg': 'Retrieving URL '
                     'https://www.archive.arm.gov/metadata/adc/sitemap.xml',
              'timestamp': datetime.datetime(2019, 12, 10, 19, 10, 23, 18000, tzinfo=tzutc())},
             {'level': 20,
              'msg': 'Extracted 193 from the sitemap document.',
              'timestamp': datetime.datetime(2019, 12, 10, 19, 10, 23, 144000, tzinfo=tzutc())},
             {'level': 20,
              'msg': 'Looking to process 3 records...',
              'timestamp': datetime.datetime(2019, 12, 10, 19, 10, 23, 144000, tzinfo=tzutc())}],
     'sitemaps': ['https://www.archive.arm.gov/metadata/adc/sitemap.xml'],
     'urlset': [{'lastmod': datetime.datetime(2019, 11, 25, 0, 0, tzinfo=tzutc()),
                 'url': 'https://www.archive.arm.gov/metadata/adc/html/microbasepiavg.html'},
                {'lastmod': datetime.datetime(2019, 11, 25, 0, 0, tzinfo=tzutc()),
                 'url': 'https://www.archive.arm.gov/metadata/adc/html/wsicloudspec.html'},
                {'lastmod': datetime.datetime(2019, 11, 25, 0, 0, tzinfo=tzutc()),
                 'url': 'https://www.archive.arm.gov/metadata/adc/html/30ecor.html'}]}
    
