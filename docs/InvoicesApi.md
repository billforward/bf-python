# swagger_client.InvoicesApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_charge_to_invoice**](InvoicesApi.md#add_charge_to_invoice) | **POST** /invoices/{invoice-ID}/charges | Creates a charge on the specified invoice.
[**aggregate_invoices**](InvoicesApi.md#aggregate_invoices) | **POST** /invoices/aggregate | Aggregate Invoices into to one parent Invoice
[**execute_invoice**](InvoicesApi.md#execute_invoice) | **POST** /invoices/{invoice-ID}/execute | Attempt payment for the outstanding value of an invoice
[**generate_line_payments_for_all_invoices**](InvoicesApi.md#generate_line_payments_for_all_invoices) | **POST** /invoices/generate-line-payments | Generates InvoiceLinePayments for all existing InvoicePayments.
[**get_all_invoices**](InvoicesApi.md#get_all_invoices) | **GET** /invoices | Retrieves a collection of all invoices. By default 10 values are returned. Records are returned in natural order.
[**get_all_invoices_as_csv**](InvoicesApi.md#get_all_invoices_as_csv) | **GET** /invoices/all.csv | Retrieves a collection of all invoices. By default 10 values are returned. Records are returned in natural order.
[**get_bucketed_revenue_attributions_as_csv**](InvoicesApi.md#get_bucketed_revenue_attributions_as_csv) | **GET** /invoices/bucketed-revenue-attributions.csv | Retrieves (as CSV) all attributions of Invoice costs to Invoice lines, bucketed.
[**get_charges_on_invoice**](InvoicesApi.md#get_charges_on_invoice) | **GET** /invoices/{invoice-ID}/charges | Returns all charges for the specified invoice. By default 10 values are returned. Records are returned in natural order.
[**get_credit_invoice_line_payments_from_invoices_as_csv**](InvoicesApi.md#get_credit_invoice_line_payments_from_invoices_as_csv) | **GET** /invoices/credit.csv | Retrieves credit note-paid from InvoicePayments upon line items, in CSV format.
[**get_credit_invoice_line_payments_from_invoices_as_csv_by_payment_received**](InvoicesApi.md#get_credit_invoice_line_payments_from_invoices_as_csv_by_payment_received) | **GET** /invoices/payment-received/credit.csv | Retrieves credit note-paid from InvoicePayments upon line items, in CSV format.
[**get_debit_invoice_line_payments_from_invoices_as_csv**](InvoicesApi.md#get_debit_invoice_line_payments_from_invoices_as_csv) | **GET** /invoices/revenue.csv | Retrieves received revenue from InvoicePayments upon line items, in CSV format.
[**get_debit_invoice_line_payments_from_invoices_as_csv_by_payment_received**](InvoicesApi.md#get_debit_invoice_line_payments_from_invoices_as_csv_by_payment_received) | **GET** /invoices/payment-received/revenue.csv | Retrieves received revenue from InvoicePayments upon line items, in CSV format.
[**get_invoice_as_html**](InvoicesApi.md#get_invoice_as_html) | **GET** /invoices/{ID}.html | Retrieves a single invoice specified by the ID parameter.
[**get_invoice_as_pdf**](InvoicesApi.md#get_invoice_as_pdf) | **GET** /invoices/{ID}.pdf | Retrieves a single invoice specified by the ID parameter.
[**get_invoice_by_id**](InvoicesApi.md#get_invoice_by_id) | **GET** /invoices/{invoice-ID} | Retrieves a single invoice specified by the invoice-ID parameter.
[**get_invoice_by_id_as_csv**](InvoicesApi.md#get_invoice_by_id_as_csv) | **GET** /invoices/{ID}.csv | Retrieves a single invoice specified by the ID parameter.
[**get_invoice_by_subscription_id**](InvoicesApi.md#get_invoice_by_subscription_id) | **GET** /invoices/subscription/{subscription-ID} | Retrieves a collection of invoices specified by the subscription-ID parameter. By default 10 values are returned. Records are returned in natural order.
[**get_invoice_by_subscription_version_id**](InvoicesApi.md#get_invoice_by_subscription_version_id) | **GET** /invoices/subscription/version/{subscription-version-ID} | Retrieves a collection of invoices specified by the subscription-version-ID parameter. By default 10 values are returned. Records are returned in natural order.
[**get_invoice_by_version_id**](InvoicesApi.md#get_invoice_by_version_id) | **GET** /invoices/version/{version-ID} | Retrieves a single invoice, specified by the version-ID parameter.
[**get_invoices_by_account_id**](InvoicesApi.md#get_invoices_by_account_id) | **GET** /invoices/account/{account-ID} | Retrieves a collection of invoices specified by the account-ID parameter. By default 10 values are returned. Records are returned in natural order.
[**get_invoices_by_period_end**](InvoicesApi.md#get_invoices_by_period_end) | **GET** /invoices/period-end/{lower-threshold}/{upper-threshold} | Retrieves a collection of invoice objects with period-end times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.
[**get_invoices_by_period_start**](InvoicesApi.md#get_invoices_by_period_start) | **GET** /invoices/period-start/{lower-threshold}/{upper-threshold} | Retrieves a collection of invoice objects with period-start times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.
[**get_invoices_by_period_start_as_csv**](InvoicesApi.md#get_invoices_by_period_start_as_csv) | **GET** /invoices/period-start/{lower-threshold}/{upper-threshold}.csv | Retrieves a collection of invoice objects with period-start times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.
[**get_invoices_by_state**](InvoicesApi.md#get_invoices_by_state) | **GET** /invoices/state/{state} | Retrieves a collection of invoices, specified by the state parameter. By default 10 values are returned. Records are returned in natural order.
[**get_invoices_by_state_and_period_start**](InvoicesApi.md#get_invoices_by_state_and_period_start) | **GET** /invoices/state/{state}/period-start/{lower-threshold}/{upper-threshold} | Retrieves a collection of invoice objects specified by the state parameter and with period-start times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.
[**get_invoices_by_state_and_period_start_as_csv**](InvoicesApi.md#get_invoices_by_state_and_period_start_as_csv) | **GET** /invoices/state/{state}/period-start/{lower-threshold}/{upper-threshold}.csv | Retrieves a collection of invoice objects specified by the state parameter and with period-start times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.
[**get_invoices_by_state_as_csv**](InvoicesApi.md#get_invoices_by_state_as_csv) | **GET** /invoices/state/{state}.csv | Retrieves a collection of invoices, specified by the state parameter. By default 10 values are returned. Records are returned in natural order.
[**get_line_payments**](InvoicesApi.md#get_line_payments) | **GET** /invoices/line-payments | Retrieves all InvoiceLine payment attributions.
[**get_line_payments_as_csv**](InvoicesApi.md#get_line_payments_as_csv) | **GET** /invoices/line-payments.csv | Retrieves (as CSV) all InvoiceLine payment attributions.
[**get_metadata_for_invoice**](InvoicesApi.md#get_metadata_for_invoice) | **GET** /invoices/{invoice-ID}/metadata | Retrieve any associated metadata.
[**get_refund_invoice_line_payments_from_invoices_as_csv**](InvoicesApi.md#get_refund_invoice_line_payments_from_invoices_as_csv) | **GET** /invoices/refund.csv | Retrieves awarded refunds from InvoicePayments upon line items, in CSV format.
[**get_refund_invoice_line_payments_from_invoices_as_csv_by_refund_received**](InvoicesApi.md#get_refund_invoice_line_payments_from_invoices_as_csv_by_refund_received) | **GET** /invoices/payment-received/refund.csv | Retrieves awarded refunds from InvoicePayments upon line items, in CSV format.
[**get_revenue_attributions**](InvoicesApi.md#get_revenue_attributions) | **GET** /invoices/revenue-attributions | Retrieves all attributions of Invoice costs to Invoice lines.
[**get_revenue_attributions_as_csv**](InvoicesApi.md#get_revenue_attributions_as_csv) | **GET** /invoices/revenue-attributions.csv | Retrieves (as CSV) all attributions of Invoice costs to Invoice lines.
[**get_swagger_for_invoice**](InvoicesApi.md#get_swagger_for_invoice) | **GET** /invoices/swagger-end-point/{query-string} | 
[**import_invoice**](InvoicesApi.md#import_invoice) | **POST** /invoices/import | Import an invoice.
[**recalculate_invoice**](InvoicesApi.md#recalculate_invoice) | **POST** /invoices/{invoice-ID}/recalculate | Re-calculate an Invoice.
[**remove_charge_from_invoice**](InvoicesApi.md#remove_charge_from_invoice) | **DELETE** /invoices/{invoice-ID}/charges/{charge-ID} | Removes the specified charge from the specified Invoice.
[**remove_metadata_from_invoice**](InvoicesApi.md#remove_metadata_from_invoice) | **DELETE** /invoices/{invoice-ID}/metadata | Remove any associated metadata.
[**set_metadata_for_invoice**](InvoicesApi.md#set_metadata_for_invoice) | **POST** /invoices/{invoice-ID}/metadata | Remove any existing metadata keys and create the provided data.
[**update_invoice**](InvoicesApi.md#update_invoice) | **PUT** /invoices | Update an Invoice.
[**upsert_metadata_for_invoice**](InvoicesApi.md#upsert_metadata_for_invoice) | **PUT** /invoices/{invoice-ID}/metadata | Update any existing metadata key-values and insert any new key-values, no keys will be removed.
[**void_invoice**](InvoicesApi.md#void_invoice) | **DELETE** /invoices/{invoice-ID} | Voids the invoice specified by the invoice identifier parameter.


# **add_charge_to_invoice**
> SubscriptionChargePagedMetadata add_charge_to_invoice(invoice_id, charge)

Creates a charge on the specified invoice.

{\"nickname\":\"Add to invoice\",\"response\":\"addChargeToInvoice.html\",\"request\":\"addChargeToInvoiceRequest.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
invoice_id = 'invoice_id_example' # str | ID of the invoice.
charge = swagger_client.AddChargeRequest() # AddChargeRequest | The charge request

try: 
    # Creates a charge on the specified invoice.
    api_response = api_instance.add_charge_to_invoice(invoice_id, charge)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->add_charge_to_invoice: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**| ID of the invoice. | 
 **charge** | [**AddChargeRequest**](AddChargeRequest.md)| The charge request | 

### Return type

[**SubscriptionChargePagedMetadata**](SubscriptionChargePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aggregate_invoices**
> InvoicePagedMetadata aggregate_invoices(request)

Aggregate Invoices into to one parent Invoice

{\"nickname\":\"Aggregate invoices\",\"response\":\"AggregateResponse.html\",\"request\":\"AggregateRequest.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
request = swagger_client.BillingEntityBase() # BillingEntityBase | 

try: 
    # Aggregate Invoices into to one parent Invoice
    api_response = api_instance.aggregate_invoices(request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->aggregate_invoices: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**BillingEntityBase**](BillingEntityBase.md)|  | 

### Return type

[**InvoicePagedMetadata**](InvoicePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_invoice**
> InvoicePagedMetadata execute_invoice(invoice_id, request)

Attempt payment for the outstanding value of an invoice

{\"nickname\":\"Execute invoice\",\"response\":\"executeInvoiceResponse.html\",\"request\":\"ExecuteInvoiceRequest.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
invoice_id = 'invoice_id_example' # str | 
request = swagger_client.BillingEntityBase() # BillingEntityBase | 

try: 
    # Attempt payment for the outstanding value of an invoice
    api_response = api_instance.execute_invoice(invoice_id, request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->execute_invoice: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **request** | [**BillingEntityBase**](BillingEntityBase.md)|  | 

### Return type

[**InvoicePagedMetadata**](InvoicePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_line_payments_for_all_invoices**
> InvoiceLinePaymentPagedMetadata generate_line_payments_for_all_invoices(organizations=organizations)

Generates InvoiceLinePayments for all existing InvoicePayments.

{ \"nickname\" : \"Generate InvoiceLinePayments\",\"response\" : \"Generate InvoiceLinePayments.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Generates InvoiceLinePayments for all existing InvoicePayments.
    api_response = api_instance.generate_line_payments_for_all_invoices(organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->generate_line_payments_for_all_invoices: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**InvoiceLinePaymentPagedMetadata**](InvoiceLinePaymentPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_invoices**
> InvoicePagedMetadata get_all_invoices(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, exclude_children=exclude_children, metadata=metadata)

Retrieves a collection of all invoices. By default 10 values are returned. Records are returned in natural order.

{ \"nickname\" : \"Retrieve all invoices\",\"response\" : \"getInvoiceAll.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first invoice to return. (optional) (default to 0)
records = 10 # int | The maximum number of invoices to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired products should be returned. (optional) (default to false)
exclude_children = true # bool | Should child invoices be excluded. (optional) (default to true)
metadata = 'metadata_example' # str |  (optional)

try: 
    # Retrieves a collection of all invoices. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_invoices(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, exclude_children=exclude_children, metadata=metadata)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->get_all_invoices: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first invoice to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of invoices to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to false]
 **exclude_children** | **bool**| Should child invoices be excluded. | [optional] [default to true]
 **metadata** | **str**|  | [optional] 

### Return type

[**InvoicePagedMetadata**](InvoicePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_invoices_as_csv**
> InvoicePagedMetadata get_all_invoices_as_csv(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Retrieves a collection of all invoices. By default 10 values are returned. Records are returned in natural order.

{ \"nickname\" : \"Retrieve all invoices\",\"response\" : \"getInvoiceAll.csv\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first invoice to return. (optional) (default to 0)
records = 10 # int | The maximum number of invoices to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired products should be returned. (optional) (default to false)

try: 
    # Retrieves a collection of all invoices. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_invoices_as_csv(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->get_all_invoices_as_csv: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first invoice to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of invoices to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to false]

### Return type

[**InvoicePagedMetadata**](InvoicePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bucketed_revenue_attributions_as_csv**
> str get_bucketed_revenue_attributions_as_csv(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end)

Retrieves (as CSV) all attributions of Invoice costs to Invoice lines, bucketed.

{ \"nickname\" : \"(CSV) Retrieve bucketed revenue attributions\",\"response\" : \"getBucketedRevenueAttributions.csv\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
recognition_start = 'recognition_start_example' # str | The UTC DateTime specifying the start of the interval within which revenue attributions will be recognised (example input: 2015-09-13T11:50:24). (optional)
recognition_end = 'recognition_end_example' # str | The UTC DateTime specifying the end of the interval within which revenue attributions will be recognised (example input: 2015-10-13T11:50:24). (optional)

try: 
    # Retrieves (as CSV) all attributions of Invoice costs to Invoice lines, bucketed.
    api_response = api_instance.get_bucketed_revenue_attributions_as_csv(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->get_bucketed_revenue_attributions_as_csv: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **recognition_start** | **str**| The UTC DateTime specifying the start of the interval within which revenue attributions will be recognised (example input: 2015-09-13T11:50:24). | [optional] 
 **recognition_end** | **str**| The UTC DateTime specifying the end of the interval within which revenue attributions will be recognised (example input: 2015-10-13T11:50:24). | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_charges_on_invoice**
> SubscriptionChargePagedMetadata get_charges_on_invoice(invoice_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, state=state, type=type, include_retired=include_retired)

Returns all charges for the specified invoice. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"List on invoice\",\"response\":\"getChargesInvoice.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
invoice_id = 'invoice_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first subscription to return. (optional) (default to 0)
records = 10 # int | The maximum number of subscriptions to return. (optional) (default to 10)
order_by = 'id' # str | Specify a field used to order the result set. (optional) (default to id)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
state = 'state_example' # str | Ihe direction of any ordering, either ASC or DESC. (optional)
type = 'type_example' # str | Ihe direction of any ordering, either ASC or DESC. (optional)
include_retired = false # bool | Whether retired subscriptions should be returned. (optional) (default to false)

try: 
    # Returns all charges for the specified invoice. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_charges_on_invoice(invoice_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, state=state, type=type, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->get_charges_on_invoice: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first subscription to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of subscriptions to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to id]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **state** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] 
 **type** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] 
 **include_retired** | **bool**| Whether retired subscriptions should be returned. | [optional] [default to false]

### Return type

[**SubscriptionChargePagedMetadata**](SubscriptionChargePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit_invoice_line_payments_from_invoices_as_csv**
> InvoiceLinePaymentPagedMetadata get_credit_invoice_line_payments_from_invoices_as_csv(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end)

Retrieves credit note-paid from InvoicePayments upon line items, in CSV format.

{ \"nickname\" : \"Credit InvoiceLinePayments CSV\",\"response\" : \"Credit InvoiceLinePayments.csv\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
recognition_start = 'recognition_start_example' # str | The UTC DateTime specifying the start of the interval within which credit payments will be recognised (example input: 2015-09-13T11:50:24). (optional)
recognition_end = 'recognition_end_example' # str | The UTC DateTime specifying the end of the interval within which credit payments will be recognised (example input: 2015-10-13T11:50:24). (optional)

try: 
    # Retrieves credit note-paid from InvoicePayments upon line items, in CSV format.
    api_response = api_instance.get_credit_invoice_line_payments_from_invoices_as_csv(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->get_credit_invoice_line_payments_from_invoices_as_csv: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **recognition_start** | **str**| The UTC DateTime specifying the start of the interval within which credit payments will be recognised (example input: 2015-09-13T11:50:24). | [optional] 
 **recognition_end** | **str**| The UTC DateTime specifying the end of the interval within which credit payments will be recognised (example input: 2015-10-13T11:50:24). | [optional] 

### Return type

[**InvoiceLinePaymentPagedMetadata**](InvoiceLinePaymentPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit_invoice_line_payments_from_invoices_as_csv_by_payment_received**
> InvoiceLinePaymentPagedMetadata get_credit_invoice_line_payments_from_invoices_as_csv_by_payment_received(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end)

Retrieves credit note-paid from InvoicePayments upon line items, in CSV format.

{ \"nickname\" : \"Credit InvoiceLinePayments CSV\",\"response\" : \"Credit InvoiceLinePayments.csv\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
recognition_start = 'recognition_start_example' # str | The UTC DateTime specifying the start of the interval within which credit payments will be recognised (example input: 2015-09-13T11:50:24). (optional)
recognition_end = 'recognition_end_example' # str | The UTC DateTime specifying the end of the interval within which credit payments will be recognised (example input: 2015-10-13T11:50:24). (optional)

try: 
    # Retrieves credit note-paid from InvoicePayments upon line items, in CSV format.
    api_response = api_instance.get_credit_invoice_line_payments_from_invoices_as_csv_by_payment_received(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->get_credit_invoice_line_payments_from_invoices_as_csv_by_payment_received: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **recognition_start** | **str**| The UTC DateTime specifying the start of the interval within which credit payments will be recognised (example input: 2015-09-13T11:50:24). | [optional] 
 **recognition_end** | **str**| The UTC DateTime specifying the end of the interval within which credit payments will be recognised (example input: 2015-10-13T11:50:24). | [optional] 

### Return type

[**InvoiceLinePaymentPagedMetadata**](InvoiceLinePaymentPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debit_invoice_line_payments_from_invoices_as_csv**
> InvoiceLinePaymentPagedMetadata get_debit_invoice_line_payments_from_invoices_as_csv(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end)

Retrieves received revenue from InvoicePayments upon line items, in CSV format.

{ \"nickname\" : \"Debit InvoiceLinePayments CSV\",\"response\" : \"Debit InvoiceLinePayments.csv\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
recognition_start = 'recognition_start_example' # str | The UTC DateTime specifying the start of the interval within which revenue will be recognised (example input: 2015-09-13T11:50:24). (optional)
recognition_end = 'recognition_end_example' # str | The UTC DateTime specifying the end of the interval within which revenue will be recognised (example input: 2015-10-13T11:50:24). (optional)

try: 
    # Retrieves received revenue from InvoicePayments upon line items, in CSV format.
    api_response = api_instance.get_debit_invoice_line_payments_from_invoices_as_csv(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->get_debit_invoice_line_payments_from_invoices_as_csv: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **recognition_start** | **str**| The UTC DateTime specifying the start of the interval within which revenue will be recognised (example input: 2015-09-13T11:50:24). | [optional] 
 **recognition_end** | **str**| The UTC DateTime specifying the end of the interval within which revenue will be recognised (example input: 2015-10-13T11:50:24). | [optional] 

### Return type

[**InvoiceLinePaymentPagedMetadata**](InvoiceLinePaymentPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debit_invoice_line_payments_from_invoices_as_csv_by_payment_received**
> InvoiceLinePaymentPagedMetadata get_debit_invoice_line_payments_from_invoices_as_csv_by_payment_received(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end)

Retrieves received revenue from InvoicePayments upon line items, in CSV format.

{ \"nickname\" : \"Debit InvoiceLinePayments CSV\",\"response\" : \"Debit InvoiceLinePayments.csv\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
recognition_start = 'recognition_start_example' # str | The UTC DateTime specifying the start of the interval within which revenue will be recognised (example input: 2015-09-13T11:50:24). (optional)
recognition_end = 'recognition_end_example' # str | The UTC DateTime specifying the end of the interval within which revenue will be recognised (example input: 2015-10-13T11:50:24). (optional)

try: 
    # Retrieves received revenue from InvoicePayments upon line items, in CSV format.
    api_response = api_instance.get_debit_invoice_line_payments_from_invoices_as_csv_by_payment_received(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->get_debit_invoice_line_payments_from_invoices_as_csv_by_payment_received: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **recognition_start** | **str**| The UTC DateTime specifying the start of the interval within which revenue will be recognised (example input: 2015-09-13T11:50:24). | [optional] 
 **recognition_end** | **str**| The UTC DateTime specifying the end of the interval within which revenue will be recognised (example input: 2015-10-13T11:50:24). | [optional] 

### Return type

[**InvoiceLinePaymentPagedMetadata**](InvoiceLinePaymentPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_as_html**
> str get_invoice_as_html(id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, tier_breakdown=tier_breakdown, inclusive_end=inclusive_end, show_zero_cost=show_zero_cost, show_plan_only_when_ambiguous=show_plan_only_when_ambiguous)

Retrieves a single invoice specified by the ID parameter.

{ \"nickname\" : \"HTML invoice\",\"response\" : \"getInvoiceByID.HTML.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
id = 'id_example' # str | The ID of the invoice.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first invoice to return. (optional) (default to 0)
records = 10 # int | The maximum number of invoices to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired products should be returned. (optional) (default to false)
tier_breakdown = false # bool | Whether to provide a breakdown of charge tiering. (optional) (default to false)
inclusive_end = false # bool | Whether to present in the Invoice date range only those dates whose entirety are involved in the billing period. In other words: when true, this subtracts 1 from the \"period end\" date shown to the customer. (optional) (default to false)
show_zero_cost = true # bool | Whether to show zero-cost lines. (optional) (default to true)
show_plan_only_when_ambiguous = true # bool | Whether to state which plan the Invoice lines came from, regardless of whether there's only one plan involved in this Invoice. (optional) (default to true)

try: 
    # Retrieves a single invoice specified by the ID parameter.
    api_response = api_instance.get_invoice_as_html(id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, tier_breakdown=tier_breakdown, inclusive_end=inclusive_end, show_zero_cost=show_zero_cost, show_plan_only_when_ambiguous=show_plan_only_when_ambiguous)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->get_invoice_as_html: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the invoice. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first invoice to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of invoices to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to false]
 **tier_breakdown** | **bool**| Whether to provide a breakdown of charge tiering. | [optional] [default to false]
 **inclusive_end** | **bool**| Whether to present in the Invoice date range only those dates whose entirety are involved in the billing period. In other words: when true, this subtracts 1 from the \&quot;period end\&quot; date shown to the customer. | [optional] [default to false]
 **show_zero_cost** | **bool**| Whether to show zero-cost lines. | [optional] [default to true]
 **show_plan_only_when_ambiguous** | **bool**| Whether to state which plan the Invoice lines came from, regardless of whether there&#39;s only one plan involved in this Invoice. | [optional] [default to true]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_as_pdf**
> file get_invoice_as_pdf(id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, tier_breakdown=tier_breakdown, inclusive_end=inclusive_end, show_zero_cost=show_zero_cost, show_plan_only_when_ambiguous=show_plan_only_when_ambiguous, include_footer=include_footer, group_line_items_by=group_line_items_by)

Retrieves a single invoice specified by the ID parameter.

{ \"nickname\" : \"PDF Invoice\",\"response\" : \"getInvoiceByID.pdf\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
id = 'id_example' # str | The ID of the invoice.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first invoice to return. (optional) (default to 0)
records = 10 # int | The maximum number of invoices to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired products should be returned. (optional) (default to false)
tier_breakdown = false # bool | Whether to provide a breakdown of charge tiering. (optional) (default to false)
inclusive_end = false # bool | Whether to present in the Invoice date range only those dates whose entirety are involved in the billing period. In other words: when true, this subtracts 1 from the \"period end\" date shown to the customer. (optional) (default to false)
show_zero_cost = true # bool | Whether to show zero-cost lines. (optional) (default to true)
show_plan_only_when_ambiguous = true # bool | Whether to state which plan the Invoice lines came from, regardless of whether there's only one plan involved in this Invoice. (optional) (default to true)
include_footer = true # bool |  (optional)
group_line_items_by = 'group_line_items_by_example' # str |  (optional)

try: 
    # Retrieves a single invoice specified by the ID parameter.
    api_response = api_instance.get_invoice_as_pdf(id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, tier_breakdown=tier_breakdown, inclusive_end=inclusive_end, show_zero_cost=show_zero_cost, show_plan_only_when_ambiguous=show_plan_only_when_ambiguous, include_footer=include_footer, group_line_items_by=group_line_items_by)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->get_invoice_as_pdf: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the invoice. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first invoice to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of invoices to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to false]
 **tier_breakdown** | **bool**| Whether to provide a breakdown of charge tiering. | [optional] [default to false]
 **inclusive_end** | **bool**| Whether to present in the Invoice date range only those dates whose entirety are involved in the billing period. In other words: when true, this subtracts 1 from the \&quot;period end\&quot; date shown to the customer. | [optional] [default to false]
 **show_zero_cost** | **bool**| Whether to show zero-cost lines. | [optional] [default to true]
 **show_plan_only_when_ambiguous** | **bool**| Whether to state which plan the Invoice lines came from, regardless of whether there&#39;s only one plan involved in this Invoice. | [optional] [default to true]
 **include_footer** | **bool**|  | [optional] 
 **group_line_items_by** | **str**|  | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/pdf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_by_id**
> InvoicePagedMetadata get_invoice_by_id(invoice_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, exclude_children=exclude_children)

Retrieves a single invoice specified by the invoice-ID parameter.

{ \"nickname\" : \"Retrieve an existing invoice\",\"response\" : \"getInvoiceByID.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
invoice_id = 'invoice_id_example' # str | The ID of the invoice.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first invoice to return. (optional) (default to 0)
records = 10 # int | The maximum number of invoices to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired products should be returned. (optional) (default to false)
exclude_children = true # bool | Should child invoices be excluded. (optional) (default to true)

try: 
    # Retrieves a single invoice specified by the invoice-ID parameter.
    api_response = api_instance.get_invoice_by_id(invoice_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, exclude_children=exclude_children)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->get_invoice_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**| The ID of the invoice. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first invoice to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of invoices to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to false]
 **exclude_children** | **bool**| Should child invoices be excluded. | [optional] [default to true]

### Return type

[**InvoicePagedMetadata**](InvoicePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_by_id_as_csv**
> str get_invoice_by_id_as_csv(id, organizations=organizations)

Retrieves a single invoice specified by the ID parameter.

{ \"nickname\" : \"CSV invoice\",\"response\" : \"getInvoiceByID.csv\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
id = 'id_example' # str | The ID of the invoice.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Retrieves a single invoice specified by the ID parameter.
    api_response = api_instance.get_invoice_by_id_as_csv(id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->get_invoice_by_id_as_csv: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the invoice. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_by_subscription_id**
> InvoicePagedMetadata get_invoice_by_subscription_id(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, exclude_children=exclude_children)

Retrieves a collection of invoices specified by the subscription-ID parameter. By default 10 values are returned. Records are returned in natural order.

{ \"nickname\" : \"Retrieve by subscription\",\"response\" : \"getInvoiceBySubscriptionID.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
subscription_id = 'subscription_id_example' # str | ID of the subscription.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first invoice to return. (optional) (default to 0)
records = 10 # int | The maximum number of invoices to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired products should be returned. (optional) (default to false)
exclude_children = true # bool | Should child invoices be excluded. (optional) (default to true)

try: 
    # Retrieves a collection of invoices specified by the subscription-ID parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_invoice_by_subscription_id(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, exclude_children=exclude_children)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->get_invoice_by_subscription_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| ID of the subscription. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first invoice to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of invoices to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to false]
 **exclude_children** | **bool**| Should child invoices be excluded. | [optional] [default to true]

### Return type

[**InvoicePagedMetadata**](InvoicePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_by_subscription_version_id**
> InvoicePagedMetadata get_invoice_by_subscription_version_id(subscription_version_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, exclude_children=exclude_children)

Retrieves a collection of invoices specified by the subscription-version-ID parameter. By default 10 values are returned. Records are returned in natural order.

{ \"nickname\" : \"Retrieve by subscription version\",\"response\" : \"getInvoiceBySubscriptionVersionID.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
subscription_version_id = 'subscription_version_id_example' # str | Version ID of the subscription.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first invoice to return. (optional) (default to 0)
records = 10 # int | The maximum number of invoices to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired products should be returned. (optional) (default to false)
exclude_children = true # bool | Should child invoices be excluded. (optional) (default to true)

try: 
    # Retrieves a collection of invoices specified by the subscription-version-ID parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_invoice_by_subscription_version_id(subscription_version_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, exclude_children=exclude_children)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->get_invoice_by_subscription_version_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_version_id** | **str**| Version ID of the subscription. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first invoice to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of invoices to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to false]
 **exclude_children** | **bool**| Should child invoices be excluded. | [optional] [default to true]

### Return type

[**InvoicePagedMetadata**](InvoicePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_by_version_id**
> InvoicePagedMetadata get_invoice_by_version_id(version_id, organizations=organizations)

Retrieves a single invoice, specified by the version-ID parameter.

{ \"nickname\" : \"Retrieve by version\",\"response\" : \"getInvoiceByVersionID.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
version_id = 'version_id_example' # str | The version-ID of the invoice.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Retrieves a single invoice, specified by the version-ID parameter.
    api_response = api_instance.get_invoice_by_version_id(version_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->get_invoice_by_version_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | **str**| The version-ID of the invoice. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**InvoicePagedMetadata**](InvoicePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices_by_account_id**
> InvoicePagedMetadata get_invoices_by_account_id(account_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, exclude_children=exclude_children)

Retrieves a collection of invoices specified by the account-ID parameter. By default 10 values are returned. Records are returned in natural order.

{ \"nickname\" : \"Retrieve by account\",\"response\" : \"getInvoiceByAccountID.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
account_id = 'account_id_example' # str | ID of the account.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first invoice to return. (optional) (default to 0)
records = 10 # int | The maximum number of invoices to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired products should be returned. (optional) (default to false)
exclude_children = true # bool | Should child invoices be excluded. (optional) (default to true)

try: 
    # Retrieves a collection of invoices specified by the account-ID parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_invoices_by_account_id(account_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, exclude_children=exclude_children)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->get_invoices_by_account_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first invoice to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of invoices to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to false]
 **exclude_children** | **bool**| Should child invoices be excluded. | [optional] [default to true]

### Return type

[**InvoicePagedMetadata**](InvoicePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices_by_period_end**
> InvoicePagedMetadata get_invoices_by_period_end(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Retrieves a collection of invoice objects with period-end times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.

{ \"nickname\" : \"Retrieve by period-end\",\"response\" : \"getInvoiceByPeriodEnd.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
lower_threshold = 'lower_threshold_example' # str | The UTC DateTime specifying the start of the result period.
upper_threshold = 'upper_threshold_example' # str | The UTC DateTime specifying the end of the result period.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first taxation-link to return. (optional) (default to 0)
records = 10 # int | The maximum number of taxation-links to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired products should be returned. (optional) (default to false)

try: 
    # Retrieves a collection of invoice objects with period-end times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_invoices_by_period_end(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->get_invoices_by_period_end: %s\n" % e
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
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to false]

### Return type

[**InvoicePagedMetadata**](InvoicePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices_by_period_start**
> InvoicePagedMetadata get_invoices_by_period_start(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Retrieves a collection of invoice objects with period-start times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.

{ \"nickname\" : \"Retrieve by period-start\",\"response\" : \"getInvoiceByPeriodStart.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
lower_threshold = 'lower_threshold_example' # str | The UTC DateTime specifying the start of the result period.
upper_threshold = 'upper_threshold_example' # str | The UTC DateTime specifying the end of the result period.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first taxation-link to return. (optional) (default to 0)
records = 10 # int | The maximum number of taxation-links to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired products should be returned. (optional) (default to false)

try: 
    # Retrieves a collection of invoice objects with period-start times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_invoices_by_period_start(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->get_invoices_by_period_start: %s\n" % e
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
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to false]

### Return type

[**InvoicePagedMetadata**](InvoicePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices_by_period_start_as_csv**
> InvoicePagedMetadata get_invoices_by_period_start_as_csv(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Retrieves a collection of invoice objects with period-start times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.

{ \"nickname\" : \"Retrieve by period-start\",\"response\" : \"getInvoiceByPeriodStart.csv\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
lower_threshold = 'lower_threshold_example' # str | The UTC DateTime specifying the start of the result period.
upper_threshold = 'upper_threshold_example' # str | The UTC DateTime specifying the end of the result period.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first taxation-link to return. (optional) (default to 0)
records = 10 # int | The maximum number of taxation-links to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired products should be returned. (optional) (default to false)

try: 
    # Retrieves a collection of invoice objects with period-start times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_invoices_by_period_start_as_csv(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->get_invoices_by_period_start_as_csv: %s\n" % e
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
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to false]

### Return type

[**InvoicePagedMetadata**](InvoicePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices_by_state**
> InvoicePagedMetadata get_invoices_by_state(state, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Retrieves a collection of invoices, specified by the state parameter. By default 10 values are returned. Records are returned in natural order.

{ \"nickname\" : \"Retrieve by state\",\"response\" : \"getInvoiceByState.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
state = 'state_example' # str | The current state of the invoice, either Paid, Pending,  Unpaid or Voided.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first subscription to return. (optional) (default to 0)
records = 10 # int | The maximum number of subscriptions to return. (optional) (default to 10)
order_by = 'ID' # str | Specify a field used to order the result set. (optional) (default to ID)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired products should be returned. (optional) (default to false)

try: 
    # Retrieves a collection of invoices, specified by the state parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_invoices_by_state(state, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->get_invoices_by_state: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| The current state of the invoice, either Paid, Pending,  Unpaid or Voided. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first subscription to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of subscriptions to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to ID]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to false]

### Return type

[**InvoicePagedMetadata**](InvoicePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices_by_state_and_period_start**
> InvoicePagedMetadata get_invoices_by_state_and_period_start(state, lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Retrieves a collection of invoice objects specified by the state parameter and with period-start times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.

{ \"nickname\" : \"Retrieve by state and period-start\",\"response\" : \"getInvoiceByStateAndPeriodStart.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
state = 'state_example' # str | The current state of the invoice, either Paid, Pending,  Unpaid or Voided.
lower_threshold = 'lower_threshold_example' # str | The UTC DateTime specifying the start of the result period.
upper_threshold = 'upper_threshold_example' # str | The UTC DateTime specifying the end of the result period.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first taxation-link to return. (optional) (default to 0)
records = 10 # int | The maximum number of taxation-links to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired products should be returned. (optional) (default to false)

try: 
    # Retrieves a collection of invoice objects specified by the state parameter and with period-start times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_invoices_by_state_and_period_start(state, lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->get_invoices_by_state_and_period_start: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| The current state of the invoice, either Paid, Pending,  Unpaid or Voided. | 
 **lower_threshold** | **str**| The UTC DateTime specifying the start of the result period. | 
 **upper_threshold** | **str**| The UTC DateTime specifying the end of the result period. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first taxation-link to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of taxation-links to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to false]

### Return type

[**InvoicePagedMetadata**](InvoicePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices_by_state_and_period_start_as_csv**
> InvoicePagedMetadata get_invoices_by_state_and_period_start_as_csv(state, lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Retrieves a collection of invoice objects specified by the state parameter and with period-start times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.

{ \"nickname\" : \"Retrieve by state and period-start\",\"response\" : \"getInvoiceByStateAndPeriodStart.csv\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
state = 'state_example' # str | The current state of the invoice, either Paid, Pending,  Unpaid or Voided.
lower_threshold = 'lower_threshold_example' # str | The UTC DateTime specifying the start of the result period.
upper_threshold = 'upper_threshold_example' # str | The UTC DateTime specifying the end of the result period.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first taxation-link to return. (optional) (default to 0)
records = 10 # int | The maximum number of taxation-links to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired products should be returned. (optional) (default to false)

try: 
    # Retrieves a collection of invoice objects specified by the state parameter and with period-start times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_invoices_by_state_and_period_start_as_csv(state, lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->get_invoices_by_state_and_period_start_as_csv: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| The current state of the invoice, either Paid, Pending,  Unpaid or Voided. | 
 **lower_threshold** | **str**| The UTC DateTime specifying the start of the result period. | 
 **upper_threshold** | **str**| The UTC DateTime specifying the end of the result period. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first taxation-link to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of taxation-links to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to false]

### Return type

[**InvoicePagedMetadata**](InvoicePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices_by_state_as_csv**
> InvoicePagedMetadata get_invoices_by_state_as_csv(state, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Retrieves a collection of invoices, specified by the state parameter. By default 10 values are returned. Records are returned in natural order.

{ \"nickname\" : \"Retrieve by state\",\"response\" : \"getInvoiceByState.csv\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
state = 'state_example' # str | The current state of the invoice, either Paid, Pending,  Unpaid or Voided.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first subscription to return. (optional) (default to 0)
records = 10 # int | The maximum number of subscriptions to return. (optional) (default to 10)
order_by = 'ID' # str | Specify a field used to order the result set. (optional) (default to ID)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired products should be returned. (optional) (default to false)

try: 
    # Retrieves a collection of invoices, specified by the state parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_invoices_by_state_as_csv(state, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->get_invoices_by_state_as_csv: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| The current state of the invoice, either Paid, Pending,  Unpaid or Voided. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first subscription to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of subscriptions to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to ID]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to false]

### Return type

[**InvoicePagedMetadata**](InvoicePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_line_payments**
> InvoiceLinePaymentPagedMetadata get_line_payments(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end, include_gateway=include_gateway, exclude_gateway=exclude_gateway)

Retrieves all InvoiceLine payment attributions.

{ \"nickname\" : \"Retrieve InvoiceLine payment attributions\",\"response\" : \"getInvoiceLinePayments.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
recognition_start = 'recognition_start_example' # str | The UTC DateTime specifying the start of the interval within which line payment attributions will be recognised (example input: 2015-09-13T11:50:24). (optional)
recognition_end = 'recognition_end_example' # str | The UTC DateTime specifying the end of the interval within which line payment attributions will be recognised (example input: 2015-10-13T11:50:24). (optional)
include_gateway = ['include_gateway_example'] # list[str] | Include attributions only from payments made via these payment gateways. Takes precedence over `exclude_gateway` param (if both are provided). (optional)
exclude_gateway = ['exclude_gateway_example'] # list[str] | Include attributions from payments made via all payment gateways, except these. (optional)

try: 
    # Retrieves all InvoiceLine payment attributions.
    api_response = api_instance.get_line_payments(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end, include_gateway=include_gateway, exclude_gateway=exclude_gateway)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->get_line_payments: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **recognition_start** | **str**| The UTC DateTime specifying the start of the interval within which line payment attributions will be recognised (example input: 2015-09-13T11:50:24). | [optional] 
 **recognition_end** | **str**| The UTC DateTime specifying the end of the interval within which line payment attributions will be recognised (example input: 2015-10-13T11:50:24). | [optional] 
 **include_gateway** | [**list[str]**](str.md)| Include attributions only from payments made via these payment gateways. Takes precedence over &#x60;exclude_gateway&#x60; param (if both are provided). | [optional] 
 **exclude_gateway** | [**list[str]**](str.md)| Include attributions from payments made via all payment gateways, except these. | [optional] 

### Return type

[**InvoiceLinePaymentPagedMetadata**](InvoiceLinePaymentPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_line_payments_as_csv**
> InvoiceLinePaymentPagedMetadata get_line_payments_as_csv(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end, include_gateway=include_gateway, exclude_gateway=exclude_gateway)

Retrieves (as CSV) all InvoiceLine payment attributions.

{ \"nickname\" : \"(CSV) Retrieve InvoiceLine payment attributions\",\"response\" : \"getInvoiceLinePayments.csv\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
recognition_start = 'recognition_start_example' # str | The UTC DateTime specifying the start of the interval within which line payment attributions will be recognised (example input: 2015-09-13T11:50:24). (optional)
recognition_end = 'recognition_end_example' # str | The UTC DateTime specifying the end of the interval within which line payment attributions will be recognised (example input: 2015-10-13T11:50:24). (optional)
include_gateway = ['include_gateway_example'] # list[str] | Include attributions only from payments made via these payment gateways. Takes precedence over `exclude_gateway` param (if both are provided). (optional)
exclude_gateway = ['exclude_gateway_example'] # list[str] | Include attributions from payments made via all payment gateways, except these. (optional)

try: 
    # Retrieves (as CSV) all InvoiceLine payment attributions.
    api_response = api_instance.get_line_payments_as_csv(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end, include_gateway=include_gateway, exclude_gateway=exclude_gateway)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->get_line_payments_as_csv: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **recognition_start** | **str**| The UTC DateTime specifying the start of the interval within which line payment attributions will be recognised (example input: 2015-09-13T11:50:24). | [optional] 
 **recognition_end** | **str**| The UTC DateTime specifying the end of the interval within which line payment attributions will be recognised (example input: 2015-10-13T11:50:24). | [optional] 
 **include_gateway** | [**list[str]**](str.md)| Include attributions only from payments made via these payment gateways. Takes precedence over &#x60;exclude_gateway&#x60; param (if both are provided). | [optional] 
 **exclude_gateway** | [**list[str]**](str.md)| Include attributions from payments made via all payment gateways, except these. | [optional] 

### Return type

[**InvoiceLinePaymentPagedMetadata**](InvoiceLinePaymentPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_for_invoice**
> DynamicMetadata get_metadata_for_invoice(invoice_id, organizations=organizations)

Retrieve any associated metadata.

{\"nickname\":\"Retrieve metadata on invoice\",\"request\":\"getInvoiceMetadataRequest.html\",\"response\":\"getInvoiceMetadataResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
invoice_id = 'invoice_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Retrieve any associated metadata.
    api_response = api_instance.get_metadata_for_invoice(invoice_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->get_metadata_for_invoice: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**DynamicMetadata**](DynamicMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_refund_invoice_line_payments_from_invoices_as_csv**
> InvoiceLinePaymentPagedMetadata get_refund_invoice_line_payments_from_invoices_as_csv(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end)

Retrieves awarded refunds from InvoicePayments upon line items, in CSV format.

{ \"nickname\" : \"Refund InvoiceLinePayments CSV\",\"response\" : \"Refund InvoiceLinePayments.csv\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
recognition_start = 'recognition_start_example' # str | The UTC DateTime specifying the start of the interval within which refunds will be recognised (example input: 2015-09-13T11:50:24). (optional)
recognition_end = 'recognition_end_example' # str | The UTC DateTime specifying the end of the interval within which refunds will be recognised (example input: 2015-10-13T11:50:24). (optional)

try: 
    # Retrieves awarded refunds from InvoicePayments upon line items, in CSV format.
    api_response = api_instance.get_refund_invoice_line_payments_from_invoices_as_csv(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->get_refund_invoice_line_payments_from_invoices_as_csv: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **recognition_start** | **str**| The UTC DateTime specifying the start of the interval within which refunds will be recognised (example input: 2015-09-13T11:50:24). | [optional] 
 **recognition_end** | **str**| The UTC DateTime specifying the end of the interval within which refunds will be recognised (example input: 2015-10-13T11:50:24). | [optional] 

### Return type

[**InvoiceLinePaymentPagedMetadata**](InvoiceLinePaymentPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_refund_invoice_line_payments_from_invoices_as_csv_by_refund_received**
> InvoiceLinePaymentPagedMetadata get_refund_invoice_line_payments_from_invoices_as_csv_by_refund_received(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end)

Retrieves awarded refunds from InvoicePayments upon line items, in CSV format.

{ \"nickname\" : \"Refund InvoiceLinePayments CSV\",\"response\" : \"Refund InvoiceLinePayments.csv\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
recognition_start = 'recognition_start_example' # str | The UTC DateTime specifying the start of the interval within which refunds will be recognised (example input: 2015-09-13T11:50:24). (optional)
recognition_end = 'recognition_end_example' # str | The UTC DateTime specifying the end of the interval within which refunds will be recognised (example input: 2015-10-13T11:50:24). (optional)

try: 
    # Retrieves awarded refunds from InvoicePayments upon line items, in CSV format.
    api_response = api_instance.get_refund_invoice_line_payments_from_invoices_as_csv_by_refund_received(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->get_refund_invoice_line_payments_from_invoices_as_csv_by_refund_received: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **recognition_start** | **str**| The UTC DateTime specifying the start of the interval within which refunds will be recognised (example input: 2015-09-13T11:50:24). | [optional] 
 **recognition_end** | **str**| The UTC DateTime specifying the end of the interval within which refunds will be recognised (example input: 2015-10-13T11:50:24). | [optional] 

### Return type

[**InvoiceLinePaymentPagedMetadata**](InvoiceLinePaymentPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_revenue_attributions**
> RevenueAttributionPagedMetadata get_revenue_attributions(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end)

Retrieves all attributions of Invoice costs to Invoice lines.

{ \"nickname\" : \"Retrieve revenue attributions\",\"response\" : \"getRevenueAttributions.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
recognition_start = 'recognition_start_example' # str | The UTC DateTime specifying the start of the interval within which revenue attributions will be recognised (example input: 2015-09-13T11:50:24). (optional)
recognition_end = 'recognition_end_example' # str | The UTC DateTime specifying the end of the interval within which revenue attributions will be recognised (example input: 2015-10-13T11:50:24). (optional)

try: 
    # Retrieves all attributions of Invoice costs to Invoice lines.
    api_response = api_instance.get_revenue_attributions(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->get_revenue_attributions: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **recognition_start** | **str**| The UTC DateTime specifying the start of the interval within which revenue attributions will be recognised (example input: 2015-09-13T11:50:24). | [optional] 
 **recognition_end** | **str**| The UTC DateTime specifying the end of the interval within which revenue attributions will be recognised (example input: 2015-10-13T11:50:24). | [optional] 

### Return type

[**RevenueAttributionPagedMetadata**](RevenueAttributionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_revenue_attributions_as_csv**
> str get_revenue_attributions_as_csv(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end)

Retrieves (as CSV) all attributions of Invoice costs to Invoice lines.

{ \"nickname\" : \"(CSV) Retrieve revenue attributions\",\"response\" : \"getRevenueAttributions.csv\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
recognition_start = 'recognition_start_example' # str | The UTC DateTime specifying the start of the interval within which revenue attributions will be recognised (example input: 2015-09-13T11:50:24). (optional)
recognition_end = 'recognition_end_example' # str | The UTC DateTime specifying the end of the interval within which revenue attributions will be recognised (example input: 2015-10-13T11:50:24). (optional)

try: 
    # Retrieves (as CSV) all attributions of Invoice costs to Invoice lines.
    api_response = api_instance.get_revenue_attributions_as_csv(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->get_revenue_attributions_as_csv: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **recognition_start** | **str**| The UTC DateTime specifying the start of the interval within which revenue attributions will be recognised (example input: 2015-09-13T11:50:24). | [optional] 
 **recognition_end** | **str**| The UTC DateTime specifying the end of the interval within which revenue attributions will be recognised (example input: 2015-10-13T11:50:24). | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_swagger_for_invoice**
> SwaggerTypeListInv get_swagger_for_invoice(query_string, organizations=organizations, offset=offset, records=records, format=format, wildcard=wildcard, entity=entity)



{ \"nickname\" : \"\",\"response\" : \"\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
query_string = 'query_string_example' # str | The query string used to search.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The starting index of the search results. (optional) (default to 0)
records = 10 # int | The number of search results to return. (optional) (default to 10)
format = 'JSON' # str | The response format, either JSON or XML. (optional) (default to JSON)
wildcard = false # bool | Toggle if we search for full words or whether a wildcard is used. (optional) (default to false)
entity = false # bool | Is an entity returned with the search results. (optional) (default to false)

try: 
    # 
    api_response = api_instance.get_swagger_for_invoice(query_string, organizations=organizations, offset=offset, records=records, format=format, wildcard=wildcard, entity=entity)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->get_swagger_for_invoice: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_string** | **str**| The query string used to search. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The starting index of the search results. | [optional] [default to 0]
 **records** | **int**| The number of search results to return. | [optional] [default to 10]
 **format** | **str**| The response format, either JSON or XML. | [optional] [default to JSON]
 **wildcard** | **bool**| Toggle if we search for full words or whether a wildcard is used. | [optional] [default to false]
 **entity** | **bool**| Is an entity returned with the search results. | [optional] [default to false]

### Return type

[**SwaggerTypeListInv**](SwaggerTypeListInv.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_invoice**
> InvoicePagedMetadata import_invoice(request)

Import an invoice.

{\"nickname\":\"Import invoice\",\"response\":\"ImportInvoiceResponse.html\",\"request\":\"ImportInvoiceRequest.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
request = swagger_client.BillingEntityBase() # BillingEntityBase | 

try: 
    # Import an invoice.
    api_response = api_instance.import_invoice(request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->import_invoice: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**BillingEntityBase**](BillingEntityBase.md)|  | 

### Return type

[**InvoicePagedMetadata**](InvoicePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recalculate_invoice**
> InvoicePagedMetadata recalculate_invoice(invoice_id, request)

Re-calculate an Invoice.

{\"nickname\":\"Re-calculate an invoice\",\"response\":\"recalculateInvoiceResponse.html\",\"request\":\"RecalculateInvoiceRequest.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
invoice_id = 'invoice_id_example' # str | 
request = swagger_client.InvoiceRecalculationRequest() # InvoiceRecalculationRequest | 

try: 
    # Re-calculate an Invoice.
    api_response = api_instance.recalculate_invoice(invoice_id, request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->recalculate_invoice: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **request** | [**InvoiceRecalculationRequest**](InvoiceRecalculationRequest.md)|  | 

### Return type

[**InvoicePagedMetadata**](InvoicePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_charge_from_invoice**
> SubscriptionChargePagedMetadata remove_charge_from_invoice(invoice_id, charge_id, organizations=organizations)

Removes the specified charge from the specified Invoice.

{\"nickname\":\"Remove from invoice\",\"response\":\"deleteChargesInvoice.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
invoice_id = 'invoice_id_example' # str | 
charge_id = 'charge_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Removes the specified charge from the specified Invoice.
    api_response = api_instance.remove_charge_from_invoice(invoice_id, charge_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->remove_charge_from_invoice: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **charge_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**SubscriptionChargePagedMetadata**](SubscriptionChargePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_metadata_from_invoice**
> DynamicMetadata remove_metadata_from_invoice(invoice_id, organizations=organizations)

Remove any associated metadata.

{\"nickname\":\"Clear metadata from invoice\",\"request\" :\"deleteInvoiceMetadataRequest.html\",\"response\":\"deleteInvoiceMetadataResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
invoice_id = 'invoice_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Remove any associated metadata.
    api_response = api_instance.remove_metadata_from_invoice(invoice_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->remove_metadata_from_invoice: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**DynamicMetadata**](DynamicMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_metadata_for_invoice**
> DynamicMetadata set_metadata_for_invoice(metadata, invoice_id, organizations=organizations)

Remove any existing metadata keys and create the provided data.

{\"nickname\":\"Set metadata on invoice\",\"request\":\"setInvoiceMetadataRequest.html\",\"response\":\"setInvoiceMetadataResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
metadata = swagger_client.DynamicMetadata() # DynamicMetadata | 
invoice_id = 'invoice_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Remove any existing metadata keys and create the provided data.
    api_response = api_instance.set_metadata_for_invoice(metadata, invoice_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->set_metadata_for_invoice: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata** | [**DynamicMetadata**](DynamicMetadata.md)|  | 
 **invoice_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**DynamicMetadata**](DynamicMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invoice**
> InvoicePagedMetadata update_invoice(invoice)

Update an Invoice.

{\"nickname\":\"Update an invoice\",\"response\":\"updateInvoiceResponse.html\",\"request\":\"updateInvoiceRequest.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
invoice = swagger_client.Invoice() # Invoice | The invoice object to be updated.

try: 
    # Update an Invoice.
    api_response = api_instance.update_invoice(invoice)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->update_invoice: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice** | [**Invoice**](Invoice.md)| The invoice object to be updated. | 

### Return type

[**InvoicePagedMetadata**](InvoicePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_metadata_for_invoice**
> DynamicMetadata upsert_metadata_for_invoice(metadata, invoice_id, organizations=organizations)

Update any existing metadata key-values and insert any new key-values, no keys will be removed.

{\"nickname\":\"Upsert metadata on invoice\",\"request\":\"upsertInvoiceMetadataRequest.html\",\"response\":\"upsertInvoiceMetadataResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
metadata = swagger_client.DynamicMetadata() # DynamicMetadata | 
invoice_id = 'invoice_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Update any existing metadata key-values and insert any new key-values, no keys will be removed.
    api_response = api_instance.upsert_metadata_for_invoice(metadata, invoice_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->upsert_metadata_for_invoice: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata** | [**DynamicMetadata**](DynamicMetadata.md)|  | 
 **invoice_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**DynamicMetadata**](DynamicMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **void_invoice**
> InvoicePagedMetadata void_invoice(invoice_id, organizations)

Voids the invoice specified by the invoice identifier parameter.

{ \"nickname\" : \"Void an invoice\",\"response\" : \"voidInvoice.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
invoice_id = 'invoice_id_example' # str | ID of the invoice.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls.

try: 
    # Voids the invoice specified by the invoice identifier parameter.
    api_response = api_instance.void_invoice(invoice_id, organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling InvoicesApi->void_invoice: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**| ID of the invoice. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | 

### Return type

[**InvoicePagedMetadata**](InvoicePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

