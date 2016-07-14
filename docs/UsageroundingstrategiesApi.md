# billforward.UsageroundingstrategiesApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_usage_rounding_strategy**](UsageroundingstrategiesApi.md#create_usage_rounding_strategy) | **POST** /usage-rounding-strategies | Create a new rounding strategy
[**get_usage_rounding_strategy_by_id**](UsageroundingstrategiesApi.md#get_usage_rounding_strategy_by_id) | **GET** /usage-rounding-strategies/{usage-rounding-strategies-ID} | Returns a collection of usage-rounding-strategies, specified by the usage-rounding-strategies-id parameter. By default 10 values are returned. Records are returned in natural order.
[**get_usage_rounding_strategy_by_pricing_component_id**](UsageroundingstrategiesApi.md#get_usage_rounding_strategy_by_pricing_component_id) | **GET** /usage-rounding-strategies/pricing-component/{pricing-component-ID} | Returns a collection of usage-rounding-strategies, specified by the pricing-component-ID parameter. By default 10 values are returned. Records are returned in natural order.
[**update_usage_rounding_strategy**](UsageroundingstrategiesApi.md#update_usage_rounding_strategy) | **PUT** /usage-rounding-strategies | Update a rounding strategy


# **create_usage_rounding_strategy**
> UsageRoundingStrategyPagedMetadata create_usage_rounding_strategy(usage_rounding_strategy)

Create a new rounding strategy

{\"nickname\":\"Create a new rounding strategy\",\"request\":\"createUsageRoundingStrategiesRequest.html\",\"response\":\"createUsageRoundingStrategiesResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.UsageroundingstrategiesApi()
usage_rounding_strategy = billforward.MutableBillingEntity() # MutableBillingEntity | The usage-rounding-strategy object to be created.

try: 
    # Create a new rounding strategy
    api_response = api_instance.create_usage_rounding_strategy(usage_rounding_strategy)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsageroundingstrategiesApi->create_usage_rounding_strategy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usage_rounding_strategy** | [**MutableBillingEntity**](MutableBillingEntity.md)| The usage-rounding-strategy object to be created. | 

### Return type

[**UsageRoundingStrategyPagedMetadata**](UsageRoundingStrategyPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_rounding_strategy_by_id**
> UsageRoundingStrategyPagedMetadata get_usage_rounding_strategy_by_id(usage_rounding_strategies_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of usage-rounding-strategies, specified by the usage-rounding-strategies-id parameter. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve an existing round strategy\",\"response\":\"getUsageRoundingStrategiesByID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.UsageroundingstrategiesApi()
usage_rounding_strategies_id = 'usage_rounding_strategies_id_example' # str | The string ID of the usage-rounding-strategies.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first pricing-component to return. (optional) (default to 0)
records = 10 # int | The maximum number of pricing-components to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)

try: 
    # Returns a collection of usage-rounding-strategies, specified by the usage-rounding-strategies-id parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_usage_rounding_strategy_by_id(usage_rounding_strategies_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsageroundingstrategiesApi->get_usage_rounding_strategy_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usage_rounding_strategies_id** | **str**| The string ID of the usage-rounding-strategies. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first pricing-component to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of pricing-components to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]

### Return type

[**UsageRoundingStrategyPagedMetadata**](UsageRoundingStrategyPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_rounding_strategy_by_pricing_component_id**
> UsageRoundingStrategyPagedMetadata get_usage_rounding_strategy_by_pricing_component_id(pricing_component_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of usage-rounding-strategies, specified by the pricing-component-ID parameter. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by pricing component\",\"response\":\"getUsageRoundingStrategiesByPricingComponent.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.UsageroundingstrategiesApi()
pricing_component_id = 'pricing_component_id_example' # str | The string pricing-component-ID of the pricing-component.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first pricing-component to return. (optional) (default to 0)
records = 10 # int | The maximum number of pricing-components to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)

try: 
    # Returns a collection of usage-rounding-strategies, specified by the pricing-component-ID parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_usage_rounding_strategy_by_pricing_component_id(pricing_component_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsageroundingstrategiesApi->get_usage_rounding_strategy_by_pricing_component_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pricing_component_id** | **str**| The string pricing-component-ID of the pricing-component. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first pricing-component to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of pricing-components to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]

### Return type

[**UsageRoundingStrategyPagedMetadata**](UsageRoundingStrategyPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_usage_rounding_strategy**
> UsageRoundingStrategyPagedMetadata update_usage_rounding_strategy(usage_rounding_strategy)

Update a rounding strategy

{\"nickname\":\"Update a rounding strategy\",\"request\":\"updateUsageRoundingStrategiesRequest.html\",\"response\":\"updateUsageRoundingStrategiesResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.UsageroundingstrategiesApi()
usage_rounding_strategy = billforward.MutableBillingEntity() # MutableBillingEntity | The usage-rounding-strategy object to be updated.

try: 
    # Update a rounding strategy
    api_response = api_instance.update_usage_rounding_strategy(usage_rounding_strategy)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsageroundingstrategiesApi->update_usage_rounding_strategy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usage_rounding_strategy** | [**MutableBillingEntity**](MutableBillingEntity.md)| The usage-rounding-strategy object to be updated. | 

### Return type

[**UsageRoundingStrategyPagedMetadata**](UsageRoundingStrategyPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

