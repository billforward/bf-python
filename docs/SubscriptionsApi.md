# billforward.SubscriptionsApi

All URIs are relative to *https://app.billforward.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_charge_to_subscription**](SubscriptionsApi.md#add_charge_to_subscription) | **POST** /subscriptions/{subscription-ID}/charge | 
[**add_coupon_to_subscription**](SubscriptionsApi.md#add_coupon_to_subscription) | **POST** /subscriptions/{subscription-ID}/coupons | 
[**add_credit_note_to_subscription**](SubscriptionsApi.md#add_credit_note_to_subscription) | **POST** /subscriptions/{subscription-ID}/credit | 
[**add_payment_method_to_subscription**](SubscriptionsApi.md#add_payment_method_to_subscription) | **POST** /subscriptions/{subscription-ID}/payment-methods | 
[**advance_subscription**](SubscriptionsApi.md#advance_subscription) | **POST** /subscriptions/{subscription-ID}/advance | 
[**available_payment_methods_for_subscription**](SubscriptionsApi.md#available_payment_methods_for_subscription) | **GET** /subscriptions/{subscription-ID}/payment-methods | 
[**batch_create_subscriptions**](SubscriptionsApi.md#batch_create_subscriptions) | **POST** /subscriptions/batch | 
[**batch_increment_usage**](SubscriptionsApi.md#batch_increment_usage) | **POST** /subscriptions/{subscriptionID}/increment-values | 
[**cancel_subscription**](SubscriptionsApi.md#cancel_subscription) | **POST** /subscriptions/{subscription-ID}/cancel | 
[**create_aggregating_subscription**](SubscriptionsApi.md#create_aggregating_subscription) | **POST** /subscriptions/aggregating | 
[**create_subscription_from_request**](SubscriptionsApi.md#create_subscription_from_request) | **POST** /subscriptions/create | 
[**create_timer**](SubscriptionsApi.md#create_timer) | **POST** /subscriptions/{subscription-ID}/timer | 
[**delete_metadata_for_subscription**](SubscriptionsApi.md#delete_metadata_for_subscription) | **DELETE** /subscriptions/{subscription-ID}/metadata | 
[**freeze_subscription**](SubscriptionsApi.md#freeze_subscription) | **POST** /subscriptions/{subscription-ID}/freeze | 
[**get_affiliate1**](SubscriptionsApi.md#get_affiliate1) | **GET** /subscriptions/{subscriptionID}/affiliate | 
[**get_applicable_coupons_for_subscription**](SubscriptionsApi.md#get_applicable_coupons_for_subscription) | **GET** /subscriptions/{subscription-ID}/applicable-coupons | 
[**get_available_credit_subscription**](SubscriptionsApi.md#get_available_credit_subscription) | **GET** /subscriptions/{subscription-ID}/credit | 
[**get_charges_on_subscription**](SubscriptionsApi.md#get_charges_on_subscription) | **GET** /subscriptions/{subscription-ID}/charges | 
[**get_children_of_subscription**](SubscriptionsApi.md#get_children_of_subscription) | **GET** /subscriptions/{subscription-ID}/children | 
[**get_coupons_on_subscription**](SubscriptionsApi.md#get_coupons_on_subscription) | **GET** /subscriptions/{subscription-ID}/coupons | 
[**get_invoices_for_subscription_by_state**](SubscriptionsApi.md#get_invoices_for_subscription_by_state) | **GET** /subscriptions/{subscriptionID}/invoices/{state} | 
[**get_metadata_for_subscription**](SubscriptionsApi.md#get_metadata_for_subscription) | **GET** /subscriptions/{subscription-ID}/metadata | 
[**get_parent_subscription**](SubscriptionsApi.md#get_parent_subscription) | **GET** /subscriptions/{subscription-ID}/parent | 
[**get_pricing_component_values_of_subscription**](SubscriptionsApi.md#get_pricing_component_values_of_subscription) | **GET** /subscriptions/{subscription-ID}/values | 
[**get_subscription_by_account_id**](SubscriptionsApi.md#get_subscription_by_account_id) | **GET** /subscriptions/account/{account-ID} | 
[**get_subscription_by_id**](SubscriptionsApi.md#get_subscription_by_id) | **GET** /subscriptions/{subscription-ID} | 
[**get_subscription_by_product_id**](SubscriptionsApi.md#get_subscription_by_product_id) | **GET** /subscriptions/product/{product-ID} | 
[**get_subscription_by_product_rate_plan_id**](SubscriptionsApi.md#get_subscription_by_product_rate_plan_id) | **GET** /subscriptions/product-rate-plan/{product-rate-plan-ID} | 
[**get_subscription_by_state**](SubscriptionsApi.md#get_subscription_by_state) | **GET** /subscriptions/state/{state} | 
[**get_subscription_by_version_id**](SubscriptionsApi.md#get_subscription_by_version_id) | **GET** /subscriptions/version/{version-ID} | 
[**get_subscriptions_by_initial_period_start**](SubscriptionsApi.md#get_subscriptions_by_initial_period_start) | **GET** /subscriptions/initial-period-start/{lower-threshold}/{upper-threshold} | 
[**get_subscriptions_by_period_end**](SubscriptionsApi.md#get_subscriptions_by_period_end) | **GET** /subscriptions/period-end/{lower-threshold}/{upper-threshold} | 
[**get_subscriptions_by_period_start**](SubscriptionsApi.md#get_subscriptions_by_period_start) | **GET** /subscriptions/period-start/{lower-threshold}/{upper-threshold} | 
[**get_subscriptions_by_successful_periods**](SubscriptionsApi.md#get_subscriptions_by_successful_periods) | **GET** /subscriptions/successful-periods/{lower-threshold}/{upper-threshold} | 
[**get_swagger_subscription**](SubscriptionsApi.md#get_swagger_subscription) | **GET** /subscriptions/swagger-end-point/{query-string} | 
[**get_timers_for_subscription**](SubscriptionsApi.md#get_timers_for_subscription) | **GET** /subscriptions/{subscription-ID}/timer | 
[**import_subscription**](SubscriptionsApi.md#import_subscription) | **POST** /subscriptions/import | 
[**invoice_charges_on_subscription**](SubscriptionsApi.md#invoice_charges_on_subscription) | **POST** /subscriptions/{subscription-ID}/invoice-charges | 
[**migrate_subscription**](SubscriptionsApi.md#migrate_subscription) | **POST** /subscriptions/{subscription-ID}/migrate | 
[**pause_subscription**](SubscriptionsApi.md#pause_subscription) | **POST** /subscriptions/{subscription-ID}/pause | 
[**remove_coupon_from_subscription**](SubscriptionsApi.md#remove_coupon_from_subscription) | **DELETE** /subscriptions/{subscription-ID}/coupons/{coupon-code} | 
[**remove_credit_from_subscription**](SubscriptionsApi.md#remove_credit_from_subscription) | **DELETE** /subscriptions/{subscription-ID}/credit/{value} | 
[**remove_payment_method_from_subscription**](SubscriptionsApi.md#remove_payment_method_from_subscription) | **DELETE** /subscriptions/{subscription-ID}/payment-methods/{payment-method-ID} | 
[**remove_pricing_component_value_change_from_subscription**](SubscriptionsApi.md#remove_pricing_component_value_change_from_subscription) | **DELETE** /subscriptions/{subscription-ID}/values/{pricing-component} | 
[**resume_subscription**](SubscriptionsApi.md#resume_subscription) | **POST** /subscriptions/{subscription-ID}/resume | 
[**revive_subscription**](SubscriptionsApi.md#revive_subscription) | **POST** /subscriptions/{subscription-ID}/revive | 
[**set_affiliate1**](SubscriptionsApi.md#set_affiliate1) | **POST** /subscriptions/{subscriptionID}/affiliate | 
[**set_metadata_for_subscription**](SubscriptionsApi.md#set_metadata_for_subscription) | **POST** /subscriptions/{subscription-ID}/metadata | 
[**set_pricing_component_value_on_subscription**](SubscriptionsApi.md#set_pricing_component_value_on_subscription) | **POST** /subscriptions/{subscription-ID}/pricing-component-values | 
[**set_pricing_component_value_on_subscription1**](SubscriptionsApi.md#set_pricing_component_value_on_subscription1) | **POST** /subscriptions/{subscription-ID}/values/{pricing-component} | 
[**set_pricing_component_value_on_subscription_batch_update**](SubscriptionsApi.md#set_pricing_component_value_on_subscription_batch_update) | **POST** /subscriptions/{subscription-ID}/values | 
[**start_all_subscriptions**](SubscriptionsApi.md#start_all_subscriptions) | **POST** /subscriptions/{accountID}/start | 
[**update_subscription_from_request**](SubscriptionsApi.md#update_subscription_from_request) | **PUT** /subscriptions/update | 
[**upsert_metadata_for_subscription**](SubscriptionsApi.md#upsert_metadata_for_subscription) | **PUT** /subscriptions/{subscription-ID}/metadata | 

# **add_charge_to_subscription**
> InlineResponseDefault28 add_charge_to_subscription(subscription_id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
body = billforward.AddChargeRequest() # AddChargeRequest |  (optional)

try:
    api_response = api_instance.add_charge_to_subscription(subscription_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->add_charge_to_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**AddChargeRequest**](AddChargeRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault28**](InlineResponseDefault28.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_coupon_to_subscription**
> InlineResponseDefault23 add_coupon_to_subscription(subscription_id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
body = billforward.AddCouponCodeRequest() # AddCouponCodeRequest |  (optional)

try:
    api_response = api_instance.add_coupon_to_subscription(subscription_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->add_coupon_to_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**AddCouponCodeRequest**](AddCouponCodeRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault23**](InlineResponseDefault23.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_credit_note_to_subscription**
> InlineResponseDefault4 add_credit_note_to_subscription(subscription_id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
body = billforward.CreditSubscriptionRequest() # CreditSubscriptionRequest |  (optional)

try:
    api_response = api_instance.add_credit_note_to_subscription(subscription_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->add_credit_note_to_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**CreditSubscriptionRequest**](CreditSubscriptionRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault4**](InlineResponseDefault4.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_payment_method_to_subscription**
> InlineResponseDefault40 add_payment_method_to_subscription(subscription_id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
body = billforward.AddPaymentMethodRequest() # AddPaymentMethodRequest |  (optional)

try:
    api_response = api_instance.add_payment_method_to_subscription(subscription_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->add_payment_method_to_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**AddPaymentMethodRequest**](AddPaymentMethodRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault40**](InlineResponseDefault40.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **advance_subscription**
> InlineResponseDefault61 advance_subscription(subscription_id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
body = billforward.TimeRequest() # TimeRequest |  (optional)

try:
    api_response = api_instance.advance_subscription(subscription_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->advance_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**TimeRequest**](TimeRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault61**](InlineResponseDefault61.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **available_payment_methods_for_subscription**
> InlineResponseDefault9 available_payment_methods_for_subscription(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'id' # str |  (optional) (default to id)
order = 'DESC' # str |  (optional) (default to DESC)

try:
    api_response = api_instance.available_payment_methods_for_subscription(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->available_payment_methods_for_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to id]
 **order** | **str**|  | [optional] [default to DESC]

### Return type

[**InlineResponseDefault9**](InlineResponseDefault9.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_create_subscriptions**
> InlineResponseDefault26 batch_create_subscriptions(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
body = billforward.CreateSubscriptionBatchRequest() # CreateSubscriptionBatchRequest |  (optional)

try:
    api_response = api_instance.batch_create_subscriptions(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->batch_create_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSubscriptionBatchRequest**](CreateSubscriptionBatchRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault26**](InlineResponseDefault26.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_increment_usage**
> InlineResponseDefault62 batch_increment_usage(subscription_id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
body = billforward.BatchIncrementValuesRequest() # BatchIncrementValuesRequest |  (optional)

try:
    api_response = api_instance.batch_increment_usage(subscription_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->batch_increment_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**BatchIncrementValuesRequest**](BatchIncrementValuesRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault62**](InlineResponseDefault62.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_subscription**
> InlineResponseDefault63 cancel_subscription(subscription_id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
body = billforward.SubscriptionCancellation() # SubscriptionCancellation |  (optional)

try:
    api_response = api_instance.cancel_subscription(subscription_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->cancel_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**SubscriptionCancellation**](SubscriptionCancellation.md)|  | [optional] 

### Return type

[**InlineResponseDefault63**](InlineResponseDefault63.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_aggregating_subscription**
> InlineResponseDefault51 create_aggregating_subscription(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
body = billforward.CreateAggregatingSubscriptionRequest() # CreateAggregatingSubscriptionRequest |  (optional)

try:
    api_response = api_instance.create_aggregating_subscription(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->create_aggregating_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAggregatingSubscriptionRequest**](CreateAggregatingSubscriptionRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault51**](InlineResponseDefault51.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subscription_from_request**
> InlineResponseDefault51 create_subscription_from_request(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
body = billforward.CreateSubscriptionRequest() # CreateSubscriptionRequest |  (optional)

try:
    api_response = api_instance.create_subscription_from_request(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->create_subscription_from_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSubscriptionRequest**](CreateSubscriptionRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault51**](InlineResponseDefault51.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_timer**
> InlineResponseDefault65 create_timer(subscription_id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
body = billforward.CreateSubscriptionTimerRequest() # CreateSubscriptionTimerRequest |  (optional)

try:
    api_response = api_instance.create_timer(subscription_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->create_timer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**CreateSubscriptionTimerRequest**](CreateSubscriptionTimerRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault65**](InlineResponseDefault65.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_metadata_for_subscription**
> InlineResponseDefault7 delete_metadata_for_subscription(subscription_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.delete_metadata_for_subscription(subscription_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->delete_metadata_for_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault7**](InlineResponseDefault7.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **freeze_subscription**
> InlineResponseDefault51 freeze_subscription(subscription_id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
body = billforward.PauseRequest() # PauseRequest |  (optional)

try:
    api_response = api_instance.freeze_subscription(subscription_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->freeze_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**PauseRequest**](PauseRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault51**](InlineResponseDefault51.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
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
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_affiliate1(subscription_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_affiliate1: %s\n" % e)
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

# **get_applicable_coupons_for_subscription**
> InlineResponseDefault22 get_applicable_coupons_for_subscription(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_applicable_coupons_for_subscription(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_applicable_coupons_for_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to false]

### Return type

[**InlineResponseDefault22**](InlineResponseDefault22.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_credit_subscription**
> InlineResponseDefault3 get_available_credit_subscription(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'id' # str |  (optional) (default to id)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_available_credit_subscription(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_available_credit_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to id]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to false]

### Return type

[**InlineResponseDefault3**](InlineResponseDefault3.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_charges_on_subscription**
> InlineResponseDefault10 get_charges_on_subscription(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, state=state, type=type, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)
state = 'state_example' # str |  (optional)
type = 'type_example' # str |  (optional)
include_retired = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_charges_on_subscription(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, state=state, type=type, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_charges_on_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]
 **state** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **include_retired** | **bool**|  | [optional] [default to false]

### Return type

[**InlineResponseDefault10**](InlineResponseDefault10.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_children_of_subscription**
> InlineResponseDefault26 get_children_of_subscription(subscription_id, exclude_service_ended=exclude_service_ended, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
exclude_service_ended = false # bool |  (optional) (default to false)
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)

try:
    api_response = api_instance.get_children_of_subscription(subscription_id, exclude_service_ended=exclude_service_ended, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_children_of_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **exclude_service_ended** | **bool**|  | [optional] [default to false]
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]

### Return type

[**InlineResponseDefault26**](InlineResponseDefault26.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupons_on_subscription**
> InlineResponseDefault22 get_coupons_on_subscription(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_coupons_on_subscription(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_coupons_on_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to false]

### Return type

[**InlineResponseDefault22**](InlineResponseDefault22.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices_for_subscription_by_state**
> InlineResponseDefault8 get_invoices_for_subscription_by_state(subscription_id, state, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
state = 'state_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)

try:
    api_response = api_instance.get_invoices_for_subscription_by_state(subscription_id, state, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_invoices_for_subscription_by_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **state** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]

### Return type

[**InlineResponseDefault8**](InlineResponseDefault8.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_for_subscription**
> InlineResponseDefault7 get_metadata_for_subscription(subscription_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_metadata_for_subscription(subscription_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_metadata_for_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault7**](InlineResponseDefault7.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parent_subscription**
> InlineResponseDefault26 get_parent_subscription(subscription_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_parent_subscription(subscription_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_parent_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault26**](InlineResponseDefault26.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pricing_component_values_of_subscription**
> InlineResponseDefault68 get_pricing_component_values_of_subscription(subscription_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_pricing_component_values_of_subscription(subscription_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_pricing_component_values_of_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault68**](InlineResponseDefault68.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_by_account_id**
> InlineResponseDefault26 get_subscription_by_account_id(account_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, exclude_children=exclude_children)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
account_id = 'account_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'id' # str |  (optional) (default to id)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = false # bool |  (optional) (default to false)
exclude_children = true # bool |  (optional) (default to true)

try:
    api_response = api_instance.get_subscription_by_account_id(account_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, exclude_children=exclude_children)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_subscription_by_account_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to id]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to false]
 **exclude_children** | **bool**|  | [optional] [default to true]

### Return type

[**InlineResponseDefault26**](InlineResponseDefault26.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_by_id**
> InlineResponseDefault51 get_subscription_by_id(subscription_id, organizations=organizations, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
include_retired = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_subscription_by_id(subscription_id, organizations=organizations, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_subscription_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **include_retired** | **bool**|  | [optional] [default to false]

### Return type

[**InlineResponseDefault51**](InlineResponseDefault51.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_by_product_id**
> InlineResponseDefault26 get_subscription_by_product_id(product_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, exclude_children=exclude_children)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
product_id = 'product_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'id' # str |  (optional) (default to id)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = false # bool |  (optional) (default to false)
exclude_children = true # bool |  (optional) (default to true)

try:
    api_response = api_instance.get_subscription_by_product_id(product_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, exclude_children=exclude_children)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_subscription_by_product_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to id]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to false]
 **exclude_children** | **bool**|  | [optional] [default to true]

### Return type

[**InlineResponseDefault26**](InlineResponseDefault26.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_by_product_rate_plan_id**
> InlineResponseDefault26 get_subscription_by_product_rate_plan_id(product_rate_plan_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, exclude_children=exclude_children)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
product_rate_plan_id = 'product_rate_plan_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'id' # str |  (optional) (default to id)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = false # bool |  (optional) (default to false)
exclude_children = true # bool |  (optional) (default to true)

try:
    api_response = api_instance.get_subscription_by_product_rate_plan_id(product_rate_plan_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, exclude_children=exclude_children)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_subscription_by_product_rate_plan_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_rate_plan_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to id]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to false]
 **exclude_children** | **bool**|  | [optional] [default to true]

### Return type

[**InlineResponseDefault26**](InlineResponseDefault26.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_by_state**
> InlineResponseDefault26 get_subscription_by_state(state, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, exclude_children=exclude_children)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
state = 'state_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'id' # str |  (optional) (default to id)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = false # bool |  (optional) (default to false)
exclude_children = true # bool |  (optional) (default to true)

try:
    api_response = api_instance.get_subscription_by_state(state, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, exclude_children=exclude_children)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_subscription_by_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to id]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to false]
 **exclude_children** | **bool**|  | [optional] [default to true]

### Return type

[**InlineResponseDefault26**](InlineResponseDefault26.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_by_version_id**
> InlineResponseDefault51 get_subscription_by_version_id(version_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
version_id = 'version_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_subscription_by_version_id(version_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_subscription_by_version_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault51**](InlineResponseDefault51.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscriptions_by_initial_period_start**
> InlineResponseDefault26 get_subscriptions_by_initial_period_start(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
lower_threshold = billforward.SimpleDateParam() # SimpleDateParam | 
upper_threshold = billforward.SimpleDateParam() # SimpleDateParam | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)

try:
    api_response = api_instance.get_subscriptions_by_initial_period_start(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_subscriptions_by_initial_period_start: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lower_threshold** | [**SimpleDateParam**](.md)|  | 
 **upper_threshold** | [**SimpleDateParam**](.md)|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]

### Return type

[**InlineResponseDefault26**](InlineResponseDefault26.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscriptions_by_period_end**
> InlineResponseDefault26 get_subscriptions_by_period_end(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
lower_threshold = billforward.SimpleDateParam() # SimpleDateParam | 
upper_threshold = billforward.SimpleDateParam() # SimpleDateParam | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)

try:
    api_response = api_instance.get_subscriptions_by_period_end(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_subscriptions_by_period_end: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lower_threshold** | [**SimpleDateParam**](.md)|  | 
 **upper_threshold** | [**SimpleDateParam**](.md)|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]

### Return type

[**InlineResponseDefault26**](InlineResponseDefault26.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscriptions_by_period_start**
> InlineResponseDefault26 get_subscriptions_by_period_start(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
lower_threshold = billforward.SimpleDateParam() # SimpleDateParam | 
upper_threshold = billforward.SimpleDateParam() # SimpleDateParam | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)

try:
    api_response = api_instance.get_subscriptions_by_period_start(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_subscriptions_by_period_start: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lower_threshold** | [**SimpleDateParam**](.md)|  | 
 **upper_threshold** | [**SimpleDateParam**](.md)|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]

### Return type

[**InlineResponseDefault26**](InlineResponseDefault26.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscriptions_by_successful_periods**
> InlineResponseDefault26 get_subscriptions_by_successful_periods(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
lower_threshold = 56 # int | 
upper_threshold = 56 # int | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)

try:
    api_response = api_instance.get_subscriptions_by_successful_periods(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_subscriptions_by_successful_periods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lower_threshold** | **int**|  | 
 **upper_threshold** | **int**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]

### Return type

[**InlineResponseDefault26**](InlineResponseDefault26.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_swagger_subscription**
> InlineResponseDefault69 get_swagger_subscription(query_string, organizations=organizations, offset=offset, records=records, format=format, wildcard=wildcard, entity=entity)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
query_string = 'query_string_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
format = 'JSON' # str |  (optional) (default to JSON)
wildcard = true # bool |  (optional) (default to true)
entity = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_swagger_subscription(query_string, organizations=organizations, offset=offset, records=records, format=format, wildcard=wildcard, entity=entity)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_swagger_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_string** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **format** | **str**|  | [optional] [default to JSON]
 **wildcard** | **bool**|  | [optional] [default to true]
 **entity** | **bool**|  | [optional] [default to false]

### Return type

[**InlineResponseDefault69**](InlineResponseDefault69.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_timers_for_subscription**
> InlineResponseDefault64 get_timers_for_subscription(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, state=state, event=event)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = false # bool |  (optional) (default to false)
state = 'state_example' # str |  (optional)
event = 'event_example' # str |  (optional)

try:
    api_response = api_instance.get_timers_for_subscription(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, state=state, event=event)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_timers_for_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to false]
 **state** | **str**|  | [optional] 
 **event** | **str**|  | [optional] 

### Return type

[**InlineResponseDefault64**](InlineResponseDefault64.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_subscription**
> InlineResponseDefault51 import_subscription(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
body = billforward.ImportSubscriptionRequest() # ImportSubscriptionRequest |  (optional)

try:
    api_response = api_instance.import_subscription(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->import_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImportSubscriptionRequest**](ImportSubscriptionRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault51**](InlineResponseDefault51.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoice_charges_on_subscription**
> InlineResponseDefault29 invoice_charges_on_subscription(subscription_id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
body = billforward.InvoiceChargeRequest() # InvoiceChargeRequest |  (optional)

try:
    api_response = api_instance.invoice_charges_on_subscription(subscription_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->invoice_charges_on_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**InvoiceChargeRequest**](InvoiceChargeRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault29**](InlineResponseDefault29.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrate_subscription**
> InlineResponseDefault70 migrate_subscription(subscription_id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
body = billforward.MigrationRequest() # MigrationRequest |  (optional)

try:
    api_response = api_instance.migrate_subscription(subscription_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->migrate_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**MigrationRequest**](MigrationRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault70**](InlineResponseDefault70.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause_subscription**
> InlineResponseDefault51 pause_subscription(subscription_id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
body = billforward.PauseRequest() # PauseRequest |  (optional)

try:
    api_response = api_instance.pause_subscription(subscription_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->pause_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**PauseRequest**](PauseRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault51**](InlineResponseDefault51.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_coupon_from_subscription**
> InlineResponseDefault23 remove_coupon_from_subscription(subscription_id, coupon_code, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
coupon_code = 'coupon_code_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.remove_coupon_from_subscription(subscription_id, coupon_code, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->remove_coupon_from_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **coupon_code** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault23**](InlineResponseDefault23.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_credit_from_subscription**
> InlineResponseDefault3 remove_credit_from_subscription(subscription_id, value, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
value = 'value_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.remove_credit_from_subscription(subscription_id, value, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->remove_credit_from_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **value** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault3**](InlineResponseDefault3.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_payment_method_from_subscription**
> InlineResponseDefault51 remove_payment_method_from_subscription(subscription_id, payment_method_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
payment_method_id = 'payment_method_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.remove_payment_method_from_subscription(subscription_id, payment_method_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->remove_payment_method_from_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **payment_method_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault51**](InlineResponseDefault51.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_pricing_component_value_change_from_subscription**
> InlineResponseDefault68 remove_pricing_component_value_change_from_subscription(subscription_id, pricing_component, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
pricing_component = 'pricing_component_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.remove_pricing_component_value_change_from_subscription(subscription_id, pricing_component, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->remove_pricing_component_value_change_from_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **pricing_component** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault68**](InlineResponseDefault68.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_subscription**
> InlineResponseDefault51 resume_subscription(subscription_id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
body = billforward.ResumeRequest() # ResumeRequest |  (optional)

try:
    api_response = api_instance.resume_subscription(subscription_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->resume_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**ResumeRequest**](ResumeRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault51**](InlineResponseDefault51.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revive_subscription**
> InlineResponseDefault26 revive_subscription(subscription_id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
body = billforward.SubscriptionReviveRequest() # SubscriptionReviveRequest |  (optional)

try:
    api_response = api_instance.revive_subscription(subscription_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->revive_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**SubscriptionReviveRequest**](SubscriptionReviveRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault26**](InlineResponseDefault26.md)

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
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
body = billforward.SetSubscriptionAffiliateRequest() # SetSubscriptionAffiliateRequest |  (optional)

try:
    api_response = api_instance.set_affiliate1(subscription_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->set_affiliate1: %s\n" % e)
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

# **set_metadata_for_subscription**
> InlineResponseDefault7 set_metadata_for_subscription(subscription_id, body=body, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
body = 'body_example' # str |  (optional)
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.set_metadata_for_subscription(subscription_id, body=body, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->set_metadata_for_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**str**](str.md)|  | [optional] 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault7**](InlineResponseDefault7.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_pricing_component_value_on_subscription**
> InlineResponseDefault72 set_pricing_component_value_on_subscription(subscription_id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
body = billforward.PricingComponentValue() # PricingComponentValue |  (optional)

try:
    api_response = api_instance.set_pricing_component_value_on_subscription(subscription_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->set_pricing_component_value_on_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**PricingComponentValue**](PricingComponentValue.md)|  | [optional] 

### Return type

[**InlineResponseDefault72**](InlineResponseDefault72.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_pricing_component_value_on_subscription1**
> InlineResponseDefault71 set_pricing_component_value_on_subscription1(subscription_id, pricing_component, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
pricing_component = 'pricing_component_example' # str | 
body = billforward.PricingComponentValueRequest() # PricingComponentValueRequest |  (optional)

try:
    api_response = api_instance.set_pricing_component_value_on_subscription1(subscription_id, pricing_component, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->set_pricing_component_value_on_subscription1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **pricing_component** | **str**|  | 
 **body** | [**PricingComponentValueRequest**](PricingComponentValueRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault71**](InlineResponseDefault71.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_pricing_component_value_on_subscription_batch_update**
> InlineResponseDefault62 set_pricing_component_value_on_subscription_batch_update(subscription_id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
body = billforward.BatchUpdatePricingComponentValuesRequest() # BatchUpdatePricingComponentValuesRequest |  (optional)

try:
    api_response = api_instance.set_pricing_component_value_on_subscription_batch_update(subscription_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->set_pricing_component_value_on_subscription_batch_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**BatchUpdatePricingComponentValuesRequest**](BatchUpdatePricingComponentValuesRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault62**](InlineResponseDefault62.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_all_subscriptions**
> InlineResponseDefault73 start_all_subscriptions(account_id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
account_id = 'account_id_example' # str | 
body = billforward.StartAllSubscriptionsRequest() # StartAllSubscriptionsRequest |  (optional)

try:
    api_response = api_instance.start_all_subscriptions(account_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->start_all_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **body** | [**StartAllSubscriptionsRequest**](StartAllSubscriptionsRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault73**](InlineResponseDefault73.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subscription_from_request**
> InlineResponseDefault51 update_subscription_from_request(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
body = billforward.UpdateSubscriptionRequest() # UpdateSubscriptionRequest |  (optional)

try:
    api_response = api_instance.update_subscription_from_request(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->update_subscription_from_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateSubscriptionRequest**](UpdateSubscriptionRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault51**](InlineResponseDefault51.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_metadata_for_subscription**
> InlineResponseDefault7 upsert_metadata_for_subscription(subscription_id, body=body, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SubscriptionsApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
body = 'body_example' # str |  (optional)
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.upsert_metadata_for_subscription(subscription_id, body=body, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->upsert_metadata_for_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **body** | [**str**](str.md)|  | [optional] 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault7**](InlineResponseDefault7.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

