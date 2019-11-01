# willitsync

# Workflow

1. Update the YAML configuration in SwaggerHub.  Saving it will commit it to GitHub (SWAGGERHUB branch) if a GitHub integration has been created.
2. Pull the SWAGGERHUB changes
3. Branch locally into devel
4. Cherry-pick the SWAGGERHUB commit corresponding to the code generation
5. In another terminal window, cd into the openapi-generator folder and run the following to generate the code

```shell
$ java -jar modules/openapi-generator-cli/target/openapi-generator-cli.jar generate \
-i $HOME/git/willitsync/yaml-resolved/swagger.yaml \
--generator-name python-flask \
-o $HOME/git/willitsync/python-flask
```

6. In the local willitsync terminal window, run `git status` to see what has changed.  Revert any files that you did not wish to change.
7. Test

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

8. Commit the changes on the devel branch (possibly squash the cherry-picked commit?)
9. When development work is done, the version number could be updated, but this necessitates creating a new GitHub integration.  Most of the details of creating the new integration is straightforward, but be sure to set the items below correctly.  Consult the documentation at https://app.swaggerhub.com/help/integrations/github-sync for details. 
  * Sync Method:  Basic Sync
  * Branch:  SWAGGERHUB
  * Generated API Code:  YAML (Resolved)
