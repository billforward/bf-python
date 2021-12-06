# billforward.ReceiptsApi

All URIs are relative to *https://app.billforward.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_receipt**](ReceiptsApi.md#create_receipt) | **POST** /receipts | 
[**get_all_receipts**](ReceiptsApi.md#get_all_receipts) | **GET** /receipts | 
[**get_receipt_by_id**](ReceiptsApi.md#get_receipt_by_id) | **GET** /receipts/{receipt-ID} | 
[**get_receipts_by_invoice**](ReceiptsApi.md#get_receipts_by_invoice) | **GET** /receipts/invoice/{invoice-ID} | 
[**get_receipts_by_payment**](ReceiptsApi.md#get_receipts_by_payment) | **GET** /receipts/payment/{payment-ID} | 
[**get_receipts_for_debit_payments_as_csv**](ReceiptsApi.md#get_receipts_for_debit_payments_as_csv) | **GET** /receipts/debits.csv | 
[**get_receipts_for_refund_payments_as_csv**](ReceiptsApi.md#get_receipts_for_refund_payments_as_csv) | **GET** /receipts/refunds.csv | 

# **create_receipt**
> InlineResponseDefault55 create_receipt(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.ReceiptsApi(billforward.ApiClient(configuration))
body = billforward.Receipt() # Receipt |  (optional)

try:
    api_response = api_instance.create_receipt(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptsApi->create_receipt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Receipt**](Receipt.md)|  | [optional] 

### Return type

[**InlineResponseDefault55**](InlineResponseDefault55.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_receipts**
> InlineResponseDefault54 get_all_receipts(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, account_id=account_id, invoice_id=invoice_id, payment_method_id=payment_method_id, type=type, gateway=gateway, decision=decision)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.ReceiptsApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)
account_id = ['account_id_example'] # list[str] |  (optional)
invoice_id = ['invoice_id_example'] # list[str] |  (optional)
payment_method_id = ['payment_method_id_example'] # list[str] |  (optional)
type = 'type_example' # str |  (optional)
gateway = 'gateway_example' # str |  (optional)
decision = 'decision_example' # str |  (optional)

try:
    api_response = api_instance.get_all_receipts(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, account_id=account_id, invoice_id=invoice_id, payment_method_id=payment_method_id, type=type, gateway=gateway, decision=decision)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptsApi->get_all_receipts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]
 **account_id** | [**list[str]**](str.md)|  | [optional] 
 **invoice_id** | [**list[str]**](str.md)|  | [optional] 
 **payment_method_id** | [**list[str]**](str.md)|  | [optional] 
 **type** | **str**|  | [optional] 
 **gateway** | **str**|  | [optional] 
 **decision** | **str**|  | [optional] 

### Return type

[**InlineResponseDefault54**](InlineResponseDefault54.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_receipt_by_id**
> InlineResponseDefault55 get_receipt_by_id(receipt_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.ReceiptsApi(billforward.ApiClient(configuration))
receipt_id = 'receipt_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_receipt_by_id(receipt_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptsApi->get_receipt_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receipt_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault55**](InlineResponseDefault55.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_receipts_by_invoice**
> InlineResponseDefault54 get_receipts_by_invoice(invoice_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.ReceiptsApi(billforward.ApiClient(configuration))
invoice_id = 'invoice_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)

try:
    api_response = api_instance.get_receipts_by_invoice(invoice_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptsApi->get_receipts_by_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]

### Return type

[**InlineResponseDefault54**](InlineResponseDefault54.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_receipts_by_payment**
> InlineResponseDefault54 get_receipts_by_payment(payment_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.ReceiptsApi(billforward.ApiClient(configuration))
payment_id = 'payment_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)

try:
    api_response = api_instance.get_receipts_by_payment(payment_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptsApi->get_receipts_by_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]

### Return type

[**InlineResponseDefault54**](InlineResponseDefault54.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_receipts_for_debit_payments_as_csv**
> get_receipts_for_debit_payments_as_csv(organizations=organizations, received_start=received_start, received_end=received_end, offset=offset, records=records, order_by=order_by, order=order, gateway=gateway)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.ReceiptsApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
received_start = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
received_end = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
offset = 56 # int |  (optional)
records = 56 # int |  (optional)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)
gateway = ['gateway_example'] # list[str] |  (optional)

try:
    api_instance.get_receipts_for_debit_payments_as_csv(organizations=organizations, received_start=received_start, received_end=received_end, offset=offset, records=records, order_by=order_by, order=order, gateway=gateway)
except ApiException as e:
    print("Exception when calling ReceiptsApi->get_receipts_for_debit_payments_as_csv: %s\n" % e)
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
 **gateway** | [**list[str]**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_receipts_for_refund_payments_as_csv**
> get_receipts_for_refund_payments_as_csv(organizations=organizations, completed_start=completed_start, completed_end=completed_end, offset=offset, records=records, order_by=order_by, order=order)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.ReceiptsApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
completed_start = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
completed_end = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
offset = 56 # int |  (optional)
records = 56 # int |  (optional)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)

try:
    api_instance.get_receipts_for_refund_payments_as_csv(organizations=organizations, completed_start=completed_start, completed_end=completed_end, offset=offset, records=records, order_by=order_by, order=order)
except ApiException as e:
    print("Exception when calling ReceiptsApi->get_receipts_for_refund_payments_as_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **completed_start** | [**SimpleDateParam**](.md)|  | [optional] 
 **completed_end** | [**SimpleDateParam**](.md)|  | [optional] 
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

