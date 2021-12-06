# billforward.PaymentsApi

All URIs are relative to *https://app.billforward.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_offline_payment**](PaymentsApi.md#create_offline_payment) | **POST** /payments/offline | 
[**create_payment**](PaymentsApi.md#create_payment) | **POST** /payments | 
[**get_all_payments**](PaymentsApi.md#get_all_payments) | **GET** /payments | 
[**get_payment_as_csv**](PaymentsApi.md#get_payment_as_csv) | **GET** /payments/csv | 
[**get_payment_by_id**](PaymentsApi.md#get_payment_by_id) | **GET** /payments/{payment-ID} | 
[**get_payment_by_invoice_id**](PaymentsApi.md#get_payment_by_invoice_id) | **GET** /payments/invoice/{invoice-ID} | 
[**get_payment_by_payment_gateway**](PaymentsApi.md#get_payment_by_payment_gateway) | **GET** /payments/gateway/{gateway} | 
[**get_payment_by_payment_method_id**](PaymentsApi.md#get_payment_by_payment_method_id) | **GET** /payments/payment-method/{payment-method-ID} | 
[**refund_payment**](PaymentsApi.md#refund_payment) | **POST** /payments/{payment_id}/refund | 
[**update_payment**](PaymentsApi.md#update_payment) | **PUT** /payments | 

# **create_offline_payment**
> InlineResponseDefault41 create_offline_payment(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.PaymentsApi(billforward.ApiClient(configuration))
body = billforward.CreateOfflinePaymentRequest() # CreateOfflinePaymentRequest |  (optional)

try:
    api_response = api_instance.create_offline_payment(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->create_offline_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOfflinePaymentRequest**](CreateOfflinePaymentRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault41**](InlineResponseDefault41.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_payment**
> InlineResponseDefault41 create_payment(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.PaymentsApi(billforward.ApiClient(configuration))
body = billforward.Payment() # Payment |  (optional)

try:
    api_response = api_instance.create_payment(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->create_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Payment**](Payment.md)|  | [optional] 

### Return type

[**InlineResponseDefault41**](InlineResponseDefault41.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_payments**
> InlineResponseDefault42 get_all_payments(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, account_id=account_id, subscription_id=subscription_id)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.PaymentsApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = true # bool |  (optional) (default to true)
account_id = ['account_id_example'] # list[str] |  (optional)
subscription_id = ['subscription_id_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_all_payments(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, account_id=account_id, subscription_id=subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->get_all_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to true]
 **account_id** | [**list[str]**](str.md)|  | [optional] 
 **subscription_id** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault42**](InlineResponseDefault42.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_as_csv**
> get_payment_as_csv(organizations=organizations, received_start=received_start, received_end=received_end, offset=offset, records=records, order_by=order_by, order=order)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.PaymentsApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
received_start = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
received_end = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
offset = 56 # int |  (optional)
records = 56 # int |  (optional)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)

try:
    api_instance.get_payment_as_csv(organizations=organizations, received_start=received_start, received_end=received_end, offset=offset, records=records, order_by=order_by, order=order)
except ApiException as e:
    print("Exception when calling PaymentsApi->get_payment_as_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **received_start** | [**SimpleDateParam**](.md)|  | [optional] 
 **received_end** | [**SimpleDateParam**](.md)|  | [optional] 
 **offset** | **int**|  | [optional] 
 **records** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_by_id**
> InlineResponseDefault41 get_payment_by_id(payment_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.PaymentsApi(billforward.ApiClient(configuration))
payment_id = 'payment_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_payment_by_id(payment_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->get_payment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault41**](InlineResponseDefault41.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_by_invoice_id**
> InlineResponseDefault42 get_payment_by_invoice_id(invoice_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.PaymentsApi(billforward.ApiClient(configuration))
invoice_id = 'invoice_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'id' # str |  (optional) (default to id)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = true # bool |  (optional) (default to true)

try:
    api_response = api_instance.get_payment_by_invoice_id(invoice_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->get_payment_by_invoice_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to id]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to true]

### Return type

[**InlineResponseDefault42**](InlineResponseDefault42.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_by_payment_gateway**
> InlineResponseDefault42 get_payment_by_payment_gateway(gateway, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.PaymentsApi(billforward.ApiClient(configuration))
gateway = 'gateway_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'id' # str |  (optional) (default to id)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = true # bool |  (optional) (default to true)

try:
    api_response = api_instance.get_payment_by_payment_gateway(gateway, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->get_payment_by_payment_gateway: %s\n" % e)
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

[**InlineResponseDefault42**](InlineResponseDefault42.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_by_payment_method_id**
> InlineResponseDefault42 get_payment_by_payment_method_id(payment_method_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.PaymentsApi(billforward.ApiClient(configuration))
payment_method_id = 'payment_method_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'id' # str |  (optional) (default to id)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = true # bool |  (optional) (default to true)

try:
    api_response = api_instance.get_payment_by_payment_method_id(payment_method_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->get_payment_by_payment_method_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to id]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to true]

### Return type

[**InlineResponseDefault42**](InlineResponseDefault42.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_payment**
> InlineResponseDefault43 refund_payment(payment_id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.PaymentsApi(billforward.ApiClient(configuration))
payment_id = 'payment_id_example' # str | 
body = billforward.PaymentRefundRequest() # PaymentRefundRequest |  (optional)

try:
    api_response = api_instance.refund_payment(payment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->refund_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**|  | 
 **body** | [**PaymentRefundRequest**](PaymentRefundRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault43**](InlineResponseDefault43.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payment**
> InlineResponseDefault41 update_payment(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.PaymentsApi(billforward.ApiClient(configuration))
body = billforward.Payment() # Payment |  (optional)

try:
    api_response = api_instance.update_payment(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->update_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Payment**](Payment.md)|  | [optional] 

### Return type

[**InlineResponseDefault41**](InlineResponseDefault41.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

