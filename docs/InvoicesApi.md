# billforward.InvoicesApi

All URIs are relative to *https://app.billforward.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_charge_to_invoice**](InvoicesApi.md#add_charge_to_invoice) | **POST** /invoices/{invoice-ID}/charges | 
[**execute_invoice**](InvoicesApi.md#execute_invoice) | **POST** /invoices/{invoice-ID}/execute | 
[**get_all_invoices**](InvoicesApi.md#get_all_invoices) | **GET** /invoices | 
[**get_all_invoices_as_csv**](InvoicesApi.md#get_all_invoices_as_csv) | **GET** /invoices/all.csv | 
[**get_bucketed_revenue_attributions_as_csv**](InvoicesApi.md#get_bucketed_revenue_attributions_as_csv) | **GET** /invoices/bucketed-revenue-attributions.csv | 
[**get_charges_on_invoice**](InvoicesApi.md#get_charges_on_invoice) | **GET** /invoices/{invoice-ID}/charges | 
[**get_credit_invoice_line_payments_from_invoices_as_csv**](InvoicesApi.md#get_credit_invoice_line_payments_from_invoices_as_csv) | **GET** /invoices/credit.csv | 
[**get_credit_invoice_line_payments_from_invoices_as_csv_by_payment_received**](InvoicesApi.md#get_credit_invoice_line_payments_from_invoices_as_csv_by_payment_received) | **GET** /invoices/payment-received/credit.csv | 
[**get_debit_invoice_line_payments_from_invoices_as_csv**](InvoicesApi.md#get_debit_invoice_line_payments_from_invoices_as_csv) | **GET** /invoices/revenue.csv | 
[**get_debit_invoice_line_payments_from_invoices_as_csv_by_payment_received**](InvoicesApi.md#get_debit_invoice_line_payments_from_invoices_as_csv_by_payment_received) | **GET** /invoices/payment-received/revenue.csv | 
[**get_hosted_payments**](InvoicesApi.md#get_hosted_payments) | **GET** /invoices/{invoiceID}/hosted-payments | 
[**get_invoice_as_html**](InvoicesApi.md#get_invoice_as_html) | **GET** /invoices/{ID}.html | 
[**get_invoice_as_pdf**](InvoicesApi.md#get_invoice_as_pdf) | **GET** /invoices/{id}.pdf | 
[**get_invoice_by_id**](InvoicesApi.md#get_invoice_by_id) | **GET** /invoices/{invoice-ID} | 
[**get_invoice_by_id_as_csv**](InvoicesApi.md#get_invoice_by_id_as_csv) | **GET** /invoices/{ID}.csv | 
[**get_invoice_by_subscription_id**](InvoicesApi.md#get_invoice_by_subscription_id) | **GET** /invoices/subscription/{subscription-ID} | 
[**get_invoice_by_subscription_version_id**](InvoicesApi.md#get_invoice_by_subscription_version_id) | **GET** /invoices/subscription/version/{subscription-version-ID} | 
[**get_invoice_by_version_id**](InvoicesApi.md#get_invoice_by_version_id) | **GET** /invoices/version/{version-ID} | 
[**get_invoice_template**](InvoicesApi.md#get_invoice_template) | **GET** /invoices/template | 
[**get_invoices_by_account_id1**](InvoicesApi.md#get_invoices_by_account_id1) | **GET** /invoices/account/{account-ID} | 
[**get_invoices_by_period_end**](InvoicesApi.md#get_invoices_by_period_end) | **GET** /invoices/period-end/{lower-threshold}/{upper-threshold} | 
[**get_invoices_by_period_start**](InvoicesApi.md#get_invoices_by_period_start) | **GET** /invoices/period-start/{lower-threshold}/{upper-threshold} | 
[**get_invoices_by_period_start_as_csv**](InvoicesApi.md#get_invoices_by_period_start_as_csv) | **GET** /invoices/period-start/{lower-threshold}/{upper-threshold}.csv | 
[**get_invoices_by_state**](InvoicesApi.md#get_invoices_by_state) | **GET** /invoices/state/{state} | 
[**get_invoices_by_state_and_period_start**](InvoicesApi.md#get_invoices_by_state_and_period_start) | **GET** /invoices/state/{state}/period-start/{lower-threshold}/{upper-threshold} | 
[**get_invoices_by_state_and_period_start_as_csv**](InvoicesApi.md#get_invoices_by_state_and_period_start_as_csv) | **GET** /invoices/state/{state}/period-start/{lower-threshold}/{upper-threshold}.csv | 
[**get_invoices_by_state_as_csv**](InvoicesApi.md#get_invoices_by_state_as_csv) | **GET** /invoices/state/{state}.csv | 
[**get_line_payments**](InvoicesApi.md#get_line_payments) | **GET** /invoices/line-payments | 
[**get_line_payments_as_csv**](InvoicesApi.md#get_line_payments_as_csv) | **GET** /invoices/line-payments.csv | 
[**get_metadata_for_invoice**](InvoicesApi.md#get_metadata_for_invoice) | **GET** /invoices/{invoice-ID}/metadata | 
[**get_refund_for_refunded_invoice**](InvoicesApi.md#get_refund_for_refunded_invoice) | **GET** /invoices/{invoice-ID}/refunds | 
[**get_refund_invoice_line_payments_from_invoices_as_csv**](InvoicesApi.md#get_refund_invoice_line_payments_from_invoices_as_csv) | **GET** /invoices/refund.csv | 
[**get_refund_invoice_line_payments_from_invoices_as_csv_by_refund_received**](InvoicesApi.md#get_refund_invoice_line_payments_from_invoices_as_csv_by_refund_received) | **GET** /invoices/payment-received/refund.csv | 
[**get_revenue_attributions**](InvoicesApi.md#get_revenue_attributions) | **GET** /invoices/revenue-attributions | 
[**get_revenue_attributions_as_csv**](InvoicesApi.md#get_revenue_attributions_as_csv) | **GET** /invoices/revenue-attributions.csv | 
[**get_swagger_for_invoice**](InvoicesApi.md#get_swagger_for_invoice) | **GET** /invoices/swagger-end-point/{query-string} | 
[**import_invoice**](InvoicesApi.md#import_invoice) | **POST** /invoices/import | 
[**issue_invoice**](InvoicesApi.md#issue_invoice) | **PUT** /invoices/{invoice-id}/issue | 
[**list_original_invoice**](InvoicesApi.md#list_original_invoice) | **GET** /invoices/{invoice-id}/original | 
[**list_split_invoice**](InvoicesApi.md#list_split_invoice) | **GET** /invoices/{invoice-id}/split | 
[**recalculate_invoice**](InvoicesApi.md#recalculate_invoice) | **POST** /invoices/{invoice-ID}/recalculate | 
[**refund_invoice**](InvoicesApi.md#refund_invoice) | **POST** /invoices/{invoice-id}/refund | 
[**remove_charge_from_invoice**](InvoicesApi.md#remove_charge_from_invoice) | **DELETE** /invoices/{invoice-ID}/charges/{charge-ID} | 
[**remove_metadata_from_invoice**](InvoicesApi.md#remove_metadata_from_invoice) | **DELETE** /invoices/{invoice-ID}/metadata | 
[**set_metadata_for_invoice**](InvoicesApi.md#set_metadata_for_invoice) | **POST** /invoices/{invoice-ID}/metadata | 
[**split_invoice**](InvoicesApi.md#split_invoice) | **POST** /invoices/{invoice-id}/split | 
[**update_invoice**](InvoicesApi.md#update_invoice) | **PUT** /invoices | 
[**update_invoice_template**](InvoicesApi.md#update_invoice_template) | **PUT** /invoices/template | 
[**upsert_metadata_for_invoice**](InvoicesApi.md#upsert_metadata_for_invoice) | **PUT** /invoices/{invoice-ID}/metadata | 
[**void_invoice**](InvoicesApi.md#void_invoice) | **DELETE** /invoices/{invoice-ID} | 

# **add_charge_to_invoice**
> InlineResponseDefault28 add_charge_to_invoice(invoice_id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
invoice_id = 'invoice_id_example' # str | 
body = billforward.AddChargeRequest() # AddChargeRequest |  (optional)

try:
    api_response = api_instance.add_charge_to_invoice(invoice_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->add_charge_to_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **body** | [**AddChargeRequest**](AddChargeRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault28**](InlineResponseDefault28.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_invoice**
> InlineResponseDefault29 execute_invoice(invoice_id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
invoice_id = 'invoice_id_example' # str | 
body = billforward.InvoiceExecutionRequest() # InvoiceExecutionRequest |  (optional)

try:
    api_response = api_instance.execute_invoice(invoice_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->execute_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **body** | [**InvoiceExecutionRequest**](InvoiceExecutionRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault29**](InlineResponseDefault29.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_invoices**
> InlineResponseDefault8 get_all_invoices(organizations=organizations, state=state, account_id=account_id, subscription_id=subscription_id, subscription_version_id=subscription_version_id, invoice_version_id=invoice_version_id, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, exclude_children=exclude_children, metadata=metadata)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
state = ['state_example'] # list[str] |  (optional)
account_id = ['account_id_example'] # list[str] |  (optional)
subscription_id = ['subscription_id_example'] # list[str] |  (optional)
subscription_version_id = ['subscription_version_id_example'] # list[str] |  (optional)
invoice_version_id = ['invoice_version_id_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = false # bool |  (optional) (default to false)
exclude_children = true # bool |  (optional) (default to true)
metadata = 'metadata_example' # str |  (optional)

try:
    api_response = api_instance.get_all_invoices(organizations=organizations, state=state, account_id=account_id, subscription_id=subscription_id, subscription_version_id=subscription_version_id, invoice_version_id=invoice_version_id, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, exclude_children=exclude_children, metadata=metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_all_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **state** | [**list[str]**](str.md)|  | [optional] 
 **account_id** | [**list[str]**](str.md)|  | [optional] 
 **subscription_id** | [**list[str]**](str.md)|  | [optional] 
 **subscription_version_id** | [**list[str]**](str.md)|  | [optional] 
 **invoice_version_id** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to false]
 **exclude_children** | **bool**|  | [optional] [default to true]
 **metadata** | **str**|  | [optional] 

### Return type

[**InlineResponseDefault8**](InlineResponseDefault8.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_invoices_as_csv**
> get_all_invoices_as_csv(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = false # bool |  (optional) (default to false)

try:
    api_instance.get_all_invoices_as_csv(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_all_invoices_as_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bucketed_revenue_attributions_as_csv**
> get_bucketed_revenue_attributions_as_csv(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end, date_interval_inclusivity=date_interval_inclusivity, date_granularity=date_granularity, date_time_format=date_time_format, boolean_format=boolean_format, monetary_amount_format=monetary_amount_format)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
recognition_start = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
recognition_end = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
date_interval_inclusivity = 'Exclusive' # str |  (optional) (default to Exclusive)
date_granularity = 'Second' # str |  (optional) (default to Second)
date_time_format = 'UTCExcel' # str |  (optional) (default to UTCExcel)
boolean_format = 'TrueFalseLowercase' # str |  (optional) (default to TrueFalseLowercase)
monetary_amount_format = 'NoCommasPeriod2DP' # str |  (optional) (default to NoCommasPeriod2DP)

try:
    api_instance.get_bucketed_revenue_attributions_as_csv(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end, date_interval_inclusivity=date_interval_inclusivity, date_granularity=date_granularity, date_time_format=date_time_format, boolean_format=boolean_format, monetary_amount_format=monetary_amount_format)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_bucketed_revenue_attributions_as_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **recognition_start** | [**SimpleDateParam**](.md)|  | [optional] 
 **recognition_end** | [**SimpleDateParam**](.md)|  | [optional] 
 **date_interval_inclusivity** | **str**|  | [optional] [default to Exclusive]
 **date_granularity** | **str**|  | [optional] [default to Second]
 **date_time_format** | **str**|  | [optional] [default to UTCExcel]
 **boolean_format** | **str**|  | [optional] [default to TrueFalseLowercase]
 **monetary_amount_format** | **str**|  | [optional] [default to NoCommasPeriod2DP]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_charges_on_invoice**
> InlineResponseDefault10 get_charges_on_invoice(invoice_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, state=state, type=type, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
invoice_id = 'invoice_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'id' # str |  (optional) (default to id)
order = 'DESC' # str |  (optional) (default to DESC)
state = 'state_example' # str |  (optional)
type = 'type_example' # str |  (optional)
include_retired = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_charges_on_invoice(invoice_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, state=state, type=type, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_charges_on_invoice: %s\n" % e)
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
 **state** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **include_retired** | **bool**|  | [optional] [default to false]

### Return type

[**InlineResponseDefault10**](InlineResponseDefault10.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit_invoice_line_payments_from_invoices_as_csv**
> get_credit_invoice_line_payments_from_invoices_as_csv(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end, date_interval_inclusivity=date_interval_inclusivity, date_time_format=date_time_format, date_granularity=date_granularity, boolean_format=boolean_format, monetary_amount_format=monetary_amount_format)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
recognition_start = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
recognition_end = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
date_interval_inclusivity = 'Exclusive' # str |  (optional) (default to Exclusive)
date_time_format = 'UTCExcel' # str |  (optional) (default to UTCExcel)
date_granularity = 'Second' # str |  (optional) (default to Second)
boolean_format = 'TrueFalseLowercase' # str |  (optional) (default to TrueFalseLowercase)
monetary_amount_format = 'NoCommasPeriod2DP' # str |  (optional) (default to NoCommasPeriod2DP)

try:
    api_instance.get_credit_invoice_line_payments_from_invoices_as_csv(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end, date_interval_inclusivity=date_interval_inclusivity, date_time_format=date_time_format, date_granularity=date_granularity, boolean_format=boolean_format, monetary_amount_format=monetary_amount_format)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_credit_invoice_line_payments_from_invoices_as_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **recognition_start** | [**SimpleDateParam**](.md)|  | [optional] 
 **recognition_end** | [**SimpleDateParam**](.md)|  | [optional] 
 **date_interval_inclusivity** | **str**|  | [optional] [default to Exclusive]
 **date_time_format** | **str**|  | [optional] [default to UTCExcel]
 **date_granularity** | **str**|  | [optional] [default to Second]
 **boolean_format** | **str**|  | [optional] [default to TrueFalseLowercase]
 **monetary_amount_format** | **str**|  | [optional] [default to NoCommasPeriod2DP]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit_invoice_line_payments_from_invoices_as_csv_by_payment_received**
> get_credit_invoice_line_payments_from_invoices_as_csv_by_payment_received(organizations=organizations, start=start, end=end, date_interval_inclusivity=date_interval_inclusivity, date_time_format=date_time_format, date_granularity=date_granularity, boolean_format=boolean_format, monetary_amount_format=monetary_amount_format)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
start = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
end = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
date_interval_inclusivity = 'Exclusive' # str |  (optional) (default to Exclusive)
date_time_format = 'UTCExcel' # str |  (optional) (default to UTCExcel)
date_granularity = 'Second' # str |  (optional) (default to Second)
boolean_format = 'TrueFalseLowercase' # str |  (optional) (default to TrueFalseLowercase)
monetary_amount_format = 'NoCommasPeriod2DP' # str |  (optional) (default to NoCommasPeriod2DP)

try:
    api_instance.get_credit_invoice_line_payments_from_invoices_as_csv_by_payment_received(organizations=organizations, start=start, end=end, date_interval_inclusivity=date_interval_inclusivity, date_time_format=date_time_format, date_granularity=date_granularity, boolean_format=boolean_format, monetary_amount_format=monetary_amount_format)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_credit_invoice_line_payments_from_invoices_as_csv_by_payment_received: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **start** | [**SimpleDateParam**](.md)|  | [optional] 
 **end** | [**SimpleDateParam**](.md)|  | [optional] 
 **date_interval_inclusivity** | **str**|  | [optional] [default to Exclusive]
 **date_time_format** | **str**|  | [optional] [default to UTCExcel]
 **date_granularity** | **str**|  | [optional] [default to Second]
 **boolean_format** | **str**|  | [optional] [default to TrueFalseLowercase]
 **monetary_amount_format** | **str**|  | [optional] [default to NoCommasPeriod2DP]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debit_invoice_line_payments_from_invoices_as_csv**
> get_debit_invoice_line_payments_from_invoices_as_csv(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end, date_interval_inclusivity=date_interval_inclusivity, date_time_format=date_time_format, date_granularity=date_granularity, boolean_format=boolean_format, monetary_amount_format=monetary_amount_format)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
recognition_start = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
recognition_end = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
date_interval_inclusivity = 'Exclusive' # str |  (optional) (default to Exclusive)
date_time_format = 'UTCExcel' # str |  (optional) (default to UTCExcel)
date_granularity = 'Second' # str |  (optional) (default to Second)
boolean_format = 'TrueFalseLowercase' # str |  (optional) (default to TrueFalseLowercase)
monetary_amount_format = 'NoCommasPeriod2DP' # str |  (optional) (default to NoCommasPeriod2DP)

try:
    api_instance.get_debit_invoice_line_payments_from_invoices_as_csv(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end, date_interval_inclusivity=date_interval_inclusivity, date_time_format=date_time_format, date_granularity=date_granularity, boolean_format=boolean_format, monetary_amount_format=monetary_amount_format)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_debit_invoice_line_payments_from_invoices_as_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **recognition_start** | [**SimpleDateParam**](.md)|  | [optional] 
 **recognition_end** | [**SimpleDateParam**](.md)|  | [optional] 
 **date_interval_inclusivity** | **str**|  | [optional] [default to Exclusive]
 **date_time_format** | **str**|  | [optional] [default to UTCExcel]
 **date_granularity** | **str**|  | [optional] [default to Second]
 **boolean_format** | **str**|  | [optional] [default to TrueFalseLowercase]
 **monetary_amount_format** | **str**|  | [optional] [default to NoCommasPeriod2DP]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debit_invoice_line_payments_from_invoices_as_csv_by_payment_received**
> get_debit_invoice_line_payments_from_invoices_as_csv_by_payment_received(organizations=organizations, start=start, end=end, date_interval_inclusivity=date_interval_inclusivity, date_time_format=date_time_format, date_granularity=date_granularity, boolean_format=boolean_format, monetary_amount_format=monetary_amount_format)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
start = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
end = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
date_interval_inclusivity = 'Exclusive' # str |  (optional) (default to Exclusive)
date_time_format = 'UTCExcel' # str |  (optional) (default to UTCExcel)
date_granularity = 'Second' # str |  (optional) (default to Second)
boolean_format = 'TrueFalseLowercase' # str |  (optional) (default to TrueFalseLowercase)
monetary_amount_format = 'NoCommasPeriod2DP' # str |  (optional) (default to NoCommasPeriod2DP)

try:
    api_instance.get_debit_invoice_line_payments_from_invoices_as_csv_by_payment_received(organizations=organizations, start=start, end=end, date_interval_inclusivity=date_interval_inclusivity, date_time_format=date_time_format, date_granularity=date_granularity, boolean_format=boolean_format, monetary_amount_format=monetary_amount_format)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_debit_invoice_line_payments_from_invoices_as_csv_by_payment_received: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **start** | [**SimpleDateParam**](.md)|  | [optional] 
 **end** | [**SimpleDateParam**](.md)|  | [optional] 
 **date_interval_inclusivity** | **str**|  | [optional] [default to Exclusive]
 **date_time_format** | **str**|  | [optional] [default to UTCExcel]
 **date_granularity** | **str**|  | [optional] [default to Second]
 **boolean_format** | **str**|  | [optional] [default to TrueFalseLowercase]
 **monetary_amount_format** | **str**|  | [optional] [default to NoCommasPeriod2DP]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hosted_payments**
> list[HostedPayment] get_hosted_payments(invoice_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
invoice_id = 'invoice_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_hosted_payments(invoice_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_hosted_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**list[HostedPayment]**](HostedPayment.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_as_html**
> get_invoice_as_html(id, organizations=organizations, tier_breakdown=tier_breakdown, inclusive_end=inclusive_end, show_zero_cost=show_zero_cost, show_plan_only_when_ambiguous=show_plan_only_when_ambiguous, include_footer=include_footer, header_display=header_display, group_line_items_by=group_line_items_by, hide_tax_if_zero=hide_tax_if_zero, show_unit_price=show_unit_price, representing_account_id=representing_account_id, company_address_on_top=company_address_on_top, upgrade_duration_wording=upgrade_duration_wording, refresh_cache=refresh_cache)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
id = 'id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
tier_breakdown = true # bool |  (optional)
inclusive_end = true # bool |  (optional)
show_zero_cost = true # bool |  (optional)
show_plan_only_when_ambiguous = true # bool |  (optional)
include_footer = true # bool |  (optional)
header_display = 'header_display_example' # str |  (optional)
group_line_items_by = 'group_line_items_by_example' # str |  (optional)
hide_tax_if_zero = true # bool |  (optional)
show_unit_price = 'show_unit_price_example' # str |  (optional)
representing_account_id = 'representing_account_id_example' # str |  (optional)
company_address_on_top = true # bool |  (optional)
upgrade_duration_wording = true # bool |  (optional)
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_instance.get_invoice_as_html(id, organizations=organizations, tier_breakdown=tier_breakdown, inclusive_end=inclusive_end, show_zero_cost=show_zero_cost, show_plan_only_when_ambiguous=show_plan_only_when_ambiguous, include_footer=include_footer, header_display=header_display, group_line_items_by=group_line_items_by, hide_tax_if_zero=hide_tax_if_zero, show_unit_price=show_unit_price, representing_account_id=representing_account_id, company_address_on_top=company_address_on_top, upgrade_duration_wording=upgrade_duration_wording, refresh_cache=refresh_cache)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoice_as_html: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **tier_breakdown** | **bool**|  | [optional] 
 **inclusive_end** | **bool**|  | [optional] 
 **show_zero_cost** | **bool**|  | [optional] 
 **show_plan_only_when_ambiguous** | **bool**|  | [optional] 
 **include_footer** | **bool**|  | [optional] 
 **header_display** | **str**|  | [optional] 
 **group_line_items_by** | **str**|  | [optional] 
 **hide_tax_if_zero** | **bool**|  | [optional] 
 **show_unit_price** | **str**|  | [optional] 
 **representing_account_id** | **str**|  | [optional] 
 **company_address_on_top** | **bool**|  | [optional] 
 **upgrade_duration_wording** | **bool**|  | [optional] 
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_as_pdf**
> get_invoice_as_pdf(id, organizations=organizations, offset=offset, order_by=order_by, order=order, include_retired=include_retired, tier_breakdown=tier_breakdown, inclusive_end=inclusive_end, show_zero_cost=show_zero_cost, show_plan_only_when_ambiguous=show_plan_only_when_ambiguous, include_footer=include_footer, header_display=header_display, group_line_items_by=group_line_items_by, hide_tax_if_zero=hide_tax_if_zero, show_unit_price=show_unit_price, representing_account_id=representing_account_id, company_address_on_top=company_address_on_top, upgrade_duration_wording=upgrade_duration_wording, refresh_cache=refresh_cache)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
id = 'id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = false # bool |  (optional) (default to false)
tier_breakdown = true # bool |  (optional)
inclusive_end = true # bool |  (optional)
show_zero_cost = true # bool |  (optional)
show_plan_only_when_ambiguous = true # bool |  (optional)
include_footer = true # bool |  (optional)
header_display = 'header_display_example' # str |  (optional)
group_line_items_by = 'group_line_items_by_example' # str |  (optional)
hide_tax_if_zero = true # bool |  (optional)
show_unit_price = 'show_unit_price_example' # str |  (optional)
representing_account_id = 'representing_account_id_example' # str |  (optional)
company_address_on_top = true # bool |  (optional)
upgrade_duration_wording = true # bool |  (optional)
refresh_cache = false # bool |  (optional) (default to false)

try:
    api_instance.get_invoice_as_pdf(id, organizations=organizations, offset=offset, order_by=order_by, order=order, include_retired=include_retired, tier_breakdown=tier_breakdown, inclusive_end=inclusive_end, show_zero_cost=show_zero_cost, show_plan_only_when_ambiguous=show_plan_only_when_ambiguous, include_footer=include_footer, header_display=header_display, group_line_items_by=group_line_items_by, hide_tax_if_zero=hide_tax_if_zero, show_unit_price=show_unit_price, representing_account_id=representing_account_id, company_address_on_top=company_address_on_top, upgrade_duration_wording=upgrade_duration_wording, refresh_cache=refresh_cache)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoice_as_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to false]
 **tier_breakdown** | **bool**|  | [optional] 
 **inclusive_end** | **bool**|  | [optional] 
 **show_zero_cost** | **bool**|  | [optional] 
 **show_plan_only_when_ambiguous** | **bool**|  | [optional] 
 **include_footer** | **bool**|  | [optional] 
 **header_display** | **str**|  | [optional] 
 **group_line_items_by** | **str**|  | [optional] 
 **hide_tax_if_zero** | **bool**|  | [optional] 
 **show_unit_price** | **str**|  | [optional] 
 **representing_account_id** | **str**|  | [optional] 
 **company_address_on_top** | **bool**|  | [optional] 
 **upgrade_duration_wording** | **bool**|  | [optional] 
 **refresh_cache** | **bool**|  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_by_id**
> InlineResponseDefault8 get_invoice_by_id(invoice_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
invoice_id = 'invoice_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_invoice_by_id(invoice_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoice_by_id: %s\n" % e)
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
 **include_retired** | **bool**|  | [optional] [default to false]

### Return type

[**InlineResponseDefault8**](InlineResponseDefault8.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_by_id_as_csv**
> get_invoice_by_id_as_csv(id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
id = 'id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_instance.get_invoice_by_id_as_csv(id, organizations=organizations)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoice_by_id_as_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_by_subscription_id**
> InlineResponseDefault8 get_invoice_by_subscription_id(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_invoice_by_subscription_id(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoice_by_subscription_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to false]

### Return type

[**InlineResponseDefault8**](InlineResponseDefault8.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_by_subscription_version_id**
> InlineResponseDefault8 get_invoice_by_subscription_version_id(subscription_version_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
subscription_version_id = 'subscription_version_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_invoice_by_subscription_version_id(subscription_version_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoice_by_subscription_version_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_version_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to false]

### Return type

[**InlineResponseDefault8**](InlineResponseDefault8.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_by_version_id**
> InlineResponseDefault29 get_invoice_by_version_id(version_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
version_id = 'version_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_invoice_by_version_id(version_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoice_by_version_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault29**](InlineResponseDefault29.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_template**
> InlineResponseDefault30 get_invoice_template(organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_invoice_template(organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoice_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault30**](InlineResponseDefault30.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices_by_account_id1**
> InlineResponseDefault8 get_invoices_by_account_id1(account_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, exclude_children=exclude_children)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
account_id = 'account_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = false # bool |  (optional) (default to false)
exclude_children = true # bool |  (optional) (default to true)

try:
    api_response = api_instance.get_invoices_by_account_id1(account_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, exclude_children=exclude_children)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoices_by_account_id1: %s\n" % e)
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

# **get_invoices_by_period_end**
> InlineResponseDefault8 get_invoices_by_period_end(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
lower_threshold = billforward.SimpleDateParam() # SimpleDateParam | 
upper_threshold = billforward.SimpleDateParam() # SimpleDateParam | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_invoices_by_period_end(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoices_by_period_end: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lower_threshold** | [**SimpleDateParam**](.md)|  | 
 **upper_threshold** | [**SimpleDateParam**](.md)|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to false]

### Return type

[**InlineResponseDefault8**](InlineResponseDefault8.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices_by_period_start**
> InlineResponseDefault8 get_invoices_by_period_start(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
lower_threshold = billforward.SimpleDateParam() # SimpleDateParam | 
upper_threshold = billforward.SimpleDateParam() # SimpleDateParam | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_invoices_by_period_start(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoices_by_period_start: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lower_threshold** | [**SimpleDateParam**](.md)|  | 
 **upper_threshold** | [**SimpleDateParam**](.md)|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to false]

### Return type

[**InlineResponseDefault8**](InlineResponseDefault8.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices_by_period_start_as_csv**
> get_invoices_by_period_start_as_csv(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
lower_threshold = billforward.SimpleDateParam() # SimpleDateParam | 
upper_threshold = billforward.SimpleDateParam() # SimpleDateParam | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = false # bool |  (optional) (default to false)

try:
    api_instance.get_invoices_by_period_start_as_csv(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoices_by_period_start_as_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lower_threshold** | [**SimpleDateParam**](.md)|  | 
 **upper_threshold** | [**SimpleDateParam**](.md)|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices_by_state**
> InlineResponseDefault8 get_invoices_by_state(state, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
state = 'state_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'id' # str |  (optional) (default to id)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_invoices_by_state(state, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoices_by_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to id]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to false]

### Return type

[**InlineResponseDefault8**](InlineResponseDefault8.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices_by_state_and_period_start**
> InlineResponseDefault8 get_invoices_by_state_and_period_start(state, lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
state = 'state_example' # str | 
lower_threshold = billforward.SimpleDateParam() # SimpleDateParam | 
upper_threshold = billforward.SimpleDateParam() # SimpleDateParam | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_invoices_by_state_and_period_start(state, lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoices_by_state_and_period_start: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**|  | 
 **lower_threshold** | [**SimpleDateParam**](.md)|  | 
 **upper_threshold** | [**SimpleDateParam**](.md)|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to false]

### Return type

[**InlineResponseDefault8**](InlineResponseDefault8.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices_by_state_and_period_start_as_csv**
> get_invoices_by_state_and_period_start_as_csv(state, lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
state = 'state_example' # str | 
lower_threshold = billforward.SimpleDateParam() # SimpleDateParam | 
upper_threshold = billforward.SimpleDateParam() # SimpleDateParam | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = false # bool |  (optional) (default to false)

try:
    api_instance.get_invoices_by_state_and_period_start_as_csv(state, lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoices_by_state_and_period_start_as_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**|  | 
 **lower_threshold** | [**SimpleDateParam**](.md)|  | 
 **upper_threshold** | [**SimpleDateParam**](.md)|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices_by_state_as_csv**
> get_invoices_by_state_as_csv(state, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
state = 'state_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'id' # str |  (optional) (default to id)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = false # bool |  (optional) (default to false)

try:
    api_instance.get_invoices_by_state_as_csv(state, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoices_by_state_as_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to id]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_line_payments**
> InlineResponseDefault31 get_line_payments(organizations=organizations, payment_direction=payment_direction, date_discriminator=date_discriminator, recognition_start=recognition_start, recognition_end=recognition_end, include_gateway=include_gateway, exclude_gateway=exclude_gateway)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
payment_direction = 'All' # str |  (optional) (default to All)
date_discriminator = 'PeriodStart' # str |  (optional) (default to PeriodStart)
recognition_start = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
recognition_end = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
include_gateway = ['include_gateway_example'] # list[str] |  (optional)
exclude_gateway = ['exclude_gateway_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_line_payments(organizations=organizations, payment_direction=payment_direction, date_discriminator=date_discriminator, recognition_start=recognition_start, recognition_end=recognition_end, include_gateway=include_gateway, exclude_gateway=exclude_gateway)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_line_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **payment_direction** | **str**|  | [optional] [default to All]
 **date_discriminator** | **str**|  | [optional] [default to PeriodStart]
 **recognition_start** | [**SimpleDateParam**](.md)|  | [optional] 
 **recognition_end** | [**SimpleDateParam**](.md)|  | [optional] 
 **include_gateway** | [**list[str]**](str.md)|  | [optional] 
 **exclude_gateway** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault31**](InlineResponseDefault31.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_line_payments_as_csv**
> get_line_payments_as_csv(organizations=organizations, payment_direction=payment_direction, date_discriminator=date_discriminator, recognition_start=recognition_start, recognition_end=recognition_end, include_gateway=include_gateway, exclude_gateway=exclude_gateway, date_interval_inclusivity=date_interval_inclusivity, date_time_format=date_time_format, date_granularity=date_granularity, boolean_format=boolean_format, monetary_amount_format=monetary_amount_format)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
payment_direction = 'All' # str |  (optional) (default to All)
date_discriminator = 'PeriodStart' # str |  (optional) (default to PeriodStart)
recognition_start = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
recognition_end = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
include_gateway = ['include_gateway_example'] # list[str] |  (optional)
exclude_gateway = ['exclude_gateway_example'] # list[str] |  (optional)
date_interval_inclusivity = 'Exclusive' # str |  (optional) (default to Exclusive)
date_time_format = 'UTCExcel' # str |  (optional) (default to UTCExcel)
date_granularity = 'Second' # str |  (optional) (default to Second)
boolean_format = 'TrueFalseLowercase' # str |  (optional) (default to TrueFalseLowercase)
monetary_amount_format = 'NoCommasPeriod2DP' # str |  (optional) (default to NoCommasPeriod2DP)

try:
    api_instance.get_line_payments_as_csv(organizations=organizations, payment_direction=payment_direction, date_discriminator=date_discriminator, recognition_start=recognition_start, recognition_end=recognition_end, include_gateway=include_gateway, exclude_gateway=exclude_gateway, date_interval_inclusivity=date_interval_inclusivity, date_time_format=date_time_format, date_granularity=date_granularity, boolean_format=boolean_format, monetary_amount_format=monetary_amount_format)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_line_payments_as_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **payment_direction** | **str**|  | [optional] [default to All]
 **date_discriminator** | **str**|  | [optional] [default to PeriodStart]
 **recognition_start** | [**SimpleDateParam**](.md)|  | [optional] 
 **recognition_end** | [**SimpleDateParam**](.md)|  | [optional] 
 **include_gateway** | [**list[str]**](str.md)|  | [optional] 
 **exclude_gateway** | [**list[str]**](str.md)|  | [optional] 
 **date_interval_inclusivity** | **str**|  | [optional] [default to Exclusive]
 **date_time_format** | **str**|  | [optional] [default to UTCExcel]
 **date_granularity** | **str**|  | [optional] [default to Second]
 **boolean_format** | **str**|  | [optional] [default to TrueFalseLowercase]
 **monetary_amount_format** | **str**|  | [optional] [default to NoCommasPeriod2DP]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_for_invoice**
> InlineResponseDefault7 get_metadata_for_invoice(invoice_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
invoice_id = 'invoice_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_metadata_for_invoice(invoice_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_metadata_for_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault7**](InlineResponseDefault7.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_refund_for_refunded_invoice**
> InlineResponseDefault32 get_refund_for_refunded_invoice(invoice_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
invoice_id = 'invoice_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_refund_for_refunded_invoice(invoice_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_refund_for_refunded_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault32**](InlineResponseDefault32.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_refund_invoice_line_payments_from_invoices_as_csv**
> get_refund_invoice_line_payments_from_invoices_as_csv(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end, date_interval_inclusivity=date_interval_inclusivity, date_time_format=date_time_format, date_granularity=date_granularity, boolean_format=boolean_format, monetary_amount_format=monetary_amount_format)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
recognition_start = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
recognition_end = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
date_interval_inclusivity = 'Exclusive' # str |  (optional) (default to Exclusive)
date_time_format = 'UTCExcel' # str |  (optional) (default to UTCExcel)
date_granularity = 'Second' # str |  (optional) (default to Second)
boolean_format = 'TrueFalseLowercase' # str |  (optional) (default to TrueFalseLowercase)
monetary_amount_format = 'NoCommasPeriod2DP' # str |  (optional) (default to NoCommasPeriod2DP)

try:
    api_instance.get_refund_invoice_line_payments_from_invoices_as_csv(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end, date_interval_inclusivity=date_interval_inclusivity, date_time_format=date_time_format, date_granularity=date_granularity, boolean_format=boolean_format, monetary_amount_format=monetary_amount_format)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_refund_invoice_line_payments_from_invoices_as_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **recognition_start** | [**SimpleDateParam**](.md)|  | [optional] 
 **recognition_end** | [**SimpleDateParam**](.md)|  | [optional] 
 **date_interval_inclusivity** | **str**|  | [optional] [default to Exclusive]
 **date_time_format** | **str**|  | [optional] [default to UTCExcel]
 **date_granularity** | **str**|  | [optional] [default to Second]
 **boolean_format** | **str**|  | [optional] [default to TrueFalseLowercase]
 **monetary_amount_format** | **str**|  | [optional] [default to NoCommasPeriod2DP]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_refund_invoice_line_payments_from_invoices_as_csv_by_refund_received**
> get_refund_invoice_line_payments_from_invoices_as_csv_by_refund_received(organizations=organizations, start=start, end=end, date_interval_inclusivity=date_interval_inclusivity, date_time_format=date_time_format, date_granularity=date_granularity, boolean_format=boolean_format, monetary_amount_format=monetary_amount_format)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
start = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
end = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
date_interval_inclusivity = 'Exclusive' # str |  (optional) (default to Exclusive)
date_time_format = 'UTCExcel' # str |  (optional) (default to UTCExcel)
date_granularity = 'Second' # str |  (optional) (default to Second)
boolean_format = 'TrueFalseLowercase' # str |  (optional) (default to TrueFalseLowercase)
monetary_amount_format = 'NoCommasPeriod2DP' # str |  (optional) (default to NoCommasPeriod2DP)

try:
    api_instance.get_refund_invoice_line_payments_from_invoices_as_csv_by_refund_received(organizations=organizations, start=start, end=end, date_interval_inclusivity=date_interval_inclusivity, date_time_format=date_time_format, date_granularity=date_granularity, boolean_format=boolean_format, monetary_amount_format=monetary_amount_format)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_refund_invoice_line_payments_from_invoices_as_csv_by_refund_received: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **start** | [**SimpleDateParam**](.md)|  | [optional] 
 **end** | [**SimpleDateParam**](.md)|  | [optional] 
 **date_interval_inclusivity** | **str**|  | [optional] [default to Exclusive]
 **date_time_format** | **str**|  | [optional] [default to UTCExcel]
 **date_granularity** | **str**|  | [optional] [default to Second]
 **boolean_format** | **str**|  | [optional] [default to TrueFalseLowercase]
 **monetary_amount_format** | **str**|  | [optional] [default to NoCommasPeriod2DP]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_revenue_attributions**
> InlineResponseDefault33 get_revenue_attributions(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
recognition_start = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
recognition_end = billforward.SimpleDateParam() # SimpleDateParam |  (optional)

try:
    api_response = api_instance.get_revenue_attributions(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_revenue_attributions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **recognition_start** | [**SimpleDateParam**](.md)|  | [optional] 
 **recognition_end** | [**SimpleDateParam**](.md)|  | [optional] 

### Return type

[**InlineResponseDefault33**](InlineResponseDefault33.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_revenue_attributions_as_csv**
> get_revenue_attributions_as_csv(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end, date_interval_inclusivity=date_interval_inclusivity, date_granularity=date_granularity, date_time_format=date_time_format, boolean_format=boolean_format, monetary_amount_format=monetary_amount_format)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
recognition_start = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
recognition_end = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
date_interval_inclusivity = 'Exclusive' # str |  (optional) (default to Exclusive)
date_granularity = 'Second' # str |  (optional) (default to Second)
date_time_format = 'UTCExcel' # str |  (optional) (default to UTCExcel)
boolean_format = 'TrueFalseLowercase' # str |  (optional) (default to TrueFalseLowercase)
monetary_amount_format = 'NoCommasPeriod2DP' # str |  (optional) (default to NoCommasPeriod2DP)

try:
    api_instance.get_revenue_attributions_as_csv(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end, date_interval_inclusivity=date_interval_inclusivity, date_granularity=date_granularity, date_time_format=date_time_format, boolean_format=boolean_format, monetary_amount_format=monetary_amount_format)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_revenue_attributions_as_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **recognition_start** | [**SimpleDateParam**](.md)|  | [optional] 
 **recognition_end** | [**SimpleDateParam**](.md)|  | [optional] 
 **date_interval_inclusivity** | **str**|  | [optional] [default to Exclusive]
 **date_granularity** | **str**|  | [optional] [default to Second]
 **date_time_format** | **str**|  | [optional] [default to UTCExcel]
 **boolean_format** | **str**|  | [optional] [default to TrueFalseLowercase]
 **monetary_amount_format** | **str**|  | [optional] [default to NoCommasPeriod2DP]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_swagger_for_invoice**
> InlineResponseDefault34 get_swagger_for_invoice(query_string, organizations=organizations, offset=offset, records=records, format=format, wildcard=wildcard, entity=entity)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
query_string = 'query_string_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
format = 'JSON' # str |  (optional) (default to JSON)
wildcard = true # bool |  (optional) (default to true)
entity = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_swagger_for_invoice(query_string, organizations=organizations, offset=offset, records=records, format=format, wildcard=wildcard, entity=entity)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_swagger_for_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_string** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **format** | **str**|  | [optional] [default to JSON]
 **wildcard** | **bool**|  | [optional] [default to true]
 **entity** | **bool**|  | [optional] [default to false]

### Return type

[**InlineResponseDefault34**](InlineResponseDefault34.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_invoice**
> InlineResponseDefault29 import_invoice(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
body = billforward.ImportInvoiceRequest() # ImportInvoiceRequest |  (optional)

try:
    api_response = api_instance.import_invoice(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->import_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImportInvoiceRequest**](ImportInvoiceRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault29**](InlineResponseDefault29.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_invoice**
> InlineResponseDefault35 issue_invoice(invoice_id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
invoice_id = 'invoice_id_example' # str | 
body = billforward.IssueInvoiceRequest() # IssueInvoiceRequest |  (optional)

try:
    api_response = api_instance.issue_invoice(invoice_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->issue_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **body** | [**IssueInvoiceRequest**](IssueInvoiceRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault35**](InlineResponseDefault35.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_original_invoice**
> InlineResponseDefault8 list_original_invoice(invoice_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
invoice_id = 'invoice_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.list_original_invoice(invoice_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->list_original_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault8**](InlineResponseDefault8.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_split_invoice**
> InlineResponseDefault8 list_split_invoice(invoice_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
invoice_id = 'invoice_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.list_split_invoice(invoice_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->list_split_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault8**](InlineResponseDefault8.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recalculate_invoice**
> InlineResponseDefault29 recalculate_invoice(invoice_id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
invoice_id = 'invoice_id_example' # str | 
body = billforward.InvoiceRecalculationRequest() # InvoiceRecalculationRequest |  (optional)

try:
    api_response = api_instance.recalculate_invoice(invoice_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->recalculate_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **body** | [**InvoiceRecalculationRequest**](InvoiceRecalculationRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault29**](InlineResponseDefault29.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_invoice**
> InlineResponseDefault36 refund_invoice(invoice_id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
invoice_id = 'invoice_id_example' # str | 
body = billforward.InvoiceRefundRequest() # InvoiceRefundRequest |  (optional)

try:
    api_response = api_instance.refund_invoice(invoice_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->refund_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **body** | [**InvoiceRefundRequest**](InvoiceRefundRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault36**](InlineResponseDefault36.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_charge_from_invoice**
> InlineResponseDefault10 remove_charge_from_invoice(invoice_id, charge_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
invoice_id = 'invoice_id_example' # str | 
charge_id = 'charge_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.remove_charge_from_invoice(invoice_id, charge_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->remove_charge_from_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **charge_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault10**](InlineResponseDefault10.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_metadata_from_invoice**
> InlineResponseDefault7 remove_metadata_from_invoice(invoice_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
invoice_id = 'invoice_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.remove_metadata_from_invoice(invoice_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->remove_metadata_from_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault7**](InlineResponseDefault7.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_metadata_for_invoice**
> InlineResponseDefault7 set_metadata_for_invoice(invoice_id, body=body, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
invoice_id = 'invoice_id_example' # str | 
body = 'body_example' # str |  (optional)
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.set_metadata_for_invoice(invoice_id, body=body, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->set_metadata_for_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
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

# **split_invoice**
> InlineResponseDefault8 split_invoice(invoice_id, body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
invoice_id = 'invoice_id_example' # str | 
body = billforward.InvoiceSplitServiceRequest() # InvoiceSplitServiceRequest |  (optional)

try:
    api_response = api_instance.split_invoice(invoice_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->split_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **body** | [**InvoiceSplitServiceRequest**](InvoiceSplitServiceRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault8**](InlineResponseDefault8.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invoice**
> InlineResponseDefault8 update_invoice(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
body = billforward.UpdateInvoiceRequest() # UpdateInvoiceRequest |  (optional)

try:
    api_response = api_instance.update_invoice(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->update_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateInvoiceRequest**](UpdateInvoiceRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault8**](InlineResponseDefault8.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invoice_template**
> InlineResponseDefault30 update_invoice_template(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
body = billforward.UpdateInvoiceTemplateRequest() # UpdateInvoiceTemplateRequest |  (optional)

try:
    api_response = api_instance.update_invoice_template(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->update_invoice_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateInvoiceTemplateRequest**](UpdateInvoiceTemplateRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault30**](InlineResponseDefault30.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_metadata_for_invoice**
> InlineResponseDefault7 upsert_metadata_for_invoice(invoice_id, body=body, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
invoice_id = 'invoice_id_example' # str | 
body = 'body_example' # str |  (optional)
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.upsert_metadata_for_invoice(invoice_id, body=body, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->upsert_metadata_for_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
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

# **void_invoice**
> InlineResponseDefault29 void_invoice(invoice_id, organizations=organizations, void_charges=void_charges)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.InvoicesApi(billforward.ApiClient(configuration))
invoice_id = 'invoice_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
void_charges = true # bool |  (optional) (default to true)

try:
    api_response = api_instance.void_invoice(invoice_id, organizations=organizations, void_charges=void_charges)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->void_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **void_charges** | **bool**|  | [optional] [default to true]

### Return type

[**InlineResponseDefault29**](InlineResponseDefault29.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

