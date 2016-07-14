# billforward.PricingcomponenttiersApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pricing_component_tier**](PricingcomponenttiersApi.md#create_pricing_component_tier) | **POST** /pricing-component-tiers | Create
[**get_all_pricing_component_tiers**](PricingcomponenttiersApi.md#get_all_pricing_component_tiers) | **GET** /pricing-component-tiers | Returns a collection of pricing-component-tier-tiers. By default 10 values are returned. Records are returned in natural order.
[**get_pricing_component_tier**](PricingcomponenttiersApi.md#get_pricing_component_tier) | **GET** /pricing-component-tiers/{pricing-component-tier-ID} | Returns a collection of pricing-component-tier-tiers, specified by the pricing-component-tier-ID parameter. By default 10 values are returned. Records are returned in natural order.
[**get_pricing_component_tier_by_product_rate_plan_id**](PricingcomponenttiersApi.md#get_pricing_component_tier_by_product_rate_plan_id) | **GET** /pricing-component-tiers/product-rate-plan/{product-rate-plan-ID} | Returns a collection of pricing-component-tier-tiers, specified by the product-rate-plan-ID parameter. By default 10 values are returned. Records are returned in natural order.
[**update_pricing_component_tier**](PricingcomponenttiersApi.md#update_pricing_component_tier) | **PUT** /pricing-component-tiers | Update.


# **create_pricing_component_tier**
> PricingComponentTierPagedMetadata create_pricing_component_tier(pricing_component_tier)

Create

{\"nickname\":\"Create a new tier\",\"request\":\"createPricingComponentTierRequest.html\",\"response\":\"createPricingComponentTierResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.PricingcomponenttiersApi()
pricing_component_tier = billforward.PricingComponentTier() # PricingComponentTier | The pricing-component-tier object to be updated.

try: 
    # Create
    api_response = api_instance.create_pricing_component_tier(pricing_component_tier)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PricingcomponenttiersApi->create_pricing_component_tier: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pricing_component_tier** | [**PricingComponentTier**](PricingComponentTier.md)| The pricing-component-tier object to be updated. | 

### Return type

[**PricingComponentTierPagedMetadata**](PricingComponentTierPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_pricing_component_tiers**
> PricingComponentTierPagedMetadata get_all_pricing_component_tiers(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Returns a collection of pricing-component-tier-tiers. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get all tiers\",\"response\":\"getPricingComponentTiersAll.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.PricingcomponenttiersApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first pricing-component-tier-tier to return. (optional) (default to 0)
records = 10 # int | The maximum number of pricing-component-tier-tiers to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Returns a collection of pricing-component-tier-tiers. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_pricing_component_tiers(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PricingcomponenttiersApi->get_all_pricing_component_tiers: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first pricing-component-tier-tier to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of pricing-component-tier-tiers to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**PricingComponentTierPagedMetadata**](PricingComponentTierPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pricing_component_tier**
> PricingComponentTierPagedMetadata get_pricing_component_tier(pricing_component_tier_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Returns a collection of pricing-component-tier-tiers, specified by the pricing-component-tier-ID parameter. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve an existing tier\",\"response\":\"getPricingComponentTiersByID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.PricingcomponenttiersApi()
pricing_component_tier_id = 'pricing_component_tier_id_example' # str | The string ID of the pricing-component-tier-tier.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first pricing-component-tier-tier to return. (optional) (default to 0)
records = 10 # int | The maximum number of pricing-component-tier-tiers to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Returns a collection of pricing-component-tier-tiers, specified by the pricing-component-tier-ID parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_pricing_component_tier(pricing_component_tier_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PricingcomponenttiersApi->get_pricing_component_tier: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pricing_component_tier_id** | **str**| The string ID of the pricing-component-tier-tier. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first pricing-component-tier-tier to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of pricing-component-tier-tiers to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**PricingComponentTierPagedMetadata**](PricingComponentTierPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pricing_component_tier_by_product_rate_plan_id**
> PricingComponentTierPagedMetadata get_pricing_component_tier_by_product_rate_plan_id(product_rate_plan_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Returns a collection of pricing-component-tier-tiers, specified by the product-rate-plan-ID parameter. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by rate-plan\",\"response\":\"getPricingComponentTiersByPRP.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.PricingcomponenttiersApi()
product_rate_plan_id = 'product_rate_plan_id_example' # str | The string product-rate-plan-ID of the pricing-component-tier-tier.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first pricing-component-tier-tier to return. (optional) (default to 0)
records = 10 # int | The maximum number of pricing-component-tier-tiers to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Returns a collection of pricing-component-tier-tiers, specified by the product-rate-plan-ID parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_pricing_component_tier_by_product_rate_plan_id(product_rate_plan_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PricingcomponenttiersApi->get_pricing_component_tier_by_product_rate_plan_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_rate_plan_id** | **str**| The string product-rate-plan-ID of the pricing-component-tier-tier. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first pricing-component-tier-tier to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of pricing-component-tier-tiers to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**PricingComponentTierPagedMetadata**](PricingComponentTierPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pricing_component_tier**
> PricingComponentTierPagedMetadata update_pricing_component_tier(pricing_component_tier)

Update.

{\"nickname\":\"Update a tier\",\"request\":\"updatePricingComponentTierRequest.html\",\"response\":\"updatePricingComponentTierResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.PricingcomponenttiersApi()
pricing_component_tier = billforward.PricingComponentTier() # PricingComponentTier | The pricing-component-tier object to be updated.

try: 
    # Update.
    api_response = api_instance.update_pricing_component_tier(pricing_component_tier)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PricingcomponenttiersApi->update_pricing_component_tier: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pricing_component_tier** | [**PricingComponentTier**](PricingComponentTier.md)| The pricing-component-tier object to be updated. | 

### Return type

[**PricingComponentTierPagedMetadata**](PricingComponentTierPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

