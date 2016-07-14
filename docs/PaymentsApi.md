# swagger_client.PaymentsApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment**](PaymentsApi.md#create_payment) | **POST** /payments | Create a payment.
[**get_all_payments**](PaymentsApi.md#get_all_payments) | **GET** /payments | Returns a collection of all payments. By default 10 values are returned. Records are returned in natural order.
[**get_payment_as_csv**](PaymentsApi.md#get_payment_as_csv) | **GET** /payments/csv | Retrieves payments in CSV format.
[**get_payment_by_id**](PaymentsApi.md#get_payment_by_id) | **GET** /payments/{payment-ID} | Returns a single payment, specified by the payment-ID parameter.
[**get_payment_by_invoice_id**](PaymentsApi.md#get_payment_by_invoice_id) | **GET** /payments/invoice/{invoice-ID} | Returns a collection of payments, specified by the invoice-ID parameter. By default 10 values are returned. Records are returned in natural order.
[**get_payment_by_payment_gateway**](PaymentsApi.md#get_payment_by_payment_gateway) | **GET** /payments/gateway/{gateway} | Returns a collection of payments, specified by the gateway parameter. By default 10 values are returned. Records are returned in natural order.
[**get_payment_by_payment_method_id**](PaymentsApi.md#get_payment_by_payment_method_id) | **GET** /payments/payment-method/{payment-method-ID} | Returns a collection of payments, specified by the payment-method-ID parameter. By default 10 values are returned. Records are returned in natural order.
[**update_payment**](PaymentsApi.md#update_payment) | **PUT** /payments | Update a payment.


# **create_payment**
> PaymentPagedMetadata create_payment(payment)

Create a payment.

{\"nickname\":\"Create a new payment\",\"request\":\"createPaymentRequest.html\",\"response\":\"createPaymentResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentsApi()
payment = swagger_client.Payment() # Payment | The payment object to be updated.

try: 
    # Create a payment.
    api_response = api_instance.create_payment(payment)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PaymentsApi->create_payment: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment** | [**Payment**](Payment.md)| The payment object to be updated. | 

### Return type

[**PaymentPagedMetadata**](PaymentPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_payments**
> PaymentPagedMetadata get_all_payments(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of all payments. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get all payments\",\"response\":\"getPaymentAll.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentsApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first payment to return. (optional) (default to 0)
records = 10 # int | The maximum number of payments to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)

try: 
    # Returns a collection of all payments. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_payments(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PaymentsApi->get_all_payments: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first payment to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of payments to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]

### Return type

[**PaymentPagedMetadata**](PaymentPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_as_csv**
> PaymentPagedMetadata get_payment_as_csv(received_start, received_end, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Retrieves payments in CSV format.

{ \"nickname\":\"Payments CSV\",\"response\":\"payments.csv\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentsApi()
received_start = 'received_start_example' # str | The UTC DateTime specifying the start of the interval within which payments were received.
received_end = 'received_end_example' # str | The UTC DateTime specifying the end of the interval within which payments were received.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 56 # int | The offset from the first payment to return. (optional)
records = 56 # int | The maximum number of payments to return. (optional)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | The direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Retrieves payments in CSV format.
    api_response = api_instance.get_payment_as_csv(received_start, received_end, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PaymentsApi->get_payment_as_csv: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **received_start** | **str**| The UTC DateTime specifying the start of the interval within which payments were received. | 
 **received_end** | **str**| The UTC DateTime specifying the end of the interval within which payments were received. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first payment to return. | [optional] 
 **records** | **int**| The maximum number of payments to return. | [optional] 
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| The direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**PaymentPagedMetadata**](PaymentPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_by_id**
> PaymentPagedMetadata get_payment_by_id(payment_id, organizations=organizations)

Returns a single payment, specified by the payment-ID parameter.

{\"nickname\":\"Retrieve an existing payment\",\"response\":\"getPaymentByID.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentsApi()
payment_id = 'payment_id_example' # str | The unique string-ID of the payment.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single payment, specified by the payment-ID parameter.
    api_response = api_instance.get_payment_by_id(payment_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PaymentsApi->get_payment_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**| The unique string-ID of the payment. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**PaymentPagedMetadata**](PaymentPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_by_invoice_id**
> PaymentPagedMetadata get_payment_by_invoice_id(invoice_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of payments, specified by the invoice-ID parameter. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get for invoice\",\"response\":\"getPaymentByInvoice.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentsApi()
invoice_id = 'invoice_id_example' # str | The string ID of the account
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first payment to return. (optional) (default to 0)
records = 10 # int | The maximum number of payments to return. (optional) (default to 10)
order_by = 'id' # str | Specify a field used to order the result set. (optional) (default to id)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)

try: 
    # Returns a collection of payments, specified by the invoice-ID parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_payment_by_invoice_id(invoice_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PaymentsApi->get_payment_by_invoice_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**| The string ID of the account | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first payment to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of payments to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to id]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]

### Return type

[**PaymentPagedMetadata**](PaymentPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_by_payment_gateway**
> PaymentPagedMetadata get_payment_by_payment_gateway(gateway, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of payments, specified by the gateway parameter. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by gateway\",\"response\":\"getPaymentByGateway.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentsApi()
gateway = 'gateway_example' # str | The payment gateway which generated the payment.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first payment to return. (optional) (default to 0)
records = 10 # int | The maximum number of payments to return. (optional) (default to 10)
order_by = 'id' # str | Specify a field used to order the result set. (optional) (default to id)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)

try: 
    # Returns a collection of payments, specified by the gateway parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_payment_by_payment_gateway(gateway, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PaymentsApi->get_payment_by_payment_gateway: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway** | **str**| The payment gateway which generated the payment. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first payment to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of payments to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to id]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]

### Return type

[**PaymentPagedMetadata**](PaymentPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_by_payment_method_id**
> PaymentPagedMetadata get_payment_by_payment_method_id(payment_method_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of payments, specified by the payment-method-ID parameter. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by payment method\",\"response\":\"getPaymentByPaymentMethod.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentsApi()
payment_method_id = 'payment_method_id_example' # str | ID of the PaymentMethod
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first payment to return. (optional) (default to 0)
records = 10 # int | The maximum number of payments to return. (optional) (default to 10)
order_by = 'id' # str | Specify a field used to order the result set. (optional) (default to id)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)

try: 
    # Returns a collection of payments, specified by the payment-method-ID parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_payment_by_payment_method_id(payment_method_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PaymentsApi->get_payment_by_payment_method_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | **str**| ID of the PaymentMethod | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first payment to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of payments to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to id]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]

### Return type

[**PaymentPagedMetadata**](PaymentPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payment**
> PaymentPagedMetadata update_payment(payment)

Update a payment.

{\"nickname\":\"Update a payment\",\"request\":\"updatePaymentRequest.html\",\"response\":\"updatePaymentResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentsApi()
payment = swagger_client.Payment() # Payment | The payment object to be updated.

try: 
    # Update a payment.
    api_response = api_instance.update_payment(payment)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PaymentsApi->update_payment: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment** | [**Payment**](Payment.md)| The payment object to be updated. | 

### Return type

[**PaymentPagedMetadata**](PaymentPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

