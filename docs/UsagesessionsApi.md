# billforward.UsagesessionsApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_active_sessions_for_subscription**](UsagesessionsApi.md#get_active_sessions_for_subscription) | **GET** /usage-sessions/{subscription-id}/active | Get active by subscription
[**get_usage_list_for_usage_session**](UsagesessionsApi.md#get_usage_list_for_usage_session) | **GET** /usage-sessions/{subscription-id} | Retrieve by subscription
[**start_usage_session**](UsagesessionsApi.md#start_usage_session) | **POST** /usage-sessions/start | Start a new session
[**stop_usage_session**](UsagesessionsApi.md#stop_usage_session) | **POST** /usage-sessions/stop | Stop a specified session


# **get_active_sessions_for_subscription**
> UsageSessionPagedMetadata get_active_sessions_for_subscription(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Get active by subscription

{\"nickname\":\"Get active by subscription\",\"response\":\"getActiveSessions.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.UsagesessionsApi()
subscription_id = 'subscription_id_example' # str | The subscriptionID of the subscription whose active sessions you wish to GET.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first amendment to return. (optional) (default to 0)
records = 8766 # int | The maximum number of amendments to return. (optional) (default to 8766)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'ASC' # str | The direction of any ordering, either ASC or DESC. (optional) (default to ASC)

try: 
    # Get active by subscription
    api_response = api_instance.get_active_sessions_for_subscription(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsagesessionsApi->get_active_sessions_for_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| The subscriptionID of the subscription whose active sessions you wish to GET. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first amendment to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of amendments to return. | [optional] [default to 8766]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| The direction of any ordering, either ASC or DESC. | [optional] [default to ASC]

### Return type

[**UsageSessionPagedMetadata**](UsageSessionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_list_for_usage_session**
> UsageSessionPagedMetadata get_usage_list_for_usage_session(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Retrieve by subscription

{\"nickname\":\"Retrieve by subscription\",\"response\":\"getAllSessions.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.UsagesessionsApi()
subscription_id = 'subscription_id_example' # str | The subscriptionID of the subscription whose sessions you wish to GET.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first amendment to return. (optional) (default to 0)
records = 8766 # int | The maximum number of amendments to return. (optional) (default to 8766)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'ASC' # str | The direction of any ordering, either ASC or DESC. (optional) (default to ASC)

try: 
    # Retrieve by subscription
    api_response = api_instance.get_usage_list_for_usage_session(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsagesessionsApi->get_usage_list_for_usage_session: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| The subscriptionID of the subscription whose sessions you wish to GET. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first amendment to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of amendments to return. | [optional] [default to 8766]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| The direction of any ordering, either ASC or DESC. | [optional] [default to ASC]

### Return type

[**UsageSessionPagedMetadata**](UsageSessionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_usage_session**
> UsageSessionPagedMetadata start_usage_session(usage_sessions)

Start a new session

{\"nickname\":\"Start a new session\",\"request\":\"createStartUsageSessionRequest.html\",\"response\":\"createStartUsageSessionResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.UsagesessionsApi()
usage_sessions = billforward.CompoundUsageSession() # CompoundUsageSession | An array of 'Usage Session' objects whose sessions you wish to start.

try: 
    # Start a new session
    api_response = api_instance.start_usage_session(usage_sessions)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsagesessionsApi->start_usage_session: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usage_sessions** | [**CompoundUsageSession**](CompoundUsageSession.md)| An array of &#39;Usage Session&#39; objects whose sessions you wish to start. | 

### Return type

[**UsageSessionPagedMetadata**](UsageSessionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_usage_session**
> UsageSessionPagedMetadata stop_usage_session(usage_sessions)

Stop a specified session

{\"nickname\":\"Stop a specified session\",\"request\":\"createStopUsageSessionRequest.html\",\"response\":\"createStopUsageSessionResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.UsagesessionsApi()
usage_sessions = billforward.CompoundUsageSession() # CompoundUsageSession | An array of 'Usage Session' objects whose sessions you wish to stop.

try: 
    # Stop a specified session
    api_response = api_instance.stop_usage_session(usage_sessions)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsagesessionsApi->stop_usage_session: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usage_sessions** | [**CompoundUsageSession**](CompoundUsageSession.md)| An array of &#39;Usage Session&#39; objects whose sessions you wish to stop. | 

### Return type

[**UsageSessionPagedMetadata**](UsageSessionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

