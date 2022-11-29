# billforward.PlansApi

All URIs are relative to *https://app.billforward.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](PlansApi.md#delete) | **DELETE** /plans/{path} | 
[**find**](PlansApi.md#find) | **GET** /plans/{path} | 
[**upsert**](PlansApi.md#upsert) | **PUT** /plans | 

# **delete**
> InlineResponseDefault25 delete(path, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.PlansApi(billforward.ApiClient(configuration))
path = 'path_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.delete(path, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlansApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault25**](InlineResponseDefault25.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find**
> InlineResponseDefault25 find(path, records=records, organizations=organizations, with_pricing=with_pricing, with_metadata=with_metadata)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.PlansApi(billforward.ApiClient(configuration))
path = 'path_example' # str | 
records = 56 # int |  (optional)
organizations = ['organizations_example'] # list[str] |  (optional)
with_pricing = true # bool |  (optional) (default to true)
with_metadata = true # bool |  (optional) (default to true)

try:
    api_response = api_instance.find(path, records=records, organizations=organizations, with_pricing=with_pricing, with_metadata=with_metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlansApi->find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **records** | **int**|  | [optional] 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **with_pricing** | **bool**|  | [optional] [default to true]
 **with_metadata** | **bool**|  | [optional] [default to true]

### Return type

[**InlineResponseDefault25**](InlineResponseDefault25.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert**
> InlineResponseDefault25 upsert(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.PlansApi(billforward.ApiClient(configuration))
body = [billforward.PlanRequest()] # list[PlanRequest] |  (optional)

try:
    api_response = api_instance.upsert(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlansApi->upsert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[PlanRequest]**](PlanRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault25**](InlineResponseDefault25.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

