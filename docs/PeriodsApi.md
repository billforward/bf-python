# billforward.PeriodsApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_periods_for_subscription**](PeriodsApi.md#get_all_periods_for_subscription) | **GET** /periods/{subscription-id} | Retrieve by subscription)
[**get_latest_periods**](PeriodsApi.md#get_latest_periods) | **GET** /periods | Get all periods


# **get_all_periods_for_subscription**
> PeriodPagedMetadata get_all_periods_for_subscription(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Retrieve by subscription)

{ \"nickname\" : \"Retrieve by subscription\",\"response\" : \"getPeriodsForSubscription.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.PeriodsApi()
subscription_id = 'subscription_id_example' # str | The subscriptionID of the usage.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first amendment to return. (optional) (default to 0)
records = 8766 # int | The maximum number of amendments to return. (optional) (default to 8766)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'ASC' # str | The direction of any ordering, either ASC or DESC. (optional) (default to ASC)

try: 
    # Retrieve by subscription)
    api_response = api_instance.get_all_periods_for_subscription(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PeriodsApi->get_all_periods_for_subscription: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| The subscriptionID of the usage. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first amendment to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of amendments to return. | [optional] [default to 8766]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| The direction of any ordering, either ASC or DESC. | [optional] [default to ASC]

### Return type

[**PeriodPagedMetadata**](PeriodPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_periods**
> PeriodPagedMetadata get_latest_periods(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Get all periods

{ \"nickname\" : \"Get all periods\",\"response\" : \"getPeriods.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.PeriodsApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first amendment to return. (optional) (default to 0)
records = 8766 # int | The maximum number of amendments to return. (optional) (default to 8766)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'ASC' # str | The direction of any ordering, either ASC or DESC. (optional) (default to ASC)

try: 
    # Get all periods
    api_response = api_instance.get_latest_periods(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PeriodsApi->get_latest_periods: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first amendment to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of amendments to return. | [optional] [default to 8766]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| The direction of any ordering, either ASC or DESC. | [optional] [default to ASC]

### Return type

[**PeriodPagedMetadata**](PeriodPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

