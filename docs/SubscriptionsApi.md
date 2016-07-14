# swagger_client.SubscriptionsApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_charge_to_subscription**](SubscriptionsApi.md#add_charge_to_subscription) | **POST** /subscriptions/{subscription-ID}/charge | Creates a charge on the specified subscription.
[**add_coupon_to_subscription**](SubscriptionsApi.md#add_coupon_to_subscription) | **POST** /subscriptions/{subscription-ID}/coupons | Applies a coupon to a subscription.
[**add_credit_note_to_subscription**](SubscriptionsApi.md#add_credit_note_to_subscription) | **POST** /subscriptions/{subscription-ID}/credit | Creates a credit-note which may be used by only the specified subscription.
[**add_payment_method_to_subscription**](SubscriptionsApi.md#add_payment_method_to_subscription) | **POST** /subscriptions/{subscription-ID}/payment-methods | Enables the payment method to pay invoices of this subscription.
[**advance_subscription**](SubscriptionsApi.md#advance_subscription) | **POST** /subscriptions/{subscription-ID}/advance | Advance the subscription through time.
[**available_payment_methods_for_subscription**](SubscriptionsApi.md#available_payment_methods_for_subscription) | **GET** /subscriptions/{subscription-ID}/payment-methods | Returns all available payment methods for the specified subscription. By default 10 values are returned. Records are returned in natural order.
[**batch_create_subscriptions**](SubscriptionsApi.md#batch_create_subscriptions) | **POST** /subscriptions/batch | Create multiple subscriptions.
[**cancel_subscription**](SubscriptionsApi.md#cancel_subscription) | **POST** /subscriptions/{subscription-ID}/cancel | Retires the subscription specified by the subscription-ID parameter. Retiring a subscription causes it to cancel based on the specified retirement settings for the product.
[**create_aggregating_subscription**](SubscriptionsApi.md#create_aggregating_subscription) | **POST** /subscriptions/aggregating | Create an aggregating subscription.
[**create_subscription**](SubscriptionsApi.md#create_subscription) | **POST** /subscriptions | Create a new subscription.
[**create_subscription_v2**](SubscriptionsApi.md#create_subscription_v2) | **POST** /subscriptions/create | Create a subscription (V2).
[**create_timer**](SubscriptionsApi.md#create_timer) | **POST** /subscriptions/{subscription-ID}/timer | Create a timer for a subscription event.
[**delete_metadata_for_subscription**](SubscriptionsApi.md#delete_metadata_for_subscription) | **DELETE** /subscriptions/{subscription-ID}/metadata | Remove any associated metadata.
[**freeze_subscription**](SubscriptionsApi.md#freeze_subscription) | **POST** /subscriptions/{subscription-ID}/freeze | Freeze the subscription.
[**get_all_subscriptions**](SubscriptionsApi.md#get_all_subscriptions) | **GET** /subscriptions | Retrieves a collection of all subscriptions. By default 10 values are returned. Records are returned in natural order.
[**get_applicable_coupons_for_subscription**](SubscriptionsApi.md#get_applicable_coupons_for_subscription) | **GET** /subscriptions/{subscription-ID}/applicable-coupons | Retrieves a collection of the coupons which can be applied to this subscription.
[**get_available_credit_subscription**](SubscriptionsApi.md#get_available_credit_subscription) | **GET** /subscriptions/{subscription-ID}/credit | Returns all available credit-notes for the specified subscription. By default 10 values are returned. Records are returned in natural order.
[**get_charges_on_subscription**](SubscriptionsApi.md#get_charges_on_subscription) | **GET** /subscriptions/{subscription-ID}/charges | Returns all charges for the specified subscription. By default 10 values are returned. Records are returned in natural order.
[**get_children_of_subscription**](SubscriptionsApi.md#get_children_of_subscription) | **GET** /subscriptions/{subscription-ID}/children | Return all entities whose invoices will be aggregated by the specified subscription By default 10 values are returned. Records are returned in natural order.
[**get_coupons_on_subscription**](SubscriptionsApi.md#get_coupons_on_subscription) | **GET** /subscriptions/{subscription-ID}/coupons | Retrieves a collection of the coupons and the unique codes currently applied to the subscription.
[**get_invoices_for_subscription_by_state**](SubscriptionsApi.md#get_invoices_for_subscription_by_state) | **GET** /subscriptions/{subscriptionID}/invoices/{state} | Retrieves a collection of invoice objects of the specified state for the given subscription. By default 10 values are returned. Records are returned in natural order.
[**get_metadata_for_subscription**](SubscriptionsApi.md#get_metadata_for_subscription) | **GET** /subscriptions/{subscription-ID}/metadata | Retrieve any associated metadata.
[**get_parent_subscription**](SubscriptionsApi.md#get_parent_subscription) | **GET** /subscriptions/{subscription-ID}/parent | Return the parent of the given subscription.
[**get_pricing_component_values_of_subscription**](SubscriptionsApi.md#get_pricing_component_values_of_subscription) | **GET** /subscriptions/{subscription-ID}/values | Gets the subscription&#39;s current pricing-component values.
[**get_subscription_by_account_id**](SubscriptionsApi.md#get_subscription_by_account_id) | **GET** /subscriptions/account/{account-ID} | Retrieves a collection of subscriptions, specified by the account-ID parameter. By default 10 values are returned. Records are returned in natural order.
[**get_subscription_by_id**](SubscriptionsApi.md#get_subscription_by_id) | **GET** /subscriptions/{subscription-ID} | Retrieves a single subscription, specified by the ID parameter.
[**get_subscription_by_product_id**](SubscriptionsApi.md#get_subscription_by_product_id) | **GET** /subscriptions/product/{product-ID} | Retrieves a collection of subscriptions, specified by the product-ID parameter. By default 10 values are returned. Records are returned in natural order.
[**get_subscription_by_product_rate_plan_id**](SubscriptionsApi.md#get_subscription_by_product_rate_plan_id) | **GET** /subscriptions/product-rate-plan/{product-rate-plan-ID} | Retrieves a collection of subscriptions, specified by the product-rate-plan-ID parameter. By default 10 values are returned. Records are returned in natural order.
[**get_subscription_by_state**](SubscriptionsApi.md#get_subscription_by_state) | **GET** /subscriptions/state/{state} | Retrieves a collection of subscriptions, specified by the state parameter. By default 10 values are returned. Records are returned in natural order.
[**get_subscription_by_version_id**](SubscriptionsApi.md#get_subscription_by_version_id) | **GET** /subscriptions/version/{version-ID} | Retrieves a single subscription, specified by the version-ID parameter.
[**get_subscriptions_by_initial_period_start**](SubscriptionsApi.md#get_subscriptions_by_initial_period_start) | **GET** /subscriptions/initial-period-start/{lower-threshold}/{upper-threshold} | Retrieves a collection of subscription objects with period-end times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.
[**get_subscriptions_by_period_end**](SubscriptionsApi.md#get_subscriptions_by_period_end) | **GET** /subscriptions/period-end/{lower-threshold}/{upper-threshold} | Retrieves a collection of subscription objects with period-end times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.
[**get_subscriptions_by_period_start**](SubscriptionsApi.md#get_subscriptions_by_period_start) | **GET** /subscriptions/period-start/{lower-threshold}/{upper-threshold} | Retrieves a collection of subscription objects with period-start times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.
[**get_subscriptions_by_successful_periods**](SubscriptionsApi.md#get_subscriptions_by_successful_periods) | **GET** /subscriptions/successful-periods/{lower-threshold}/{upper-threshold} | Retrieves a collection of subscription objects whose successful periods count falls within the range specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.
[**get_swagger_subscription**](SubscriptionsApi.md#get_swagger_subscription) | **GET** /subscriptions/swagger-end-point/{query-string} | 
[**get_timers_for_subscription**](SubscriptionsApi.md#get_timers_for_subscription) | **GET** /subscriptions/{subscription-ID}/timer | Retrieves a collection timer amendments for the specified subscription.. By default 10 values are returned. Records are returned in natural order.
[**import_subscription**](SubscriptionsApi.md#import_subscription) | **POST** /subscriptions/import | Import a subscription.
[**invoice_charges_on_subscription**](SubscriptionsApi.md#invoice_charges_on_subscription) | **POST** /subscriptions/{subscription-ID}/invoice-charges | Invoice any outstanding charges for the subscription.
[**migrate_subscription**](SubscriptionsApi.md#migrate_subscription) | **POST** /subscriptions/{subscription-ID}/migrate | Migrate the subscription to a new plan.
[**remove_coupon_from_subscription**](SubscriptionsApi.md#remove_coupon_from_subscription) | **DELETE** /subscriptions/{subscription-ID}/coupons/{coupon-code} | Removes the coupon from the subscription.
[**remove_credit_from_subscription**](SubscriptionsApi.md#remove_credit_from_subscription) | **DELETE** /subscriptions/{subscription-ID}/credit/{value} | Decrease the amount of credit available to the specified subscription.
[**remove_payment_method_from_subscription**](SubscriptionsApi.md#remove_payment_method_from_subscription) | **DELETE** /subscriptions/{subscription-ID}/payment-methods/{payment-method-ID} | Removes the specified payment method for the given subscription.
[**remove_pricing_component_value_change_from_subscription**](SubscriptionsApi.md#remove_pricing_component_value_change_from_subscription) | **DELETE** /subscriptions/{subscription-ID}/values/{pricing-component} | Discards from the subscription any scheduled changes in the value of the specified pricing-component.
[**resume_subscription**](SubscriptionsApi.md#resume_subscription) | **POST** /subscriptions/{subscription-ID}/resume | Resume the frozen subscription.
[**revive_subscription**](SubscriptionsApi.md#revive_subscription) | **POST** /subscriptions/{subscription-ID}/revive | Revives a cancelled subscription and returns it to its previous state
[**set_metadata_for_subscription**](SubscriptionsApi.md#set_metadata_for_subscription) | **POST** /subscriptions/{subscription-ID}/metadata | Remove any existing metadata keys and create the provided data.
[**set_pricing_component_value_on_subscription**](SubscriptionsApi.md#set_pricing_component_value_on_subscription) | **POST** /subscriptions/{subscription-ID}/pricing-component-values | Sets upon this subscription a new value for the specified pricing-component without performing an upgrade.
[**set_pricing_component_value_on_subscription_v2**](SubscriptionsApi.md#set_pricing_component_value_on_subscription_v2) | **POST** /subscriptions/{subscription-ID}/values/{pricing-component} | Upgrades/downgrades this subscription to some new value for the specified pricing-component.
[**update_subscription**](SubscriptionsApi.md#update_subscription) | **PUT** /subscriptions | Update a subscription.
[**update_subscription_v2**](SubscriptionsApi.md#update_subscription_v2) | **PUT** /subscriptions/update | Update a subscription (V2).
[**upsert_metadata_for_subscription**](SubscriptionsApi.md#upsert_metadata_for_subscription) | **PUT** /subscriptions/{subscription-ID}/metadata | Update any existing metadata key-values and insert any new key-values, no keys will be removed.


# **add_charge_to_subscription**
> SubscriptionChargePagedMetadata add_charge_to_subscription(subscription_id, charge)

Creates a charge on the specified subscription.

{\"nickname\":\"Add Charge\",\"response\":\"addChargeToSubscriptionRequest.html\",\"response\":\"addChargeToSubscription.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | ID of the subscription.
charge = swagger_client.AddChargeRequest() # AddChargeRequest | The charge request

try: 
    # Creates a charge on the specified subscription.
    api_response = api_instance.add_charge_to_subscription(subscription_id, charge)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->add_charge_to_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| ID of the subscription. | 
 **charge** | [**AddChargeRequest**](AddChargeRequest.md)| The charge request | 

### Return type

[**SubscriptionChargePagedMetadata**](SubscriptionChargePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_coupon_to_subscription**
> CouponPagedMetadata add_coupon_to_subscription(subscription_id, request)

Applies a coupon to a subscription.

{\"nickname\":\"Apply coupon\", \"request\":\"addCouponCodeRequest.html\",\"response\":\"addCouponCodeResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 
request = swagger_client.AddCouponCodeRequest() # AddCouponCodeRequest | Request containing the coupon code.

try: 
    # Applies a coupon to a subscription.
    api_response = api_instance.add_coupon_to_subscription(subscription_id, request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->add_coupon_to_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **request** | [**AddCouponCodeRequest**](AddCouponCodeRequest.md)| Request containing the coupon code. | 

### Return type

[**CouponPagedMetadata**](CouponPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_credit_note_to_subscription**
> CreditNotePagedMetadata add_credit_note_to_subscription(subscription_id, credit_note)

Creates a credit-note which may be used by only the specified subscription.

{\"nickname\":\"Add Credit\",\"request\":\"addCreditNoteToSubscriptionRequest.html\", \"response\":\"addCreditNoteToSubscription.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | ID of the subscription.
credit_note = swagger_client.CreditSubscriptionRequest() # CreditSubscriptionRequest | The credit-note request

try: 
    # Creates a credit-note which may be used by only the specified subscription.
    api_response = api_instance.add_credit_note_to_subscription(subscription_id, credit_note)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->add_credit_note_to_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| ID of the subscription. | 
 **credit_note** | [**CreditSubscriptionRequest**](CreditSubscriptionRequest.md)| The credit-note request | 

### Return type

[**CreditNotePagedMetadata**](CreditNotePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_payment_method_to_subscription**
> PaymentMethodPagedMetadata add_payment_method_to_subscription(subscription_id, payment_method)

Enables the payment method to pay invoices of this subscription.

{\"nickname\":\"Add payment-method to subscription\",\"response\":\"addPaymentMethod.html\",\"request\":\"addPaymentMethod.request.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 
payment_method = swagger_client.AddPaymentMethodRequest() # AddPaymentMethodRequest | 

try: 
    # Enables the payment method to pay invoices of this subscription.
    api_response = api_instance.add_payment_method_to_subscription(subscription_id, payment_method)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->add_payment_method_to_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **payment_method** | [**AddPaymentMethodRequest**](AddPaymentMethodRequest.md)|  | 

### Return type

[**PaymentMethodPagedMetadata**](PaymentMethodPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **advance_subscription**
> TimeResponsePagedMetadata advance_subscription(subscription_id, request)

Advance the subscription through time.

{\"nickname\":\"Advance\",\"request\":\"advanceSubscriptionRequest.html\",\"response\":\"advanceSubscription.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | ID of the subscription.
request = swagger_client.TimeRequest() # TimeRequest | The request

try: 
    # Advance the subscription through time.
    api_response = api_instance.advance_subscription(subscription_id, request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->advance_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| ID of the subscription. | 
 **request** | [**TimeRequest**](TimeRequest.md)| The request | 

### Return type

[**TimeResponsePagedMetadata**](TimeResponsePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **available_payment_methods_for_subscription**
> PaymentMethodPagedMetadata available_payment_methods_for_subscription(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Returns all available payment methods for the specified subscription. By default 10 values are returned. Records are returned in natural order.

{ \"nickname\" : \"List on subscription\",\"response\" : \"getAvailablePaymentMethods.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first subscription to return. (optional) (default to 0)
records = 10 # int | The maximum number of subscriptions to return. (optional) (default to 10)
order_by = 'id' # str | Specify a field used to order the result set. (optional) (default to id)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Returns all available payment methods for the specified subscription. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.available_payment_methods_for_subscription(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->available_payment_methods_for_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first subscription to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of subscriptions to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to id]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**PaymentMethodPagedMetadata**](PaymentMethodPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_create_subscriptions**
> SubscriptionPagedMetadata batch_create_subscriptions(request)

Create multiple subscriptions.

{\"nickname\":\"Create multiple subscriptions\",\"response\":\"createMultipleSubscriptionViaHelper.html\",\"request\":\"createMultipleSubscriptionViaHelper.request.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
request = swagger_client.CreateSubscriptionBatchRequest() # CreateSubscriptionBatchRequest | 

try: 
    # Create multiple subscriptions.
    api_response = api_instance.batch_create_subscriptions(request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->batch_create_subscriptions: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreateSubscriptionBatchRequest**](CreateSubscriptionBatchRequest.md)|  | 

### Return type

[**SubscriptionPagedMetadata**](SubscriptionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_subscription**
> SubscriptionCancellationPagedMetadata cancel_subscription(subscription_id, subscription_cancellation)

Retires the subscription specified by the subscription-ID parameter. Retiring a subscription causes it to cancel based on the specified retirement settings for the product.

{\"nickname\":\"Cancel subscription\",\"response\":\"deleteSubscription.html\",\"request\":\"deleteSubscriptionRequest.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 
subscription_cancellation = swagger_client.CancelSubscriptionRequest() # CancelSubscriptionRequest | The cancellation request

try: 
    # Retires the subscription specified by the subscription-ID parameter. Retiring a subscription causes it to cancel based on the specified retirement settings for the product.
    api_response = api_instance.cancel_subscription(subscription_id, subscription_cancellation)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->cancel_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **subscription_cancellation** | [**CancelSubscriptionRequest**](CancelSubscriptionRequest.md)| The cancellation request | 

### Return type

[**SubscriptionCancellationPagedMetadata**](SubscriptionCancellationPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_aggregating_subscription**
> SubscriptionPagedMetadata create_aggregating_subscription(request)

Create an aggregating subscription.

{\"nickname\":\"Create aggregating subscription\",\"response\":\"createAggregatingSubscription.html\",\"request\":\"createAggregatingSubscription.request.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
request = swagger_client.CreateAggregatingSubscriptionRequest() # CreateAggregatingSubscriptionRequest | 

try: 
    # Create an aggregating subscription.
    api_response = api_instance.create_aggregating_subscription(request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->create_aggregating_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreateAggregatingSubscriptionRequest**](CreateAggregatingSubscriptionRequest.md)|  | 

### Return type

[**SubscriptionPagedMetadata**](SubscriptionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subscription**
> SubscriptionPagedMetadata create_subscription(subscription)

Create a new subscription.

{\"nickname\":\"Create a new subscription\",\"request\":\"createSubscriptionRequest.html\",\"response\":\"createSubscriptionResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription = swagger_client.Subscription() # Subscription | The subscription object to be updated.

try: 
    # Create a new subscription.
    api_response = api_instance.create_subscription(subscription)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->create_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription** | [**Subscription**](Subscription.md)| The subscription object to be updated. | 

### Return type

[**SubscriptionPagedMetadata**](SubscriptionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subscription_v2**
> SubscriptionPagedMetadata create_subscription_v2(request)

Create a subscription (V2).

{\"nickname\":\"Create a subscription (V2)\",\"response\":\"createSubscriptionViaHelper.html\",\"request\":\"createSubscriptionViaHelper.request.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
request = swagger_client.CreateSubscriptionRequest() # CreateSubscriptionRequest | 

try: 
    # Create a subscription (V2).
    api_response = api_instance.create_subscription_v2(request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->create_subscription_v2: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreateSubscriptionRequest**](CreateSubscriptionRequest.md)|  | 

### Return type

[**SubscriptionPagedMetadata**](SubscriptionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_timer**
> TimerAmendment create_timer(subscription_id, request)

Create a timer for a subscription event.

{\"nickname\":\"Create Timer\",\"response\":\"createSubscriptionTimer.html\",\"request\":\"createSubscriptionTimer.request.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 
request = swagger_client.BillingEntityBase() # BillingEntityBase | 

try: 
    # Create a timer for a subscription event.
    api_response = api_instance.create_timer(subscription_id, request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->create_timer: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **request** | [**BillingEntityBase**](BillingEntityBase.md)|  | 

### Return type

[**TimerAmendment**](TimerAmendment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_metadata_for_subscription**
> DynamicMetadata delete_metadata_for_subscription(subscription_id, organizations=organizations)

Remove any associated metadata.

{\"nickname\":\"Clear from subscription\",\"request\" :\"deleteSubscriptionMetadataRequest.html\",\"response\":\"deleteSubscriptionMetadataResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Remove any associated metadata.
    api_response = api_instance.delete_metadata_for_subscription(subscription_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->delete_metadata_for_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**DynamicMetadata**](DynamicMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **freeze_subscription**
> SubscriptionPagedMetadata freeze_subscription(subscription_id, request)

Freeze the subscription.

{\"nickname\":\"Freeze\",\"request\":\"freezeSubscriptionRequest.html\",\"response\":\"freezeSubscription.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | ID of the subscription.
request = swagger_client.PauseRequest() # PauseRequest | The request

try: 
    # Freeze the subscription.
    api_response = api_instance.freeze_subscription(subscription_id, request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->freeze_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| ID of the subscription. | 
 **request** | [**PauseRequest**](PauseRequest.md)| The request | 

### Return type

[**SubscriptionPagedMetadata**](SubscriptionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_subscriptions**
> SubscriptionPagedMetadata get_all_subscriptions(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, exclude_children=exclude_children, metadata=metadata, exclude_service_ended=exclude_service_ended, account_id=account_id)

Retrieves a collection of all subscriptions. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve all subscriptions\",\"response\":\"getSubscriptionAll.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first subscription to return. (optional) (default to 0)
records = 10 # int | The maximum number of subscriptions to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired subscriptions should be returned. (optional) (default to false)
exclude_children = true # bool | Should child subscriptiosn be excluded. (optional) (default to true)
metadata = 'metadata_example' # str |  (optional)
exclude_service_ended = true # bool |  (optional)
account_id = ['account_id_example'] # list[str] | A list of accountIDs to filter subscriptions on (optional)

try: 
    # Retrieves a collection of all subscriptions. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_subscriptions(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, exclude_children=exclude_children, metadata=metadata, exclude_service_ended=exclude_service_ended, account_id=account_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->get_all_subscriptions: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first subscription to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of subscriptions to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired subscriptions should be returned. | [optional] [default to false]
 **exclude_children** | **bool**| Should child subscriptiosn be excluded. | [optional] [default to true]
 **metadata** | **str**|  | [optional] 
 **exclude_service_ended** | **bool**|  | [optional] 
 **account_id** | [**list[str]**](str.md)| A list of accountIDs to filter subscriptions on | [optional] 

### Return type

[**SubscriptionPagedMetadata**](SubscriptionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_applicable_coupons_for_subscription**
> CouponPagedMetadata get_applicable_coupons_for_subscription(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Retrieves a collection of the coupons which can be applied to this subscription.

{ \"nickname\" : \"Retrieve applicable coupons\",\"response\" : \"getApplicableCoupons.html\" }

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | ID of the subscription.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first subscription to return. (optional) (default to 0)
records = 10 # int | The maximum number of subscriptions to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired subscriptions should be returned. (optional) (default to false)

try: 
    # Retrieves a collection of the coupons which can be applied to this subscription.
    api_response = api_instance.get_applicable_coupons_for_subscription(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->get_applicable_coupons_for_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| ID of the subscription. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first subscription to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of subscriptions to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired subscriptions should be returned. | [optional] [default to false]

### Return type

[**CouponPagedMetadata**](CouponPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_credit_subscription**
> CreditNotePagedMetadata get_available_credit_subscription(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns all available credit-notes for the specified subscription. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get available credit\",\"response\":\"getAvailableCreditSubscription.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first subscription to return. (optional) (default to 0)
records = 10 # int | The maximum number of subscriptions to return. (optional) (default to 10)
order_by = 'id' # str | Specify a field used to order the result set. (optional) (default to id)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired subscriptions should be returned. (optional) (default to false)

try: 
    # Returns all available credit-notes for the specified subscription. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_available_credit_subscription(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->get_available_credit_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first subscription to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of subscriptions to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to id]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired subscriptions should be returned. | [optional] [default to false]

### Return type

[**CreditNotePagedMetadata**](CreditNotePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_charges_on_subscription**
> SubscriptionChargePagedMetadata get_charges_on_subscription(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, state=state, type=type, include_retired=include_retired)

Returns all charges for the specified subscription. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get charges\",\"response\":\"getChargesSubscription.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first subscription to return. (optional) (default to 0)
records = 10 # int | The maximum number of subscriptions to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
state = 'state_example' # str | Ihe direction of any ordering, either ASC or DESC. (optional)
type = 'type_example' # str | Ihe direction of any ordering, either ASC or DESC. (optional)
include_retired = false # bool | Whether retired subscriptions should be returned. (optional) (default to false)

try: 
    # Returns all charges for the specified subscription. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_charges_on_subscription(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, state=state, type=type, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->get_charges_on_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first subscription to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of subscriptions to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **state** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] 
 **type** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] 
 **include_retired** | **bool**| Whether retired subscriptions should be returned. | [optional] [default to false]

### Return type

[**SubscriptionChargePagedMetadata**](SubscriptionChargePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_children_of_subscription**
> SubscriptionPagedMetadata get_children_of_subscription(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Return all entities whose invoices will be aggregated by the specified subscription By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get Aggregated Entities\",\"response\":\"getAggregatedEntities.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first subscription to return. (optional) (default to 0)
records = 10 # int | The maximum number of subscriptions to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired subscriptions should be returned. (optional) (default to false)

try: 
    # Return all entities whose invoices will be aggregated by the specified subscription By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_children_of_subscription(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->get_children_of_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first subscription to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of subscriptions to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired subscriptions should be returned. | [optional] [default to false]

### Return type

[**SubscriptionPagedMetadata**](SubscriptionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupons_on_subscription**
> CouponPagedMetadata get_coupons_on_subscription(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Retrieves a collection of the coupons and the unique codes currently applied to the subscription.

{\"nickname\":\"Retrieve coupons\",\"response\":\"getCoupons.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | ID of the subscription.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first subscription to return. (optional) (default to 0)
records = 10 # int | The maximum number of subscriptions to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired subscriptions should be returned. (optional) (default to false)

try: 
    # Retrieves a collection of the coupons and the unique codes currently applied to the subscription.
    api_response = api_instance.get_coupons_on_subscription(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->get_coupons_on_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| ID of the subscription. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first subscription to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of subscriptions to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired subscriptions should be returned. | [optional] [default to false]

### Return type

[**CouponPagedMetadata**](CouponPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices_for_subscription_by_state**
> InvoicePagedMetadata get_invoices_for_subscription_by_state(subscription_id, state, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Retrieves a collection of invoice objects of the specified state for the given subscription. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve invoices by state for subscription\",\"response\":\"getInvoicesForSubscriptionByState.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | The unique id of the subscription.
state = 'state_example' # str | The state of the invoices to retrieve.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first taxation-link to return. (optional) (default to 0)
records = 10 # int | The maximum number of taxation-links to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Retrieves a collection of invoice objects of the specified state for the given subscription. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_invoices_for_subscription_by_state(subscription_id, state, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->get_invoices_for_subscription_by_state: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| The unique id of the subscription. | 
 **state** | **str**| The state of the invoices to retrieve. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first taxation-link to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of taxation-links to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**InvoicePagedMetadata**](InvoicePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_for_subscription**
> DynamicMetadata get_metadata_for_subscription(subscription_id, organizations=organizations)

Retrieve any associated metadata.

{\"nickname\":\"Retrieve on subscription\",\"request\":\"getSubscriptionMetadataRequest.html\",\"response\":\"getSubscriptionMetadataResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Retrieve any associated metadata.
    api_response = api_instance.get_metadata_for_subscription(subscription_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->get_metadata_for_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**DynamicMetadata**](DynamicMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parent_subscription**
> SubscriptionPagedMetadata get_parent_subscription(subscription_id, organizations=organizations)

Return the parent of the given subscription.

{\"nickname\":\"Get parent\",\"response\":\"getParentSubscription.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Return the parent of the given subscription.
    api_response = api_instance.get_parent_subscription(subscription_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->get_parent_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**SubscriptionPagedMetadata**](SubscriptionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pricing_component_values_of_subscription**
> PricingComponentValuePagedMetadata get_pricing_component_values_of_subscription(subscription_id)

Gets the subscription's current pricing-component values.

{\"nickname\":\"Get values\",\"response\":\"getPricingComponentValues.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | ID of the subscription.

try: 
    # Gets the subscription's current pricing-component values.
    api_response = api_instance.get_pricing_component_values_of_subscription(subscription_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->get_pricing_component_values_of_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| ID of the subscription. | 

### Return type

[**PricingComponentValuePagedMetadata**](PricingComponentValuePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_by_account_id**
> SubscriptionPagedMetadata get_subscription_by_account_id(account_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, exclude_children=exclude_children)

Retrieves a collection of subscriptions, specified by the account-ID parameter. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by account\",\"response\":\"getSubscriptionByAccount.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
account_id = 'account_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first subscription to return. (optional) (default to 0)
records = 10 # int | The maximum number of subscriptions to return. (optional) (default to 10)
order_by = 'id' # str | Specify a field used to order the result set. (optional) (default to id)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired subscriptions should be returned. (optional) (default to false)
exclude_children = true # bool | Should child subscriptiosn be excluded. (optional) (default to true)

try: 
    # Retrieves a collection of subscriptions, specified by the account-ID parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_subscription_by_account_id(account_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, exclude_children=exclude_children)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->get_subscription_by_account_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first subscription to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of subscriptions to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to id]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired subscriptions should be returned. | [optional] [default to false]
 **exclude_children** | **bool**| Should child subscriptiosn be excluded. | [optional] [default to true]

### Return type

[**SubscriptionPagedMetadata**](SubscriptionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_by_id**
> SubscriptionPagedMetadata get_subscription_by_id(subscription_id, organizations=organizations, include_retired=include_retired)

Retrieves a single subscription, specified by the ID parameter.

{\"nickname\":\"Retrieve an existing subscription\",\"response\":\"getSubscriptionByID.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
include_retired = false # bool | Whether retired subscriptions should be returned. (optional) (default to false)

try: 
    # Retrieves a single subscription, specified by the ID parameter.
    api_response = api_instance.get_subscription_by_id(subscription_id, organizations=organizations, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->get_subscription_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **include_retired** | **bool**| Whether retired subscriptions should be returned. | [optional] [default to false]

### Return type

[**SubscriptionPagedMetadata**](SubscriptionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_by_product_id**
> SubscriptionPagedMetadata get_subscription_by_product_id(product_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, exclude_children=exclude_children)

Retrieves a collection of subscriptions, specified by the product-ID parameter. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by product\",\"response\":\"getSubscriptionByProduct.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
product_id = 'product_id_example' # str | ID of the product
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first subscription to return. (optional) (default to 0)
records = 10 # int | The maximum number of subscriptions to return. (optional) (default to 10)
order_by = 'id' # str | Specify a field used to order the result set. (optional) (default to id)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired subscriptions should be returned. (optional) (default to false)
exclude_children = true # bool | Should child subscriptiosn be excluded. (optional) (default to true)

try: 
    # Retrieves a collection of subscriptions, specified by the product-ID parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_subscription_by_product_id(product_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, exclude_children=exclude_children)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->get_subscription_by_product_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of the product | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first subscription to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of subscriptions to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to id]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired subscriptions should be returned. | [optional] [default to false]
 **exclude_children** | **bool**| Should child subscriptiosn be excluded. | [optional] [default to true]

### Return type

[**SubscriptionPagedMetadata**](SubscriptionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_by_product_rate_plan_id**
> SubscriptionPagedMetadata get_subscription_by_product_rate_plan_id(product_rate_plan_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, exclude_children=exclude_children)

Retrieves a collection of subscriptions, specified by the product-rate-plan-ID parameter. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by rate-plan\",\"response\":\"getSubscriptionByProductRatePlan.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
product_rate_plan_id = 'product_rate_plan_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first subscription to return. (optional) (default to 0)
records = 10 # int | The maximum number of subscriptions to return. (optional) (default to 10)
order_by = 'id' # str | Specify a field used to order the result set. (optional) (default to id)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired subscriptions should be returned. (optional) (default to false)
exclude_children = true # bool | Should child subscriptiosn be excluded. (optional) (default to true)

try: 
    # Retrieves a collection of subscriptions, specified by the product-rate-plan-ID parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_subscription_by_product_rate_plan_id(product_rate_plan_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, exclude_children=exclude_children)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->get_subscription_by_product_rate_plan_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_rate_plan_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first subscription to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of subscriptions to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to id]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired subscriptions should be returned. | [optional] [default to false]
 **exclude_children** | **bool**| Should child subscriptiosn be excluded. | [optional] [default to true]

### Return type

[**SubscriptionPagedMetadata**](SubscriptionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_by_state**
> SubscriptionPagedMetadata get_subscription_by_state(state, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, exclude_children=exclude_children)

Retrieves a collection of subscriptions, specified by the state parameter. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by state\",\"response\":\"getSubscriptionByState.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
state = 'state_example' # str | The current state of the subscription, either Provisioned, AwaitingPayment, Paid or Cancelled
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first subscription to return. (optional) (default to 0)
records = 10 # int | The maximum number of subscriptions to return. (optional) (default to 10)
order_by = 'id' # str | Specify a field used to order the result set. (optional) (default to id)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired subscriptions should be returned. (optional) (default to false)
exclude_children = true # bool | Should child subscriptiosn be excluded. (optional) (default to true)

try: 
    # Retrieves a collection of subscriptions, specified by the state parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_subscription_by_state(state, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, exclude_children=exclude_children)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->get_subscription_by_state: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| The current state of the subscription, either Provisioned, AwaitingPayment, Paid or Cancelled | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first subscription to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of subscriptions to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to id]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired subscriptions should be returned. | [optional] [default to false]
 **exclude_children** | **bool**| Should child subscriptiosn be excluded. | [optional] [default to true]

### Return type

[**SubscriptionPagedMetadata**](SubscriptionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_by_version_id**
> SubscriptionPagedMetadata get_subscription_by_version_id(version_id, organizations=organizations)

Retrieves a single subscription, specified by the version-ID parameter.

{\"nickname\":\"Retrieve by version\",\"response\":\"getSubscriptionByVersionID.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
version_id = 'version_id_example' # str | The version-ID of the subscription.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Retrieves a single subscription, specified by the version-ID parameter.
    api_response = api_instance.get_subscription_by_version_id(version_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->get_subscription_by_version_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | **str**| The version-ID of the subscription. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**SubscriptionPagedMetadata**](SubscriptionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscriptions_by_initial_period_start**
> SubscriptionPagedMetadata get_subscriptions_by_initial_period_start(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Retrieves a collection of subscription objects with period-end times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by initial period-start\",\"response\":\"getSubscriptionByInitialPeriodStart.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
lower_threshold = 'lower_threshold_example' # str | The UTC DateTime specifying the start of the result period.
upper_threshold = 'upper_threshold_example' # str | The UTC DateTime specifying the end of the result period.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first taxation-link to return. (optional) (default to 0)
records = 10 # int | The maximum number of taxation-links to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Retrieves a collection of subscription objects with period-end times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_subscriptions_by_initial_period_start(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->get_subscriptions_by_initial_period_start: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lower_threshold** | **str**| The UTC DateTime specifying the start of the result period. | 
 **upper_threshold** | **str**| The UTC DateTime specifying the end of the result period. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first taxation-link to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of taxation-links to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**SubscriptionPagedMetadata**](SubscriptionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscriptions_by_period_end**
> SubscriptionPagedMetadata get_subscriptions_by_period_end(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Retrieves a collection of subscription objects with period-end times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by period-end\",\"response\":\"getSubscriptionByPeriodEnd.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
lower_threshold = 'lower_threshold_example' # str | The UTC DateTime specifying the start of the result period.
upper_threshold = 'upper_threshold_example' # str | The UTC DateTime specifying the end of the result period.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first taxation-link to return. (optional) (default to 0)
records = 10 # int | The maximum number of taxation-links to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Retrieves a collection of subscription objects with period-end times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_subscriptions_by_period_end(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->get_subscriptions_by_period_end: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lower_threshold** | **str**| The UTC DateTime specifying the start of the result period. | 
 **upper_threshold** | **str**| The UTC DateTime specifying the end of the result period. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first taxation-link to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of taxation-links to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**SubscriptionPagedMetadata**](SubscriptionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscriptions_by_period_start**
> SubscriptionPagedMetadata get_subscriptions_by_period_start(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Retrieves a collection of subscription objects with period-start times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by period-start\",\"response\":\"getSubscriptionByPeriodStart.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
lower_threshold = 'lower_threshold_example' # str | The UTC DateTime specifying the start of the result period.
upper_threshold = 'upper_threshold_example' # str | The UTC DateTime specifying the end of the result period.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first taxation-link to return. (optional) (default to 0)
records = 10 # int | The maximum number of taxation-links to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Retrieves a collection of subscription objects with period-start times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_subscriptions_by_period_start(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->get_subscriptions_by_period_start: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lower_threshold** | **str**| The UTC DateTime specifying the start of the result period. | 
 **upper_threshold** | **str**| The UTC DateTime specifying the end of the result period. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first taxation-link to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of taxation-links to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**SubscriptionPagedMetadata**](SubscriptionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscriptions_by_successful_periods**
> SubscriptionPagedMetadata get_subscriptions_by_successful_periods(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Retrieves a collection of subscription objects whose successful periods count falls within the range specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by successful period\",\"response\":\"getSubscriptionBySuccessfulPeriods.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
lower_threshold = 56 # int | The lower threshold of the range
upper_threshold = 56 # int | The upper threshold of the range.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first taxation-link to return. (optional) (default to 0)
records = 10 # int | The maximum number of taxation-links to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Retrieves a collection of subscription objects whose successful periods count falls within the range specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_subscriptions_by_successful_periods(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->get_subscriptions_by_successful_periods: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lower_threshold** | **int**| The lower threshold of the range | 
 **upper_threshold** | **int**| The upper threshold of the range. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first taxation-link to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of taxation-links to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**SubscriptionPagedMetadata**](SubscriptionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_swagger_subscription**
> SwaggerTypeListSubs get_swagger_subscription(query_string, organizations=organizations, offset=offset, records=records, format=format, wildcard=wildcard, entity=entity)



{ \"nickname\" : \"\",\"response\" : \"\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
query_string = 'query_string_example' # str | The query string used to search.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The starting index of the search results. (optional) (default to 0)
records = 10 # int | The number of search results to return. (optional) (default to 10)
format = 'JSON' # str | The response format, either JSON or XML. (optional) (default to JSON)
wildcard = false # bool | Toggle if we search for full words or whether a wildcard is used. (optional) (default to false)
entity = false # bool | Is an entity returned with the search results. (optional) (default to false)

try: 
    # 
    api_response = api_instance.get_swagger_subscription(query_string, organizations=organizations, offset=offset, records=records, format=format, wildcard=wildcard, entity=entity)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->get_swagger_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_string** | **str**| The query string used to search. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The starting index of the search results. | [optional] [default to 0]
 **records** | **int**| The number of search results to return. | [optional] [default to 10]
 **format** | **str**| The response format, either JSON or XML. | [optional] [default to JSON]
 **wildcard** | **bool**| Toggle if we search for full words or whether a wildcard is used. | [optional] [default to false]
 **entity** | **bool**| Is an entity returned with the search results. | [optional] [default to false]

### Return type

[**SwaggerTypeListSubs**](SwaggerTypeListSubs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_timers_for_subscription**
> TimerAmendment get_timers_for_subscription(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, state=state, event=event)

Retrieves a collection timer amendments for the specified subscription.. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get Timers\",\"response\":\"getTimersforSubscription.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first subscription to return. (optional) (default to 0)
records = 10 # int | The maximum number of subscriptions to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired timers should be returned. (optional) (default to false)
state = 'state_example' # str | The state of the timer amendment (optional)
event = 'event_example' # str | The type of timer event (optional)

try: 
    # Retrieves a collection timer amendments for the specified subscription.. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_timers_for_subscription(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, state=state, event=event)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->get_timers_for_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first subscription to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of subscriptions to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired timers should be returned. | [optional] [default to false]
 **state** | **str**| The state of the timer amendment | [optional] 
 **event** | **str**| The type of timer event | [optional] 

### Return type

[**TimerAmendment**](TimerAmendment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_subscription**
> SubscriptionPagedMetadata import_subscription(request)

Import a subscription.

{\"nickname\":\"Import\",\"request\":\"importSubscriptionRequest.html\",\"response\":\"importSubscription.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
request = swagger_client.BillingEntityBase() # BillingEntityBase | The request

try: 
    # Import a subscription.
    api_response = api_instance.import_subscription(request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->import_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**BillingEntityBase**](BillingEntityBase.md)| The request | 

### Return type

[**SubscriptionPagedMetadata**](SubscriptionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoice_charges_on_subscription**
> InvoicePagedMetadata invoice_charges_on_subscription(subscription_id, charge)

Invoice any outstanding charges for the subscription.

{\"nickname\":\"Invoice Charges\",\"request\":\"invoiceChargesRequest.html\",\"response\":\"invoiceCharges.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | ID of the subscription.
charge = swagger_client.InvoiceChargeRequest() # InvoiceChargeRequest | The charge request

try: 
    # Invoice any outstanding charges for the subscription.
    api_response = api_instance.invoice_charges_on_subscription(subscription_id, charge)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->invoice_charges_on_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| ID of the subscription. | 
 **charge** | [**InvoiceChargeRequest**](InvoiceChargeRequest.md)| The charge request | 

### Return type

[**InvoicePagedMetadata**](InvoicePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrate_subscription**
> SubscriptionPagedMetadata migrate_subscription(subscription_id, request)

Migrate the subscription to a new plan.

{\"nickname\":\"Migrate\",\"request\":\"migrateSubscriptionRequest.html\", \"response\":\"migrateSubscription.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | ID of the subscription.
request = swagger_client.MigrationRequest() # MigrationRequest | The migration request

try: 
    # Migrate the subscription to a new plan.
    api_response = api_instance.migrate_subscription(subscription_id, request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->migrate_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| ID of the subscription. | 
 **request** | [**MigrationRequest**](MigrationRequest.md)| The migration request | 

### Return type

[**SubscriptionPagedMetadata**](SubscriptionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_coupon_from_subscription**
> CouponPagedMetadata remove_coupon_from_subscription(subscription_id, coupon_code, organizations=organizations)

Removes the coupon from the subscription.

{\"nickname\":\"Remove coupon\",\"response\":\"removeCouponResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 
coupon_code = 'coupon_code_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Removes the coupon from the subscription.
    api_response = api_instance.remove_coupon_from_subscription(subscription_id, coupon_code, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->remove_coupon_from_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **coupon_code** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**CouponPagedMetadata**](CouponPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_credit_from_subscription**
> CreditNotePagedMetadata remove_credit_from_subscription(subscription_id, value, organizations=organizations)

Decrease the amount of credit available to the specified subscription.

{\"nickname\":\"Remove Credit\",\"response\":\"removeCreditForSubscription.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 
value = 'value_example' # str | <p>Either a credit note ID or a currency value.</p><p>If a credit note ID is provided any remaining credit will be removed.</p><p>If a decimal is provided this value will be removed from any credit available to the subscription. For example if the subscription is in USD setting the value as 10 will reduce credit by $10 (USD), setting 9.86  would reduce the credit by $9.86 (USD). The value will be reduced from any credit available.</p>
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Decrease the amount of credit available to the specified subscription.
    api_response = api_instance.remove_credit_from_subscription(subscription_id, value, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->remove_credit_from_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **value** | **str**| &lt;p&gt;Either a credit note ID or a currency value.&lt;/p&gt;&lt;p&gt;If a credit note ID is provided any remaining credit will be removed.&lt;/p&gt;&lt;p&gt;If a decimal is provided this value will be removed from any credit available to the subscription. For example if the subscription is in USD setting the value as 10 will reduce credit by $10 (USD), setting 9.86  would reduce the credit by $9.86 (USD). The value will be reduced from any credit available.&lt;/p&gt; | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**CreditNotePagedMetadata**](CreditNotePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_payment_method_from_subscription**
> PaymentMethodPagedMetadata remove_payment_method_from_subscription(subscription_id, payment_method_id, organizations=organizations)

Removes the specified payment method for the given subscription.

{\"nickname\":\"Remove payment-method\",\"response\":\"removePaymentMethod.html\",\"request\":\"removePaymentMethod.request.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 
payment_method_id = 'payment_method_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Removes the specified payment method for the given subscription.
    api_response = api_instance.remove_payment_method_from_subscription(subscription_id, payment_method_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->remove_payment_method_from_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **payment_method_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**PaymentMethodPagedMetadata**](PaymentMethodPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_pricing_component_value_change_from_subscription**
> PaymentMethodPagedMetadata remove_pricing_component_value_change_from_subscription(subscription_id, pricing_component, organizations=organizations)

Discards from the subscription any scheduled changes in the value of the specified pricing-component.

{\"nickname\":\"Discard value changes\",\"response\":\"removePricingComponentValueChange.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 
pricing_component = 'pricing_component_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Discards from the subscription any scheduled changes in the value of the specified pricing-component.
    api_response = api_instance.remove_pricing_component_value_change_from_subscription(subscription_id, pricing_component, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->remove_pricing_component_value_change_from_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **pricing_component** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**PaymentMethodPagedMetadata**](PaymentMethodPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_subscription**
> SubscriptionPagedMetadata resume_subscription(subscription_id, request)

Resume the frozen subscription.

{\"nickname\":\"Resume\",\"request\":\"resumeSubscriptionRequest.html\",\"response\":\"resumeSubscription.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | ID of the subscription.
request = swagger_client.ResumeRequest() # ResumeRequest | The request

try: 
    # Resume the frozen subscription.
    api_response = api_instance.resume_subscription(subscription_id, request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->resume_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| ID of the subscription. | 
 **request** | [**ResumeRequest**](ResumeRequest.md)| The request | 

### Return type

[**SubscriptionPagedMetadata**](SubscriptionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revive_subscription**
> SubscriptionPagedMetadata revive_subscription(subscription_id, request)

Revives a cancelled subscription and returns it to its previous state

{\"nickname\":\"Revive subscription\",\"request\":\"reviveSubscriptionRequest.html\", \"response\":\"reviveSubscription.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 
request = swagger_client.ReviveSubscriptionRequest() # ReviveSubscriptionRequest | The revive request

try: 
    # Revives a cancelled subscription and returns it to its previous state
    api_response = api_instance.revive_subscription(subscription_id, request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->revive_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **request** | [**ReviveSubscriptionRequest**](ReviveSubscriptionRequest.md)| The revive request | 

### Return type

[**SubscriptionPagedMetadata**](SubscriptionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_metadata_for_subscription**
> DynamicMetadata set_metadata_for_subscription(metadata, subscription_id, organizations=organizations)

Remove any existing metadata keys and create the provided data.

{\"nickname\":\"Set on subscription\",\"request\":\"setSubscriptionMetadataRequest.html\",\"response\":\"setSubscriptionMetadataResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
metadata = swagger_client.DynamicMetadata() # DynamicMetadata | 
subscription_id = 'subscription_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Remove any existing metadata keys and create the provided data.
    api_response = api_instance.set_metadata_for_subscription(metadata, subscription_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->set_metadata_for_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata** | [**DynamicMetadata**](DynamicMetadata.md)|  | 
 **subscription_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**DynamicMetadata**](DynamicMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_pricing_component_value_on_subscription**
> PricingComponentValuePagedMetadata set_pricing_component_value_on_subscription(subscription_id, pricing_component_value)

Sets upon this subscription a new value for the specified pricing-component without performing an upgrade.

{\"nickname\":\"Set values\",\"request\":\"setPricingComponentValuesRequest.html\",\"response\":\"setPricingComponentValues.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | ID of the subscription.
pricing_component_value = swagger_client.PricingComponentValue() # PricingComponentValue | The pricing-component-value request

try: 
    # Sets upon this subscription a new value for the specified pricing-component without performing an upgrade.
    api_response = api_instance.set_pricing_component_value_on_subscription(subscription_id, pricing_component_value)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->set_pricing_component_value_on_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| ID of the subscription. | 
 **pricing_component_value** | [**PricingComponentValue**](PricingComponentValue.md)| The pricing-component-value request | 

### Return type

[**PricingComponentValuePagedMetadata**](PricingComponentValuePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_pricing_component_value_on_subscription_v2**
> PricingComponentValueResponsePagedMetadata set_pricing_component_value_on_subscription_v2(subscription_id, pricing_component, value)

Upgrades/downgrades this subscription to some new value for the specified pricing-component.

{\"nickname\":\"Set value\",\"request\":\"setPricingComponentValueRequest.html\",\"response\":\"setPricingComponentValue.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_id = 'subscription_id_example' # str | 
pricing_component = 'pricing_component_example' # str | Name or ID of the pricing-component.
value = swagger_client.PricingComponentValueRequest() # PricingComponentValueRequest | The pricing-component-value request

try: 
    # Upgrades/downgrades this subscription to some new value for the specified pricing-component.
    api_response = api_instance.set_pricing_component_value_on_subscription_v2(subscription_id, pricing_component, value)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->set_pricing_component_value_on_subscription_v2: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **pricing_component** | **str**| Name or ID of the pricing-component. | 
 **value** | [**PricingComponentValueRequest**](PricingComponentValueRequest.md)| The pricing-component-value request | 

### Return type

[**PricingComponentValueResponsePagedMetadata**](PricingComponentValueResponsePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subscription**
> SubscriptionPagedMetadata update_subscription(subscription)

Update a subscription.

{\"nickname\":\"Update a subscription\",\"request\":\"updateSubscriptionRequest.html\",\"response\":\"updateSubscriptionResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription = swagger_client.Subscription() # Subscription | The subscription object to be updated.

try: 
    # Update a subscription.
    api_response = api_instance.update_subscription(subscription)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->update_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription** | [**Subscription**](Subscription.md)| The subscription object to be updated. | 

### Return type

[**SubscriptionPagedMetadata**](SubscriptionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subscription_v2**
> SubscriptionPagedMetadata update_subscription_v2(request)

Update a subscription (V2).

{\"nickname\":\"Update subscription (V2)\",\"response\":\"updateSubscriptionViaHelper.html\",\"request\":\"updateSubscriptionViaHelper.request.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
request = swagger_client.UpdateSubscriptionRequest() # UpdateSubscriptionRequest | 

try: 
    # Update a subscription (V2).
    api_response = api_instance.update_subscription_v2(request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->update_subscription_v2: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**UpdateSubscriptionRequest**](UpdateSubscriptionRequest.md)|  | 

### Return type

[**SubscriptionPagedMetadata**](SubscriptionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_metadata_for_subscription**
> DynamicMetadata upsert_metadata_for_subscription(metadata, subscription_id, organizations=organizations)

Update any existing metadata key-values and insert any new key-values, no keys will be removed.

{\"nickname\":\"Upsert on subscription\",\"request\":\"upsertSubscriptionMetadataRequest.html\",\"response\":\"upsertSubscriptionMetadataResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
metadata = swagger_client.DynamicMetadata() # DynamicMetadata | 
subscription_id = 'subscription_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Update any existing metadata key-values and insert any new key-values, no keys will be removed.
    api_response = api_instance.upsert_metadata_for_subscription(metadata, subscription_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SubscriptionsApi->upsert_metadata_for_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata** | [**DynamicMetadata**](DynamicMetadata.md)|  | 
 **subscription_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**DynamicMetadata**](DynamicMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

