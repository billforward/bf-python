# billforward.NotificationsApi

All URIs are relative to *https://app.billforward.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_notifications**](NotificationsApi.md#get_all_notifications) | **GET** /notifications | 
[**get_notification_by_entity_id**](NotificationsApi.md#get_notification_by_entity_id) | **GET** /notifications/entity-ID/{entity-ID} | 
[**get_notification_by_id**](NotificationsApi.md#get_notification_by_id) | **GET** /notifications/{notification-ID} | 
[**get_notifications_by_webhook_id**](NotificationsApi.md#get_notifications_by_webhook_id) | **GET** /notifications/{lower-threshold}/{upper-threshold}/{webhookID} | 
[**get_notifications_within_date_range**](NotificationsApi.md#get_notifications_within_date_range) | **GET** /notifications/{lower-threshold}/{upper-threshold} | 
[**resend_notification**](NotificationsApi.md#resend_notification) | **POST** /notifications/{notification-ID}/resend | 

# **get_all_notifications**
> InlineResponseDefault37 get_all_notifications(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.NotificationsApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = true # bool |  (optional) (default to true)

try:
    api_response = api_instance.get_all_notifications(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->get_all_notifications: %s\n" % e)
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

[**InlineResponseDefault37**](InlineResponseDefault37.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_by_entity_id**
> InlineResponseDefault37 get_notification_by_entity_id(entity_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.NotificationsApi(billforward.ApiClient(configuration))
entity_id = 'entity_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = true # bool |  (optional) (default to true)

try:
    api_response = api_instance.get_notification_by_entity_id(entity_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->get_notification_by_entity_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to true]

### Return type

[**InlineResponseDefault37**](InlineResponseDefault37.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_by_id**
> InlineResponseDefault38 get_notification_by_id(notification_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.NotificationsApi(billforward.ApiClient(configuration))
notification_id = 'notification_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_notification_by_id(notification_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->get_notification_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault38**](InlineResponseDefault38.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notifications_by_webhook_id**
> InlineResponseDefault37 get_notifications_by_webhook_id(lower_threshold, upper_threshold, webhook_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, safety_margin=safety_margin)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.NotificationsApi(billforward.ApiClient(configuration))
lower_threshold = billforward.SimpleDateParam() # SimpleDateParam | 
upper_threshold = billforward.SimpleDateParam() # SimpleDateParam | 
webhook_id = 'webhook_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = true # bool |  (optional) (default to true)
safety_margin = 10 # int |  (optional) (default to 10)

try:
    api_response = api_instance.get_notifications_by_webhook_id(lower_threshold, upper_threshold, webhook_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, safety_margin=safety_margin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->get_notifications_by_webhook_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lower_threshold** | [**SimpleDateParam**](.md)|  | 
 **upper_threshold** | [**SimpleDateParam**](.md)|  | 
 **webhook_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to true]
 **safety_margin** | **int**|  | [optional] [default to 10]

### Return type

[**InlineResponseDefault37**](InlineResponseDefault37.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notifications_within_date_range**
> InlineResponseDefault37 get_notifications_within_date_range(lower_threshold, upper_threshold, organizations=organizations, domain=domain, action=action, webhook_id=webhook_id, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, safety_margin=safety_margin)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.NotificationsApi(billforward.ApiClient(configuration))
lower_threshold = billforward.SimpleDateParam() # SimpleDateParam | 
upper_threshold = billforward.SimpleDateParam() # SimpleDateParam | 
organizations = ['organizations_example'] # list[str] |  (optional)
domain = 'domain_example' # str |  (optional)
action = 'action_example' # str |  (optional)
webhook_id = 'webhook_id_example' # str |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = true # bool |  (optional) (default to true)
safety_margin = 10 # int |  (optional) (default to 10)

try:
    api_response = api_instance.get_notifications_within_date_range(lower_threshold, upper_threshold, organizations=organizations, domain=domain, action=action, webhook_id=webhook_id, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, safety_margin=safety_margin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->get_notifications_within_date_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lower_threshold** | [**SimpleDateParam**](.md)|  | 
 **upper_threshold** | [**SimpleDateParam**](.md)|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **domain** | **str**|  | [optional] 
 **action** | **str**|  | [optional] 
 **webhook_id** | **str**|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to true]
 **safety_margin** | **int**|  | [optional] [default to 10]

### Return type

[**InlineResponseDefault37**](InlineResponseDefault37.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_notification**
> InlineResponseDefault39 resend_notification(notification_id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.NotificationsApi(billforward.ApiClient(configuration))
notification_id = 'notification_id_example' # str | 
body = billforward.NotificationSendRequest() # NotificationSendRequest |  (optional)

try:
    api_response = api_instance.resend_notification(notification_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->resend_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**|  | 
 **body** | [**NotificationSendRequest**](NotificationSendRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault39**](InlineResponseDefault39.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

