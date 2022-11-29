# billforward.ContractsApi

All URIs are relative to *https://app.billforward.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_contract_period**](ContractsApi.md#add_contract_period) | **POST** /contracts/{contract}/period | 
[**create_contract**](ContractsApi.md#create_contract) | **POST** /contracts | 
[**get_all_contracts**](ContractsApi.md#get_all_contracts) | **GET** /contracts | 
[**get_contract_by_id**](ContractsApi.md#get_contract_by_id) | **GET** /contracts/{contract} | 
[**start_contract**](ContractsApi.md#start_contract) | **POST** /contracts/{contract}/start | 
[**update_contract**](ContractsApi.md#update_contract) | **PUT** /contracts | 
[**void_contract**](ContractsApi.md#void_contract) | **DELETE** /contracts/{contract} | 
[**void_final_contract_period**](ContractsApi.md#void_final_contract_period) | **DELETE** /contracts/{contract}/period | 

# **add_contract_period**
> InlineResponseDefault19 add_contract_period(contract, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.ContractsApi(billforward.ApiClient(configuration))
contract = 'contract_example' # str | 
body = billforward.AddContractPeriodRequest() # AddContractPeriodRequest |  (optional)

try:
    api_response = api_instance.add_contract_period(contract, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->add_contract_period: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**|  | 
 **body** | [**AddContractPeriodRequest**](AddContractPeriodRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault19**](InlineResponseDefault19.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contract**
> InlineResponseDefault19 create_contract(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.ContractsApi(billforward.ApiClient(configuration))
body = billforward.CreateContractRequest() # CreateContractRequest |  (optional)

try:
    api_response = api_instance.create_contract(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->create_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateContractRequest**](CreateContractRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault19**](InlineResponseDefault19.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_contracts**
> InlineResponseDefault20 get_all_contracts(state=state, account_id=account_id, subscription_id=subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.ContractsApi(billforward.ApiClient(configuration))
state = ['state_example'] # list[str] |  (optional)
account_id = ['account_id_example'] # list[str] |  (optional)
subscription_id = ['subscription_id_example'] # list[str] |  (optional)
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)

try:
    api_response = api_instance.get_all_contracts(state=state, account_id=account_id, subscription_id=subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->get_all_contracts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | [**list[str]**](str.md)|  | [optional] 
 **account_id** | [**list[str]**](str.md)|  | [optional] 
 **subscription_id** | [**list[str]**](str.md)|  | [optional] 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]

### Return type

[**InlineResponseDefault20**](InlineResponseDefault20.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contract_by_id**
> InlineResponseDefault19 get_contract_by_id(contract, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.ContractsApi(billforward.ApiClient(configuration))
contract = 'contract_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_contract_by_id(contract, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->get_contract_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault19**](InlineResponseDefault19.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_contract**
> InlineResponseDefault21 start_contract(contract, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.ContractsApi(billforward.ApiClient(configuration))
contract = 'contract_example' # str | 
body = billforward.StartContractRequest() # StartContractRequest |  (optional)

try:
    api_response = api_instance.start_contract(contract, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->start_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**|  | 
 **body** | [**StartContractRequest**](StartContractRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault21**](InlineResponseDefault21.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contract**
> InlineResponseDefault19 update_contract(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.ContractsApi(billforward.ApiClient(configuration))
body = billforward.UpdateContractRequest() # UpdateContractRequest |  (optional)

try:
    api_response = api_instance.update_contract(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->update_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateContractRequest**](UpdateContractRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault19**](InlineResponseDefault19.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **void_contract**
> InlineResponseDefault19 void_contract(contract, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.ContractsApi(billforward.ApiClient(configuration))
contract = 'contract_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.void_contract(contract, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->void_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault19**](InlineResponseDefault19.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **void_final_contract_period**
> InlineResponseDefault19 void_final_contract_period(contract, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.ContractsApi(billforward.ApiClient(configuration))
contract = 'contract_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.void_final_contract_period(contract, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->void_final_contract_period: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault19**](InlineResponseDefault19.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

