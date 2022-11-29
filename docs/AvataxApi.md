# billforward.AvataxApi

All URIs are relative to *https://app.billforward.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_avatax_configuration**](AvataxApi.md#create_avatax_configuration) | **POST** /tax/avatax | 
[**get_avatax_configuration**](AvataxApi.md#get_avatax_configuration) | **GET** /tax/avatax | 
[**ping**](AvataxApi.md#ping) | **POST** /tax/avatax/ping | 
[**update_avatax_configuration**](AvataxApi.md#update_avatax_configuration) | **PUT** /tax/avatax/{avatax-config-ID} | 

# **create_avatax_configuration**
> InlineResponseDefault75 create_avatax_configuration(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.AvataxApi(billforward.ApiClient(configuration))
body = billforward.AvataxConfigRequest() # AvataxConfigRequest |  (optional)

try:
    api_response = api_instance.create_avatax_configuration(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvataxApi->create_avatax_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AvataxConfigRequest**](AvataxConfigRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault75**](InlineResponseDefault75.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_avatax_configuration**
> InlineResponseDefault74 get_avatax_configuration(organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.AvataxApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_avatax_configuration(organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvataxApi->get_avatax_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault74**](InlineResponseDefault74.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping**
> InlineResponseDefault76 ping(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.AvataxApi(billforward.ApiClient(configuration))
body = billforward.AvataxPingRequest() # AvataxPingRequest |  (optional)

try:
    api_response = api_instance.ping(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvataxApi->ping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AvataxPingRequest**](AvataxPingRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault76**](InlineResponseDefault76.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_avatax_configuration**
> InlineResponseDefault75 update_avatax_configuration(avatax_config_id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.AvataxApi(billforward.ApiClient(configuration))
avatax_config_id = 'avatax_config_id_example' # str | 
body = billforward.AvataxConfigRequest() # AvataxConfigRequest |  (optional)

try:
    api_response = api_instance.update_avatax_configuration(avatax_config_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvataxApi->update_avatax_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avatax_config_id** | **str**|  | 
 **body** | [**AvataxConfigRequest**](AvataxConfigRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault75**](InlineResponseDefault75.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

