# billforward.PricingcomponentvaluesApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pricing_component_value**](PricingcomponentvaluesApi.md#create_pricing_component_value) | **POST** /pricing-component-values | Create a pricing-component-value.
[**get_all_pricing_component_values**](PricingcomponentvaluesApi.md#get_all_pricing_component_values) | **GET** /pricing-component-values | Returns a collection of pricing-component-values.By default 10 values are returned. Records are returned in natural order.
[**get_pricing_component_value**](PricingcomponentvaluesApi.md#get_pricing_component_value) | **GET** /pricing-component-values/{pricing-component-ID} | Returns a collection of pricing-component-values, specified by the pricing-component-ID parameter.By default 10 values are returned. Records are returned in natural order.
[**get_pricing_component_value_by_subscription_id**](PricingcomponentvaluesApi.md#get_pricing_component_value_by_subscription_id) | **GET** /pricing-component-values/subscription/{subscription-ID} | Returns a collection of pricing-component-values, specified by the subscription-ID parameter.By default 10 values are returned. Records are returned in natural order.
[**update_pricing_component_value**](PricingcomponentvaluesApi.md#update_pricing_component_value) | **PUT** /pricing-component-values | Update a pricing-component-value.


# **create_pricing_component_value**
> PricingComponentValuePagedMetadata create_pricing_component_value(pricing_component_value)

Create a pricing-component-value.

{\"nickname\":\"Create a new value\",\"request\":\"createPricingComponentValueRequest.html\",\"response\":\"createPricingComponentValueResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.PricingcomponentvaluesApi()
pricing_component_value = billforward.PricingComponentValue() # PricingComponentValue | The pricing-component-value object to be updated.

try: 
    # Create a pricing-component-value.
    api_response = api_instance.create_pricing_component_value(pricing_component_value)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PricingcomponentvaluesApi->create_pricing_component_value: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pricing_component_value** | [**PricingComponentValue**](PricingComponentValue.md)| The pricing-component-value object to be updated. | 

### Return type

[**PricingComponentValuePagedMetadata**](PricingComponentValuePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_pricing_component_values**
> PricingComponentValuePagedMetadata get_all_pricing_component_values(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of pricing-component-values.By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get all values\",\"response\":\"getPricingComponentValueAll.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.PricingcomponentvaluesApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first pricing-component-value to return. (optional) (default to 0)
records = 10 # int | The maximum number of pricing-component-values to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)

try: 
    # Returns a collection of pricing-component-values.By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_pricing_component_values(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PricingcomponentvaluesApi->get_all_pricing_component_values: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first pricing-component-value to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of pricing-component-values to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]

### Return type

[**PricingComponentValuePagedMetadata**](PricingComponentValuePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pricing_component_value**
> PricingComponentValuePagedMetadata get_pricing_component_value(pricing_component_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of pricing-component-values, specified by the pricing-component-ID parameter.By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get existing values\",\"response\":\"getPricingComponentValueByID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.PricingcomponentvaluesApi()
pricing_component_id = 'pricing_component_id_example' # str | The string ID of the pricing-component-value.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first pricing-component-value to return. (optional) (default to 0)
records = 10 # int | The maximum number of pricing-component-values to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)

try: 
    # Returns a collection of pricing-component-values, specified by the pricing-component-ID parameter.By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_pricing_component_value(pricing_component_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PricingcomponentvaluesApi->get_pricing_component_value: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pricing_component_id** | **str**| The string ID of the pricing-component-value. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first pricing-component-value to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of pricing-component-values to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]

### Return type

[**PricingComponentValuePagedMetadata**](PricingComponentValuePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pricing_component_value_by_subscription_id**
> PricingComponentValuePagedMetadata get_pricing_component_value_by_subscription_id(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of pricing-component-values, specified by the subscription-ID parameter.By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by subscription\",\"response\":\"getPricingComponentValueBySubscriptionID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.PricingcomponentvaluesApi()
subscription_id = 'subscription_id_example' # str | The string subscription-ID of the pricing-component-value.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first pricing-component-value to return. (optional) (default to 0)
records = 10 # int | The maximum number of pricing-component-values to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)

try: 
    # Returns a collection of pricing-component-values, specified by the subscription-ID parameter.By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_pricing_component_value_by_subscription_id(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PricingcomponentvaluesApi->get_pricing_component_value_by_subscription_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| The string subscription-ID of the pricing-component-value. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first pricing-component-value to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of pricing-component-values to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]

### Return type

[**PricingComponentValuePagedMetadata**](PricingComponentValuePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pricing_component_value**
> PricingComponentValuePagedMetadata update_pricing_component_value(pricing_component_value)

Update a pricing-component-value.

{\"nickname\":\"Update a value\",\"request\":\"updatePricingComponentValueRequest.html\",\"response\":\"updatePricingComponentValueResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.PricingcomponentvaluesApi()
pricing_component_value = billforward.PricingComponentValue() # PricingComponentValue | The pricing-component-value object to be updated.

try: 
    # Update a pricing-component-value.
    api_response = api_instance.update_pricing_component_value(pricing_component_value)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PricingcomponentvaluesApi->update_pricing_component_value: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pricing_component_value** | [**PricingComponentValue**](PricingComponentValue.md)| The pricing-component-value object to be updated. | 

### Return type

[**PricingComponentValuePagedMetadata**](PricingComponentValuePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

