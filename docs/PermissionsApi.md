# billforward.PermissionsApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_permission**](PermissionsApi.md#create_permission) | **POST** /permissions | Create a new permission.
[**get_all_permissions**](PermissionsApi.md#get_all_permissions) | **GET** /permissions | Retrieves a collection of all permissions. By default 10 values are returned. Records are returned in natural order.
[**get_available_actions_for_resource**](PermissionsApi.md#get_available_actions_for_resource) | **GET** /permissions/resources/{resource} | Retrieves all the available actions for the specified resource.
[**get_available_resources**](PermissionsApi.md#get_available_resources) | **GET** /permissions/resources | Retrieves all available resource.
[**get_permission_by_id**](PermissionsApi.md#get_permission_by_id) | **GET** /permissions/{permission-ID} | Retrieves a single permission, specified by the ID parameter.
[**revoke_permission**](PermissionsApi.md#revoke_permission) | **DELETE** /permissions/{permission-ID} | Revokes a permission


# **create_permission**
> BFPermissionPagedMetadata create_permission(permission_request)

Create a new permission.

{\"nickname\":\"Create a new permission\",\"request\":\"createPermissionRequest.html\",\"response\":\"createPermissionResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.PermissionsApi()
permission_request = billforward.BillingEntityBase() # BillingEntityBase | 

try: 
    # Create a new permission.
    api_response = api_instance.create_permission(permission_request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PermissionsApi->create_permission: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission_request** | [**BillingEntityBase**](BillingEntityBase.md)|  | 

### Return type

[**BFPermissionPagedMetadata**](BFPermissionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_permissions**
> BFPermissionPagedMetadata get_all_permissions(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Retrieves a collection of all permissions. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve all permissions\",\"response\":\"getPermissionAll.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.PermissionsApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first subscription to return. (optional) (default to 0)
records = 10 # int | The maximum number of subscriptions to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired subscriptions should be returned. (optional) (default to false)

try: 
    # Retrieves a collection of all permissions. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_permissions(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PermissionsApi->get_all_permissions: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first subscription to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of subscriptions to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired subscriptions should be returned. | [optional] [default to false]

### Return type

[**BFPermissionPagedMetadata**](BFPermissionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_actions_for_resource**
> PermissionActionEntityPagedMetadata get_available_actions_for_resource(resource, organizations=organizations)

Retrieves all the available actions for the specified resource.

{\"nickname\":\"Retrieve available actions\",\"response\":\"getAvailableActions.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.PermissionsApi()
resource = 'resource_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Retrieves all the available actions for the specified resource.
    api_response = api_instance.get_available_actions_for_resource(resource, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PermissionsApi->get_available_actions_for_resource: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**PermissionActionEntityPagedMetadata**](PermissionActionEntityPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_resources**
> PermissionResourceEntityPagedMetadata get_available_resources(organizations=organizations)

Retrieves all available resource.

{\"nickname\":\"Retrieve available resources\",\"response\":\"getAvailableResources.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.PermissionsApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Retrieves all available resource.
    api_response = api_instance.get_available_resources(organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PermissionsApi->get_available_resources: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**PermissionResourceEntityPagedMetadata**](PermissionResourceEntityPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_permission_by_id**
> BFPermissionPagedMetadata get_permission_by_id(permission_id, organizations=organizations, include_retired=include_retired)

Retrieves a single permission, specified by the ID parameter.

{\"nickname\":\"Retrieve a permission\",\"response\":\"getPermissionByID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.PermissionsApi()
permission_id = 'permission_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
include_retired = false # bool | Whether retired subscriptions should be returned. (optional) (default to false)

try: 
    # Retrieves a single permission, specified by the ID parameter.
    api_response = api_instance.get_permission_by_id(permission_id, organizations=organizations, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PermissionsApi->get_permission_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **include_retired** | **bool**| Whether retired subscriptions should be returned. | [optional] [default to false]

### Return type

[**BFPermissionPagedMetadata**](BFPermissionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_permission**
> BFPermissionPagedMetadata revoke_permission(permission_id, organizations=organizations)

Revokes a permission

{\"nickname\":\"Revoke permission\",\"response\":\"revokePermission.html\",\"request\":\"revokePErmissionRequest.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.PermissionsApi()
permission_id = 'permission_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Revokes a permission
    api_response = api_instance.revoke_permission(permission_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PermissionsApi->revoke_permission: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**BFPermissionPagedMetadata**](BFPermissionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

