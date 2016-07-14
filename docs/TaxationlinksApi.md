# swagger_client.TaxationlinksApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_taxation_link**](TaxationlinksApi.md#create_taxation_link) | **POST** /taxation-links | Create
[**get_all_taxation_links**](TaxationlinksApi.md#get_all_taxation_links) | **GET** /taxation-links | Returns a collection of all taxation-links. By default 10 values are returned. Records are returned in natural order.
[**get_taxation_link_by_id**](TaxationlinksApi.md#get_taxation_link_by_id) | **GET** /taxation-links/{taxation-link-ID} | Returns a single taxation-link, specified by the taxation-link-ID parameter.
[**get_taxation_link_by_product_rate_plan**](TaxationlinksApi.md#get_taxation_link_by_product_rate_plan) | **GET** /taxation-links/product-rate-plan/{product-rate-plan-ID} | Returns a collection of taxation-links, specified by the product-rate-plan-ID parameter. By default 10 values are returned. Records are returned in natural order.
[**get_taxation_link_by_taxation_strategy**](TaxationlinksApi.md#get_taxation_link_by_taxation_strategy) | **GET** /taxation-links/taxation-strategy/{taxation-strategy-ID} | Returns a collection of taxation-links, specified by the taxation-strategy-ID parameter. By default 10 values are returned. Records are returned in natural order.
[**update_taxation_link**](TaxationlinksApi.md#update_taxation_link) | **PUT** /taxation-links | Update


# **create_taxation_link**
> TaxationLinkPagedMetadata create_taxation_link(taxation_link)

Create

{\"nickname\":\"Add a taxation strategy to a rate-plan\",\"request\":\"createTaxationLinkRequest.html\",\"response\":\"createTaxationLinkResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TaxationlinksApi()
taxation_link = swagger_client.MutableBillingEntity() # MutableBillingEntity | The taxation-link object to be updated.

try: 
    # Create
    api_response = api_instance.create_taxation_link(taxation_link)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TaxationlinksApi->create_taxation_link: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxation_link** | [**MutableBillingEntity**](MutableBillingEntity.md)| The taxation-link object to be updated. | 

### Return type

[**TaxationLinkPagedMetadata**](TaxationLinkPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_taxation_links**
> TaxationLinkPagedMetadata get_all_taxation_links(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of all taxation-links. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get all taxation links\",\"response\":\"getTaxationLinkAll.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TaxationlinksApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first taxation-link to return. (optional) (default to 0)
records = 10 # int | The maximum number of taxation-links to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)

try: 
    # Returns a collection of all taxation-links. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_taxation_links(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TaxationlinksApi->get_all_taxation_links: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first taxation-link to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of taxation-links to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]

### Return type

[**TaxationLinkPagedMetadata**](TaxationLinkPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_taxation_link_by_id**
> TaxationLinkPagedMetadata get_taxation_link_by_id(taxation_link_id, organizations=organizations)

Returns a single taxation-link, specified by the taxation-link-ID parameter.

{\"nickname\":\"Retrieve an existing taxation link\",\"response\":\"getTaxationLinkByID.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TaxationlinksApi()
taxation_link_id = 'taxation_link_id_example' # str | The unique ID of the Taxation Link.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single taxation-link, specified by the taxation-link-ID parameter.
    api_response = api_instance.get_taxation_link_by_id(taxation_link_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TaxationlinksApi->get_taxation_link_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxation_link_id** | **str**| The unique ID of the Taxation Link. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**TaxationLinkPagedMetadata**](TaxationLinkPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_taxation_link_by_product_rate_plan**
> TaxationLinkPagedMetadata get_taxation_link_by_product_rate_plan(product_rate_plan_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of taxation-links, specified by the product-rate-plan-ID parameter. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by rate-plan\",\"response\":\"getTaxationLinkByPRPID.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TaxationlinksApi()
product_rate_plan_id = 'product_rate_plan_id_example' # str | The ID of the product-rate-plan
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first taxation-link to return. (optional) (default to 0)
records = 10 # int | The maximum number of taxation-links to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)

try: 
    # Returns a collection of taxation-links, specified by the product-rate-plan-ID parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_taxation_link_by_product_rate_plan(product_rate_plan_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TaxationlinksApi->get_taxation_link_by_product_rate_plan: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_rate_plan_id** | **str**| The ID of the product-rate-plan | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first taxation-link to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of taxation-links to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]

### Return type

[**TaxationLinkPagedMetadata**](TaxationLinkPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_taxation_link_by_taxation_strategy**
> TaxationLinkPagedMetadata get_taxation_link_by_taxation_strategy(taxation_strategy_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of taxation-links, specified by the taxation-strategy-ID parameter. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by taxation strategy\",\"response\":\"getTaxationLinkByTSID.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TaxationlinksApi()
taxation_strategy_id = 'taxation_strategy_id_example' # str | The ID of the taxation-strategy
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first taxation-link to return. (optional) (default to 0)
records = 10 # int | The maximum number of taxation-links to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)

try: 
    # Returns a collection of taxation-links, specified by the taxation-strategy-ID parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_taxation_link_by_taxation_strategy(taxation_strategy_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TaxationlinksApi->get_taxation_link_by_taxation_strategy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxation_strategy_id** | **str**| The ID of the taxation-strategy | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first taxation-link to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of taxation-links to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]

### Return type

[**TaxationLinkPagedMetadata**](TaxationLinkPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_taxation_link**
> TaxationLinkPagedMetadata update_taxation_link(taxation_link)

Update

{\"nickname\":\"Change taxation linked to rate-plan\",\"request\":\"updateTaxationLinkRequest.html\",\"response\":\"updateTaxationLinkResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TaxationlinksApi()
taxation_link = swagger_client.MutableBillingEntity() # MutableBillingEntity | The taxation-link object to be updated.

try: 
    # Update
    api_response = api_instance.update_taxation_link(taxation_link)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TaxationlinksApi->update_taxation_link: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxation_link** | [**MutableBillingEntity**](MutableBillingEntity.md)| The taxation-link object to be updated. | 

### Return type

[**TaxationLinkPagedMetadata**](TaxationLinkPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

