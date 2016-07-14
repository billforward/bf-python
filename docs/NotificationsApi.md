# swagger_client.NotificationsApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ack_notification**](NotificationsApi.md#ack_notification) | **GET** /notifications/ack/{notification-ID} | Acknowledge a newly recevied notification.
[**get_all_notifications**](NotificationsApi.md#get_all_notifications) | **GET** /notifications | Returns a collection of all notifications. By default 10 values are returned. Records are returned in natural order.
[**get_notification_by_entity_id**](NotificationsApi.md#get_notification_by_entity_id) | **GET** /notifications/entity-ID/{entity-ID} | Returns a collection of notifications, specified by the entity-ID parameter. By default 10 values are returned. Records are returned in natural order.
[**get_notification_by_id**](NotificationsApi.md#get_notification_by_id) | **GET** /notifications/{notification-ID} | Returns a single notification, specified by the notification-ID parameter.
[**get_notifications_by_webhook_id**](NotificationsApi.md#get_notifications_by_webhook_id) | **GET** /notifications/{lower-threshold}/{upper-threshold}/{webhookID} | Returns a collection of notification objects with created times within the period specified by the lower-threshold and upper-threshold parameters for the given webhook id. By default 10 values are returned. Records are returned in natural order.
[**get_notifications_within_date_range**](NotificationsApi.md#get_notifications_within_date_range) | **GET** /notifications/{lower-threshold}/{upper-threshold} | Returns a collection of notification objects with created times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.


# **ack_notification**
> NotificationPagedMetadata ack_notification(notification_id, organizations=organizations)

Acknowledge a newly recevied notification.

{\"nickname\":\"Acknowledge\",\"response\":\"getNotificationACK.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationsApi()
notification_id = 'notification_id_example' # str | ID of the notification.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Acknowledge a newly recevied notification.
    api_response = api_instance.ack_notification(notification_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling NotificationsApi->ack_notification: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**| ID of the notification. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**NotificationPagedMetadata**](NotificationPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_notifications**
> NotificationPagedMetadata get_all_notifications(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of all notifications. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get all notifications\",\"response\":\"getNotificationAll.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationsApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first Subscription to return. (optional) (default to 0)
records = 10 # int | The maximum number of Subscriptions to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)

try: 
    # Returns a collection of all notifications. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_notifications(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling NotificationsApi->get_all_notifications: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first Subscription to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of Subscriptions to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]

### Return type

[**NotificationPagedMetadata**](NotificationPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_by_entity_id**
> NotificationPagedMetadata get_notification_by_entity_id(entity_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of notifications, specified by the entity-ID parameter. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by entity\",\"response\":\"getNotificationBySubscriptionID.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationsApi()
entity_id = 'entity_id_example' # str | The string entity-ID of the notification.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first notification to return. (optional) (default to 0)
records = 10 # int | The maximum number of notifications to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)

try: 
    # Returns a collection of notifications, specified by the entity-ID parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_notification_by_entity_id(entity_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling NotificationsApi->get_notification_by_entity_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| The string entity-ID of the notification. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first notification to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of notifications to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]

### Return type

[**NotificationPagedMetadata**](NotificationPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_by_id**
> NotificationPagedMetadata get_notification_by_id(notification_id, organizations=organizations)

Returns a single notification, specified by the notification-ID parameter.

{\"nickname\":\"Retrieve an existing notification\",\"response\":\"getNotificationByID.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationsApi()
notification_id = 'notification_id_example' # str | ID of the notification.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single notification, specified by the notification-ID parameter.
    api_response = api_instance.get_notification_by_id(notification_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling NotificationsApi->get_notification_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**| ID of the notification. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**NotificationPagedMetadata**](NotificationPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notifications_by_webhook_id**
> NotificationPagedMetadata get_notifications_by_webhook_id(lower_threshold, upper_threshold, webhook_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, safety_margin=safety_margin)

Returns a collection of notification objects with created times within the period specified by the lower-threshold and upper-threshold parameters for the given webhook id. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by creation\",\"response\":\"getNotificationByCreated.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationsApi()
lower_threshold = 'lower_threshold_example' # str | The UTC DateTime specifying the start of the result period.
upper_threshold = 'upper_threshold_example' # str | The UTC DateTime specifying the end of the result period.
webhook_id = 'webhook_id_example' # str | The id of the webhook.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first taxation-link to return. (optional) (default to 0)
records = 10 # int | The maximum number of taxation-links to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)
safety_margin = 10 # int | How many seconds behind server-time upperThreshold may approach. (optional) (default to 10)

try: 
    # Returns a collection of notification objects with created times within the period specified by the lower-threshold and upper-threshold parameters for the given webhook id. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_notifications_by_webhook_id(lower_threshold, upper_threshold, webhook_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, safety_margin=safety_margin)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling NotificationsApi->get_notifications_by_webhook_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lower_threshold** | **str**| The UTC DateTime specifying the start of the result period. | 
 **upper_threshold** | **str**| The UTC DateTime specifying the end of the result period. | 
 **webhook_id** | **str**| The id of the webhook. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first taxation-link to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of taxation-links to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]
 **safety_margin** | **int**| How many seconds behind server-time upperThreshold may approach. | [optional] [default to 10]

### Return type

[**NotificationPagedMetadata**](NotificationPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notifications_within_date_range**
> NotificationPagedMetadata get_notifications_within_date_range(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, safety_margin=safety_margin)

Returns a collection of notification objects with created times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by creation\",\"response\":\"getNotificationByCreated.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationsApi()
lower_threshold = 'lower_threshold_example' # str | The UTC DateTime specifying the start of the result period.
upper_threshold = 'upper_threshold_example' # str | The UTC DateTime specifying the end of the result period.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first taxation-link to return. (optional) (default to 0)
records = 10 # int | The maximum number of taxation-links to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)
safety_margin = 10 # int | How many seconds behind server-time upperThreshold may approach. (optional) (default to 10)

try: 
    # Returns a collection of notification objects with created times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_notifications_within_date_range(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, safety_margin=safety_margin)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling NotificationsApi->get_notifications_within_date_range: %s\n" % e
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
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]
 **safety_margin** | **int**| How many seconds behind server-time upperThreshold may approach. | [optional] [default to 10]

### Return type

[**NotificationPagedMetadata**](NotificationPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

