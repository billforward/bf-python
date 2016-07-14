# billforward.AccountsApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_credit_note_to_account**](AccountsApi.md#add_credit_note_to_account) | **POST** /accounts/{account-ID}/credit | Creates a credit-note which may be used by any subscription of this account.
[**add_permission_to_account**](AccountsApi.md#add_permission_to_account) | **POST** /accounts/{account-ID}/roles/{role} | Add a role to the account
[**create_account**](AccountsApi.md#create_account) | **POST** /accounts | Create an Account.
[**delete_account**](AccountsApi.md#delete_account) | **DELETE** /accounts/{account-ID} | Delete the account specified by the account-ID parameter.
[**delete_metadata_for_account**](AccountsApi.md#delete_metadata_for_account) | **DELETE** /accounts/{account-ID}/metadata | Remove any associated metadata.
[**get_account_by_id**](AccountsApi.md#get_account_by_id) | **GET** /accounts/{account-ID} | Returns a single account, specified by the account-ID parameter.
[**get_accounts_by_created**](AccountsApi.md#get_accounts_by_created) | **GET** /accounts/created/{lower-threshold}/{upper-threshold} | Returns a collection of account objects with created times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.
[**get_accounts_by_updated**](AccountsApi.md#get_accounts_by_updated) | **GET** /accounts/updated/{lower-threshold}/{upper-threshold} | Returns a collection of account objects with updated times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.
[**get_accounts_by_user_id**](AccountsApi.md#get_accounts_by_user_id) | **GET** /accounts/user/{user-ID} | Returns a collection of accounts, specified by the user-ID parameter. By default 10 values are returned. Records are returned in natural order.
[**get_all_accounts**](AccountsApi.md#get_all_accounts) | **GET** /accounts | Returns a collection of all account objects. By default 10 values are returned. Records are returned in natural order.
[**get_available_credit_on_account**](AccountsApi.md#get_available_credit_on_account) | **GET** /accounts/{account-ID}/credit | Returns all available credit-notes for the specified account. By default 10 values are returned. Records are returned in natural order.
[**get_metadata_for_account**](AccountsApi.md#get_metadata_for_account) | **GET** /accounts/{account-ID}/metadata | Retrieve any associated metadata.
[**get_permissions_on_account**](AccountsApi.md#get_permissions_on_account) | **GET** /accounts/{account-ID}/roles | Retrieves a collection of roles, specified by the account-ID parameter. By default 10 values are returned. Records are returned in natural order.
[**remove_credit_from_account**](AccountsApi.md#remove_credit_from_account) | **DELETE** /accounts/{account-ID}/credit/{value} | Decrease the amount of credit by the value specified or entirely if no value provided.
[**remove_permission_from_account**](AccountsApi.md#remove_permission_from_account) | **DELETE** /accounts/{account-ID}/roles/{role} | Revoke the specified role.
[**set_metadata_for_account**](AccountsApi.md#set_metadata_for_account) | **POST** /accounts/{account-ID}/metadata | Remove any existing metadata keys and create the provided data.
[**update_account**](AccountsApi.md#update_account) | **PUT** /accounts | Update an Account.
[**upsert_metadata_for_account**](AccountsApi.md#upsert_metadata_for_account) | **PUT** /accounts/{account-ID}/metadata | Update any existing metadata key-values and insert any new key-values, no keys will be removed.


# **add_credit_note_to_account**
> CreditNotePagedMetadata add_credit_note_to_account(account_id, credit_note)

Creates a credit-note which may be used by any subscription of this account.

{\"nickname\":\"Add Credit\",\"request\":\"addCreditNoteToAccountRequest.html\", \"response\":\"addCreditNoteToAccount.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.AccountsApi()
account_id = 'account_id_example' # str | ID of the account.
credit_note = billforward.CreditAccountRequest() # CreditAccountRequest | The credit-note request

try: 
    # Creates a credit-note which may be used by any subscription of this account.
    api_response = api_instance.add_credit_note_to_account(account_id, credit_note)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AccountsApi->add_credit_note_to_account: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account. | 
 **credit_note** | [**CreditAccountRequest**](CreditAccountRequest.md)| The credit-note request | 

### Return type

[**CreditNotePagedMetadata**](CreditNotePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_permission_to_account**
> RolePagedMetadata add_permission_to_account(account_id, role, organizations=organizations)

Add a role to the account

{\"nickname\":\"Add Role\",\"response\":\"addRoleToAccountResponse.html\",\"request\":\"addRoleToAccountRequest.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.AccountsApi()
account_id = 'account_id_example' # str | ID of the account.
role = 'role_example' # str | ID or name of the role.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Add a role to the account
    api_response = api_instance.add_permission_to_account(account_id, role, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AccountsApi->add_permission_to_account: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account. | 
 **role** | **str**| ID or name of the role. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**RolePagedMetadata**](RolePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_account**
> AccountPagedMetadata create_account(request)

Create an Account.

{\"nickname\":\"Create a new account\",\"response\":\"createAccountResponse.html\",\"request\":\"createAccountRequest.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.AccountsApi()
request = billforward.CreateAccountRequest() # CreateAccountRequest | The account object to be created.

try: 
    # Create an Account.
    api_response = api_instance.create_account(request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AccountsApi->create_account: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreateAccountRequest**](CreateAccountRequest.md)| The account object to be created. | 

### Return type

[**AccountPagedMetadata**](AccountPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account**
> AccountPagedMetadata delete_account(account_id, delete_gateway_data, organizations)

Delete the account specified by the account-ID parameter.

{\"nickname\":\"Retire\",\"response\":\"deleteAccount.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.AccountsApi()
account_id = 'account_id_example' # str | 
delete_gateway_data = 'delete_gateway_data_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls.

try: 
    # Delete the account specified by the account-ID parameter.
    api_response = api_instance.delete_account(account_id, delete_gateway_data, organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AccountsApi->delete_account: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **delete_gateway_data** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | 

### Return type

[**AccountPagedMetadata**](AccountPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_metadata_for_account**
> DynamicMetadata delete_metadata_for_account(account_id, organizations=organizations)

Remove any associated metadata.

{\"nickname\":\"Clear metadata from account\",\"request\" :\"deleteAccountMetadataRequest.html\",\"response\":\"deleteAccountMetadataResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.AccountsApi()
account_id = 'account_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Remove any associated metadata.
    api_response = api_instance.delete_metadata_for_account(account_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AccountsApi->delete_metadata_for_account: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**DynamicMetadata**](DynamicMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_by_id**
> AccountPagedMetadata get_account_by_id(account_id, organizations=organizations)

Returns a single account, specified by the account-ID parameter.

{\"nickname\":\"Retrieve an existing account\",\"response\":\"getAccountByID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.AccountsApi()
account_id = 'account_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try: 
    # Returns a single account, specified by the account-ID parameter.
    api_response = api_instance.get_account_by_id(account_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AccountsApi->get_account_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**AccountPagedMetadata**](AccountPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts_by_created**
> AccountPagedMetadata get_accounts_by_created(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of account objects with created times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by creation\",\"response\":\"getAccountByCreated.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.AccountsApi()
lower_threshold = 'lower_threshold_example' # str | The UTC DateTime specifying the start of the result period.
upper_threshold = 'upper_threshold_example' # str | The UTC DateTime specifying the end of the result period.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first taxation-link to return. (optional) (default to 0)
records = 10 # int | The maximum number of taxation-links to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)

try: 
    # Returns a collection of account objects with created times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_accounts_by_created(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AccountsApi->get_accounts_by_created: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lower_threshold** | **str**| The UTC DateTime specifying the start of the result period. | 
 **upper_threshold** | **str**| The UTC DateTime specifying the end of the result period. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first taxation-link to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of taxation-links to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]

### Return type

[**AccountPagedMetadata**](AccountPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts_by_updated**
> AccountPagedMetadata get_accounts_by_updated(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of account objects with updated times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by updated\",\"response\":\"getAccountByUpdated.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.AccountsApi()
lower_threshold = 'lower_threshold_example' # str | The UTC DateTime specifying the start of the result period.
upper_threshold = 'upper_threshold_example' # str | The UTC DateTime specifying the end of the result period.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first taxation-link to return. (optional) (default to 0)
records = 10 # int | The maximum number of taxation-links to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)

try: 
    # Returns a collection of account objects with updated times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_accounts_by_updated(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AccountsApi->get_accounts_by_updated: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lower_threshold** | **str**| The UTC DateTime specifying the start of the result period. | 
 **upper_threshold** | **str**| The UTC DateTime specifying the end of the result period. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first taxation-link to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of taxation-links to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]

### Return type

[**AccountPagedMetadata**](AccountPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts_by_user_id**
> AccountPagedMetadata get_accounts_by_user_id(user_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of accounts, specified by the user-ID parameter. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by user\",\"response\":\"getAccountByUserID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.AccountsApi()
user_id = 'user_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first account to return. (optional) (default to 0)
records = 10 # int | The maximum number of accounts to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)

try: 
    # Returns a collection of accounts, specified by the user-ID parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_accounts_by_user_id(user_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AccountsApi->get_accounts_by_user_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first account to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of accounts to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]

### Return type

[**AccountPagedMetadata**](AccountPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_accounts**
> AccountPagedMetadata get_all_accounts(id=id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, users_only=users_only, metadata=metadata)

Returns a collection of all account objects. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get all accounts\",\"response\":\"getAccountAll.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.AccountsApi()
id = ['id_example'] # list[str] | A list of account IDs used to filter the output. (optional)
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first taxation-link to return. (optional) (default to 0)
records = 10 # int | The maximum number of taxation-links to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)
users_only = false # bool | Whether only accounts have a user should be returned. (optional) (default to false)
metadata = 'metadata_example' # str |  (optional)

try: 
    # Returns a collection of all account objects. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_accounts(id=id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, users_only=users_only, metadata=metadata)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AccountsApi->get_all_accounts: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[str]**](str.md)| A list of account IDs used to filter the output. | [optional] 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first taxation-link to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of taxation-links to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]
 **users_only** | **bool**| Whether only accounts have a user should be returned. | [optional] [default to false]
 **metadata** | **str**|  | [optional] 

### Return type

[**AccountPagedMetadata**](AccountPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_credit_on_account**
> CreditNotePagedMetadata get_available_credit_on_account(account_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns all available credit-notes for the specified account. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get available credit\",\"response\":\"getAvailableCreditAccount.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.AccountsApi()
account_id = 'account_id_example' # str | The ID of the account
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first subscription to return. (optional) (default to 0)
records = 10 # int | The maximum number of subscriptions to return. (optional) (default to 10)
order_by = 'id' # str | Specify a field used to order the result set. (optional) (default to id)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired subscriptions should be returned. (optional) (default to false)

try: 
    # Returns all available credit-notes for the specified account. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_available_credit_on_account(account_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AccountsApi->get_available_credit_on_account: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The ID of the account | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first subscription to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of subscriptions to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to id]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired subscriptions should be returned. | [optional] [default to false]

### Return type

[**CreditNotePagedMetadata**](CreditNotePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_for_account**
> DynamicMetadata get_metadata_for_account(account_id, organizations=organizations)

Retrieve any associated metadata.

{\"nickname\":\"Retrieve metadata on account\",\"request\":\"getAccountMetadataRequest.html\",\"response\":\"getAccountMetadataResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.AccountsApi()
account_id = 'account_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Retrieve any associated metadata.
    api_response = api_instance.get_metadata_for_account(account_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AccountsApi->get_metadata_for_account: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**DynamicMetadata**](DynamicMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_permissions_on_account**
> RolePagedMetadata get_permissions_on_account(account_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Retrieves a collection of roles, specified by the account-ID parameter. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"List roles on account\",\"response\":\"getRoleByAccount.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.AccountsApi()
account_id = 'account_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first subscription to return. (optional) (default to 0)
records = 10 # int | The maximum number of subscriptions to return. (optional) (default to 10)
order_by = 'id' # str | Specify a field used to order the result set. (optional) (default to id)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired subscriptions should be returned. (optional) (default to false)

try: 
    # Retrieves a collection of roles, specified by the account-ID parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_permissions_on_account(account_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AccountsApi->get_permissions_on_account: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first subscription to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of subscriptions to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to id]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired subscriptions should be returned. | [optional] [default to false]

### Return type

[**RolePagedMetadata**](RolePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_credit_from_account**
> CreditNotePagedMetadata remove_credit_from_account(account_id, value, organizations=organizations)

Decrease the amount of credit by the value specified or entirely if no value provided.

{\"nickname\":\"Remove Credit\",\"response\":\"removeCreditForAccount.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.AccountsApi()
account_id = 'account_id_example' # str | 
value = 'value_example' # str | <p>Either a credit note ID or a currency value.</p><p>If a credit note ID is provided any remaining credit will be removed from this credit note.</p><p>If a currency value is provided the format should be in the form of valueCurrency, where value is the value to remove. The currency should be an ISO 4217 Currency Code. For example setting the value as 10USD will reduce the credit on this account by $10 or 9.86USD would reduce the credit by $9.86. Note: the value will be reduced from any credit notes with available balance.</p>
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Decrease the amount of credit by the value specified or entirely if no value provided.
    api_response = api_instance.remove_credit_from_account(account_id, value, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AccountsApi->remove_credit_from_account: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **value** | **str**| &lt;p&gt;Either a credit note ID or a currency value.&lt;/p&gt;&lt;p&gt;If a credit note ID is provided any remaining credit will be removed from this credit note.&lt;/p&gt;&lt;p&gt;If a currency value is provided the format should be in the form of valueCurrency, where value is the value to remove. The currency should be an ISO 4217 Currency Code. For example setting the value as 10USD will reduce the credit on this account by $10 or 9.86USD would reduce the credit by $9.86. Note: the value will be reduced from any credit notes with available balance.&lt;/p&gt; | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**CreditNotePagedMetadata**](CreditNotePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_permission_from_account**
> RolePagedMetadata remove_permission_from_account(account_id, role, organizations=organizations)

Revoke the specified role.

{\"nickname\":\"Remove Role\",\"response\":\"removeRoleFromAccount.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.AccountsApi()
account_id = 'account_id_example' # str | 
role = 'role_example' # str | ID or name of the role.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Revoke the specified role.
    api_response = api_instance.remove_permission_from_account(account_id, role, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AccountsApi->remove_permission_from_account: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **role** | **str**| ID or name of the role. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**RolePagedMetadata**](RolePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_metadata_for_account**
> DynamicMetadata set_metadata_for_account(metadata, account_id, organizations=organizations)

Remove any existing metadata keys and create the provided data.

{\"nickname\":\"Set metadata on account\",\"request\":\"setAccountMetadataRequest.html\",\"response\":\"setAccountMetadataResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.AccountsApi()
metadata = billforward.DynamicMetadata() # DynamicMetadata | 
account_id = 'account_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Remove any existing metadata keys and create the provided data.
    api_response = api_instance.set_metadata_for_account(metadata, account_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AccountsApi->set_metadata_for_account: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata** | [**DynamicMetadata**](DynamicMetadata.md)|  | 
 **account_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**DynamicMetadata**](DynamicMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account**
> AccountPagedMetadata update_account(account)

Update an Account.

{\"nickname\":\"Update an account\",\"response\":\"updateAccountResponse.html\",\"request\":\"updateAccountRequest.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.AccountsApi()
account = billforward.Account() # Account | The account object to be created.

try: 
    # Update an Account.
    api_response = api_instance.update_account(account)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AccountsApi->update_account: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | [**Account**](Account.md)| The account object to be created. | 

### Return type

[**AccountPagedMetadata**](AccountPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_metadata_for_account**
> DynamicMetadata upsert_metadata_for_account(metadata, account_id, organizations=organizations)

Update any existing metadata key-values and insert any new key-values, no keys will be removed.

{\"nickname\":\"Upsert metadata on account\",\"request\":\"upsertAccountMetadataRequest.html\",\"response\":\"upsertAccountMetadataResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.AccountsApi()
metadata = billforward.DynamicMetadata() # DynamicMetadata | 
account_id = 'account_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Update any existing metadata key-values and insert any new key-values, no keys will be removed.
    api_response = api_instance.upsert_metadata_for_account(metadata, account_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AccountsApi->upsert_metadata_for_account: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata** | [**DynamicMetadata**](DynamicMetadata.md)|  | 
 **account_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**DynamicMetadata**](DynamicMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

