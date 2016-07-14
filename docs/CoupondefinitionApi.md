# swagger_client.CoupondefinitionApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_coupon_definition**](CoupondefinitionApi.md#create_coupon_definition) | **POST** /coupon-definitions | Create a coupon-definition.
[**delete_coupon_definition**](CoupondefinitionApi.md#delete_coupon_definition) | **DELETE** /coupon-definitions/{coupon-definition-ID} | Retire a coupon-definition, specified by the coupon-definition-ID parameter.
[**get_all_coupon_definitions**](CoupondefinitionApi.md#get_all_coupon_definitions) | **GET** /coupon-definitions | Returns a collection of coupon-definitions. By default 10 values are returned. Records are returned in natural order.
[**get_coupon_definition_by_id**](CoupondefinitionApi.md#get_coupon_definition_by_id) | **GET** /coupon-definitions/{coupon-definition-ID} | Returns a single coupon-definition, specified by the coupon-definition-ID parameter.
[**update_coupon_definition**](CoupondefinitionApi.md#update_coupon_definition) | **PUT** /coupon-definitions | Update a coupon-definition.


# **create_coupon_definition**
> CouponDefinitionPagedMetadata create_coupon_definition(coupon_definition)

Create a coupon-definition.

{\"nickname\":\"Create a new definition\",\"request\":\"createCouponDefinitionRequest.html\",\"response\":\"createCouponDefinitionResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoupondefinitionApi()
coupon_definition = swagger_client.CouponDefinition() # CouponDefinition | The coupon-definiton object to be created.

try: 
    # Create a coupon-definition.
    api_response = api_instance.create_coupon_definition(coupon_definition)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CoupondefinitionApi->create_coupon_definition: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_definition** | [**CouponDefinition**](CouponDefinition.md)| The coupon-definiton object to be created. | 

### Return type

[**CouponDefinitionPagedMetadata**](CouponDefinitionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_coupon_definition**
> CouponDefinitionPagedMetadata delete_coupon_definition(coupon_definition_id, organizations=organizations)

Retire a coupon-definition, specified by the coupon-definition-ID parameter.

{\"nickname\":\"Delete a definition\",\"response\":\"deleteCouponDefinitionByID.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoupondefinitionApi()
coupon_definition_id = 'coupon_definition_id_example' # str | ID of the coupon-definition.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Retire a coupon-definition, specified by the coupon-definition-ID parameter.
    api_response = api_instance.delete_coupon_definition(coupon_definition_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CoupondefinitionApi->delete_coupon_definition: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_definition_id** | **str**| ID of the coupon-definition. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**CouponDefinitionPagedMetadata**](CouponDefinitionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_coupon_definitions**
> CouponDefinitionPagedMetadata get_all_coupon_definitions(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of coupon-definitions. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get all coupon definitions\",\"response\":\"getCouponDefinitionAll.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoupondefinitionApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first product-rate-plan to return. (optional) (default to 0)
records = 10 # int | The maximum number of product-rate-plans to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired coupon-definitions should be returned. (optional) (default to true)

try: 
    # Returns a collection of coupon-definitions. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_coupon_definitions(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CoupondefinitionApi->get_all_coupon_definitions: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first product-rate-plan to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of product-rate-plans to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired coupon-definitions should be returned. | [optional] [default to true]

### Return type

[**CouponDefinitionPagedMetadata**](CouponDefinitionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupon_definition_by_id**
> CouponDefinitionPagedMetadata get_coupon_definition_by_id(coupon_definition_id, organizations=organizations)

Returns a single coupon-definition, specified by the coupon-definition-ID parameter.

{\"nickname\":\"Get existing coupon definition\",\"response\":\"getCouponDefinitionByID.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoupondefinitionApi()
coupon_definition_id = 'coupon_definition_id_example' # str | ID of the coupon-definition.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single coupon-definition, specified by the coupon-definition-ID parameter.
    api_response = api_instance.get_coupon_definition_by_id(coupon_definition_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CoupondefinitionApi->get_coupon_definition_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_definition_id** | **str**| ID of the coupon-definition. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**CouponDefinitionPagedMetadata**](CouponDefinitionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_coupon_definition**
> CouponDefinitionPagedMetadata update_coupon_definition(coupon_definition)

Update a coupon-definition.

{\"nickname\":\"Update a definition\",\"request\":\"updateCouponDefinitionRequest.html\",\"response\":\"updateCouponDefinitionResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoupondefinitionApi()
coupon_definition = swagger_client.CouponDefinition() # CouponDefinition | The coupon-definition object to be updated.

try: 
    # Update a coupon-definition.
    api_response = api_instance.update_coupon_definition(coupon_definition)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CoupondefinitionApi->update_coupon_definition: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_definition** | [**CouponDefinition**](CouponDefinition.md)| The coupon-definition object to be updated. | 

### Return type

[**CouponDefinitionPagedMetadata**](CouponDefinitionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

