# billforward.EBANXApi

All URIs are relative to *https://app.billforward.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_configuration1**](EBANXApi.md#delete_configuration1) | **DELETE** /ebanx | 
[**get_configuration1**](EBANXApi.md#get_configuration1) | **GET** /ebanx | 
[**handle_webhook**](EBANXApi.md#handle_webhook) | **POST** /ebanx/webhook/{organization_id} | 
[**upsert_configuration1**](EBANXApi.md#upsert_configuration1) | **POST** /ebanx | 

# **delete_configuration1**
> APIConfiguration delete_configuration1(organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.EBANXApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.delete_configuration1(organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EBANXApi->delete_configuration1: %s\n" % e)
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

# **get_configuration1**
> InlineResponseDefault14 get_configuration1(organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.EBANXApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_configuration1(organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EBANXApi->get_configuration1: %s\n" % e)
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

# **handle_webhook**
> InlineResponseDefault27 handle_webhook(organization_id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.EBANXApi(billforward.ApiClient(configuration))
organization_id = 'organization_id_example' # str | 
body = billforward.EBANXWebhook() # EBANXWebhook |  (optional)

try:
    api_response = api_instance.handle_webhook(organization_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EBANXApi->handle_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 
 **body** | [**EBANXWebhook**](EBANXWebhook.md)|  | [optional] 

### Return type

[**InlineResponseDefault27**](InlineResponseDefault27.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_configuration1**
> InlineResponseDefault14 upsert_configuration1(body=body, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.EBANXApi(billforward.ApiClient(configuration))
body = billforward.EBANXGatewayRequest() # EBANXGatewayRequest |  (optional)
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.upsert_configuration1(body=body, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EBANXApi->upsert_configuration1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EBANXGatewayRequest**](EBANXGatewayRequest.md)|  | [optional] 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault14**](InlineResponseDefault14.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

