# billforward.CouponbookdefinitionApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_coupon_book_definition**](CouponbookdefinitionApi.md#create_coupon_book_definition) | **POST** /coupon-book-definitions | Create a coupon-book-definition.
[**delete_coupon_book_definition**](CouponbookdefinitionApi.md#delete_coupon_book_definition) | **DELETE** /coupon-book-definitions/{coupon-book-definition-ID} | Retire a coupon-book-definition, specified by the coupon-book-definition-ID parameter.
[**get_all_coupon_book_definitions**](CouponbookdefinitionApi.md#get_all_coupon_book_definitions) | **GET** /coupon-book-definitions | Returns a collection of coupon-book-definitions. By default 10 values are returned. Records are returned in natural order.
[**get_coupon_book_definition_by_coupon_definition_id**](CouponbookdefinitionApi.md#get_coupon_book_definition_by_coupon_definition_id) | **GET** /coupon-book-definitions/coupon-definition/{coupon-definition-ID} | Returns a collection of coupon-book-definitions, specified by coupon-definition-ID parameter. By default 10 coupon-book-definitions are returned. Records are returned in natural order.
[**get_coupon_book_definition_by_id**](CouponbookdefinitionApi.md#get_coupon_book_definition_by_id) | **GET** /coupon-book-definitions/{coupon-book-definition-ID} | Returns a single coupon-book-definition, specified by the coupon-book-definition-ID parameter.
[**update_coupon_book_definition**](CouponbookdefinitionApi.md#update_coupon_book_definition) | **PUT** /coupon-book-definitions | Update a coupon-book-definition.


# **create_coupon_book_definition**
> CouponBookDefinitionPagedMetadata create_coupon_book_definition(coupon_book_definition)

Create a coupon-book-definition.

{\"nickname\":\"Create a new book definition\",\"request\":\"createCouponBookDefinitionRequest.html\",\"response\":\"createCouponBookDefinitionResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.CouponbookdefinitionApi()
coupon_book_definition = billforward.CouponBookDefinition() # CouponBookDefinition | The coupon-book-definition object to be created.

try: 
    # Create a coupon-book-definition.
    api_response = api_instance.create_coupon_book_definition(coupon_book_definition)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponbookdefinitionApi->create_coupon_book_definition: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_book_definition** | [**CouponBookDefinition**](CouponBookDefinition.md)| The coupon-book-definition object to be created. | 

### Return type

[**CouponBookDefinitionPagedMetadata**](CouponBookDefinitionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_coupon_book_definition**
> CouponBookDefinitionPagedMetadata delete_coupon_book_definition(coupon_book_definition_id, organizations=organizations)

Retire a coupon-book-definition, specified by the coupon-book-definition-ID parameter.

{\"nickname\":\"Delete book definition\",\"response\":\"deleteCouponBookDefinitionByID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.CouponbookdefinitionApi()
coupon_book_definition_id = 'coupon_book_definition_id_example' # str | ID of the coupon-definition.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Retire a coupon-book-definition, specified by the coupon-book-definition-ID parameter.
    api_response = api_instance.delete_coupon_book_definition(coupon_book_definition_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponbookdefinitionApi->delete_coupon_book_definition: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_book_definition_id** | **str**| ID of the coupon-definition. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**CouponBookDefinitionPagedMetadata**](CouponBookDefinitionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_coupon_book_definitions**
> CouponBookDefinitionPagedMetadata get_all_coupon_book_definitions(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of coupon-book-definitions. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get all book definitions\",\"response\":\"getCouponBookDefinitionAll.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.CouponbookdefinitionApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first product-rate-plan to return. (optional) (default to 0)
records = 10 # int | The maximum number of product-rate-plans to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired coupon-book-definitions should be returned. (optional) (default to true)

try: 
    # Returns a collection of coupon-book-definitions. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_coupon_book_definitions(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponbookdefinitionApi->get_all_coupon_book_definitions: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first product-rate-plan to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of product-rate-plans to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired coupon-book-definitions should be returned. | [optional] [default to true]

### Return type

[**CouponBookDefinitionPagedMetadata**](CouponBookDefinitionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupon_book_definition_by_coupon_definition_id**
> CouponBookDefinitionPagedMetadata get_coupon_book_definition_by_coupon_definition_id(coupon_definition_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of coupon-book-definitions, specified by coupon-definition-ID parameter. By default 10 coupon-book-definitions are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by coupon definition\",\"response\":\"getCouponBookDefinitionByCouponDefinitionID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.CouponbookdefinitionApi()
coupon_definition_id = 'coupon_definition_id_example' # str | The string coupon-definition-ID of the coupon-book-definition.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first coupon-book-definition to return. (optional) (default to 0)
records = 10 # int | The maximum number of coupon-book-definitions to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired coupon-book-definitions should be returned. (optional) (default to true)

try: 
    # Returns a collection of coupon-book-definitions, specified by coupon-definition-ID parameter. By default 10 coupon-book-definitions are returned. Records are returned in natural order.
    api_response = api_instance.get_coupon_book_definition_by_coupon_definition_id(coupon_definition_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponbookdefinitionApi->get_coupon_book_definition_by_coupon_definition_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_definition_id** | **str**| The string coupon-definition-ID of the coupon-book-definition. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first coupon-book-definition to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of coupon-book-definitions to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired coupon-book-definitions should be returned. | [optional] [default to true]

### Return type

[**CouponBookDefinitionPagedMetadata**](CouponBookDefinitionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupon_book_definition_by_id**
> CouponBookDefinitionPagedMetadata get_coupon_book_definition_by_id(coupon_book_definition_id, organizations=organizations)

Returns a single coupon-book-definition, specified by the coupon-book-definition-ID parameter.

{\"nickname\":\"Retrieve an existing book definition\",\"response\":\"getCouponBookDefinitionByID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.CouponbookdefinitionApi()
coupon_book_definition_id = 'coupon_book_definition_id_example' # str | ID of the coupon-book-definition.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single coupon-book-definition, specified by the coupon-book-definition-ID parameter.
    api_response = api_instance.get_coupon_book_definition_by_id(coupon_book_definition_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponbookdefinitionApi->get_coupon_book_definition_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_book_definition_id** | **str**| ID of the coupon-book-definition. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**CouponBookDefinitionPagedMetadata**](CouponBookDefinitionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_coupon_book_definition**
> CouponBookDefinitionPagedMetadata update_coupon_book_definition(coupon_book_definition)

Update a coupon-book-definition.

{\"nickname\":\"Update a book definition\",\"request\":\"updateCouponBookDefinitionRequest.html\",\"response\":\"updateCouponBookDefinitionResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.CouponbookdefinitionApi()
coupon_book_definition = billforward.CouponBookDefinition() # CouponBookDefinition | The coupon-book-definition object to be updated.

try: 
    # Update a coupon-book-definition.
    api_response = api_instance.update_coupon_book_definition(coupon_book_definition)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponbookdefinitionApi->update_coupon_book_definition: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_book_definition** | [**CouponBookDefinition**](CouponBookDefinition.md)| The coupon-book-definition object to be updated. | 

### Return type

[**CouponBookDefinitionPagedMetadata**](CouponBookDefinitionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

