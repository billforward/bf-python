# billforward.EmailsubscriptionsApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_email_subscription**](EmailsubscriptionsApi.md#create_email_subscription) | **POST** /email-subscriptions | Create an email subscription.
[**delete_email_subscription_by_type**](EmailsubscriptionsApi.md#delete_email_subscription_by_type) | **DELETE** /email-subscriptions/type&#x3D;{type} | Unsubscribe from the email specified by the type parameter.
[**get_all_email_subscriptions**](EmailsubscriptionsApi.md#get_all_email_subscriptions) | **GET** /email-subscriptions | Returns a collection of all email-subscriptions. By default 10 values are returned. Records are returned in natural order.
[**get_email_subscription_by_id**](EmailsubscriptionsApi.md#get_email_subscription_by_id) | **GET** /email-subscriptions/{email-subscription-id} | Retrieves a single email subscription, specified by ID.
[**update_email_subscription**](EmailsubscriptionsApi.md#update_email_subscription) | **PUT** /email-subscriptions | Update an email subscription.


# **create_email_subscription**
> EmailSubscriptionPagedMetadata create_email_subscription(request)

Create an email subscription.

{\"nickname\":\"Create an email subscription\",\"request\":\"createEmailSubscriptionRequest.html\",\"response\":\"creatEmailSubscriptionResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.EmailsubscriptionsApi()
request = billforward.BillingEntityBase() # BillingEntityBase | .

try: 
    # Create an email subscription.
    api_response = api_instance.create_email_subscription(request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling EmailsubscriptionsApi->create_email_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**BillingEntityBase**](BillingEntityBase.md)| . | 

### Return type

[**EmailSubscriptionPagedMetadata**](EmailSubscriptionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email_subscription_by_type**
> EmailSubscriptionPagedMetadata delete_email_subscription_by_type(type, organizations=organizations)

Unsubscribe from the email specified by the type parameter.

{ \"nickname\" : \"Unsubscribe\",\"response\" : \"unsubscribeEmail.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.EmailsubscriptionsApi()
type = 'type_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Unsubscribe from the email specified by the type parameter.
    api_response = api_instance.delete_email_subscription_by_type(type, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling EmailsubscriptionsApi->delete_email_subscription_by_type: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**EmailSubscriptionPagedMetadata**](EmailSubscriptionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_email_subscriptions**
> EmailSubscriptionPagedMetadata get_all_email_subscriptions(state, type, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Returns a collection of all email-subscriptions. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get all email subscriptions\",\"response\":\"getEmailSubscriptionsAll.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.EmailsubscriptionsApi()
state = 'state_example' # str | Constrains search to Email Subscriptions of a specific state.
type = 'type_example' # str | Constrains search to Email Subscriptions of a specific type
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first email-subscription to return. (optional) (default to 0)
records = 10 # int | The maximum number of email-subscription to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Returns a collection of all email-subscriptions. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_email_subscriptions(state, type, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling EmailsubscriptionsApi->get_all_email_subscriptions: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| Constrains search to Email Subscriptions of a specific state. | 
 **type** | **str**| Constrains search to Email Subscriptions of a specific type | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first email-subscription to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of email-subscription to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**EmailSubscriptionPagedMetadata**](EmailSubscriptionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_subscription_by_id**
> EmailSubscriptionPagedMetadata get_email_subscription_by_id(email_subscription_id, organizations=organizations, include_retired=include_retired)

Retrieves a single email subscription, specified by ID.

{ \"nickname\" : \"Retrieve by ID\",\"response\" : \"getEmailSubscriptionByID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.EmailsubscriptionsApi()
email_subscription_id = 'email_subscription_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
include_retired = false # bool | Include deleted email-subscriptions (optional) (default to false)

try: 
    # Retrieves a single email subscription, specified by ID.
    api_response = api_instance.get_email_subscription_by_id(email_subscription_id, organizations=organizations, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling EmailsubscriptionsApi->get_email_subscription_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_subscription_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **include_retired** | **bool**| Include deleted email-subscriptions | [optional] [default to false]

### Return type

[**EmailSubscriptionPagedMetadata**](EmailSubscriptionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_subscription**
> EmailSubscriptionPagedMetadata update_email_subscription(request)

Update an email subscription.

{\"nickname\":\"Update EmailSubscription\",\"request\":\"updateEmailSubscriptionRequest.html\",\"response\":\"updateEmailSubscriptionResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.EmailsubscriptionsApi()
request = billforward.BillingEntityBase() # BillingEntityBase | .

try: 
    # Update an email subscription.
    api_response = api_instance.update_email_subscription(request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling EmailsubscriptionsApi->update_email_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**BillingEntityBase**](BillingEntityBase.md)| . | 

### Return type

[**EmailSubscriptionPagedMetadata**](EmailSubscriptionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

