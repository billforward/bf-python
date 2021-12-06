# billforward.ChargesApi

All URIs are relative to *https://app.billforward.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_recalculate_subscription_charge**](ChargesApi.md#batch_recalculate_subscription_charge) | **POST** /charges/recalculate | 
[**get_all_subscription_charges**](ChargesApi.md#get_all_subscription_charges) | **GET** /charges | 
[**get_subscription_charge_by_id**](ChargesApi.md#get_subscription_charge_by_id) | **GET** /charges/{charge-id} | 
[**recalculate_subscription_charge**](ChargesApi.md#recalculate_subscription_charge) | **POST** /charges/{charge-ID}/recalculate | 
[**void_subscription_charge**](ChargesApi.md#void_subscription_charge) | **DELETE** /charges/{charge-id} | 

# **batch_recalculate_subscription_charge**
> InlineResponseDefault15 batch_recalculate_subscription_charge(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.ChargesApi(billforward.ApiClient(configuration))
body = billforward.RecalculateChargeBatchRequest() # RecalculateChargeBatchRequest |  (optional)

try:
    api_response = api_instance.batch_recalculate_subscription_charge(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChargesApi->batch_recalculate_subscription_charge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecalculateChargeBatchRequest**](RecalculateChargeBatchRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault15**](InlineResponseDefault15.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_subscription_charges**
> InlineResponseDefault10 get_all_subscription_charges(account_id=account_id, product_rate_plan=product_rate_plan, state=state, pricing_component_type=pricing_component_type, parent_invoice_id=parent_invoice_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.ChargesApi(billforward.ApiClient(configuration))
account_id = 'account_id_example' # str |  (optional)
product_rate_plan = 'product_rate_plan_example' # str |  (optional)
state = 'state_example' # str |  (optional)
pricing_component_type = 'pricing_component_type_example' # str |  (optional)
parent_invoice_id = ['parent_invoice_id_example'] # list[str] |  (optional)
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_all_subscription_charges(account_id=account_id, product_rate_plan=product_rate_plan, state=state, pricing_component_type=pricing_component_type, parent_invoice_id=parent_invoice_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChargesApi->get_all_subscription_charges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | [optional] 
 **product_rate_plan** | **str**|  | [optional] 
 **state** | **str**|  | [optional] 
 **pricing_component_type** | **str**|  | [optional] 
 **parent_invoice_id** | [**list[str]**](str.md)|  | [optional] 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
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

# **get_subscription_charge_by_id**
> InlineResponseDefault16 get_subscription_charge_by_id(charge_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.ChargesApi(billforward.ApiClient(configuration))
charge_id = 'charge_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'id' # str |  (optional) (default to id)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_subscription_charge_by_id(charge_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChargesApi->get_subscription_charge_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charge_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to id]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to false]

### Return type

[**InlineResponseDefault16**](InlineResponseDefault16.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recalculate_subscription_charge**
> InlineResponseDefault10 recalculate_subscription_charge(charge_id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.ChargesApi(billforward.ApiClient(configuration))
charge_id = 'charge_id_example' # str | 
body = billforward.RecalculateChargeRequest() # RecalculateChargeRequest |  (optional)

try:
    api_response = api_instance.recalculate_subscription_charge(charge_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChargesApi->recalculate_subscription_charge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charge_id** | **str**|  | 
 **body** | [**RecalculateChargeRequest**](RecalculateChargeRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault10**](InlineResponseDefault10.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **void_subscription_charge**
> InlineResponseDefault16 void_subscription_charge(charge_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.ChargesApi(billforward.ApiClient(configuration))
charge_id = 'charge_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.void_subscription_charge(charge_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChargesApi->void_subscription_charge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charge_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault16**](InlineResponseDefault16.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

