# billforward.PermissionsApi

All URIs are relative to *https://app.billforward.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_permission**](PermissionsApi.md#create_permission) | **POST** /permissions | 
[**get_all_permissions**](PermissionsApi.md#get_all_permissions) | **GET** /permissions | 
[**get_available_actions_for_resource**](PermissionsApi.md#get_available_actions_for_resource) | **GET** /permissions/resources/{resource} | 
[**get_available_resources**](PermissionsApi.md#get_available_resources) | **GET** /permissions/resources | 
[**get_permission_by_id**](PermissionsApi.md#get_permission_by_id) | **GET** /permissions/{permission-ID} | 
[**revoke_permission**](PermissionsApi.md#revoke_permission) | **DELETE** /permissions/{permission-ID} | 

# **create_permission**
> InlineResponseDefault45 create_permission(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.PermissionsApi(billforward.ApiClient(configuration))
body = billforward.CreatePermissionRequest() # CreatePermissionRequest |  (optional)

try:
    api_response = api_instance.create_permission(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->create_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreatePermissionRequest**](CreatePermissionRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault45**](InlineResponseDefault45.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_permissions**
> InlineResponseDefault44 get_all_permissions(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.PermissionsApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_all_permissions(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->get_all_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to false]

### Return type

[**InlineResponseDefault44**](InlineResponseDefault44.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_actions_for_resource**
> InlineResponseDefault46 get_available_actions_for_resource(resource, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.PermissionsApi(billforward.ApiClient(configuration))
resource = 'resource_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_available_actions_for_resource(resource, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->get_available_actions_for_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault46**](InlineResponseDefault46.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_resources**
> InlineResponseDefault47 get_available_resources(organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.PermissionsApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_available_resources(organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->get_available_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault47**](InlineResponseDefault47.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_permission_by_id**
> InlineResponseDefault45 get_permission_by_id(permission_id, organizations=organizations, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.PermissionsApi(billforward.ApiClient(configuration))
permission_id = 'permission_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
include_retired = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_permission_by_id(permission_id, organizations=organizations, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->get_permission_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **include_retired** | **bool**|  | [optional] [default to false]

### Return type

[**InlineResponseDefault45**](InlineResponseDefault45.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_permission**
> InlineResponseDefault45 revoke_permission(permission_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.PermissionsApi(billforward.ApiClient(configuration))
permission_id = 'permission_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.revoke_permission(permission_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->revoke_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault45**](InlineResponseDefault45.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

