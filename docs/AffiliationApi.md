# billforward.AffiliationApi

All URIs are relative to *https://app.billforward.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_invoice**](AffiliationApi.md#create_invoice) | **POST** /affiliate/{account-id}/invoice | 
[**get_affiliate**](AffiliationApi.md#get_affiliate) | **GET** /product-rate-plans/{productRatePlanID}/affiliate | 
[**get_affiliate1**](AffiliationApi.md#get_affiliate1) | **GET** /subscriptions/{subscriptionID}/affiliate | 
[**quote_invoice**](AffiliationApi.md#quote_invoice) | **GET** /affiliate/{account-id}/quote/invoice/{invoice-id} | 
[**quote_subscription**](AffiliationApi.md#quote_subscription) | **GET** /affiliate/{account-id}/quote/subscription/{subscription-id} | 
[**set_affiliate**](AffiliationApi.md#set_affiliate) | **POST** /product-rate-plans/{product-rate-plan-ID}/affiliate | 
[**set_affiliate1**](AffiliationApi.md#set_affiliate1) | **POST** /subscriptions/{subscriptionID}/affiliate | 
[**update_affiliate**](AffiliationApi.md#update_affiliate) | **PUT** /product-rate-plans/{product-rate-plan-ID}/affiliate | 

# **create_invoice**
> InlineResponseDefault8 create_invoice(account_id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.AffiliationApi(billforward.ApiClient(configuration))
account_id = 'account_id_example' # str | 
body = billforward.CreateCommissionInvoiceRequest() # CreateCommissionInvoiceRequest |  (optional)

try:
    api_response = api_instance.create_invoice(account_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AffiliationApi->create_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **body** | [**CreateCommissionInvoiceRequest**](CreateCommissionInvoiceRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault8**](InlineResponseDefault8.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_affiliate**
> InlineResponseDefault48 get_affiliate(product_rate_plan_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.AffiliationApi(billforward.ApiClient(configuration))
product_rate_plan_id = 'product_rate_plan_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_affiliate(product_rate_plan_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AffiliationApi->get_affiliate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_rate_plan_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault48**](InlineResponseDefault48.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_affiliate1**
> InlineResponseDefault66 get_affiliate1(subscription_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.AffiliationApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_affiliate1(subscription_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AffiliationApi->get_affiliate1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault66**](InlineResponseDefault66.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_invoice**
> InlineResponseDefault13 quote_invoice(account_id, invoice_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.AffiliationApi(billforward.ApiClient(configuration))
account_id = 'account_id_example' # str | 
invoice_id = 'invoice_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.quote_invoice(account_id, invoice_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AffiliationApi->quote_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **invoice_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault13**](InlineResponseDefault13.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_subscription**
> InlineResponseDefault13 quote_subscription(account_id, subscription_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.AffiliationApi(billforward.ApiClient(configuration))
account_id = 'account_id_example' # str | 
subscription_id = 'subscription_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.quote_subscription(account_id, subscription_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AffiliationApi->quote_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **subscription_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault13**](InlineResponseDefault13.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_affiliate**
> InlineResponseDefault49 set_affiliate(product_rate_plan_id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.AffiliationApi(billforward.ApiClient(configuration))
product_rate_plan_id = 'product_rate_plan_id_example' # str | 
body = billforward.SetRatePlanAffiliateRequest() # SetRatePlanAffiliateRequest |  (optional)

try:
    api_response = api_instance.set_affiliate(product_rate_plan_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AffiliationApi->set_affiliate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_rate_plan_id** | **str**|  | 
 **body** | [**SetRatePlanAffiliateRequest**](SetRatePlanAffiliateRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault49**](InlineResponseDefault49.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_affiliate1**
> InlineResponseDefault67 set_affiliate1(subscription_id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.AffiliationApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
body = billforward.SetSubscriptionAffiliateRequest() # SetSubscriptionAffiliateRequest |  (optional)

try:
    api_response = api_instance.set_affiliate1(subscription_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AffiliationApi->set_affiliate1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**SetSubscriptionAffiliateRequest**](SetSubscriptionAffiliateRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault67**](InlineResponseDefault67.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_affiliate**
> InlineResponseDefault49 update_affiliate(product_rate_plan_id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.AffiliationApi(billforward.ApiClient(configuration))
product_rate_plan_id = 'product_rate_plan_id_example' # str | 
body = billforward.UpdateRatePlanAffiliateRequest() # UpdateRatePlanAffiliateRequest |  (optional)

try:
    api_response = api_instance.update_affiliate(product_rate_plan_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AffiliationApi->update_affiliate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_rate_plan_id** | **str**|  | 
 **body** | [**UpdateRatePlanAffiliateRequest**](UpdateRatePlanAffiliateRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault49**](InlineResponseDefault49.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

