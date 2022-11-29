# billforward.DefaultApi

All URIs are relative to *https://app.billforward.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_totp_secret**](DefaultApi.md#create_totp_secret) | **POST** /2fa/totp | 
[**enable2fa**](DefaultApi.md#enable2fa) | **POST** /2fa/enable | 
[**get_qr_code**](DefaultApi.md#get_qr_code) | **GET** /barcode/qr/acc/{accountId} | 

# **create_totp_secret**
> create_totp_secret(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.DefaultApi(billforward.ApiClient(configuration))
body = billforward.CreateTOTPRequest() # CreateTOTPRequest |  (optional)

try:
    api_instance.create_totp_secret(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->create_totp_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTOTPRequest**](CreateTOTPRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable2fa**
> enable2fa(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.DefaultApi(billforward.ApiClient(configuration))
body = billforward.CreateTOTPRequest() # CreateTOTPRequest |  (optional)

try:
    api_instance.enable2fa(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->enable2fa: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTOTPRequest**](CreateTOTPRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_qr_code**
> get_qr_code(account_id, organizations=organizations, include_billforward_logo=include_billforward_logo)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.DefaultApi(billforward.ApiClient(configuration))
account_id = 'account_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
include_billforward_logo = true # bool |  (optional)

try:
    api_instance.get_qr_code(account_id, organizations=organizations, include_billforward_logo=include_billforward_logo)
except ApiException as e:
    print("Exception when calling DefaultApi->get_qr_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **include_billforward_logo** | **bool**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

