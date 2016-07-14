# billforward.CouponmodifierApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_coupon_modifier**](CouponmodifierApi.md#create_coupon_modifier) | **POST** /coupon-modifiers | Create a coupon-modifier.
[**delete_coupon_modifier**](CouponmodifierApi.md#delete_coupon_modifier) | **DELETE** /coupon-modifiers/{coupon-modifier-ID} | Retire a coupon-modifier, specified by the coupon-modifier-ID parameter.
[**get_all_coupon_modifiers**](CouponmodifierApi.md#get_all_coupon_modifiers) | **GET** /coupon-modifiers | Returns a collection of coupon-modifiers. By default 10 values are returned. Records are returned in natural order.
[**get_coupon_modifier_by_coupon_code**](CouponmodifierApi.md#get_coupon_modifier_by_coupon_code) | **GET** /coupon-modifiers/coupon-code/{coupon-code} | Returns a collection of coupon-modifiers, specified by the coupon-code parameter.
[**get_coupon_modifier_by_coupon_definition_id**](CouponmodifierApi.md#get_coupon_modifier_by_coupon_definition_id) | **GET** /coupon-modifiers/coupon-definition/{coupon-definition-ID} | Returns a collection of coupon-modifiers, specified by the coupon-definition-ID parameter.
[**get_coupon_modifier_by_id**](CouponmodifierApi.md#get_coupon_modifier_by_id) | **GET** /coupon-modifiers/{coupon-modifier-ID} | Returns a single coupon-modifier, specified by the coupon-modifier-ID parameter.
[**update_coupon_modifier**](CouponmodifierApi.md#update_coupon_modifier) | **PUT** /coupon-modifiers | Update a coupon-instance.


# **create_coupon_modifier**
> CouponModifierBasePagedMetadata create_coupon_modifier(coupon_instance)

Create a coupon-modifier.

{\"nickname\":\"Create a new modifier\",\"request\":\"createCouponModifierRequest.html\",\"response\":\"createCouponModifierResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.CouponmodifierApi()
coupon_instance = billforward.CouponModifierBase() # CouponModifierBase | The coupon-instance object to be created.

try: 
    # Create a coupon-modifier.
    api_response = api_instance.create_coupon_modifier(coupon_instance)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponmodifierApi->create_coupon_modifier: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_instance** | [**CouponModifierBase**](CouponModifierBase.md)| The coupon-instance object to be created. | 

### Return type

[**CouponModifierBasePagedMetadata**](CouponModifierBasePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_coupon_modifier**
> CouponModifierBasePagedMetadata delete_coupon_modifier(coupon_modifier_id, organizations=organizations)

Retire a coupon-modifier, specified by the coupon-modifier-ID parameter.

{\"nickname\":\"Delete a modifier\",\"response\":\"deleteCouponModifierByID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.CouponmodifierApi()
coupon_modifier_id = 'coupon_modifier_id_example' # str | ID of the coupon-modifier.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Retire a coupon-modifier, specified by the coupon-modifier-ID parameter.
    api_response = api_instance.delete_coupon_modifier(coupon_modifier_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponmodifierApi->delete_coupon_modifier: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_modifier_id** | **str**| ID of the coupon-modifier. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**CouponModifierBasePagedMetadata**](CouponModifierBasePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_coupon_modifiers**
> CouponModifierBasePagedMetadata get_all_coupon_modifiers(organizations=organizations, offset=offset, records=records)

Returns a collection of coupon-modifiers. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get all modifiers\",\"response\":\"getCouponModifierAll.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.CouponmodifierApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first product-rate-plan to return. (optional) (default to 0)
records = 10 # int | The maximum number of product-rate-plans to return. (optional) (default to 10)

try: 
    # Returns a collection of coupon-modifiers. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_coupon_modifiers(organizations=organizations, offset=offset, records=records)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponmodifierApi->get_all_coupon_modifiers: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first product-rate-plan to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of product-rate-plans to return. | [optional] [default to 10]

### Return type

[**CouponModifierBasePagedMetadata**](CouponModifierBasePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupon_modifier_by_coupon_code**
> CouponModifierBasePagedMetadata get_coupon_modifier_by_coupon_code(coupon_code, organizations=organizations, offset=offset, records=records)

Returns a collection of coupon-modifiers, specified by the coupon-code parameter.

{\"nickname\":\"Retrieve by coupon code\",\"response\":\"getCouponCode.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.CouponmodifierApi()
coupon_code = 'coupon_code_example' # str | The coupon-code.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first product-rate-plan to return. (optional) (default to 0)
records = 10 # int | The maximum number of product-rate-plans to return. (optional) (default to 10)

try: 
    # Returns a collection of coupon-modifiers, specified by the coupon-code parameter.
    api_response = api_instance.get_coupon_modifier_by_coupon_code(coupon_code, organizations=organizations, offset=offset, records=records)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponmodifierApi->get_coupon_modifier_by_coupon_code: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_code** | **str**| The coupon-code. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first product-rate-plan to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of product-rate-plans to return. | [optional] [default to 10]

### Return type

[**CouponModifierBasePagedMetadata**](CouponModifierBasePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupon_modifier_by_coupon_definition_id**
> CouponModifierBasePagedMetadata get_coupon_modifier_by_coupon_definition_id(coupon_definition_id, organizations=organizations)

Returns a collection of coupon-modifiers, specified by the coupon-definition-ID parameter.

{\"nickname\":\"Retrieve by coupon definition\",\"response\":\"getCouponModifierByCouponDefinitionID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.CouponmodifierApi()
coupon_definition_id = 'coupon_definition_id_example' # str | ID of the coupon-definition.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a collection of coupon-modifiers, specified by the coupon-definition-ID parameter.
    api_response = api_instance.get_coupon_modifier_by_coupon_definition_id(coupon_definition_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponmodifierApi->get_coupon_modifier_by_coupon_definition_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_definition_id** | **str**| ID of the coupon-definition. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**CouponModifierBasePagedMetadata**](CouponModifierBasePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupon_modifier_by_id**
> CouponModifierBasePagedMetadata get_coupon_modifier_by_id(coupon_modifier_id, organizations=organizations)

Returns a single coupon-modifier, specified by the coupon-modifier-ID parameter.

{\"nickname\":\"Get existing modifier\",\"response\":\"getCouponModifierByID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.CouponmodifierApi()
coupon_modifier_id = 'coupon_modifier_id_example' # str | ID of the coupon-modifier.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single coupon-modifier, specified by the coupon-modifier-ID parameter.
    api_response = api_instance.get_coupon_modifier_by_id(coupon_modifier_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponmodifierApi->get_coupon_modifier_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_modifier_id** | **str**| ID of the coupon-modifier. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**CouponModifierBasePagedMetadata**](CouponModifierBasePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_coupon_modifier**
> CouponModifierBasePagedMetadata update_coupon_modifier(coupon_instance)

Update a coupon-instance.

{\"nickname\":\"Update a modifier\",\"request\":\"updateCouponInstanceRequest.html\",\"response\":\"updateCouponInstanceResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.CouponmodifierApi()
coupon_instance = billforward.CouponModifierBase() # CouponModifierBase | The coupon-instance object to be updated.

try: 
    # Update a coupon-instance.
    api_response = api_instance.update_coupon_modifier(coupon_instance)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponmodifierApi->update_coupon_modifier: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_instance** | [**CouponModifierBase**](CouponModifierBase.md)| The coupon-instance object to be updated. | 

### Return type

[**CouponModifierBasePagedMetadata**](CouponModifierBasePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

