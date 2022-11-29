# billforward.CheckoutApi

All URIs are relative to *https://app.billforward.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**build_subscription_checkout**](CheckoutApi.md#build_subscription_checkout) | **GET** /public/checkouts/subscriptions/{checkout-definition-path} | 
[**create_account1**](CheckoutApi.md#create_account1) | **POST** /public/accounts | 
[**create_subscription_checkout_definition**](CheckoutApi.md#create_subscription_checkout_definition) | **POST** /checkouts/subscriptions | 
[**get_subscription_checkout_definition**](CheckoutApi.md#get_subscription_checkout_definition) | **GET** /checkouts/subscriptions/{checkout-definition-path} | 
[**subscription_checkout**](CheckoutApi.md#subscription_checkout) | **POST** /public/checkouts/subscriptions | 

# **build_subscription_checkout**
> InlineResponseDefault50 build_subscription_checkout(checkout_definition_path, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.CheckoutApi(billforward.ApiClient(configuration))
checkout_definition_path = 'checkout_definition_path_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.build_subscription_checkout(checkout_definition_path, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckoutApi->build_subscription_checkout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_definition_path** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault50**](InlineResponseDefault50.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_account1**
> InlineResponseDefault6 create_account1(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.CheckoutApi(billforward.ApiClient(configuration))
body = billforward.Account() # Account |  (optional)

try:
    api_response = api_instance.create_account1(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckoutApi->create_account1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Account**](Account.md)|  | [optional] 

### Return type

[**InlineResponseDefault6**](InlineResponseDefault6.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subscription_checkout_definition**
> InlineResponseDefault17 create_subscription_checkout_definition(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.CheckoutApi(billforward.ApiClient(configuration))
body = billforward.CreateSubscriptionCheckoutDefinitionRequest() # CreateSubscriptionCheckoutDefinitionRequest |  (optional)

try:
    api_response = api_instance.create_subscription_checkout_definition(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckoutApi->create_subscription_checkout_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSubscriptionCheckoutDefinitionRequest**](CreateSubscriptionCheckoutDefinitionRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault17**](InlineResponseDefault17.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_checkout_definition**
> InlineResponseDefault17 get_subscription_checkout_definition(checkout_definition_path, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.CheckoutApi(billforward.ApiClient(configuration))
checkout_definition_path = 'checkout_definition_path_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_subscription_checkout_definition(checkout_definition_path, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckoutApi->get_subscription_checkout_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_definition_path** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault17**](InlineResponseDefault17.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_checkout**
> InlineResponseDefault51 subscription_checkout(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.CheckoutApi(billforward.ApiClient(configuration))
body = billforward.SubscriptionCheckoutActionRequest() # SubscriptionCheckoutActionRequest |  (optional)

try:
    api_response = api_instance.subscription_checkout(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckoutApi->subscription_checkout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubscriptionCheckoutActionRequest**](SubscriptionCheckoutActionRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault51**](InlineResponseDefault51.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

