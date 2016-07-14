# swagger_client.ReceiptsApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_receipt**](ReceiptsApi.md#create_receipt) | **POST** /receipts | Create a receipt.
[**get_all_receipts**](ReceiptsApi.md#get_all_receipts) | **GET** /receipts | Returns a collection of all receipts. By default 10 values are returned. receipts are returned in natural order
[**get_receipt_by_id**](ReceiptsApi.md#get_receipt_by_id) | **GET** /receipts/{receipt-ID} | Returns a single receipt, specified by the ID parameter.
[**get_receipts_by_invoice**](ReceiptsApi.md#get_receipts_by_invoice) | **GET** /receipts/invoice/{invoice-ID} | Returns a receipt for the receipt payment.
[**get_receipts_by_payment**](ReceiptsApi.md#get_receipts_by_payment) | **GET** /receipts/payment/{payment-ID} | Returns a collection of receipts for the payment.
[**get_receipts_for_debit_payments_as_csv**](ReceiptsApi.md#get_receipts_for_debit_payments_as_csv) | **GET** /receipts/debits.csv | Retrieves debit payments in CSV format.
[**get_receipts_for_refund_payments_as_csv**](ReceiptsApi.md#get_receipts_for_refund_payments_as_csv) | **GET** /receipts/refunds.csv | Retrieves refunded payments in CSV format.


# **create_receipt**
> ReceiptPagedMetadata create_receipt(receipt)

Create a receipt.

{\"nickname\":\"Create a new receipt\",\"request\":\"createReceiptRequest.html\",\"response\":\"createReceiptResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReceiptsApi()
receipt = swagger_client.Receipt() # Receipt | The receipt object to be created.

try: 
    # Create a receipt.
    api_response = api_instance.create_receipt(receipt)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ReceiptsApi->create_receipt: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receipt** | [**Receipt**](Receipt.md)| The receipt object to be created. | 

### Return type

[**ReceiptPagedMetadata**](ReceiptPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_receipts**
> ReceiptPagedMetadata get_all_receipts(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, account_id=account_id, invoice_id=invoice_id, payment_method_id=payment_method_id, type=type, gateway=gateway, decision=decision)

Returns a collection of all receipts. By default 10 values are returned. receipts are returned in natural order

{\"nickname\":\"Get all receipts\",\"response\":\"getreceiptsAll.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReceiptsApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first receipt to return. (optional) (default to 0)
records = 10 # int | The maximum number of receipts to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
account_id = ['account_id_example'] # list[str] |  (optional)
invoice_id = ['invoice_id_example'] # list[str] |  (optional)
payment_method_id = ['payment_method_id_example'] # list[str] |  (optional)
type = 'type_example' # str |  (optional)
gateway = 'gateway_example' # str |  (optional)
decision = 'decision_example' # str |  (optional)

try: 
    # Returns a collection of all receipts. By default 10 values are returned. receipts are returned in natural order
    api_response = api_instance.get_all_receipts(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, account_id=account_id, invoice_id=invoice_id, payment_method_id=payment_method_id, type=type, gateway=gateway, decision=decision)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ReceiptsApi->get_all_receipts: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first receipt to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of receipts to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **account_id** | [**list[str]**](str.md)|  | [optional] 
 **invoice_id** | [**list[str]**](str.md)|  | [optional] 
 **payment_method_id** | [**list[str]**](str.md)|  | [optional] 
 **type** | **str**|  | [optional] 
 **gateway** | **str**|  | [optional] 
 **decision** | **str**|  | [optional] 

### Return type

[**ReceiptPagedMetadata**](ReceiptPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_receipt_by_id**
> ReceiptPagedMetadata get_receipt_by_id(receipt_id, organizations=organizations)

Returns a single receipt, specified by the ID parameter.

{\"nickname\":\"Retrieve an existing receipt\",\"response\":\"getreceiptByID.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReceiptsApi()
receipt_id = 'receipt_id_example' # str | ID of the receipt.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single receipt, specified by the ID parameter.
    api_response = api_instance.get_receipt_by_id(receipt_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ReceiptsApi->get_receipt_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receipt_id** | **str**| ID of the receipt. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**ReceiptPagedMetadata**](ReceiptPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_receipts_by_invoice**
> ReceiptPagedMetadata get_receipts_by_invoice(invoice_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Returns a receipt for the receipt payment.

{\"nickname\":\"Retrieve by invoice\",\"response\":\"getreceiptsByInvoice.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReceiptsApi()
invoice_id = 'invoice_id_example' # str | ID of the Invoice.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first receipt to return. (optional) (default to 0)
records = 10 # int | The maximum number of receipts to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Returns a receipt for the receipt payment.
    api_response = api_instance.get_receipts_by_invoice(invoice_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ReceiptsApi->get_receipts_by_invoice: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**| ID of the Invoice. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first receipt to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of receipts to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**ReceiptPagedMetadata**](ReceiptPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_receipts_by_payment**
> ReceiptPagedMetadata get_receipts_by_payment(payment_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Returns a collection of receipts for the payment.

{\"nickname\":\"Retrieve by payment\",\"response\":\"getreceiptsByPayment.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReceiptsApi()
payment_id = 'payment_id_example' # str | ID of the payment.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first receipt to return. (optional) (default to 0)
records = 10 # int | The maximum number of receipts to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Returns a collection of receipts for the payment.
    api_response = api_instance.get_receipts_by_payment(payment_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ReceiptsApi->get_receipts_by_payment: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**| ID of the payment. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first receipt to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of receipts to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**ReceiptPagedMetadata**](ReceiptPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_receipts_for_debit_payments_as_csv**
> ReceiptPagedMetadata get_receipts_for_debit_payments_as_csv(organizations=organizations, received_start=received_start, received_end=received_end, offset=offset, records=records, order_by=order_by, order=order, gateway=gateway)

Retrieves debit payments in CSV format.

{ \"nickname\":\"Debit payments CSV\",\"response\":\"Debit payments.csv\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReceiptsApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
received_start = 'received_start_example' # str | The UTC DateTime specifying the start of the interval within which payments were received. (optional)
received_end = 'received_end_example' # str | The UTC DateTime specifying the end of the interval within which payments were received. (optional)
offset = 56 # int | The offset from the first payment to return. (optional)
records = 56 # int | The maximum number of payments to return. (optional)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | The direction of any ordering, either ASC or DESC. (optional) (default to DESC)
gateway = ['gateway_example'] # list[str] | A list of payment gateways to include in the account.  If none are specified, all gateways will be included. (optional)

try: 
    # Retrieves debit payments in CSV format.
    api_response = api_instance.get_receipts_for_debit_payments_as_csv(organizations=organizations, received_start=received_start, received_end=received_end, offset=offset, records=records, order_by=order_by, order=order, gateway=gateway)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ReceiptsApi->get_receipts_for_debit_payments_as_csv: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **received_start** | **str**| The UTC DateTime specifying the start of the interval within which payments were received. | [optional] 
 **received_end** | **str**| The UTC DateTime specifying the end of the interval within which payments were received. | [optional] 
 **offset** | **int**| The offset from the first payment to return. | [optional] 
 **records** | **int**| The maximum number of payments to return. | [optional] 
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| The direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **gateway** | [**list[str]**](str.md)| A list of payment gateways to include in the account.  If none are specified, all gateways will be included. | [optional] 

### Return type

[**ReceiptPagedMetadata**](ReceiptPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_receipts_for_refund_payments_as_csv**
> ReceiptPagedMetadata get_receipts_for_refund_payments_as_csv(organizations=organizations, completed_start=completed_start, completed_end=completed_end, offset=offset, records=records, order_by=order_by, order=order)

Retrieves refunded payments in CSV format.

{ \"nickname\":\"Refunded payments CSV\",\"response\":\"Refunded payments.csv\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReceiptsApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
completed_start = 'completed_start_example' # str | The UTC DateTime specifying the start of the interval within which payments were received. (optional)
completed_end = 'completed_end_example' # str | The UTC DateTime specifying the end of the interval within which payments were received. (optional)
offset = 56 # int | The offset from the first payment to return. (optional)
records = 56 # int | The maximum number of payments to return. (optional)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | The direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Retrieves refunded payments in CSV format.
    api_response = api_instance.get_receipts_for_refund_payments_as_csv(organizations=organizations, completed_start=completed_start, completed_end=completed_end, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ReceiptsApi->get_receipts_for_refund_payments_as_csv: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **completed_start** | **str**| The UTC DateTime specifying the start of the interval within which payments were received. | [optional] 
 **completed_end** | **str**| The UTC DateTime specifying the end of the interval within which payments were received. | [optional] 
 **offset** | **int**| The offset from the first payment to return. | [optional] 
 **records** | **int**| The maximum number of payments to return. | [optional] 
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| The direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**ReceiptPagedMetadata**](ReceiptPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

