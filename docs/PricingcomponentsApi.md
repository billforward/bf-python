# swagger_client.PricingcomponentsApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pricing_component**](PricingcomponentsApi.md#create_pricing_component) | **POST** /pricing-components | Create a pricing-component.
[**get_all_pricing_components**](PricingcomponentsApi.md#get_all_pricing_components) | **GET** /pricing-components | Returns a collection of pricing-components. By default 10 values are returned. Records are returned in natural order.
[**get_pricing_component**](PricingcomponentsApi.md#get_pricing_component) | **GET** /pricing-components/{pricing-component-ID} | Returns a collection of pricing-components, specified by the pricing-component-ID parameter. By default 10 values are returned. Records are returned in natural order.
[**get_pricing_component_by_product_rate_plan_id**](PricingcomponentsApi.md#get_pricing_component_by_product_rate_plan_id) | **GET** /pricing-components/product-rate-plan/{product-rate-plan-ID} | Returns a collection of pricing-components, specified by the product-rate-plan-ID parameter. By default 10 values are returned. Records are returned in natural order.
[**retire_pricing_component**](PricingcomponentsApi.md#retire_pricing_component) | **DELETE** /pricing-components/{pricing-component-ID} | Retires the pricing-component specified by the pricing-component-ID parameter.
[**update_pricing_component**](PricingcomponentsApi.md#update_pricing_component) | **PUT** /pricing-components | Update a pricing-component.


# **create_pricing_component**
> PricingComponentPagedMetadata create_pricing_component(pricing_component)

Create a pricing-component.

{\"nickname\":\"Create a new pricing-component\",\"request\":\"createPricingComponentRequest.html\",\"response\":\"createPricingComponentResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PricingcomponentsApi()
pricing_component = swagger_client.PricingComponent() # PricingComponent | The pricing-component object to be updated.

try: 
    # Create a pricing-component.
    api_response = api_instance.create_pricing_component(pricing_component)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PricingcomponentsApi->create_pricing_component: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pricing_component** | [**PricingComponent**](PricingComponent.md)| The pricing-component object to be updated. | 

### Return type

[**PricingComponentPagedMetadata**](PricingComponentPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_pricing_components**
> PricingComponentPagedMetadata get_all_pricing_components(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of pricing-components. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get all pricing-components\",\"response\":\"getPricingComponentsAll.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PricingcomponentsApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first pricing-component to return. (optional) (default to 0)
records = 10 # int | The maximum number of pricing-components to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)

try: 
    # Returns a collection of pricing-components. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_pricing_components(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PricingcomponentsApi->get_all_pricing_components: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first pricing-component to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of pricing-components to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]

### Return type

[**PricingComponentPagedMetadata**](PricingComponentPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pricing_component**
> PricingComponentPagedMetadata get_pricing_component(pricing_component_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of pricing-components, specified by the pricing-component-ID parameter. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve an existing pricing-component\",\"response\":\"getPricingComponentsByID.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PricingcomponentsApi()
pricing_component_id = 'pricing_component_id_example' # str | The string ID of the pricing-component.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first pricing-component to return. (optional) (default to 0)
records = 10 # int | The maximum number of pricing-components to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)

try: 
    # Returns a collection of pricing-components, specified by the pricing-component-ID parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_pricing_component(pricing_component_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PricingcomponentsApi->get_pricing_component: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pricing_component_id** | **str**| The string ID of the pricing-component. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first pricing-component to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of pricing-components to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]

### Return type

[**PricingComponentPagedMetadata**](PricingComponentPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pricing_component_by_product_rate_plan_id**
> PricingComponentPagedMetadata get_pricing_component_by_product_rate_plan_id(product_rate_plan_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of pricing-components, specified by the product-rate-plan-ID parameter. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by rate-plan\",\"response\":\"getPricingComponentsByPRP.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PricingcomponentsApi()
product_rate_plan_id = 'product_rate_plan_id_example' # str | The string product-rate-plan-ID of the pricing-component.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first pricing-component to return. (optional) (default to 0)
records = 10 # int | The maximum number of pricing-components to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)

try: 
    # Returns a collection of pricing-components, specified by the product-rate-plan-ID parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_pricing_component_by_product_rate_plan_id(product_rate_plan_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PricingcomponentsApi->get_pricing_component_by_product_rate_plan_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_rate_plan_id** | **str**| The string product-rate-plan-ID of the pricing-component. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first pricing-component to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of pricing-components to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]

### Return type

[**PricingComponentPagedMetadata**](PricingComponentPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retire_pricing_component**
> PricingComponentPagedMetadata retire_pricing_component(pricing_component_id, organizations=organizations)

Retires the pricing-component specified by the pricing-component-ID parameter.

{\"nickname\":\"Delete a pricing-component\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PricingcomponentsApi()
pricing_component_id = 'pricing_component_id_example' # str | The string ID of the pricing-component.
organizations = ['organizations_example'] # list[str] | A list of organization IDs used to restrict the scope of API calls. (optional)

try: 
    # Retires the pricing-component specified by the pricing-component-ID parameter.
    api_response = api_instance.retire_pricing_component(pricing_component_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PricingcomponentsApi->retire_pricing_component: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pricing_component_id** | **str**| The string ID of the pricing-component. | 
 **organizations** | [**list[str]**](str.md)| A list of organization IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**PricingComponentPagedMetadata**](PricingComponentPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pricing_component**
> PricingComponentPagedMetadata update_pricing_component(pricing_component)

Update a pricing-component.

{\"nickname\":\"Update a pricing-component\",\"request\":\"updatePricingComponentRequest.html\",\"response\":\"updatePricingComponentResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PricingcomponentsApi()
pricing_component = swagger_client.PricingComponent() # PricingComponent | The pricing-component object to be updated.

try: 
    # Update a pricing-component.
    api_response = api_instance.update_pricing_component(pricing_component)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PricingcomponentsApi->update_pricing_component: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pricing_component** | [**PricingComponent**](PricingComponent.md)| The pricing-component object to be updated. | 

### Return type

[**PricingComponentPagedMetadata**](PricingComponentPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

