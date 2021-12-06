# billforward.AccountsApi

All URIs are relative to *https://app.billforward.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_charge_to_account**](AccountsApi.md#add_charge_to_account) | **POST** /accounts/{account-ID}/invoice | 
[**add_credit_note_to_account**](AccountsApi.md#add_credit_note_to_account) | **POST** /accounts/{account-ID}/credit | 
[**create_account**](AccountsApi.md#create_account) | **POST** /accounts | 
[**create_address**](AccountsApi.md#create_address) | **POST** /addresses | 
[**delete_account**](AccountsApi.md#delete_account) | **DELETE** /accounts/{account-ID} | 
[**delete_metadata_for_account**](AccountsApi.md#delete_metadata_for_account) | **DELETE** /accounts/{account-ID}/metadata | 
[**get_account_by_id**](AccountsApi.md#get_account_by_id) | **GET** /accounts/{account-ID} | 
[**get_all_accounts**](AccountsApi.md#get_all_accounts) | **GET** /accounts | 
[**get_available_credit_on_account**](AccountsApi.md#get_available_credit_on_account) | **GET** /accounts/{account-ID}/credit | 
[**get_invoices_by_account_id**](AccountsApi.md#get_invoices_by_account_id) | **GET** /accounts/{account-ID}/invoices | 
[**get_metadata_for_account**](AccountsApi.md#get_metadata_for_account) | **GET** /accounts/{account-ID}/metadata | 
[**get_payment_method_by_account_id**](AccountsApi.md#get_payment_method_by_account_id) | **GET** /accounts/{account-ID}/payment-methods | 
[**get_subscription_charges**](AccountsApi.md#get_subscription_charges) | **GET** /accounts/{account-ID}/charges | 
[**halt_aggregation**](AccountsApi.md#halt_aggregation) | **POST** /accounts/{account-ID}/halt-aggregation | 
[**remove_credit_from_account2**](AccountsApi.md#remove_credit_from_account2) | **DELETE** /accounts/{account-ID}/credit | 
[**set_metadata_for_account**](AccountsApi.md#set_metadata_for_account) | **POST** /accounts/{account-ID}/metadata | 
[**update_account**](AccountsApi.md#update_account) | **PUT** /accounts | 
[**update_address**](AccountsApi.md#update_address) | **PUT** /addresses | 
[**upsert_metadata_for_account**](AccountsApi.md#upsert_metadata_for_account) | **PUT** /accounts/{account-ID}/metadata | 

# **add_charge_to_account**
> InlineResponseDefault2 add_charge_to_account(account_id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.AccountsApi(billforward.ApiClient(configuration))
account_id = 'account_id_example' # str | 
body = billforward.AddChargesToAccountAPIRequest() # AddChargesToAccountAPIRequest |  (optional)

try:
    api_response = api_instance.add_charge_to_account(account_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->add_charge_to_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **body** | [**AddChargesToAccountAPIRequest**](AddChargesToAccountAPIRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault2**](InlineResponseDefault2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_credit_note_to_account**
> InlineResponseDefault4 add_credit_note_to_account(account_id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.AccountsApi(billforward.ApiClient(configuration))
account_id = 'account_id_example' # str | 
body = billforward.CreditAccountRequest() # CreditAccountRequest |  (optional)

try:
    api_response = api_instance.add_credit_note_to_account(account_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->add_credit_note_to_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **body** | [**CreditAccountRequest**](CreditAccountRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault4**](InlineResponseDefault4.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_account**
> InlineResponseDefault6 create_account(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.AccountsApi(billforward.ApiClient(configuration))
body = billforward.Account() # Account |  (optional)

try:
    api_response = api_instance.create_account(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->create_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Account**](Account.md)|  | [optional] 

### Return type

[**InlineResponseDefault6**](InlineResponseDefault6.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_address**
> InlineResponseDefault12 create_address(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.AccountsApi(billforward.ApiClient(configuration))
body = billforward.Address() # Address |  (optional)

try:
    api_response = api_instance.create_address(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->create_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Address**](Address.md)|  | [optional] 

### Return type

[**InlineResponseDefault12**](InlineResponseDefault12.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account**
> InlineResponseDefault6 delete_account(account_id, delete_gateway_data=delete_gateway_data, delete_personal_data=delete_personal_data, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.AccountsApi(billforward.ApiClient(configuration))
account_id = 'account_id_example' # str | 
delete_gateway_data = false # bool |  (optional) (default to false)
delete_personal_data = false # bool |  (optional) (default to false)
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.delete_account(account_id, delete_gateway_data=delete_gateway_data, delete_personal_data=delete_personal_data, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->delete_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **delete_gateway_data** | **bool**|  | [optional] [default to false]
 **delete_personal_data** | **bool**|  | [optional] [default to false]
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault6**](InlineResponseDefault6.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_metadata_for_account**
> InlineResponseDefault7 delete_metadata_for_account(account_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.AccountsApi(billforward.ApiClient(configuration))
account_id = 'account_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.delete_metadata_for_account(account_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->delete_metadata_for_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault7**](InlineResponseDefault7.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_by_id**
> InlineResponseDefault6 get_account_by_id(account_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.AccountsApi(billforward.ApiClient(configuration))
account_id = 'account_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_account_by_id(account_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_account_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault6**](InlineResponseDefault6.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_accounts**
> InlineResponseDefault5 get_all_accounts(id=id, organizations=organizations, include_retired=include_retired, users_only=users_only, metadata=metadata)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.AccountsApi(billforward.ApiClient(configuration))
id = ['id_example'] # list[str] |  (optional)
organizations = ['organizations_example'] # list[str] |  (optional)
include_retired = true # bool |  (optional) (default to true)
users_only = false # bool |  (optional) (default to false)
metadata = 'metadata_example' # str |  (optional)

try:
    api_response = api_instance.get_all_accounts(id=id, organizations=organizations, include_retired=include_retired, users_only=users_only, metadata=metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_all_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[str]**](str.md)|  | [optional] 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **include_retired** | **bool**|  | [optional] [default to true]
 **users_only** | **bool**|  | [optional] [default to false]
 **metadata** | **str**|  | [optional] 

### Return type

[**InlineResponseDefault5**](InlineResponseDefault5.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_credit_on_account**
> InlineResponseDefault3 get_available_credit_on_account(account_id, organizations=organizations, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.AccountsApi(billforward.ApiClient(configuration))
account_id = 'account_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
include_retired = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_available_credit_on_account(account_id, organizations=organizations, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_available_credit_on_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **include_retired** | **bool**|  | [optional] [default to false]

### Return type

[**InlineResponseDefault3**](InlineResponseDefault3.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices_by_account_id**
> InlineResponseDefault8 get_invoices_by_account_id(account_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, exclude_children=exclude_children)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.AccountsApi(billforward.ApiClient(configuration))
account_id = 'account_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = false # bool |  (optional) (default to false)
exclude_children = true # bool |  (optional) (default to true)

try:
    api_response = api_instance.get_invoices_by_account_id(account_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, exclude_children=exclude_children)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_invoices_by_account_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to false]
 **exclude_children** | **bool**|  | [optional] [default to true]

### Return type

[**InlineResponseDefault8**](InlineResponseDefault8.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_for_account**
> InlineResponseDefault7 get_metadata_for_account(account_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.AccountsApi(billforward.ApiClient(configuration))
account_id = 'account_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_metadata_for_account(account_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_metadata_for_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault7**](InlineResponseDefault7.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_method_by_account_id**
> InlineResponseDefault9 get_payment_method_by_account_id(account_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, default_only=default_only)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.AccountsApi(billforward.ApiClient(configuration))
account_id = 'account_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'id' # str |  (optional) (default to id)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = true # bool |  (optional) (default to true)
default_only = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_payment_method_by_account_id(account_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, default_only=default_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_payment_method_by_account_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to id]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to true]
 **default_only** | **bool**|  | [optional] [default to false]

### Return type

[**InlineResponseDefault9**](InlineResponseDefault9.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_charges**
> InlineResponseDefault10 get_subscription_charges(account_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.AccountsApi(billforward.ApiClient(configuration))
account_id = 'account_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'id' # str |  (optional) (default to id)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_subscription_charges(account_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_subscription_charges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to id]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to false]

### Return type

[**InlineResponseDefault10**](InlineResponseDefault10.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **halt_aggregation**
> InlineResponseDefault11 halt_aggregation(account_id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.AccountsApi(billforward.ApiClient(configuration))
account_id = 'account_id_example' # str | 
body = billforward.HaltAggregationRequest() # HaltAggregationRequest |  (optional)

try:
    api_response = api_instance.halt_aggregation(account_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->halt_aggregation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **body** | [**HaltAggregationRequest**](HaltAggregationRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault11**](InlineResponseDefault11.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_credit_from_account2**
> InlineResponseDefault4 remove_credit_from_account2(account_id, body=body, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.AccountsApi(billforward.ApiClient(configuration))
account_id = 'account_id_example' # str | 
body = billforward.RemoveCreditAccountRequest() # RemoveCreditAccountRequest |  (optional)
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.remove_credit_from_account2(account_id, body=body, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->remove_credit_from_account2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **body** | [**RemoveCreditAccountRequest**](RemoveCreditAccountRequest.md)|  | [optional] 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault4**](InlineResponseDefault4.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_metadata_for_account**
> InlineResponseDefault7 set_metadata_for_account(account_id, body=body, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.AccountsApi(billforward.ApiClient(configuration))
account_id = 'account_id_example' # str | 
body = 'body_example' # str |  (optional)
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.set_metadata_for_account(account_id, body=body, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->set_metadata_for_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **body** | [**str**](str.md)|  | [optional] 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault7**](InlineResponseDefault7.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account**
> InlineResponseDefault6 update_account(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.AccountsApi(billforward.ApiClient(configuration))
body = billforward.Account() # Account |  (optional)

try:
    api_response = api_instance.update_account(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->update_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Account**](Account.md)|  | [optional] 

### Return type

[**InlineResponseDefault6**](InlineResponseDefault6.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_address**
> InlineResponseDefault12 update_address(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.AccountsApi(billforward.ApiClient(configuration))
body = billforward.Address() # Address |  (optional)

try:
    api_response = api_instance.update_address(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->update_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Address**](Address.md)|  | [optional] 

### Return type

[**InlineResponseDefault12**](InlineResponseDefault12.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_metadata_for_account**
> InlineResponseDefault7 upsert_metadata_for_account(account_id, body=body, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.AccountsApi(billforward.ApiClient(configuration))
account_id = 'account_id_example' # str | 
body = 'body_example' # str |  (optional)
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.upsert_metadata_for_account(account_id, body=body, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->upsert_metadata_for_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **body** | [**str**](str.md)|  | [optional] 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault7**](InlineResponseDefault7.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

