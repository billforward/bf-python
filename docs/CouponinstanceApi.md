# billforward.CouponinstanceApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_coupon_instance**](CouponinstanceApi.md#create_coupon_instance) | **POST** /coupon-instances | Create a coupon-instance.
[**delete_coupon_instance**](CouponinstanceApi.md#delete_coupon_instance) | **DELETE** /coupon-instances/{coupon-instance-ID} | Retire a coupon-instance, specified by the coupon-instance-ID parameter.
[**get_all_attachable_coupon_instances**](CouponinstanceApi.md#get_all_attachable_coupon_instances) | **GET** /coupon-instances/attachable/{attachableness}/{has_code} | Returns a collection of attachable coupon-instances. An attachable coupon-instance has at least one remaining use, and is not deleted. By default 10 values are returned. Records are returned in natural order.
[**get_all_coupon_instances**](CouponinstanceApi.md#get_all_coupon_instances) | **GET** /coupon-instances | Returns a collection of coupon-instances. By default 10 values are returned. Records are returned in natural order.
[**get_coupon_instance_by_coupon_code**](CouponinstanceApi.md#get_coupon_instance_by_coupon_code) | **GET** /coupon-instances/coupon/{coupon-code} | Returns a collection of coupon-instances, specified by coupon-code parameter. By default 10 coupon-instances are returned. Records are returned in natural order.
[**get_coupon_instance_by_coupon_definition_id**](CouponinstanceApi.md#get_coupon_instance_by_coupon_definition_id) | **GET** /coupon-instances/coupon-definition/{coupon-definition-ID} | Returns a collection of coupon-instances, specified by coupon-definition-ID parameter. By default 10 coupon-instances are returned. Records are returned in natural order.
[**get_coupon_instance_by_id**](CouponinstanceApi.md#get_coupon_instance_by_id) | **GET** /coupon-instances/{coupon-instance-ID} | Returns a single coupon-instance, specified by the coupon-instance-ID parameter.
[**get_coupon_instance_by_target_id**](CouponinstanceApi.md#get_coupon_instance_by_target_id) | **GET** /coupon-instances/target/{target-ID} | Returns a collection of coupon-instances, specified by target-ID parameter. By default 10 coupon-instances are returned. Records are returned in natural order.
[**get_coupon_instance_by_target_type**](CouponinstanceApi.md#get_coupon_instance_by_target_type) | **GET** /coupon-instances/target-entity/{target} | Returns a collection of coupon-instances, specified by target parameter. By default 10 coupon-instances are returned. Records are returned in natural order.
[**update_coupon_instance**](CouponinstanceApi.md#update_coupon_instance) | **PUT** /coupon-instances | Update a coupon-instance.


# **create_coupon_instance**
> CouponInstancePagedMetadata create_coupon_instance(coupon_instance)

Create a coupon-instance.

{\"nickname\":\"Create a new coupon\",\"request\":\"createCouponInstanceRequest.html\",\"response\":\"createCouponInstanceResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.CouponinstanceApi()
coupon_instance = billforward.CouponInstance() # CouponInstance | The coupon-instance object to be created.

try: 
    # Create a coupon-instance.
    api_response = api_instance.create_coupon_instance(coupon_instance)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponinstanceApi->create_coupon_instance: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_instance** | [**CouponInstance**](CouponInstance.md)| The coupon-instance object to be created. | 

### Return type

[**CouponInstancePagedMetadata**](CouponInstancePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_coupon_instance**
> CouponInstancePagedMetadata delete_coupon_instance(coupon_instance_id, organizations=organizations)

Retire a coupon-instance, specified by the coupon-instance-ID parameter.

{\"nickname\":\"Delete a coupon\",\"response\":\"deleteCouponInstanceByID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.CouponinstanceApi()
coupon_instance_id = 'coupon_instance_id_example' # str | ID of the coupon-instance.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Retire a coupon-instance, specified by the coupon-instance-ID parameter.
    api_response = api_instance.delete_coupon_instance(coupon_instance_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponinstanceApi->delete_coupon_instance: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_instance_id** | **str**| ID of the coupon-instance. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**CouponInstancePagedMetadata**](CouponInstancePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_attachable_coupon_instances**
> CouponInstancePagedMetadata get_all_attachable_coupon_instances(attachableness, has_code, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Returns a collection of attachable coupon-instances. An attachable coupon-instance has at least one remaining use, and is not deleted. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get attachable coupons\",\"response\":\"getCouponInstanceAllAttachable.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.CouponinstanceApi()
attachableness = true # bool | The attachableness of the coupon-instance.
has_code = true # bool | Whether the coupon-instances have coupon codes or not.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first coupon-instance to return. (optional) (default to 0)
records = 10 # int | The maximum number of coupon-instances to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Returns a collection of attachable coupon-instances. An attachable coupon-instance has at least one remaining use, and is not deleted. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_attachable_coupon_instances(attachableness, has_code, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponinstanceApi->get_all_attachable_coupon_instances: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachableness** | **bool**| The attachableness of the coupon-instance. | 
 **has_code** | **bool**| Whether the coupon-instances have coupon codes or not. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first coupon-instance to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of coupon-instances to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**CouponInstancePagedMetadata**](CouponInstancePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_coupon_instances**
> CouponInstancePagedMetadata get_all_coupon_instances(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of coupon-instances. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get all coupons\",\"response\":\"getCouponInstanceAll.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.CouponinstanceApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first coupon-instance to return. (optional) (default to 0)
records = 10 # int | The maximum number of coupon-instances to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired coupon-instances should be returned. (optional) (default to true)

try: 
    # Returns a collection of coupon-instances. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_coupon_instances(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponinstanceApi->get_all_coupon_instances: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first coupon-instance to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of coupon-instances to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired coupon-instances should be returned. | [optional] [default to true]

### Return type

[**CouponInstancePagedMetadata**](CouponInstancePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupon_instance_by_coupon_code**
> CouponInstancePagedMetadata get_coupon_instance_by_coupon_code(coupon_code, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of coupon-instances, specified by coupon-code parameter. By default 10 coupon-instances are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by coupon code\",\"response\":\"getCouponInstanceByCouponCode.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.CouponinstanceApi()
coupon_code = 'coupon_code_example' # str | The string coupon-code of the coupon-instance.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first coupon-instance to return. (optional) (default to 0)
records = 10 # int | The maximum number of coupon-instances to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired coupon-instances should be returned. (optional) (default to true)

try: 
    # Returns a collection of coupon-instances, specified by coupon-code parameter. By default 10 coupon-instances are returned. Records are returned in natural order.
    api_response = api_instance.get_coupon_instance_by_coupon_code(coupon_code, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponinstanceApi->get_coupon_instance_by_coupon_code: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_code** | **str**| The string coupon-code of the coupon-instance. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first coupon-instance to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of coupon-instances to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired coupon-instances should be returned. | [optional] [default to true]

### Return type

[**CouponInstancePagedMetadata**](CouponInstancePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupon_instance_by_coupon_definition_id**
> CouponInstancePagedMetadata get_coupon_instance_by_coupon_definition_id(coupon_definition_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of coupon-instances, specified by coupon-definition-ID parameter. By default 10 coupon-instances are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by coupon definition\",\"response\":\"getCouponInstanceByCouponDefinitionID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.CouponinstanceApi()
coupon_definition_id = 'coupon_definition_id_example' # str | The string coupon-definition-ID of the coupon-instance.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first coupon-instance to return. (optional) (default to 0)
records = 10 # int | The maximum number of coupon-instances to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired coupon-instances should be returned. (optional) (default to true)

try: 
    # Returns a collection of coupon-instances, specified by coupon-definition-ID parameter. By default 10 coupon-instances are returned. Records are returned in natural order.
    api_response = api_instance.get_coupon_instance_by_coupon_definition_id(coupon_definition_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponinstanceApi->get_coupon_instance_by_coupon_definition_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_definition_id** | **str**| The string coupon-definition-ID of the coupon-instance. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first coupon-instance to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of coupon-instances to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired coupon-instances should be returned. | [optional] [default to true]

### Return type

[**CouponInstancePagedMetadata**](CouponInstancePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupon_instance_by_id**
> CouponInstancePagedMetadata get_coupon_instance_by_id(coupon_instance_id, organizations=organizations)

Returns a single coupon-instance, specified by the coupon-instance-ID parameter.

{\"nickname\":\"Get existing coupon\",\"response\":\"getCouponInstanceByID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.CouponinstanceApi()
coupon_instance_id = 'coupon_instance_id_example' # str | ID of the coupon-instance.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single coupon-instance, specified by the coupon-instance-ID parameter.
    api_response = api_instance.get_coupon_instance_by_id(coupon_instance_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponinstanceApi->get_coupon_instance_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_instance_id** | **str**| ID of the coupon-instance. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**CouponInstancePagedMetadata**](CouponInstancePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupon_instance_by_target_id**
> CouponInstancePagedMetadata get_coupon_instance_by_target_id(target_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of coupon-instances, specified by target-ID parameter. By default 10 coupon-instances are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by target\",\"response\":\"getCouponInstanceByTargetID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.CouponinstanceApi()
target_id = 'target_id_example' # str | The string target-ID of the coupon-instance.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first coupon-instance to return. (optional) (default to 0)
records = 10 # int | The maximum number of coupon-instances to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired coupon-instances should be returned. (optional) (default to true)

try: 
    # Returns a collection of coupon-instances, specified by target-ID parameter. By default 10 coupon-instances are returned. Records are returned in natural order.
    api_response = api_instance.get_coupon_instance_by_target_id(target_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponinstanceApi->get_coupon_instance_by_target_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **str**| The string target-ID of the coupon-instance. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first coupon-instance to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of coupon-instances to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired coupon-instances should be returned. | [optional] [default to true]

### Return type

[**CouponInstancePagedMetadata**](CouponInstancePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupon_instance_by_target_type**
> CouponInstancePagedMetadata get_coupon_instance_by_target_type(target, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of coupon-instances, specified by target parameter. By default 10 coupon-instances are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by target type\",\"response\":\"getCouponInstanceByTarget.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.CouponinstanceApi()
target = 'target_example' # str | The string target of the coupon-instance.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first coupon-instance to return. (optional) (default to 0)
records = 10 # int | The maximum number of coupon-instances to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired coupon-instances should be returned. (optional) (default to true)

try: 
    # Returns a collection of coupon-instances, specified by target parameter. By default 10 coupon-instances are returned. Records are returned in natural order.
    api_response = api_instance.get_coupon_instance_by_target_type(target, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponinstanceApi->get_coupon_instance_by_target_type: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target** | **str**| The string target of the coupon-instance. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first coupon-instance to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of coupon-instances to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired coupon-instances should be returned. | [optional] [default to true]

### Return type

[**CouponInstancePagedMetadata**](CouponInstancePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_coupon_instance**
> CouponInstancePagedMetadata update_coupon_instance(coupon_instance)

Update a coupon-instance.

{\"nickname\":\"Update a coupon\",\"request\":\"updateCouponInstanceRequest.html\",\"response\":\"updateCouponInstanceResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.CouponinstanceApi()
coupon_instance = billforward.CouponInstance() # CouponInstance | The coupon-instance object to be updated.

try: 
    # Update a coupon-instance.
    api_response = api_instance.update_coupon_instance(coupon_instance)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponinstanceApi->update_coupon_instance: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_instance** | [**CouponInstance**](CouponInstance.md)| The coupon-instance object to be updated. | 

### Return type

[**CouponInstancePagedMetadata**](CouponInstancePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

