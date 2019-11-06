# willitsync

# Workflow

## SlenderNodes

1. Grab the devel branch of jevans97 SlenderNodes
2. cd /path/to/SlenderNodes/schema_org/src

Create a Anaconda environment for python 3.7 like so

3. conda env create -n willitsync37 --file=environment.yml
4. conda activate willitsync37

## OpenAPI

1. If and only if there has been a change in the YAML configuration file, in another terminal window, cd into the openapi-generator folder and run the following to generate the code

```shell
$ java -jar modules/openapi-generator-cli/target/openapi-generator-cli.jar generate \
-i $HOME/git/willitsync/yaml-resolved/swagger.yaml \
--generator-name python-flask \
-o $HOME/git/willitsync/python-flask
```

2. In a willitsync environment terminal window, run `git status` to see what has changed.  Revert any files that you did not wish to change.  It's quite possibly that you will want to restore all files listed by `git status`.
3. cd python-flask

Install additional requirements to run the openapi server

4. python -m pip install -r requirements.txt
5. python -m pip install -r test-requirements.txt

Run the server

6. python -m openapi_server

7. In another terminal window (does not have to be a willitsync environment terminal window), you can test with

```python
>>> import requests

>>> url = 'http://localhost:8080/jevans97utk/willitsync/1.0.2/robots'
>>> params = {'url':  'https://nytimes.com/robots.txt'}
>>> r = requests.get(url, params=params)
>>> r.json()
[{'evaluated_date': '2019-11-05T15:43:10',
  'log': None,
  'sitemaps': ['https://www.nytimes.com/sitemaps/www.nytimes.com/sitemap.xml.gz',
   'https://www.nytimes.com/sitemaps/new/news.xml.gz',
   'https://www.nytimes.com/sitemaps/sitemap_video/sitemap.xml.gz',
   'https://www.nytimes.com/sitemaps/www.nytimes.com_realestate/sitemap.xml.gz',
   'https://www.nytimes.com/sitemaps/www.nytimes.com/2016_election_sitemap.xml.gz',
   'https://www.nytimes.com/elections/2018/sitemap'],
  'url': 'https://nytimes.com/robots.txt'}]
```

```python
>>> url = 'http://localhost:8080/jevans97utk/willitsync/1.0.2/so'
>>> params = {'url': 'https://www.archive.arm.gov/metadata/html/pghnoaaaosM1.b1.html'}
>>> r = requests.get(url, params=params) 
>>> r.json()['metadata']
```
