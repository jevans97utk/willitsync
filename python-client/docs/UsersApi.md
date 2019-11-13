# openapi_client.UsersApi

All URIs are relative to *https://localhost:8080/willitsync/1.1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_validate_metadata**](UsersApi.md#get_validate_metadata) | **GET** /scivalid | Retrieve and validate a science metadata XML document
[**get_validate_so**](UsersApi.md#get_validate_so) | **GET** /sovalid | Retrieve and validate a schema.org JSON-LD document
[**parse_landingpage**](UsersApi.md#parse_landingpage) | **GET** /so | Extract schema.org metadata from web page
[**parse_robots**](UsersApi.md#parse_robots) | **GET** /robots | Retrieve sitemap references from a robots.txt file
[**parse_sitemap**](UsersApi.md#parse_sitemap) | **GET** /sitemap | Get locatiosn from a sitemap.
[**validate_metadata**](UsersApi.md#validate_metadata) | **POST** /scivalid | Validate provided science metadata XML document
[**validate_so**](UsersApi.md#validate_so) | **POST** /sovalid | Validate provided schema.org JSON-LD document


# **get_validate_metadata**
> SCIMetadata get_validate_metadata(url, formatid)

Retrieve and validate a science metadata XML document

Given a url referencing an XML metadata document, retrieve and validate the XML. 

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.UsersApi()
url = 'https://my.server/metadata/iso_metadata.xml' # str | URL referencing a science metadata XML document to retrieve  and validate. 
formatid = 'http://www.isotc211.org/2005/gmd' # str | The DataONE formatId of the XML to test for validity. 

try:
    # Retrieve and validate a science metadata XML document
    api_response = api_instance.get_validate_metadata(url, formatid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_validate_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| URL referencing a science metadata XML document to retrieve  and validate.  | 
 **formatid** | **str**| The DataONE formatId of the XML to test for validity.  | 

### Return type

[**SCIMetadata**](SCIMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata successfully parsed and validated. The response body  contains the retrieved XML metadata.  |  -  |
**400** | Bad input parameter |  -  |
**404** | No XML document found at url |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_validate_so**
> SOMetadata get_validate_so(url, sotype=sotype)

Retrieve and validate a schema.org JSON-LD document

Given a url referencing a schema.org JSON-LD document, verify that  the structure matches expected model indicated in the type parameter. 

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.UsersApi()
url = 'https://my.server.net/data/dataset_1/jsonld.json' # str | URL referencing a schema.org JSON-LD document or a landing page containing schema.org JSON-LD to retrieve and validate. 
sotype = 'Dataset' # str | The name of the schema.org type to test for validity.  (optional) (default to 'Dataset')

try:
    # Retrieve and validate a schema.org JSON-LD document
    api_response = api_instance.get_validate_so(url, sotype=sotype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_validate_so: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| URL referencing a schema.org JSON-LD document or a landing page containing schema.org JSON-LD to retrieve and validate.  | 
 **sotype** | **str**| The name of the schema.org type to test for validity.  | [optional] [default to &#39;Dataset&#39;]

### Return type

[**SOMetadata**](SOMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON-LD successfully parsed and validated. The response body contains the retrieved schema.org JSON-LD object in the metadata element.  |  -  |
**400** | Bad input parameter |  -  |
**404** | No JSON-LD document found at url |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parse_landingpage**
> SOMetadata parse_landingpage(url)

Extract schema.org metadata from web page

Parses landing page to extract schema.org JSON-LD metadata 

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.UsersApi()
url = 'https://my.server.org/data/dataset_1' # str | URL pointing to langing page to be parsed 

try:
    # Extract schema.org metadata from web page
    api_response = api_instance.parse_landingpage(url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->parse_landingpage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| URL pointing to langing page to be parsed  | 

### Return type

[**SOMetadata**](SOMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Landing page successfully retrieved and parsed |  -  |
**400** | Bad input parameter |  -  |
**404** | No landing page document found at url |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parse_robots**
> RobotsFile parse_robots(url)

Retrieve sitemap references from a robots.txt file

Given a robots.txt file, parse, and retrieve referenced sitemap locations. 

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.UsersApi()
url = 'https://my.server.org/robots.txt' # str | URL pointing to a robots.txt file

try:
    # Retrieve sitemap references from a robots.txt file
    api_response = api_instance.parse_robots(url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->parse_robots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| URL pointing to a robots.txt file | 

### Return type

[**RobotsFile**](RobotsFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Parsed robots.txt file |  -  |
**400** | bad input parameter |  -  |
**404** | No robots.txt file found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parse_sitemap**
> Sitemap parse_sitemap(url, maxlocs=maxlocs)

Get locatiosn from a sitemap.

Parses a sitemap to retrieve location entries. 

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.UsersApi()
url = 'https://my.server.org/sitemap.xml' # str | URL pointing to a sitemap xml document
maxlocs = 100 # int | Maximum number of sitemap locations to return  (optional) (default to 100)

try:
    # Get locatiosn from a sitemap.
    api_response = api_instance.parse_sitemap(url, maxlocs=maxlocs)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->parse_sitemap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| URL pointing to a sitemap xml document | 
 **maxlocs** | **int**| Maximum number of sitemap locations to return  | [optional] [default to 100]

### Return type

[**Sitemap**](Sitemap.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sitemap successfully retrieved and parsed |  -  |
**400** | Bad input parameter |  -  |
**404** | No sitemap document found at url |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_metadata**
> SCIMetadata validate_metadata(formatid, body)

Validate provided science metadata XML document

Given an XML metadata document, validate the XML. 

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.UsersApi()
formatid = 'http://www.isotc211.org/2005/gmd' # str | The DataONE formatId of the XML to test for validity. 
body = 'body_example' # str | Science metadata XML document to validate. 

try:
    # Validate provided science metadata XML document
    api_response = api_instance.validate_metadata(formatid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->validate_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **formatid** | **str**| The DataONE formatId of the XML to test for validity.  | 
 **body** | **str**| Science metadata XML document to validate.  | 

### Return type

[**SCIMetadata**](SCIMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/xml, application/xml
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON-LD successfully parsed and validated. The response body contains the retrieved schema.org JSON-LD object in the metadata element.  |  -  |
**400** | Bad input parameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_so**
> SOMetadata validate_so(body, type=type)

Validate provided schema.org JSON-LD document

Given a schema.org JSON-LD document, verify that the structure  matches expected model indicated in the type parameter. 

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.UsersApi()
body = None # object | Schema.org JSON-LD to validate. 
type = 'Dataset' # str | The name of the schema.org type to test for validity.  (optional) (default to 'Dataset')

try:
    # Validate provided schema.org JSON-LD document
    api_response = api_instance.validate_so(body, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->validate_so: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**| Schema.org JSON-LD to validate.  | 
 **type** | **str**| The name of the schema.org type to test for validity.  | [optional] [default to &#39;Dataset&#39;]

### Return type

[**SOMetadata**](SOMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON-LD successfully parsed and validated. The response body contains the retrieved schema.org JSON-LD object in the metadata element.  |  -  |
**400** | Bad input parameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

