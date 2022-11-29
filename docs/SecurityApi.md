# billforward.SecurityApi

All URIs are relative to *https://app.billforward.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_flexcheck_user_login**](SecurityApi.md#create_flexcheck_user_login) | **POST** /users/flexcheck | 
[**create_role**](SecurityApi.md#create_role) | **POST** /roles | 
[**create_user_login**](SecurityApi.md#create_user_login) | **POST** /users | 
[**get_all_roles**](SecurityApi.md#get_all_roles) | **GET** /roles | 
[**get_current_user**](SecurityApi.md#get_current_user) | **GET** /users/mine | 
[**get_my_organizations**](SecurityApi.md#get_my_organizations) | **GET** /users/mine/organizations | 
[**get_private_permanent_api_token**](SecurityApi.md#get_private_permanent_api_token) | **POST** /users/generate-permanent-api-token | 
[**get_role_by_id**](SecurityApi.md#get_role_by_id) | **GET** /roles/{role} | 
[**get_simple_all_users**](SecurityApi.md#get_simple_all_users) | **GET** /users | 
[**get_temporary_api_tokens**](SecurityApi.md#get_temporary_api_tokens) | **GET** /users/generate-tokens | 
[**get_user_by_username**](SecurityApi.md#get_user_by_username) | **GET** /users/username/{email} | 
[**invite_user_login**](SecurityApi.md#invite_user_login) | **POST** /users/invite | 
[**link_open_id_token_to_user**](SecurityApi.md#link_open_id_token_to_user) | **POST** /users/invite/openid | 
[**refresh_permanent_api_token**](SecurityApi.md#refresh_permanent_api_token) | **POST** /users/refresh-permanent-api-token | 
[**remove_permission_from_role**](SecurityApi.md#remove_permission_from_role) | **DELETE** /roles/{role}/permission/{resource}/{action} | 
[**request_password_reset_code**](SecurityApi.md#request_password_reset_code) | **POST** /users/password-reset/request-reset-code | 
[**revoke_role**](SecurityApi.md#revoke_role) | **DELETE** /roles/{role} | 
[**update_email**](SecurityApi.md#update_email) | **PUT** /users/{email}/email | 
[**update_role**](SecurityApi.md#update_role) | **PUT** /roles | 
[**update_user_infos**](SecurityApi.md#update_user_infos) | **PUT** /users/{email} | 
[**update_user_password**](SecurityApi.md#update_user_password) | **PUT** /users/{email}/password | 
[**update_user_password_with_reset_code**](SecurityApi.md#update_user_password_with_reset_code) | **POST** /users/password-reset/password-update | 

# **create_flexcheck_user_login**
> InlineResponseDefault83 create_flexcheck_user_login(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SecurityApi(billforward.ApiClient(configuration))
body = billforward.UserCreateRequest() # UserCreateRequest |  (optional)

try:
    api_response = api_instance.create_flexcheck_user_login(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->create_flexcheck_user_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserCreateRequest**](UserCreateRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault83**](InlineResponseDefault83.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_role**
> InlineResponseDefault57 create_role(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SecurityApi(billforward.ApiClient(configuration))
body = billforward.CreateRoleRequest() # CreateRoleRequest |  (optional)

try:
    api_response = api_instance.create_role(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->create_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRoleRequest**](CreateRoleRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault57**](InlineResponseDefault57.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_login**
> InlineResponseDefault83 create_user_login(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SecurityApi(billforward.ApiClient(configuration))
body = billforward.UserCreateRequest() # UserCreateRequest |  (optional)

try:
    api_response = api_instance.create_user_login(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->create_user_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserCreateRequest**](UserCreateRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault83**](InlineResponseDefault83.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_roles**
> InlineResponseDefault56 get_all_roles(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SecurityApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_all_roles(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_all_roles: %s\n" % e)
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

[**InlineResponseDefault56**](InlineResponseDefault56.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user**
> InlineResponseDefault85 get_current_user(organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SecurityApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_current_user(organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_current_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault85**](InlineResponseDefault85.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_organizations**
> InlineResponseDefault86 get_my_organizations()



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SecurityApi(billforward.ApiClient(configuration))

try:
    api_response = api_instance.get_my_organizations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_my_organizations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponseDefault86**](InlineResponseDefault86.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_private_permanent_api_token**
> OAuthToken get_private_permanent_api_token(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SecurityApi(billforward.ApiClient(configuration))
body = billforward.UserPrivatePermanentTokenRequest() # UserPrivatePermanentTokenRequest |  (optional)

try:
    api_response = api_instance.get_private_permanent_api_token(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_private_permanent_api_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserPrivatePermanentTokenRequest**](UserPrivatePermanentTokenRequest.md)|  | [optional] 

### Return type

[**OAuthToken**](OAuthToken.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_by_id**
> InlineResponseDefault57 get_role_by_id(role, organizations=organizations, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SecurityApi(billforward.ApiClient(configuration))
role = 'role_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
include_retired = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_role_by_id(role, organizations=organizations, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_role_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **include_retired** | **bool**|  | [optional] [default to false]

### Return type

[**InlineResponseDefault57**](InlineResponseDefault57.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_simple_all_users**
> InlineResponseDefault84 get_simple_all_users(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SecurityApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)

try:
    api_response = api_instance.get_simple_all_users(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_simple_all_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]

### Return type

[**InlineResponseDefault84**](InlineResponseDefault84.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_temporary_api_tokens**
> TokensResponse get_temporary_api_tokens()



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SecurityApi(billforward.ApiClient(configuration))

try:
    api_response = api_instance.get_temporary_api_tokens()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_temporary_api_tokens: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TokensResponse**](TokensResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_username**
> InlineResponseDefault87 get_user_by_username(email, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SecurityApi(billforward.ApiClient(configuration))
email = 'email_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_user_by_username(email, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_user_by_username: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault87**](InlineResponseDefault87.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_user_login**
> InlineResponseDefault83 invite_user_login(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SecurityApi(billforward.ApiClient(configuration))
body = billforward.UserInviteRequest() # UserInviteRequest |  (optional)

try:
    api_response = api_instance.invite_user_login(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->invite_user_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserInviteRequest**](UserInviteRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault83**](InlineResponseDefault83.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_open_id_token_to_user**
> InlineResponseDefault88 link_open_id_token_to_user(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SecurityApi(billforward.ApiClient(configuration))
body = billforward.OpenIdUserLinkRequest() # OpenIdUserLinkRequest |  (optional)

try:
    api_response = api_instance.link_open_id_token_to_user(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->link_open_id_token_to_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OpenIdUserLinkRequest**](OpenIdUserLinkRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault88**](InlineResponseDefault88.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_permanent_api_token**
> OAuthToken refresh_permanent_api_token(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SecurityApi(billforward.ApiClient(configuration))
body = billforward.UserPrivatePermanentTokenRefreshRequest() # UserPrivatePermanentTokenRefreshRequest |  (optional)

try:
    api_response = api_instance.refresh_permanent_api_token(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->refresh_permanent_api_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserPrivatePermanentTokenRefreshRequest**](UserPrivatePermanentTokenRefreshRequest.md)|  | [optional] 

### Return type

[**OAuthToken**](OAuthToken.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_permission_from_role**
> InlineResponseDefault57 remove_permission_from_role(role, resource, action, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SecurityApi(billforward.ApiClient(configuration))
role = 'role_example' # str | 
resource = 'resource_example' # str | 
action = 'action_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.remove_permission_from_role(role, resource, action, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->remove_permission_from_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**|  | 
 **resource** | **str**|  | 
 **action** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault57**](InlineResponseDefault57.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_password_reset_code**
> InlineResponseDefault89 request_password_reset_code(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SecurityApi(billforward.ApiClient(configuration))
body = billforward.PasswordResetCodeRequest() # PasswordResetCodeRequest |  (optional)

try:
    api_response = api_instance.request_password_reset_code(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->request_password_reset_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PasswordResetCodeRequest**](PasswordResetCodeRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault89**](InlineResponseDefault89.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_role**
> InlineResponseDefault57 revoke_role(role, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SecurityApi(billforward.ApiClient(configuration))
role = 'role_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.revoke_role(role, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->revoke_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault57**](InlineResponseDefault57.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email**
> InlineResponseDefault85 update_email(email, body=body, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SecurityApi(billforward.ApiClient(configuration))
email = 'email_example' # str | 
body = billforward.UpdateEmailRequest() # UpdateEmailRequest |  (optional)
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.update_email(email, body=body, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->update_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **body** | [**UpdateEmailRequest**](UpdateEmailRequest.md)|  | [optional] 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault85**](InlineResponseDefault85.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role**
> InlineResponseDefault57 update_role(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SecurityApi(billforward.ApiClient(configuration))
body = billforward.UpdateRoleRequest() # UpdateRoleRequest |  (optional)

try:
    api_response = api_instance.update_role(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->update_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateRoleRequest**](UpdateRoleRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault57**](InlineResponseDefault57.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_infos**
> InlineResponseDefault90 update_user_infos(email, body=body, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SecurityApi(billforward.ApiClient(configuration))
email = 'email_example' # str | 
body = billforward.UpdateUserInfoRequest() # UpdateUserInfoRequest |  (optional)
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.update_user_infos(email, body=body, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->update_user_infos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **body** | [**UpdateUserInfoRequest**](UpdateUserInfoRequest.md)|  | [optional] 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault90**](InlineResponseDefault90.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_password**
> InlineResponseDefault91 update_user_password(email, body=body, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SecurityApi(billforward.ApiClient(configuration))
email = 'email_example' # str | 
body = billforward.UpdatePasswordRequest() # UpdatePasswordRequest |  (optional)
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.update_user_password(email, body=body, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->update_user_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **body** | [**UpdatePasswordRequest**](UpdatePasswordRequest.md)|  | [optional] 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault91**](InlineResponseDefault91.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_password_with_reset_code**
> InlineResponseDefault91 update_user_password_with_reset_code(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.SecurityApi(billforward.ApiClient(configuration))
body = billforward.PasswordUpdateWithResetCodeRequest() # PasswordUpdateWithResetCodeRequest |  (optional)

try:
    api_response = api_instance.update_user_password_with_reset_code(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->update_user_password_with_reset_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PasswordUpdateWithResetCodeRequest**](PasswordUpdateWithResetCodeRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault91**](InlineResponseDefault91.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

