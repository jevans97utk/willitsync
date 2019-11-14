# Willitsync Client

Example, get sitemaps from robots file:
```
willitsync -v DEBUG robot -u "https://doi.pangaea.de/robots.txt"
debug: in main()
debug: Calling robot with url = https://doi.pangaea.de/robots.txt
{'evaluated_date': datetime.datetime(2019, 11, 13, 13, 45, 2, 718000, tzinfo=tzutc()),
 'log': [{'level': 20,
          'msg': 'parse_robots:...',
          'timestamp': datetime.datetime(2019, 11, 13, 13, 45, 2, 718000, tzinfo=tzutc())}],
 'sitemaps': ['https://doi.pangaea.de/sitemap.xml'],
 'url': 'https://doi.pangaea.de/robots.txt'}
```

Example, get locations from sitemap:
```
willitsync -v DEBUG sitemap -u "https://doi.pangaea.de/sitemap-0.xml.gz"

```

Example, get schema.org markup from landing page:

```
willitsync -v DEBUG so -u "https://doi.pangaea.de/10.1594/PANGAEA.901968"
debug: in main()
debug: Calling so with url = https://doi.pangaea.de/10.1594/PANGAEA.901968
{'evaluated_date': datetime.datetime(2019, 11, 13, 13, 40, 38, 588000, tzinfo=tzutc()),
 'log': [{'level': 20,
          'msg': 'Requesting landing page '
                 'https://doi.pangaea.de/10.1594/PANGAEA.901968...',
          'timestamp': datetime.datetime(2019, 11, 13, 13, 40, 38, 624000, tzinfo=tzutc())},
         {'level': 20,
          'msg': 'Retrieving URL https://doi.pangaea.de/10.1594/PANGAEA.901968',
          'timestamp': datetime.datetime(2019, 11, 13, 13, 40, 38, 624000, tzinfo=tzutc())}],
 'metadata': {'@context': 'http://schema.org/',
              '@id': 'https://doi.org/10.1594/PANGAEA.901968',
              '@reverse': {'isBasedOn': {'@type': 'CreativeWork',
                                         'creator': [{'@type': 'Person',
                                                      'email': 'hnjovu@mwekawildlife.org',
                                                      'familyName': 'Njovu',
                                                      'givenName': 'Henry',
                                                      'url': 'http://www.mwekawildlife.org/'},
                                                     {'@id': 'https://orcid.org/0000-0002-1262-0827',
                                                      '@type': 'Person',

```