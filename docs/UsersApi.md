# billforward.UsersApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UsersApi.md#create_user) | **POST** /users | Create a user.
[**create_user_login**](UsersApi.md#create_user_login) | **POST** /users/create-user-login | Create a user.
[**get_all_users**](UsersApi.md#get_all_users) | **GET** /users | Returns a collection of Users. By default 10 values are returned. Records are returned in natural order.
[**get_user_by_id**](UsersApi.md#get_user_by_id) | **GET** /users/{user-ID} | Returns a single User, specified by the ID parameter.
[**get_user_by_password_reset_code**](UsersApi.md#get_user_by_password_reset_code) | **GET** /users/password-reset-code/{password-reset-code} | Returns a single User, specified by the password-reset-code parameter.
[**get_user_by_sms_password_reset_code**](UsersApi.md#get_user_by_sms_password_reset_code) | **GET** /users/sms-password-reset-code/{sms-password-reset-code} | Returns a single User, specified by the sms-password-reset-code parameter.
[**get_user_by_username**](UsersApi.md#get_user_by_username) | **GET** /users/username/{username} | Returns a single User, specified by the username parameter, this is by default the e-mail address of the user.
[**reset_user_password**](UsersApi.md#reset_user_password) | **POST** /users/password-reset | Create a password reset request.
[**retire_user**](UsersApi.md#retire_user) | **DELETE** /users/{user-ID} | Retires the user with the specified user-ID.
[**update_user**](UsersApi.md#update_user) | **PUT** /users | Update a user.
[**update_user_password**](UsersApi.md#update_user_password) | **POST** /users/password-update | Update a user&#39;s password.


# **create_user**
> UserPagedMetadata create_user(user)

Create a user.

{\"nickname\":\"Create a new user\",\"request\":\"createUserRequest.html\",\"response\":\"createUserResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.UsersApi()
user = billforward.User() # User | The user object to be created.

try: 
    # Create a user.
    api_response = api_instance.create_user(user)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->create_user: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**User**](User.md)| The user object to be created. | 

### Return type

[**UserPagedMetadata**](UserPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_login**
> UserCreationResponsePagedMetadata create_user_login(user)

Create a user.

{\"nickname\":\"Create a new user with login\",\"request\":\"createUserWithLoginRequest.html\",\"response\":\"createUserWithLoginResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.UsersApi()
user = billforward.UserCreationRequest() # UserCreationRequest | The user object to be created.

try: 
    # Create a user.
    api_response = api_instance.create_user_login(user)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->create_user_login: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**UserCreationRequest**](UserCreationRequest.md)| The user object to be created. | 

### Return type

[**UserCreationResponsePagedMetadata**](UserCreationResponsePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_users**
> UserPagedMetadata get_all_users(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Returns a collection of Users. By default 10 values are returned. Records are returned in natural order.

{ \"nickname\" : \"Get all users\",\"response\" : \"getUserAll.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.UsersApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first user to return. (optional) (default to 0)
records = 10 # int | The maximum number of users to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Returns a collection of Users. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_users(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->get_all_users: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first user to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of users to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**UserPagedMetadata**](UserPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_id**
> UserPagedMetadata get_user_by_id(user_id, organizations=organizations)

Returns a single User, specified by the ID parameter.

{ \"nickname\" : \"Retrieve an existing user\",\"response\" : \"getUserByID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.UsersApi()
user_id = 'user_id_example' # str | ID of the User.
organizations = ['organizations_example'] # list[str] | A list of organization -IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single User, specified by the ID parameter.
    api_response = api_instance.get_user_by_id(user_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->get_user_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of the User. | 
 **organizations** | [**list[str]**](str.md)| A list of organization -IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**UserPagedMetadata**](UserPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_password_reset_code**
> UserPagedMetadata get_user_by_password_reset_code(password_reset_code, organizations=organizations)

Returns a single User, specified by the password-reset-code parameter.

{ \"nickname\" : \"Retrieve by reset code\",\"response\" : \"getUserByPasswordResetCode.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.UsersApi()
password_reset_code = 'password_reset_code_example' # str | The unique password reset code of the User.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single User, specified by the password-reset-code parameter.
    api_response = api_instance.get_user_by_password_reset_code(password_reset_code, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->get_user_by_password_reset_code: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_reset_code** | **str**| The unique password reset code of the User. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**UserPagedMetadata**](UserPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_sms_password_reset_code**
> UserPagedMetadata get_user_by_sms_password_reset_code(sms_password_reset_code, organizations=organizations)

Returns a single User, specified by the sms-password-reset-code parameter.

{ \"nickname\" : \"Retrieve by sms reset code\",\"response\" : \"getUserBySMSPasswordResetCode.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.UsersApi()
sms_password_reset_code = 'sms_password_reset_code_example' # str | The unique SMS password reset code of the User.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single User, specified by the sms-password-reset-code parameter.
    api_response = api_instance.get_user_by_sms_password_reset_code(sms_password_reset_code, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->get_user_by_sms_password_reset_code: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sms_password_reset_code** | **str**| The unique SMS password reset code of the User. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**UserPagedMetadata**](UserPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_username**
> UserPagedMetadata get_user_by_username(username, organizations=organizations)

Returns a single User, specified by the username parameter, this is by default the e-mail address of the user.

{ \"nickname\" : \"Retrieve by username\",\"response\" : \"getUserByUsername.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.UsersApi()
username = 'username_example' # str | The unique username of the User.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single User, specified by the username parameter, this is by default the e-mail address of the user.
    api_response = api_instance.get_user_by_username(username, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->get_user_by_username: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The unique username of the User. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**UserPagedMetadata**](UserPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_user_password**
> UserPagedMetadata reset_user_password(request)

Create a password reset request.

{\"nickname\":\"Create a password reset request\",\"request\":\"PasswordResetRequest.html\",\"response\":\"PasswordResetResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.UsersApi()
request = billforward.PasswordResetRequest() # PasswordResetRequest | 

try: 
    # Create a password reset request.
    api_response = api_instance.reset_user_password(request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->reset_user_password: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**PasswordResetRequest**](PasswordResetRequest.md)|  | 

### Return type

[**UserPagedMetadata**](UserPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retire_user**
> UserPagedMetadata retire_user(user_id, organizations)

Retires the user with the specified user-ID.

{ \"nickname\" : \"Delete a user\",\"response\" : \"deleteUser.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.UsersApi()
user_id = 'user_id_example' # str | ID of the User.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls.

try: 
    # Retires the user with the specified user-ID.
    api_response = api_instance.retire_user(user_id, organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->retire_user: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of the User. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | 

### Return type

[**UserPagedMetadata**](UserPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> UserPagedMetadata update_user(user)

Update a user.

{ \"nickname\" : \"Update a user\", \"request\" : \"updateUserRequest.html\" ,\"response\" : \"updateUserResponse.html\" }

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.UsersApi()
user = billforward.User() # User | The user object to be updated.

try: 
    # Update a user.
    api_response = api_instance.update_user(user)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->update_user: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**User**](User.md)| The user object to be updated. | 

### Return type

[**UserPagedMetadata**](UserPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_password**
> UserPagedMetadata update_user_password(password_reset)

Update a user's password.

{ \"nickname\" : \"Update password using reset code\", \"request\" : \"updateUserPassword.html\" ,\"response\" : \"updateUserPasswordResponse.html\" }

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.UsersApi()
password_reset = billforward.BillingEntityBase() # BillingEntityBase | The password reset object.

try: 
    # Update a user's password.
    api_response = api_instance.update_user_password(password_reset)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->update_user_password: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_reset** | [**BillingEntityBase**](BillingEntityBase.md)| The password reset object. | 

### Return type

[**UserPagedMetadata**](UserPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

