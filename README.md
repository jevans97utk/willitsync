# willitsync

# Workflow

1. Update the YAML configuration in SwaggerHub
2. Push the integration to github, this lands in SWAGGERHUB branch
3. Branch from devel into new feature branch
4. Cherry-pick the SWAGGERHUB commit ???
5. Regenerate the code (check developers_controller.py for business logic)
6. Test

```python
import requests

url = 'http://localhost:8080/datadavev/willitsync/1.0.0/robots'
params = {'url':  'https://latimes.com/robots.txt'}
r = requests.get(url, params=params)
r.json()
'[[{"url": "https://latimes.com/robots.txt", "log": null, "evaluated_date": "2019-10-31T10:36:07", "sitemaps": ["https://www.latimes.com/sitemap.xml", "https://www.latimes.com/news-sitemap.xml"]}]]'
```

