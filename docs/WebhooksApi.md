# billforward.WebhooksApi

All URIs are relative to *https://app.billforward.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook**](WebhooksApi.md#create_webhook) | **POST** /webhooks | 
[**create_webhook_v2**](WebhooksApi.md#create_webhook_v2) | **POST** /webhooks/create | 
[**get_all_webhooks**](WebhooksApi.md#get_all_webhooks) | **GET** /webhooks | 
[**get_allowed_webhook_subscriptions**](WebhooksApi.md#get_allowed_webhook_subscriptions) | **GET** /webhooks/allowed-subscriptions | 
[**get_webhook_by_id**](WebhooksApi.md#get_webhook_by_id) | **GET** /webhooks/{webhook-ID} | 
[**retire_webhook**](WebhooksApi.md#retire_webhook) | **DELETE** /webhooks/{webhook-ID} | 
[**update_webhook**](WebhooksApi.md#update_webhook) | **PUT** /webhooks | 
[**verify_webhook**](WebhooksApi.md#verify_webhook) | **GET** /webhooks/verify/{verification-ID} | 

# **create_webhook**
> InlineResponseDefault102 create_webhook(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.WebhooksApi(billforward.ApiClient(configuration))
body = billforward.Webhook() # Webhook |  (optional)

try:
    api_response = api_instance.create_webhook(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->create_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Webhook**](Webhook.md)|  | [optional] 

### Return type

[**InlineResponseDefault102**](InlineResponseDefault102.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_webhook_v2**
> InlineResponseDefault102 create_webhook_v2(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.WebhooksApi(billforward.ApiClient(configuration))
body = billforward.LegacyCreateWebhookRequest() # LegacyCreateWebhookRequest |  (optional)

try:
    api_response = api_instance.create_webhook_v2(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->create_webhook_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LegacyCreateWebhookRequest**](LegacyCreateWebhookRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault102**](InlineResponseDefault102.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_webhooks**
> InlineResponseDefault101 get_all_webhooks(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.WebhooksApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = true # bool |  (optional) (default to true)

try:
    api_response = api_instance.get_all_webhooks(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->get_all_webhooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to true]

### Return type

[**InlineResponseDefault101**](InlineResponseDefault101.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_allowed_webhook_subscriptions**
> InlineResponseDefault103 get_allowed_webhook_subscriptions(organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.WebhooksApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_allowed_webhook_subscriptions(organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->get_allowed_webhook_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault103**](InlineResponseDefault103.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_by_id**
> InlineResponseDefault102 get_webhook_by_id(webhook_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.WebhooksApi(billforward.ApiClient(configuration))
webhook_id = 'webhook_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_webhook_by_id(webhook_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->get_webhook_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault102**](InlineResponseDefault102.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retire_webhook**
> InlineResponseDefault102 retire_webhook(webhook_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.WebhooksApi(billforward.ApiClient(configuration))
webhook_id = 'webhook_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.retire_webhook(webhook_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->retire_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault102**](InlineResponseDefault102.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook**
> InlineResponseDefault102 update_webhook(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.WebhooksApi(billforward.ApiClient(configuration))
body = billforward.Webhook() # Webhook |  (optional)

try:
    api_response = api_instance.update_webhook(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->update_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Webhook**](Webhook.md)|  | [optional] 

### Return type

[**InlineResponseDefault102**](InlineResponseDefault102.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_webhook**
> InlineResponseDefault102 verify_webhook(verification_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.WebhooksApi(billforward.ApiClient(configuration))
verification_id = 'verification_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.verify_webhook(verification_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->verify_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verification_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault102**](InlineResponseDefault102.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

