# swagger_client.RolesApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_role**](RolesApi.md#create_role) | **POST** /roles | Create a new role.
[**get_all_roles**](RolesApi.md#get_all_roles) | **GET** /roles | Retrieves a collection of all roles. By default 10 values are returned. Records are returned in natural order.
[**get_role_by_id**](RolesApi.md#get_role_by_id) | **GET** /roles/{role} | Retrieves a single role, specified by the ID parameter.
[**remove_permission_from_role**](RolesApi.md#remove_permission_from_role) | **DELETE** /roles/{role}/permission/{resource}/{action} | Revokes a particular permission
[**revoke_role**](RolesApi.md#revoke_role) | **DELETE** /roles/{role} | Revokes a role
[**update_role**](RolesApi.md#update_role) | **PUT** /roles | Update a role.


# **create_role**
> RolePagedMetadata create_role(role_request)

Create a new role.

{\"nickname\":\"Create a new role\",\"request\":\"createRoleRequest.html\",\"response\":\"createRoleResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
role_request = swagger_client.BillingEntityBase() # BillingEntityBase | 

try: 
    # Create a new role.
    api_response = api_instance.create_role(role_request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RolesApi->create_role: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_request** | [**BillingEntityBase**](BillingEntityBase.md)|  | 

### Return type

[**RolePagedMetadata**](RolePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_roles**
> RolePagedMetadata get_all_roles(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Retrieves a collection of all roles. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve all roles\",\"response\":\"getRoleAll.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int | The offset from the first subscription to return. (optional) (default to 0)
records = 10 # int | The maximum number of subscriptions to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired subscriptions should be returned. (optional) (default to false)

try: 
    # Retrieves a collection of all roles. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_roles(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RolesApi->get_all_roles: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**| The offset from the first subscription to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of subscriptions to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired subscriptions should be returned. | [optional] [default to false]

### Return type

[**RolePagedMetadata**](RolePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_by_id**
> RolePagedMetadata get_role_by_id(role, organizations=organizations, include_retired=include_retired)

Retrieves a single role, specified by the ID parameter.

{\"nickname\":\"Retrieve a role\",\"response\":\"getRoleByID.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
role = 'role_example' # str | ID or name of the role.
organizations = ['organizations_example'] # list[str] |  (optional)
include_retired = false # bool | Whether retired subscriptions should be returned. (optional) (default to false)

try: 
    # Retrieves a single role, specified by the ID parameter.
    api_response = api_instance.get_role_by_id(role, organizations=organizations, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RolesApi->get_role_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| ID or name of the role. | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **include_retired** | **bool**| Whether retired subscriptions should be returned. | [optional] [default to false]

### Return type

[**RolePagedMetadata**](RolePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_permission_from_role**
> RolePagedMetadata remove_permission_from_role(role, resource, action, organizations=organizations)

Revokes a particular permission

{\"nickname\":\"Remove Permission from role\",\"response\":\"removePermissionFromGroup.html\",\"request\":\"removePermissionFromGroupRequest.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
role = 'role_example' # str | ID or name of the role.
resource = 'resource_example' # str | 
action = 'action_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try: 
    # Revokes a particular permission
    api_response = api_instance.remove_permission_from_role(role, resource, action, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RolesApi->remove_permission_from_role: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| ID or name of the role. | 
 **resource** | **str**|  | 
 **action** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**RolePagedMetadata**](RolePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_role**
> RolePagedMetadata revoke_role(role, organizations=organizations)

Revokes a role

{\"nickname\":\"Revoke role\",\"response\":\"revokeRole.html\",\"request\":\"revokeRoleRequest.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
role = 'role_example' # str | ID or name of the role.
organizations = ['organizations_example'] # list[str] |  (optional)

try: 
    # Revokes a role
    api_response = api_instance.revoke_role(role, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RolesApi->revoke_role: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| ID or name of the role. | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**RolePagedMetadata**](RolePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role**
> RolePagedMetadata update_role(role_request)

Update a role.

{\"nickname\":\"Update a role\",\"request\":\"updateRoleRequest.html\",\"response\":\"updateRoleResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
role_request = swagger_client.UpdateRoleRequest() # UpdateRoleRequest | 

try: 
    # Update a role.
    api_response = api_instance.update_role(role_request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RolesApi->update_role: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_request** | [**UpdateRoleRequest**](UpdateRoleRequest.md)|  | 

### Return type

[**RolePagedMetadata**](RolePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

