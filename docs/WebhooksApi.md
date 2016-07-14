# billforward.WebhooksApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook**](WebhooksApi.md#create_webhook) | **POST** /webhooks | Create a webhook.
[**create_webhook_v2**](WebhooksApi.md#create_webhook_v2) | **POST** /webhooks/create | Create a webhook.
[**get_all_webhooks**](WebhooksApi.md#get_all_webhooks) | **GET** /webhooks | Returns a collection of Webhooks, specified by the accountID parameter. By default 10 values are returned. Records are returned in natural order.
[**get_webhook_by_id**](WebhooksApi.md#get_webhook_by_id) | **GET** /webhooks/{webhook-ID} | Returns a single webhook, specified by the webhook-ID parameter.
[**retire_webhook**](WebhooksApi.md#retire_webhook) | **DELETE** /webhooks/{webhook-ID} | Retires the specified webhook.
[**update_webhook**](WebhooksApi.md#update_webhook) | **PUT** /webhooks | Update a webhook.
[**verify_webhook**](WebhooksApi.md#verify_webhook) | **GET** /webhooks/verify/{verification-ID} | New webhooks must be verified before use, use the verificationID of the webhook to perform verification.


# **create_webhook**
> WebhookPagedMetadata create_webhook(webhook)

Create a webhook.

{\"nickname\":\"Add a new webhook\",\"request\":\"createWebhookRequest.html\",\"response\":\"createWebhookResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.WebhooksApi()
webhook = billforward.MutableBillingEntity() # MutableBillingEntity | The webhook object to be created.

try: 
    # Create a webhook.
    api_response = api_instance.create_webhook(webhook)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WebhooksApi->create_webhook: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook** | [**MutableBillingEntity**](MutableBillingEntity.md)| The webhook object to be created. | 

### Return type

[**WebhookPagedMetadata**](WebhookPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_webhook_v2**
> WebhookPagedMetadata create_webhook_v2(request)

Create a webhook.

{\"nickname\":\"Add a new webhook\",\"request\":\"createWebhookRequest.html\",\"response\":\"createWebhookResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.WebhooksApi()
request = billforward.BillingEntityBase() # BillingEntityBase | 

try: 
    # Create a webhook.
    api_response = api_instance.create_webhook_v2(request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WebhooksApi->create_webhook_v2: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**BillingEntityBase**](BillingEntityBase.md)|  | 

### Return type

[**WebhookPagedMetadata**](WebhookPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_webhooks**
> WebhookPagedMetadata get_all_webhooks(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of Webhooks, specified by the accountID parameter. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get all webhooks\",\"response\":\"getWebhookAll.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.WebhooksApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first webhook to return. (optional) (default to 0)
records = 10 # int | The maximum number of webhooks to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)

try: 
    # Returns a collection of Webhooks, specified by the accountID parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_webhooks(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WebhooksApi->get_all_webhooks: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first webhook to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of webhooks to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]

### Return type

[**WebhookPagedMetadata**](WebhookPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_by_id**
> WebhookPagedMetadata get_webhook_by_id(webhook_id, organizations=organizations)

Returns a single webhook, specified by the webhook-ID parameter.

{\"nickname\":\"Retrieve an existing webhook\",\"response\":\"getWebhookByID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.WebhooksApi()
webhook_id = 'webhook_id_example' # str | ID of the webhook.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single webhook, specified by the webhook-ID parameter.
    api_response = api_instance.get_webhook_by_id(webhook_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WebhooksApi->get_webhook_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| ID of the webhook. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**WebhookPagedMetadata**](WebhookPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retire_webhook**
> WebhookPagedMetadata retire_webhook(webhook_id, organizations)

Retires the specified webhook.

{\"nickname\":\"Remove a webhook\",\"response\":\"deleteWebhook.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.WebhooksApi()
webhook_id = 'webhook_id_example' # str | ID of the webhook.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls.

try: 
    # Retires the specified webhook.
    api_response = api_instance.retire_webhook(webhook_id, organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WebhooksApi->retire_webhook: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| ID of the webhook. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | 

### Return type

[**WebhookPagedMetadata**](WebhookPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook**
> WebhookPagedMetadata update_webhook(webhook)

Update a webhook.

{\"nickname\":\"Update a webhook\",\"request\":\"updateWebhookRequest.html\",\"response\":\"updateWebhookResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.WebhooksApi()
webhook = billforward.MutableBillingEntity() # MutableBillingEntity | The webhook object to be updated.

try: 
    # Update a webhook.
    api_response = api_instance.update_webhook(webhook)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WebhooksApi->update_webhook: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook** | [**MutableBillingEntity**](MutableBillingEntity.md)| The webhook object to be updated. | 

### Return type

[**WebhookPagedMetadata**](WebhookPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_webhook**
> WebhookPagedMetadata verify_webhook(verification_id, organizations=organizations)

New webhooks must be verified before use, use the verificationID of the webhook to perform verification.

{\"nickname\":\"Verify a webhook\",\"response\":\"verifyWebhook.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.WebhooksApi()
verification_id = 'verification_id_example' # str | verificationID of the webhook.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # New webhooks must be verified before use, use the verificationID of the webhook to perform verification.
    api_response = api_instance.verify_webhook(verification_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WebhooksApi->verify_webhook: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verification_id** | **str**| verificationID of the webhook. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**WebhookPagedMetadata**](WebhookPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

