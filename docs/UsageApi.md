# swagger_client.UsageApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_usage_instance**](UsageApi.md#create_usage_instance) | **POST** /usage | Add usage
[**get_usage_by_id**](UsageApi.md#get_usage_by_id) | **GET** /usage/{subscription-id}/{period-id} | Retrieve by subscription and period
[**get_usage_by_subscription_id**](UsageApi.md#get_usage_by_subscription_id) | **GET** /usage/{subscription-id} | Retrieve by subscription
[**get_usage_by_subscription_id_uo_m_period_and_usage_type**](UsageApi.md#get_usage_by_subscription_id_uo_m_period_and_usage_type) | **GET** /usage/{subscription-id}/{uom}/{period-id}/{usage-type} | Retrieve by subscription, period and type
[**update_usage_instance**](UsageApi.md#update_usage_instance) | **PUT** /usage | Update usage


# **create_usage_instance**
> UsagePagedMetadata create_usage_instance(usage)

Add usage

{\"nickname\":\"Add usage\",\"request\":\"createUsageRequest.html\",\"response\":\"createUsageResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsageApi()
usage = swagger_client.CompoundUsage() # CompoundUsage | An array of The 'Usage' objects to be created.

try: 
    # Add usage
    api_response = api_instance.create_usage_instance(usage)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsageApi->create_usage_instance: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usage** | [**CompoundUsage**](CompoundUsage.md)| An array of The &#39;Usage&#39; objects to be created. | 

### Return type

[**UsagePagedMetadata**](UsagePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_by_id**
> UsagePagedMetadata get_usage_by_id(subscription_id, period_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Retrieve by subscription and period

{\"nickname\":\"Retrieve by subscription and period\",\"response\":\"getUsageForPeriod.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsageApi()
subscription_id = 'subscription_id_example' # str | The subscriptionID of the usage.
period_id = 56 # int | The periodID of the usage.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first amendment to return. (optional) (default to 0)
records = 8766 # int | The maximum number of amendments to return. (optional) (default to 8766)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'ASC' # str | The direction of any ordering, either ASC or DESC. (optional) (default to ASC)

try: 
    # Retrieve by subscription and period
    api_response = api_instance.get_usage_by_id(subscription_id, period_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsageApi->get_usage_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| The subscriptionID of the usage. | 
 **period_id** | **int**| The periodID of the usage. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first amendment to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of amendments to return. | [optional] [default to 8766]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| The direction of any ordering, either ASC or DESC. | [optional] [default to ASC]

### Return type

[**UsagePagedMetadata**](UsagePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_by_subscription_id**
> UsagePagedMetadata get_usage_by_subscription_id(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Retrieve by subscription

{\"nickname\":\"Retrieve by subscription\",\"response\":\"getUsage.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsageApi()
subscription_id = 'subscription_id_example' # str | The subscriptionID of the subscription whose Usage instances you wish to GET.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first amendment to return. (optional) (default to 0)
records = 8766 # int | The maximum number of amendments to return. (optional) (default to 8766)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'ASC' # str | The direction of any ordering, either ASC or DESC. (optional) (default to ASC)

try: 
    # Retrieve by subscription
    api_response = api_instance.get_usage_by_subscription_id(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsageApi->get_usage_by_subscription_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| The subscriptionID of the subscription whose Usage instances you wish to GET. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first amendment to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of amendments to return. | [optional] [default to 8766]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| The direction of any ordering, either ASC or DESC. | [optional] [default to ASC]

### Return type

[**UsagePagedMetadata**](UsagePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_by_subscription_id_uo_m_period_and_usage_type**
> UsagePagedMetadata get_usage_by_subscription_id_uo_m_period_and_usage_type(subscription_id, uom, period_id, usage_type, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Retrieve by subscription, period and type

{\"nickname\":\"Retrieve by subscription, period and type\",\"response\":\"getDetailedUsageForPeriod.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsageApi()
subscription_id = 'subscription_id_example' # str | The subscriptionID of the usage.
uom = 'uom_example' # str | The uom of the usage.
period_id = 56 # int | The periodID of the usage.
usage_type = 'usage_type_example' # str | The type of the usage.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first amendment to return. (optional) (default to 0)
records = 8766 # int | The maximum number of amendments to return. (optional) (default to 8766)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'ASC' # str | The direction of any ordering, either ASC or DESC. (optional) (default to ASC)

try: 
    # Retrieve by subscription, period and type
    api_response = api_instance.get_usage_by_subscription_id_uo_m_period_and_usage_type(subscription_id, uom, period_id, usage_type, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsageApi->get_usage_by_subscription_id_uo_m_period_and_usage_type: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| The subscriptionID of the usage. | 
 **uom** | **str**| The uom of the usage. | 
 **period_id** | **int**| The periodID of the usage. | 
 **usage_type** | **str**| The type of the usage. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first amendment to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of amendments to return. | [optional] [default to 8766]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| The direction of any ordering, either ASC or DESC. | [optional] [default to ASC]

### Return type

[**UsagePagedMetadata**](UsagePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_usage_instance**
> UsagePagedMetadata update_usage_instance(usage)

Update usage

{\"nickname\":\"Update usage\",\"request\":\"updateUsageRequest.html\",\"response\":\"updateUsageResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsageApi()
usage = swagger_client.CompoundUsage() # CompoundUsage | An array of The 'Usage' objects to be updated.

try: 
    # Update usage
    api_response = api_instance.update_usage_instance(usage)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsageApi->update_usage_instance: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usage** | [**CompoundUsage**](CompoundUsage.md)| An array of The &#39;Usage&#39; objects to be updated. | 

### Return type

[**UsagePagedMetadata**](UsagePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

