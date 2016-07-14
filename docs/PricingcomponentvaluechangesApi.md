# swagger_client.PricingcomponentvaluechangesApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pricing_component_value_change**](PricingcomponentvaluechangesApi.md#create_pricing_component_value_change) | **POST** /pricing-component-value-changes | Create a pricing-component-value-change.
[**get_all_pricing_component_value_changes**](PricingcomponentvaluechangesApi.md#get_all_pricing_component_value_changes) | **GET** /pricing-component-value-changes | Returns a collection of pricing-component-value-changes. By default 10 values are returned. Records are returned in natural order.
[**get_pricing_component_value_change**](PricingcomponentvaluechangesApi.md#get_pricing_component_value_change) | **GET** /pricing-component-value-changes/{ID} | Returns a single pricing-component-value-changes, specified by the ID parameter.
[**get_pricing_component_value_change_by_component_id**](PricingcomponentvaluechangesApi.md#get_pricing_component_value_change_by_component_id) | **GET** /pricing-component-value-changes/component-ID/{pricing-component-ID} | Returns a collection of pricing-component-value-changes, specified by the pricing-component-value-ID parameter. By default 10 values are returned. Records are returned in natural order.
[**get_pricing_component_value_change_by_invoice_id**](PricingcomponentvaluechangesApi.md#get_pricing_component_value_change_by_invoice_id) | **GET** /pricing-component-value-changes/invoice/{invoice-ID} | Returns a collection of pricing-component-value-changes, specified by the invoice-ID parameter. By default 10 values are returned. Records are returned in natural order.
[**get_pricing_component_value_change_by_subscription_id**](PricingcomponentvaluechangesApi.md#get_pricing_component_value_change_by_subscription_id) | **GET** /pricing-component-value-changes/subscription/{subscription-ID} | Returns a collection of pricing-component-value-changes, specified by the subscription-ID parameter. By default 10 values are returned. Records are returned in natural order.


# **create_pricing_component_value_change**
> PricingComponentValueChangePagedMetadata create_pricing_component_value_change(pricing_component_value_change)

Create a pricing-component-value-change.

{\"nickname\":\"Create\",\"request\":\"createPricingComponentValueChangeRequest.html\",\"response\":\"createPricingComponentValueChangeResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PricingcomponentvaluechangesApi()
pricing_component_value_change = swagger_client.InsertableBillingEntity() # InsertableBillingEntity | The pricing-component-value-change object to be updated.

try: 
    # Create a pricing-component-value-change.
    api_response = api_instance.create_pricing_component_value_change(pricing_component_value_change)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PricingcomponentvaluechangesApi->create_pricing_component_value_change: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pricing_component_value_change** | [**InsertableBillingEntity**](InsertableBillingEntity.md)| The pricing-component-value-change object to be updated. | 

### Return type

[**PricingComponentValueChangePagedMetadata**](PricingComponentValueChangePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_pricing_component_value_changes**
> PricingComponentValueChangePagedMetadata get_all_pricing_component_value_changes(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Returns a collection of pricing-component-value-changes. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get All\",\"response\":\"getPricingComponentValueChangeAll.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PricingcomponentvaluechangesApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first pricing-component-value-change to return. (optional) (default to 0)
records = 10 # int | The maximum number of pricing-component-value-changes to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Returns a collection of pricing-component-value-changes. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_pricing_component_value_changes(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PricingcomponentvaluechangesApi->get_all_pricing_component_value_changes: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first pricing-component-value-change to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of pricing-component-value-changes to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**PricingComponentValueChangePagedMetadata**](PricingComponentValueChangePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pricing_component_value_change**
> PricingComponentValueChangePagedMetadata get_pricing_component_value_change(id, organizations=organizations)

Returns a single pricing-component-value-changes, specified by the ID parameter.

{\"nickname\":\"Retrieve by id\",\"response\":\"getPricingComponentValueChangeByID.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PricingcomponentvaluechangesApi()
id = 'id_example' # str | The string ID of the pricing-component-value-change.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single pricing-component-value-changes, specified by the ID parameter.
    api_response = api_instance.get_pricing_component_value_change(id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PricingcomponentvaluechangesApi->get_pricing_component_value_change: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The string ID of the pricing-component-value-change. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**PricingComponentValueChangePagedMetadata**](PricingComponentValueChangePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pricing_component_value_change_by_component_id**
> PricingComponentValueChangePagedMetadata get_pricing_component_value_change_by_component_id(pricing_component_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Returns a collection of pricing-component-value-changes, specified by the pricing-component-value-ID parameter. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by Component-ID\",\"response\":\"getPricingComponentValueChangeByID.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PricingcomponentvaluechangesApi()
pricing_component_id = 'pricing_component_id_example' # str | The string ID of the pricing-component-value.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first pricing-component-value-change to return. (optional) (default to 0)
records = 10 # int | The maximum number of pricing-component-value-changes to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Returns a collection of pricing-component-value-changes, specified by the pricing-component-value-ID parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_pricing_component_value_change_by_component_id(pricing_component_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PricingcomponentvaluechangesApi->get_pricing_component_value_change_by_component_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pricing_component_id** | **str**| The string ID of the pricing-component-value. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first pricing-component-value-change to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of pricing-component-value-changes to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**PricingComponentValueChangePagedMetadata**](PricingComponentValueChangePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pricing_component_value_change_by_invoice_id**
> PricingComponentValueChangePagedMetadata get_pricing_component_value_change_by_invoice_id(invoice_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Returns a collection of pricing-component-value-changes, specified by the invoice-ID parameter. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by Invoice-ID\",\"response\":\"getPricingComponentValueChangeByInvoiceID.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PricingcomponentvaluechangesApi()
invoice_id = 'invoice_id_example' # str | The string invoice-ID of the pricing-component-value-change.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first pricing-component-value-change to return. (optional) (default to 0)
records = 10 # int | The maximum number of pricing-component-value-changes to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Returns a collection of pricing-component-value-changes, specified by the invoice-ID parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_pricing_component_value_change_by_invoice_id(invoice_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PricingcomponentvaluechangesApi->get_pricing_component_value_change_by_invoice_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**| The string invoice-ID of the pricing-component-value-change. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first pricing-component-value-change to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of pricing-component-value-changes to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**PricingComponentValueChangePagedMetadata**](PricingComponentValueChangePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pricing_component_value_change_by_subscription_id**
> PricingComponentValueChangePagedMetadata get_pricing_component_value_change_by_subscription_id(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Returns a collection of pricing-component-value-changes, specified by the subscription-ID parameter. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by Subscription-ID\",\"response\":\"getPricingComponentValueChangeBySubscriptionID.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PricingcomponentvaluechangesApi()
subscription_id = 'subscription_id_example' # str | ID of the subscription.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first pricing-component-value-change to return. (optional) (default to 0)
records = 10 # int | The maximum number of pricing-component-value-changes to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Returns a collection of pricing-component-value-changes, specified by the subscription-ID parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_pricing_component_value_change_by_subscription_id(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PricingcomponentvaluechangesApi->get_pricing_component_value_change_by_subscription_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| ID of the subscription. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first pricing-component-value-change to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of pricing-component-value-changes to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**PricingComponentValueChangePagedMetadata**](PricingComponentValueChangePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

