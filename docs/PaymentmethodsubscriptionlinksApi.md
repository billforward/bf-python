# billforward.PaymentmethodsubscriptionlinksApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_method_subscription_link**](PaymentmethodsubscriptionlinksApi.md#create_payment_method_subscription_link) | **POST** /payment-method-subscription-links | Create
[**retire_payment_method_subscription_link**](PaymentmethodsubscriptionlinksApi.md#retire_payment_method_subscription_link) | **DELETE** /payment-method-subscription-links/{payment-method-subscription-link-ID} | Retires the payment-method-subscription-link specified by the link-ID parameter.


# **create_payment_method_subscription_link**
> PaymentMethodSubscriptionLinkPagedMetadata create_payment_method_subscription_link(payment_method)

Create

{\"nickname\":\"Add a payment method to a subscription\",\"request\":\"createPaymentMethodSubscriptionLinkRequest.html\",\"response\":\"createPaymentMethodSubscriptionLinkResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.PaymentmethodsubscriptionlinksApi()
payment_method = billforward.PaymentMethodSubscriptionLink() # PaymentMethodSubscriptionLink | The payment-method object to be updated.

try: 
    # Create
    api_response = api_instance.create_payment_method_subscription_link(payment_method)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PaymentmethodsubscriptionlinksApi->create_payment_method_subscription_link: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method** | [**PaymentMethodSubscriptionLink**](PaymentMethodSubscriptionLink.md)| The payment-method object to be updated. | 

### Return type

[**PaymentMethodSubscriptionLinkPagedMetadata**](PaymentMethodSubscriptionLinkPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retire_payment_method_subscription_link**
> PaymentMethodSubscriptionLinkPagedMetadata retire_payment_method_subscription_link(payment_method_subscription_link_id, organizations)

Retires the payment-method-subscription-link specified by the link-ID parameter.

{\"nickname\":\"Remove a payment method from a subscription\",\"response\":\"deletePaymentMethodSubscriptionLink.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.PaymentmethodsubscriptionlinksApi()
payment_method_subscription_link_id = 'payment_method_subscription_link_id_example' # str | ID of the link.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls.

try: 
    # Retires the payment-method-subscription-link specified by the link-ID parameter.
    api_response = api_instance.retire_payment_method_subscription_link(payment_method_subscription_link_id, organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PaymentmethodsubscriptionlinksApi->retire_payment_method_subscription_link: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_subscription_link_id** | **str**| ID of the link. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | 

### Return type

[**PaymentMethodSubscriptionLinkPagedMetadata**](PaymentMethodSubscriptionLinkPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

