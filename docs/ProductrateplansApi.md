# billforward.ProductrateplansApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_taxation_strategy_to_rate_plan**](ProductrateplansApi.md#add_taxation_strategy_to_rate_plan) | **POST** /product-rate-plans/{product-rate-plan-ID}/tax | Adds or re-enables the specified taxation-strategy for the given product-rate-plan.
[**create_rate_plan**](ProductrateplansApi.md#create_rate_plan) | **POST** /product-rate-plans | Create a new rate-plan.
[**delete_metadata_for_rate_plan**](ProductrateplansApi.md#delete_metadata_for_rate_plan) | **DELETE** /product-rate-plans/{product-rate-plan-ID}/metadata | Remove any associated metadata.
[**get_all_rate_plans**](ProductrateplansApi.md#get_all_rate_plans) | **GET** /product-rate-plans | Returns a collection of product-rate-plans. By default 10 values are returned. Records are returned in natural order.
[**get_available_taxation_strategies_for_rate_plan**](ProductrateplansApi.md#get_available_taxation_strategies_for_rate_plan) | **GET** /product-rate-plans/{product-rate-plan-ID}/tax | Returns all available taxes for the specified product-rate-plan. By default 10 values are returned. Records are returned in natural order.
[**get_metadata_for_rate_plan**](ProductrateplansApi.md#get_metadata_for_rate_plan) | **GET** /product-rate-plans/{product-rate-plan-ID}/metadata | Retrieve any associated metadata.
[**get_product_rate_plan_by_id**](ProductrateplansApi.md#get_product_rate_plan_by_id) | **GET** /product-rate-plans/{product-rate-plan-ID} | Returns product-rate-plans, specified by the product-rate-plan id or name.
[**get_rate_plan_by_product**](ProductrateplansApi.md#get_rate_plan_by_product) | **GET** /product-rate-plans/product/{product-ID} | Returns a collection of product-rate-plans, specified by the product-ID parameter. By default 10 values are returned. Records are returned in natural order.
[**get_rate_plan_by_product_and_rate_plan**](ProductrateplansApi.md#get_rate_plan_by_product_and_rate_plan) | **GET** /product-rate-plans/product/{product-ID}/rate-plan/{rate-plan-ID} | Returns a collection of product-rate-plans, specified by the product-ID parameter. By default 10 values are returned. Records are returned in natural order.
[**remove_taxation_strategy_from_rate_plan**](ProductrateplansApi.md#remove_taxation_strategy_from_rate_plan) | **DELETE** /product-rate-plans/{product-rate-plan-ID}/tax/{taxation-strategy-ID} | Removes the specified taxation-strategy for the given product-rate-plan.
[**retire_rate_plan**](ProductrateplansApi.md#retire_rate_plan) | **DELETE** /product-rate-plans/{product-rate-plan-ID} | Retires the product-rate-plan specified product-rate-plan-ID.
[**set_metadata_for_rate_plan**](ProductrateplansApi.md#set_metadata_for_rate_plan) | **POST** /product-rate-plans/{product-rate-plan-ID}/metadata | Remove any existing metadata keys and create the provided data.
[**update_rate_plan**](ProductrateplansApi.md#update_rate_plan) | **PUT** /product-rate-plans | Update a rate-plan.
[**upsert_metadata_for_rate_plan**](ProductrateplansApi.md#upsert_metadata_for_rate_plan) | **PUT** /product-rate-plans/{product-rate-plan-ID}/metadata | Update any existing metadata key-values and insert any new key-values, no keys will be removed.


# **add_taxation_strategy_to_rate_plan**
> TaxationStrategyPagedMetadata add_taxation_strategy_to_rate_plan(product_rate_plan_id, taxation_strategy)

Adds or re-enables the specified taxation-strategy for the given product-rate-plan.

{\"nickname\":\"Add tax\",\"response\":\"addTaxationStrategy.html\",\"request\":\"addTaxationStrategy.request.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.ProductrateplansApi()
product_rate_plan_id = 'product_rate_plan_id_example' # str | 
taxation_strategy = billforward.AddTaxationStrategyRequest() # AddTaxationStrategyRequest | The taxation-strategy

try: 
    # Adds or re-enables the specified taxation-strategy for the given product-rate-plan.
    api_response = api_instance.add_taxation_strategy_to_rate_plan(product_rate_plan_id, taxation_strategy)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProductrateplansApi->add_taxation_strategy_to_rate_plan: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_rate_plan_id** | **str**|  | 
 **taxation_strategy** | [**AddTaxationStrategyRequest**](AddTaxationStrategyRequest.md)| The taxation-strategy | 

### Return type

[**TaxationStrategyPagedMetadata**](TaxationStrategyPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_rate_plan**
> ProductRatePlanPagedMetadata create_rate_plan(product_rate_plan)

Create a new rate-plan.

{\"nickname\":\"Create a new rate-plan\",\"request\":\"createPRPRequest.html\",\"response\":\"createPRPResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.ProductrateplansApi()
product_rate_plan = billforward.ProductRatePlan() # ProductRatePlan | The product-rate-plan object to be created.

try: 
    # Create a new rate-plan.
    api_response = api_instance.create_rate_plan(product_rate_plan)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProductrateplansApi->create_rate_plan: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_rate_plan** | [**ProductRatePlan**](ProductRatePlan.md)| The product-rate-plan object to be created. | 

### Return type

[**ProductRatePlanPagedMetadata**](ProductRatePlanPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_metadata_for_rate_plan**
> DynamicMetadata delete_metadata_for_rate_plan(product_rate_plan_id, organizations=organizations)

Remove any associated metadata.

{\"nickname\":\"Clear metadata from rate-plan\",\"request\" :\"deleteRatePlanMetadataRequest.html\",\"response\":\"deleteRatePlanMetadataResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.ProductrateplansApi()
product_rate_plan_id = 'product_rate_plan_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Remove any associated metadata.
    api_response = api_instance.delete_metadata_for_rate_plan(product_rate_plan_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProductrateplansApi->delete_metadata_for_rate_plan: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_rate_plan_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**DynamicMetadata**](DynamicMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_rate_plans**
> ProductRatePlanPagedMetadata get_all_rate_plans(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, metadata=metadata)

Returns a collection of product-rate-plans. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get all rate-plans\",\"response\":\"getPRPAll.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.ProductrateplansApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first product-rate-plan to return. (optional) (default to 0)
records = 10 # int | The maximum number of product-rate-plans to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired products should be returned. (optional) (default to false)
metadata = 'metadata_example' # str |  (optional)

try: 
    # Returns a collection of product-rate-plans. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_rate_plans(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, metadata=metadata)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProductrateplansApi->get_all_rate_plans: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first product-rate-plan to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of product-rate-plans to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to false]
 **metadata** | **str**|  | [optional] 

### Return type

[**ProductRatePlanPagedMetadata**](ProductRatePlanPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_taxation_strategies_for_rate_plan**
> TaxationStrategyPagedMetadata get_available_taxation_strategies_for_rate_plan(product_rate_plan_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Returns all available taxes for the specified product-rate-plan. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"List taxes\",\"response\":\"getAvailableTaxationStrategies.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.ProductrateplansApi()
product_rate_plan_id = 'product_rate_plan_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first subscription to return. (optional) (default to 0)
records = 10 # int | The maximum number of subscriptions to return. (optional) (default to 10)
order_by = 'id' # str | Specify a field used to order the result set. (optional) (default to id)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Returns all available taxes for the specified product-rate-plan. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_available_taxation_strategies_for_rate_plan(product_rate_plan_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProductrateplansApi->get_available_taxation_strategies_for_rate_plan: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_rate_plan_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first subscription to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of subscriptions to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to id]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**TaxationStrategyPagedMetadata**](TaxationStrategyPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_for_rate_plan**
> DynamicMetadata get_metadata_for_rate_plan(product_rate_plan_id, organizations=organizations)

Retrieve any associated metadata.

{\"nickname\":\"Retrieve metadata on rate-plan\",\"request\":\"getRatePlanMetadataRequest.html\",\"response\":\"getRatePlanMetadataResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.ProductrateplansApi()
product_rate_plan_id = 'product_rate_plan_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Retrieve any associated metadata.
    api_response = api_instance.get_metadata_for_rate_plan(product_rate_plan_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProductrateplansApi->get_metadata_for_rate_plan: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_rate_plan_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**DynamicMetadata**](DynamicMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_rate_plan_by_id**
> ProductRatePlanPagedMetadata get_product_rate_plan_by_id(product_rate_plan_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns product-rate-plans, specified by the product-rate-plan id or name.

{\"nickname\":\"Retrieve an existing rate-plan\",\"response\":\"getPRPByID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.ProductrateplansApi()
product_rate_plan_id = 'product_rate_plan_id_example' # str | id or name of the product-rate-plan.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first product-rate-plan to return. (optional) (default to 0)
records = 10 # int | The maximum number of product-rate-plans to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired products should be returned. (optional) (default to false)

try: 
    # Returns product-rate-plans, specified by the product-rate-plan id or name.
    api_response = api_instance.get_product_rate_plan_by_id(product_rate_plan_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProductrateplansApi->get_product_rate_plan_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_rate_plan_id** | **str**| id or name of the product-rate-plan. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first product-rate-plan to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of product-rate-plans to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to false]

### Return type

[**ProductRatePlanPagedMetadata**](ProductRatePlanPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rate_plan_by_product**
> ProductRatePlanPagedMetadata get_rate_plan_by_product(product_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of product-rate-plans, specified by the product-ID parameter. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by product\",\"response\":\"getPRPByProductID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.ProductrateplansApi()
product_id = 'product_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first product-rate-plan to return. (optional) (default to 0)
records = 10 # int | The maximum number of product-rate-plans to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)

try: 
    # Returns a collection of product-rate-plans, specified by the product-ID parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_rate_plan_by_product(product_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProductrateplansApi->get_rate_plan_by_product: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first product-rate-plan to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of product-rate-plans to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]

### Return type

[**ProductRatePlanPagedMetadata**](ProductRatePlanPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rate_plan_by_product_and_rate_plan**
> ProductRatePlanPagedMetadata get_rate_plan_by_product_and_rate_plan(product_id, rate_plan_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of product-rate-plans, specified by the product-ID parameter. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by name\",\"response\":\"getPRPByNameAndProduct.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.ProductrateplansApi()
product_id = 'product_id_example' # str | 
rate_plan_id = 'rate_plan_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first product-rate-plan to return. (optional) (default to 0)
records = 10 # int | The maximum number of product-rate-plans to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired products should be returned. (optional) (default to false)

try: 
    # Returns a collection of product-rate-plans, specified by the product-ID parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_rate_plan_by_product_and_rate_plan(product_id, rate_plan_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProductrateplansApi->get_rate_plan_by_product_and_rate_plan: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 
 **rate_plan_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first product-rate-plan to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of product-rate-plans to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to false]

### Return type

[**ProductRatePlanPagedMetadata**](ProductRatePlanPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_taxation_strategy_from_rate_plan**
> TaxationStrategyPagedMetadata remove_taxation_strategy_from_rate_plan(product_rate_plan_id, taxation_strategy_id, organizations=organizations)

Removes the specified taxation-strategy for the given product-rate-plan.

{\"nickname\":\"Remove tax\",\"response\":\"removeTaxationStrategy.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.ProductrateplansApi()
product_rate_plan_id = 'product_rate_plan_id_example' # str | 
taxation_strategy_id = 'taxation_strategy_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Removes the specified taxation-strategy for the given product-rate-plan.
    api_response = api_instance.remove_taxation_strategy_from_rate_plan(product_rate_plan_id, taxation_strategy_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProductrateplansApi->remove_taxation_strategy_from_rate_plan: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_rate_plan_id** | **str**|  | 
 **taxation_strategy_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**TaxationStrategyPagedMetadata**](TaxationStrategyPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retire_rate_plan**
> ProductRatePlanPagedMetadata retire_rate_plan(product_rate_plan_id, organizations=organizations)

Retires the product-rate-plan specified product-rate-plan-ID.

{\"nickname\":\"Delete a rate-plan\",\"response\":\"deletePRP.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.ProductrateplansApi()
product_rate_plan_id = 'product_rate_plan_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Retires the product-rate-plan specified product-rate-plan-ID.
    api_response = api_instance.retire_rate_plan(product_rate_plan_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProductrateplansApi->retire_rate_plan: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_rate_plan_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**ProductRatePlanPagedMetadata**](ProductRatePlanPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_metadata_for_rate_plan**
> DynamicMetadata set_metadata_for_rate_plan(metadata, product_rate_plan_id, organizations=organizations)

Remove any existing metadata keys and create the provided data.

{\"nickname\":\"Set metadata on rate-plan\",\"request\":\"setRatePlanMetadataRequest.html\",\"response\":\"setRatePlanMetadataResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.ProductrateplansApi()
metadata = billforward.DynamicMetadata() # DynamicMetadata | 
product_rate_plan_id = 'product_rate_plan_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Remove any existing metadata keys and create the provided data.
    api_response = api_instance.set_metadata_for_rate_plan(metadata, product_rate_plan_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProductrateplansApi->set_metadata_for_rate_plan: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata** | [**DynamicMetadata**](DynamicMetadata.md)|  | 
 **product_rate_plan_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**DynamicMetadata**](DynamicMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rate_plan**
> ProductRatePlanPagedMetadata update_rate_plan(product_rate_plan)

Update a rate-plan.

{\"nickname\":\"Update a rate-plan\",\"request\":\"updatePRPRequest.html\",\"response\":\"updatePRPResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.ProductrateplansApi()
product_rate_plan = billforward.ProductRatePlan() # ProductRatePlan | The product-rate-plan object to be updated.

try: 
    # Update a rate-plan.
    api_response = api_instance.update_rate_plan(product_rate_plan)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProductrateplansApi->update_rate_plan: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_rate_plan** | [**ProductRatePlan**](ProductRatePlan.md)| The product-rate-plan object to be updated. | 

### Return type

[**ProductRatePlanPagedMetadata**](ProductRatePlanPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_metadata_for_rate_plan**
> DynamicMetadata upsert_metadata_for_rate_plan(metadata, product_rate_plan_id, organizations=organizations)

Update any existing metadata key-values and insert any new key-values, no keys will be removed.

{\"nickname\":\"Upsert metadata on rate-plan\",\"request\":\"upsertRatePlanMetadataRequest.html\",\"response\":\"upsertRatePlanMetadataResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.ProductrateplansApi()
metadata = billforward.DynamicMetadata() # DynamicMetadata | 
product_rate_plan_id = 'product_rate_plan_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Update any existing metadata key-values and insert any new key-values, no keys will be removed.
    api_response = api_instance.upsert_metadata_for_rate_plan(metadata, product_rate_plan_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProductrateplansApi->upsert_metadata_for_rate_plan: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata** | [**DynamicMetadata**](DynamicMetadata.md)|  | 
 **product_rate_plan_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**DynamicMetadata**](DynamicMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

