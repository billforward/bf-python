# billforward.CardConnectApi

All URIs are relative to *https://app.billforward.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_configuration**](CardConnectApi.md#delete_configuration) | **DELETE** /cardconnect | 
[**get_configuration**](CardConnectApi.md#get_configuration) | **GET** /cardconnect | 
[**upsert_configuration**](CardConnectApi.md#upsert_configuration) | **POST** /cardconnect | 

# **delete_configuration**
> APIConfiguration delete_configuration(organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.CardConnectApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.delete_configuration(organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CardConnectApi->delete_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**APIConfiguration**](APIConfiguration.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configuration**
> InlineResponseDefault14 get_configuration(organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.CardConnectApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_configuration(organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CardConnectApi->get_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault14**](InlineResponseDefault14.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_configuration**
> InlineResponseDefault14 upsert_configuration(body=body, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.CardConnectApi(billforward.ApiClient(configuration))
body = billforward.CardConnectGatewayRequest() # CardConnectGatewayRequest |  (optional)
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.upsert_configuration(body=body, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CardConnectApi->upsert_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CardConnectGatewayRequest**](CardConnectGatewayRequest.md)|  | [optional] 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault14**](InlineResponseDefault14.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

