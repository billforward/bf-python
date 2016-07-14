# billforward.SearchApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**perform_search**](SearchApi.md#perform_search) | **GET** /search/{query-string} | Returns the results of the global search specified by the query-string.


# **perform_search**
> SearchResultPagedMetadata perform_search(query_string, organizations=organizations, types=types, offset=offset, records=records, wildcard=wildcard, entity=entity)

Returns the results of the global search specified by the query-string.

{\"nickname\":\"Search an organizations data\",\"response\":\"getSearchByID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.SearchApi()
query_string = 'query_string_example' # str | The query string used to search.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
types = ['types_example'] # list[str] | A list of entities which will be checked when searching (optional)
offset = 0 # int | The starting index of the search results. (optional) (default to 0)
records = 10 # int | The number of search results to return. (optional) (default to 10)
wildcard = false # bool | Toggle if we search for full words or whether a wildcard is used. (optional) (default to false)
entity = false # bool | Is an entity returned with the search results. (optional) (default to false)

try: 
    # Returns the results of the global search specified by the query-string.
    api_response = api_instance.perform_search(query_string, organizations=organizations, types=types, offset=offset, records=records, wildcard=wildcard, entity=entity)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SearchApi->perform_search: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_string** | **str**| The query string used to search. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **types** | [**list[str]**](str.md)| A list of entities which will be checked when searching | [optional] 
 **offset** | **int**| The starting index of the search results. | [optional] [default to 0]
 **records** | **int**| The number of search results to return. | [optional] [default to 10]
 **wildcard** | **bool**| Toggle if we search for full words or whether a wildcard is used. | [optional] [default to false]
 **entity** | **bool**| Is an entity returned with the search results. | [optional] [default to false]

### Return type

[**SearchResultPagedMetadata**](SearchResultPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

