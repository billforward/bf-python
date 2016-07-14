# billforward.RefundsApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_refund**](RefundsApi.md#create_refund) | **POST** /refunds | &lt;p&gt;When creating a refund either the invoice, or invoice payment must be specified.&lt;/p&gt;&lt;p&gt;Creating a refund by specifying the invoiceID will refund any un-refunded value up to the full value of the payment. When refunding via the invoicePaymentID the same rules apply. Refunds will be processed by the same payment methods that took the payment.&lt;/p&gt;&lt;p&gt;Refunds can be for a partial amount of the payment. It is possible to create refunds up to the value of the total payment.&lt;/p&gt;&lt;p&gt;Once a payment or invoice is fully refunded, no more refunds can be created. Errors will be returned if the payment is greater than available refund funds.&lt;/p&gt;
[**get_all_refunds**](RefundsApi.md#get_all_refunds) | **GET** /refunds | Returns a collection of all refunds. By default 10 values are returned. Refunds are returned in natural order
[**get_refund_by_id**](RefundsApi.md#get_refund_by_id) | **GET** /refunds/{refund-ID} | Returns a single refund, specified by the ID parameter.
[**get_refund_for_original_payment**](RefundsApi.md#get_refund_for_original_payment) | **GET** /refunds/original-payment/{payment-ID} | Returns a refund for the original payment.
[**get_refund_for_refund_payment**](RefundsApi.md#get_refund_for_refund_payment) | **GET** /refunds/refund-payment/{payment-ID} | Returns a refund for the refund payment.
[**get_refund_for_refunded_invoice**](RefundsApi.md#get_refund_for_refunded_invoice) | **GET** /refunds/invoice/{invoice-ID} | Returns a refund for the refund payment.
[**get_refunds_as_csv**](RefundsApi.md#get_refunds_as_csv) | **GET** /refunds/csv | Retrieves refunds in CSV format.
[**update_refund**](RefundsApi.md#update_refund) | **PUT** /refunds | Update a refund


# **create_refund**
> RefundPagedMetadata create_refund(refund)

<p>When creating a refund either the invoice, or invoice payment must be specified.</p><p>Creating a refund by specifying the invoiceID will refund any un-refunded value up to the full value of the payment. When refunding via the invoicePaymentID the same rules apply. Refunds will be processed by the same payment methods that took the payment.</p><p>Refunds can be for a partial amount of the payment. It is possible to create refunds up to the value of the total payment.</p><p>Once a payment or invoice is fully refunded, no more refunds can be created. Errors will be returned if the payment is greater than available refund funds.</p>

{\"nickname\":\"Create a new refund\",\"request\":\"createRefundRequest.html\",\"response\":\"createRefundResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.RefundsApi()
refund = billforward.Refund() # Refund | The refund object to be created.

try: 
    # <p>When creating a refund either the invoice, or invoice payment must be specified.</p><p>Creating a refund by specifying the invoiceID will refund any un-refunded value up to the full value of the payment. When refunding via the invoicePaymentID the same rules apply. Refunds will be processed by the same payment methods that took the payment.</p><p>Refunds can be for a partial amount of the payment. It is possible to create refunds up to the value of the total payment.</p><p>Once a payment or invoice is fully refunded, no more refunds can be created. Errors will be returned if the payment is greater than available refund funds.</p>
    api_response = api_instance.create_refund(refund)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RefundsApi->create_refund: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refund** | [**Refund**](Refund.md)| The refund object to be created. | 

### Return type

[**RefundPagedMetadata**](RefundPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_refunds**
> RefundPagedMetadata get_all_refunds(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Returns a collection of all refunds. By default 10 values are returned. Refunds are returned in natural order

{\"nickname\":\"Get all refunds\",\"response\":\"getRefundsAll.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.RefundsApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first refund to return. (optional) (default to 0)
records = 10 # int | The maximum number of refunds to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Returns a collection of all refunds. By default 10 values are returned. Refunds are returned in natural order
    api_response = api_instance.get_all_refunds(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RefundsApi->get_all_refunds: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first refund to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of refunds to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**RefundPagedMetadata**](RefundPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_refund_by_id**
> RefundPagedMetadata get_refund_by_id(refund_id, organizations=organizations)

Returns a single refund, specified by the ID parameter.

{\"nickname\":\"Retrieve an existing refund\",\"response\":\"getRefundByID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.RefundsApi()
refund_id = 'refund_id_example' # str | ID of the Refund.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single refund, specified by the ID parameter.
    api_response = api_instance.get_refund_by_id(refund_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RefundsApi->get_refund_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refund_id** | **str**| ID of the Refund. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**RefundPagedMetadata**](RefundPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_refund_for_original_payment**
> RefundPagedMetadata get_refund_for_original_payment(payment_id, organizations=organizations)

Returns a refund for the original payment.

{\"nickname\":\"Retrieve by originating payment\",\"response\":\"getRefundsByPayment.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.RefundsApi()
payment_id = 'payment_id_example' # str | ID of the Payment.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a refund for the original payment.
    api_response = api_instance.get_refund_for_original_payment(payment_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RefundsApi->get_refund_for_original_payment: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**| ID of the Payment. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**RefundPagedMetadata**](RefundPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_refund_for_refund_payment**
> RefundPagedMetadata get_refund_for_refund_payment(payment_id, organizations=organizations)

Returns a refund for the refund payment.

{\"nickname\":\"Retrieve by refund payment\",\"response\":\"getRefundsByPayment.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.RefundsApi()
payment_id = 'payment_id_example' # str | ID of the Payment.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a refund for the refund payment.
    api_response = api_instance.get_refund_for_refund_payment(payment_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RefundsApi->get_refund_for_refund_payment: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**| ID of the Payment. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**RefundPagedMetadata**](RefundPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_refund_for_refunded_invoice**
> RefundPagedMetadata get_refund_for_refunded_invoice(invoice_id, organizations=organizations)

Returns a refund for the refund payment.

{\"nickname\":\"Retrieve by invoice\",\"response\":\"getRefundsByInvoice.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.RefundsApi()
invoice_id = 'invoice_id_example' # str | ID of the Invoice.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a refund for the refund payment.
    api_response = api_instance.get_refund_for_refunded_invoice(invoice_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RefundsApi->get_refund_for_refunded_invoice: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**| ID of the Invoice. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**RefundPagedMetadata**](RefundPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_refunds_as_csv**
> RefundPagedMetadata get_refunds_as_csv(completed_start, completed_end, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Retrieves refunds in CSV format.

{ \"nickname\":\"Refunds CSV\",\"response\":\"refunds.csv\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.RefundsApi()
completed_start = 'completed_start_example' # str | The UTC DateTime specifying the start of the interval within which refunds were completed.
completed_end = 'completed_end_example' # str | The UTC DateTime specifying the end of the interval within which refunds were completed.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 56 # int | The offset from the first refund to return. (optional)
records = 56 # int | The maximum number of refunds to return. (optional)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | The direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Retrieves refunds in CSV format.
    api_response = api_instance.get_refunds_as_csv(completed_start, completed_end, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RefundsApi->get_refunds_as_csv: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **completed_start** | **str**| The UTC DateTime specifying the start of the interval within which refunds were completed. | 
 **completed_end** | **str**| The UTC DateTime specifying the end of the interval within which refunds were completed. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first refund to return. | [optional] 
 **records** | **int**| The maximum number of refunds to return. | [optional] 
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| The direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**RefundPagedMetadata**](RefundPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_refund**
> RefundPagedMetadata update_refund(refund)

Update a refund

{\"nickname\":\"Update a refund\",\"request\":\"updateRefundRequest.html\",\"response\":\"updateRefundResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.RefundsApi()
refund = billforward.Refund() # Refund | The refund object to be update.

try: 
    # Update a refund
    api_response = api_instance.update_refund(refund)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RefundsApi->update_refund: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refund** | [**Refund**](Refund.md)| The refund object to be update. | 

### Return type

[**RefundPagedMetadata**](RefundPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

