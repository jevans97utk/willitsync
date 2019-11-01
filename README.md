# willitsync

# Workflow

1. Update the YAML configuration in SwaggerHub
2. Push the integration to github, this lands in SWAGGERHUB branch
3. Locally into devel
4. Cherry-pick the SWAGGERHUB commit corresponding to the code generation
5. In another terminal window, cd into the openapi-generator folder and run the following to generate the code

```shell
$ java -jar modules/openapi-generator-cli/target/openapi-generator-cli.jar generate \
-i $HOME/git/willitsync/yaml-resolved/swagger.yaml \
--generator-name python-flask \
-o $HOME/git/willitsync/python-flask
```

6. In the local willitsync terminal window, run `git status` to see what has changed.  Revert any files that you did not wish to change.
6. Test

```python
>>> import requests

>>> url = 'http://localhost:8080/jevans97utk/willitsync/1.0.1/robots'
>>> params = {'url':  'https://latimes.com/robots.txt'}
>>> r = requests.get(url, params=params)
>>> r.json()
[{'evaluated_date': '2019-11-01T08:36:02',
  'log': None,
  'sitemaps': ['https://www.latimes.com/sitemap.xml',
   'https://www.latimes.com/news-sitemap.xml'],
  'url': 'https://latimes.com/robots.txt'}]


```

