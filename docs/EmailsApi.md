# billforward.EmailsApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_email_by_id**](EmailsApi.md#get_email_by_id) | **GET** /emails/{email-ID} | Retrieves a single invoice, specified by the version-ID parameter.
[**get_email_html_by_id**](EmailsApi.md#get_email_html_by_id) | **GET** /emails/{email-ID}.html | Retrieves a single invoice, specified by the version-ID parameter.
[**get_email_text_by_id**](EmailsApi.md#get_email_text_by_id) | **GET** /emails/{email-ID}.txt | Retrieves a single invoice, specified by the version-ID parameter.


# **get_email_by_id**
> EmailPagedMetadata get_email_by_id(email_id, organizations=organizations)

Retrieves a single invoice, specified by the version-ID parameter.

{ \"nickname\" : \"Retrieve by version\",\"response\" : \"getEmailByID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.EmailsApi()
email_id = 'email_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Retrieves a single invoice, specified by the version-ID parameter.
    api_response = api_instance.get_email_by_id(email_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling EmailsApi->get_email_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**EmailPagedMetadata**](EmailPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_html_by_id**
> str get_email_html_by_id(email_id, organizations=organizations)

Retrieves a single invoice, specified by the version-ID parameter.

{ \"nickname\" : \"Retrieve by version\",\"response\" : \"getEmailByID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.EmailsApi()
email_id = 'email_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Retrieves a single invoice, specified by the version-ID parameter.
    api_response = api_instance.get_email_html_by_id(email_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling EmailsApi->get_email_html_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_text_by_id**
> str get_email_text_by_id(email_id, organizations=organizations)

Retrieves a single invoice, specified by the version-ID parameter.

{ \"nickname\" : \"Retrieve by version\",\"response\" : \"getEmailByID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.EmailsApi()
email_id = 'email_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Retrieves a single invoice, specified by the version-ID parameter.
    api_response = api_instance.get_email_text_by_id(email_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling EmailsApi->get_email_text_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

