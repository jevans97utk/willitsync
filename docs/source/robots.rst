=====================================================
Parsing a ``robots.txt`` to Gain Insight to a Sitemap
=====================================================

The ``robots.txt`` file can be employed to advertise the existance of XML Sitemap declarations.

*****
Usage
*****

::

    Usage: willitsync robot [OPTIONS]

    Options:
      -u, --url TEXT  Url to try  [required]
      --help          Show this message and exit.

********
Examples
********

See what sitemaps are offered by the New York Times::

    $ willitsync robot -u https://www.nytimes.com/robots.txt
    {'evaluated_date': datetime.datetime(2019, 12, 10, 19, 0, 1, 786000, tzinfo=tzutc()),
     'log': [{'level': 20,
              'msg': 'parse_robots:...',
              'timestamp': datetime.datetime(2019, 12, 10, 19, 0, 1, 786000, tzinfo=tzutc())}],
     'sitemaps': ['https://www.nytimes.com/sitemaps/new/news.xml.gz',
                  'https://www.nytimes.com/sitemaps/new/sitemap.xml.gz',
                  'https://www.nytimes.com/sitemaps/new/wire.xml.gz',
                  'https://www.nytimes.com/sitemaps/new/collections.xml.gz',
                  'https://www.nytimes.com/sitemaps/new/video.xml.gz',
                  'https://www.nytimes.com/sitemaps/www.nytimes.com_realestate/sitemap.xml.gz',
                  'https://www.nytimes.com/sitemaps/www.nytimes.com/2016_election_sitemap.xml.gz',
                  'https://www.nytimes.com/elections/2018/sitemap'],
     'url': 'https://www.nytimes.com/robots.txt'}


Sometimes this is not allowed, however::

    $ willitsync robot -u https://www.latimes.com/robots.txt
    .
    .
    . [traceback suppressed]
    .
    .
    .
    openapi_client.exceptions.ApiException: (403)
    Reason: FORBIDDEN
    HTTP response headers: HTTPHeaderDict({'Content-Type': 'application/json', 'Content-Length': '395', 'Server': 'Werkzeug/0.16.0 Python/3.7.3', 'Date': 'Tue, 10 Dec 2019 19:04:52 GMT'})
    HTTP response body: {
      "evaluated_date": "2019-12-10T19:04:52.034+00:00",
      "log": [
        {
          "level": 20,
          "msg": "parse_robots:...",
          "timestamp": "2019-12-10 19:04:52.034Z"
        },
        {
          "level": 40,
          "msg": "403 Client Error: Forbidden for url: https://www.latimes.com/robots.txt",
          "timestamp": "2019-12-10 19:04:52.203Z"
        }
      ],
      "url": "https://www.latimes.com/robots.txt"
    }
    
