# swagger_client.UsageperiodsApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_usage_period**](UsageperiodsApi.md#get_usage_period) | **GET** /usage-periods/{subscription-id}/{period-id} | Retrieve by subscription and period
[**get_usage_period_for_all**](UsageperiodsApi.md#get_usage_period_for_all) | **GET** /usage-periods/{subscription-id} | Retrieve by subscription
[**get_usage_period_for_invoice**](UsageperiodsApi.md#get_usage_period_for_invoice) | **GET** /usage-periods/{subscription-id}/invoice/{invoice-id} | Retrieve by invoice)


# **get_usage_period**
> UsagePeriodPagedMetadata get_usage_period(subscription_id, period_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Retrieve by subscription and period

{ \"nickname\" : \"Retrieve by subscription and period\",\"response\" : \"getUsagePeriodsForPeriod.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsageperiodsApi()
subscription_id = 'subscription_id_example' # str | The subscriptionID of the usage.
period_id = 56 # int | The periodID of the usage.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first amendment to return. (optional) (default to 0)
records = 8766 # int | The maximum number of amendments to return. (optional) (default to 8766)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'ASC' # str | The direction of any ordering, either ASC or DESC. (optional) (default to ASC)

try: 
    # Retrieve by subscription and period
    api_response = api_instance.get_usage_period(subscription_id, period_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsageperiodsApi->get_usage_period: %s\n" % e
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

[**UsagePeriodPagedMetadata**](UsagePeriodPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_period_for_all**
> UsagePeriodPagedMetadata get_usage_period_for_all(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Retrieve by subscription

{ \"nickname\" : \"Retrieve by subscription\",\"response\" : \"getUsagePeriods.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsageperiodsApi()
subscription_id = 'subscription_id_example' # str | The subscriptionID of the usage.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first amendment to return. (optional) (default to 0)
records = 8766 # int | The maximum number of amendments to return. (optional) (default to 8766)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'ASC' # str | The direction of any ordering, either ASC or DESC. (optional) (default to ASC)

try: 
    # Retrieve by subscription
    api_response = api_instance.get_usage_period_for_all(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsageperiodsApi->get_usage_period_for_all: %s\n" % e
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

[**UsagePeriodPagedMetadata**](UsagePeriodPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_period_for_invoice**
> UsagePeriodPagedMetadata get_usage_period_for_invoice(subscription_id, invoice_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Retrieve by invoice)

{ \"nickname\" : \"Retrieve by invoice\",\"response\" : \"getUsagePeriodForInvoice.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsageperiodsApi()
subscription_id = 'subscription_id_example' # str | The subscriptionID of the usage.
invoice_id = 'invoice_id_example' # str | The invoiceID of the usage.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first amendment to return. (optional) (default to 0)
records = 8766 # int | The maximum number of amendments to return. (optional) (default to 8766)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'ASC' # str | The direction of any ordering, either ASC or DESC. (optional) (default to ASC)

try: 
    # Retrieve by invoice)
    api_response = api_instance.get_usage_period_for_invoice(subscription_id, invoice_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsageperiodsApi->get_usage_period_for_invoice: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| The subscriptionID of the usage. | 
 **invoice_id** | **str**| The invoiceID of the usage. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first amendment to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of amendments to return. | [optional] [default to 8766]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| The direction of any ordering, either ASC or DESC. | [optional] [default to ASC]

### Return type

[**UsagePeriodPagedMetadata**](UsagePeriodPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

