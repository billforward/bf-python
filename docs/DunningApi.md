# billforward.DunningApi

All URIs are relative to *https://app.billforward.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dunning_line**](DunningApi.md#create_dunning_line) | **POST** /dunning-lines | 
[**get_all_dunning_lines**](DunningApi.md#get_all_dunning_lines) | **GET** /dunning-lines | 
[**get_dunning_line_by_attempt_index**](DunningApi.md#get_dunning_line_by_attempt_index) | **GET** /dunning-lines/attempt-index/{index} | 
[**get_dunning_line_by_id**](DunningApi.md#get_dunning_line_by_id) | **GET** /dunning-lines/{dunning-line-ID} | 
[**retire_dunning_line**](DunningApi.md#retire_dunning_line) | **DELETE** /dunning-lines/{dunning-line-ID} | 
[**update_dunning_line**](DunningApi.md#update_dunning_line) | **PUT** /dunning-lines | 

# **create_dunning_line**
> InlineResponseDefault1 create_dunning_line(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.DunningApi(billforward.ApiClient(configuration))
body = billforward.DunningLine() # DunningLine |  (optional)

try:
    api_response = api_instance.create_dunning_line(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DunningApi->create_dunning_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DunningLine**](DunningLine.md)|  | [optional] 

### Return type

[**InlineResponseDefault1**](InlineResponseDefault1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_dunning_lines**
> InlineResponseDefault get_all_dunning_lines(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.DunningApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = true # bool |  (optional) (default to true)

try:
    api_response = api_instance.get_all_dunning_lines(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DunningApi->get_all_dunning_lines: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to true]

### Return type

[**InlineResponseDefault**](InlineResponseDefault.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dunning_line_by_attempt_index**
> InlineResponseDefault get_dunning_line_by_attempt_index(index, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.DunningApi(billforward.ApiClient(configuration))
index = 56 # int | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = true # bool |  (optional) (default to true)

try:
    api_response = api_instance.get_dunning_line_by_attempt_index(index, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DunningApi->get_dunning_line_by_attempt_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to true]

### Return type

[**InlineResponseDefault**](InlineResponseDefault.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dunning_line_by_id**
> InlineResponseDefault1 get_dunning_line_by_id(dunning_line_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.DunningApi(billforward.ApiClient(configuration))
dunning_line_id = 'dunning_line_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_dunning_line_by_id(dunning_line_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DunningApi->get_dunning_line_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dunning_line_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault1**](InlineResponseDefault1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retire_dunning_line**
> InlineResponseDefault1 retire_dunning_line(dunning_line_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.DunningApi(billforward.ApiClient(configuration))
dunning_line_id = 'dunning_line_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.retire_dunning_line(dunning_line_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DunningApi->retire_dunning_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dunning_line_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault1**](InlineResponseDefault1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dunning_line**
> InlineResponseDefault1 update_dunning_line(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.DunningApi(billforward.ApiClient(configuration))
body = billforward.DunningLine() # DunningLine |  (optional)

try:
    api_response = api_instance.update_dunning_line(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DunningApi->update_dunning_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DunningLine**](DunningLine.md)|  | [optional] 

### Return type

[**InlineResponseDefault1**](InlineResponseDefault1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

