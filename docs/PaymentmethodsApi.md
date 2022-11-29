# billforward.PaymentMethodsApi

All URIs are relative to *https://app.billforward.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_method**](PaymentMethodsApi.md#create_payment_method) | **POST** /payment-methods | 
[**delete_payment_method**](PaymentMethodsApi.md#delete_payment_method) | **DELETE** /payment-methods/{payment-method-ID} | 
[**get_all_payment_methods**](PaymentMethodsApi.md#get_all_payment_methods) | **GET** /payment-methods | 
[**get_mandate_pdf**](PaymentMethodsApi.md#get_mandate_pdf) | **GET** /payment-methods/{payment-method-ID}/mandate.pdf | 
[**get_payment_method_by_id**](PaymentMethodsApi.md#get_payment_method_by_id) | **GET** /payment-methods/{payment-method-ID} | 
[**get_payment_method_by_link_id**](PaymentMethodsApi.md#get_payment_method_by_link_id) | **GET** /payment-methods/link-id/{linkID} | 
[**get_payment_method_by_payment_gateway**](PaymentMethodsApi.md#get_payment_method_by_payment_gateway) | **GET** /payment-methods/gateway/{gateway} | 
[**update_payment_method**](PaymentMethodsApi.md#update_payment_method) | **PUT** /payment-methods | 
[**verify_ach**](PaymentMethodsApi.md#verify_ach) | **POST** /payment-methods/{payment-method-ID}/verify/micro-deposits | 

# **create_payment_method**
> InlineResponseDefault40 create_payment_method(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.PaymentMethodsApi(billforward.ApiClient(configuration))
body = billforward.PaymentMethod() # PaymentMethod |  (optional)

try:
    api_response = api_instance.create_payment_method(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->create_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaymentMethod**](PaymentMethod.md)|  | [optional] 

### Return type

[**InlineResponseDefault40**](InlineResponseDefault40.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_payment_method**
> InlineResponseDefault40 delete_payment_method(payment_method_id, delete_gateway_data=delete_gateway_data, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.PaymentMethodsApi(billforward.ApiClient(configuration))
payment_method_id = 'payment_method_id_example' # str | 
delete_gateway_data = false # bool |  (optional) (default to false)
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.delete_payment_method(payment_method_id, delete_gateway_data=delete_gateway_data, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->delete_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | **str**|  | 
 **delete_gateway_data** | **bool**|  | [optional] [default to false]
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault40**](InlineResponseDefault40.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_payment_methods**
> InlineResponseDefault9 get_all_payment_methods(organizations=organizations, routing_number=routing_number, account_number=account_number, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.PaymentMethodsApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
routing_number = 'routing_number_example' # str |  (optional)
account_number = 'account_number_example' # str |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_all_payment_methods(organizations=organizations, routing_number=routing_number, account_number=account_number, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->get_all_payment_methods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **routing_number** | **str**|  | [optional] 
 **account_number** | **str**|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to false]

### Return type

[**InlineResponseDefault9**](InlineResponseDefault9.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mandate_pdf**
> get_mandate_pdf(payment_method_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.PaymentMethodsApi(billforward.ApiClient(configuration))
payment_method_id = 'payment_method_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_instance.get_mandate_pdf(payment_method_id, organizations=organizations)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->get_mandate_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_method_by_id**
> InlineResponseDefault40 get_payment_method_by_id(payment_method_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.PaymentMethodsApi(billforward.ApiClient(configuration))
payment_method_id = 'payment_method_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_payment_method_by_id(payment_method_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->get_payment_method_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault40**](InlineResponseDefault40.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_method_by_link_id**
> InlineResponseDefault9 get_payment_method_by_link_id(link_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.PaymentMethodsApi(billforward.ApiClient(configuration))
link_id = 'link_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_payment_method_by_link_id(link_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->get_payment_method_by_link_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault9**](InlineResponseDefault9.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_method_by_payment_gateway**
> InlineResponseDefault9 get_payment_method_by_payment_gateway(gateway, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.PaymentMethodsApi(billforward.ApiClient(configuration))
gateway = 'gateway_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'id' # str |  (optional) (default to id)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = true # bool |  (optional) (default to true)

try:
    api_response = api_instance.get_payment_method_by_payment_gateway(gateway, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->get_payment_method_by_payment_gateway: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to id]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to true]

### Return type

[**InlineResponseDefault9**](InlineResponseDefault9.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payment_method**
> InlineResponseDefault40 update_payment_method(body=body, delete_gateway_data=delete_gateway_data)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.PaymentMethodsApi(billforward.ApiClient(configuration))
body = billforward.PaymentMethod() # PaymentMethod |  (optional)
delete_gateway_data = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.update_payment_method(body=body, delete_gateway_data=delete_gateway_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->update_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaymentMethod**](PaymentMethod.md)|  | [optional] 
 **delete_gateway_data** | **bool**|  | [optional] [default to false]

### Return type

[**InlineResponseDefault40**](InlineResponseDefault40.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_ach**
> InlineResponseDefault40 verify_ach(payment_method_id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.PaymentMethodsApi(billforward.ApiClient(configuration))
payment_method_id = 'payment_method_id_example' # str | 
body = billforward.VerifyPaymentMethodRequest() # VerifyPaymentMethodRequest |  (optional)

try:
    api_response = api_instance.verify_ach(payment_method_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->verify_ach: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | **str**|  | 
 **body** | [**VerifyPaymentMethodRequest**](VerifyPaymentMethodRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault40**](InlineResponseDefault40.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

