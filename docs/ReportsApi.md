# billforward.ReportsApi

All URIs are relative to *https://app.billforward.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_accounts_overview**](ReportsApi.md#get_accounts_overview) | **GET** /reports/accounts/overview.csv | 
[**get_affiliate_charge_report**](ReportsApi.md#get_affiliate_charge_report) | **GET** /reports/affiliate/overview.csv | 
[**get_coupon_report**](ReportsApi.md#get_coupon_report) | **GET** /reports/coupons/overview.csv | 
[**get_csv_report_invoice_line_payments_bucketed**](ReportsApi.md#get_csv_report_invoice_line_payments_bucketed) | **GET** /reports/fulfilled/bucketed.csv | 
[**get_csv_report_invoice_line_payments_raw**](ReportsApi.md#get_csv_report_invoice_line_payments_raw) | **GET** /reports/fulfilled/raw.csv | 
[**get_csv_report_revenue_attributions_bucketed**](ReportsApi.md#get_csv_report_revenue_attributions_bucketed) | **GET** /reports/invoiced/bucketed.csv | 
[**get_csv_report_revenue_attributions_raw**](ReportsApi.md#get_csv_report_revenue_attributions_raw) | **GET** /reports/invoiced/raw.csv | 
[**get_csv_revenue_schedule**](ReportsApi.md#get_csv_revenue_schedule) | **GET** /reports/revenue-schedule/raw.csv | 
[**get_payment_transactions**](ReportsApi.md#get_payment_transactions) | **GET** /reports/transactions/payments.csv | 
[**get_refunds_as_csv**](ReportsApi.md#get_refunds_as_csv) | **GET** /refunds/csv | 
[**get_shipments_report**](ReportsApi.md#get_shipments_report) | **GET** /reports/shipments/overview.csv | 
[**get_subscriptions_overview**](ReportsApi.md#get_subscriptions_overview) | **GET** /reports/subscriptions/overview.csv | 

# **get_accounts_overview**
> get_accounts_overview(organizations=organizations, date_discriminator=date_discriminator, recognition_start=recognition_start, recognition_end=recognition_end, date_interval_inclusivity=date_interval_inclusivity, date_time_format=date_time_format, date_granularity=date_granularity, boolean_format=boolean_format, monetary_amount_format=monetary_amount_format, meta_column_account=meta_column_account)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.ReportsApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
date_discriminator = 'AccountCreated' # str |  (optional) (default to AccountCreated)
recognition_start = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
recognition_end = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
date_interval_inclusivity = 'Exclusive' # str |  (optional) (default to Exclusive)
date_time_format = 'UTCExcel' # str |  (optional) (default to UTCExcel)
date_granularity = 'Second' # str |  (optional) (default to Second)
boolean_format = 'TrueFalseLowercase' # str |  (optional) (default to TrueFalseLowercase)
monetary_amount_format = 'NoCommasPeriod2DP' # str |  (optional) (default to NoCommasPeriod2DP)
meta_column_account = ['meta_column_account_example'] # list[str] |  (optional)

try:
    api_instance.get_accounts_overview(organizations=organizations, date_discriminator=date_discriminator, recognition_start=recognition_start, recognition_end=recognition_end, date_interval_inclusivity=date_interval_inclusivity, date_time_format=date_time_format, date_granularity=date_granularity, boolean_format=boolean_format, monetary_amount_format=monetary_amount_format, meta_column_account=meta_column_account)
except ApiException as e:
    print("Exception when calling ReportsApi->get_accounts_overview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **date_discriminator** | **str**|  | [optional] [default to AccountCreated]
 **recognition_start** | [**SimpleDateParam**](.md)|  | [optional] 
 **recognition_end** | [**SimpleDateParam**](.md)|  | [optional] 
 **date_interval_inclusivity** | **str**|  | [optional] [default to Exclusive]
 **date_time_format** | **str**|  | [optional] [default to UTCExcel]
 **date_granularity** | **str**|  | [optional] [default to Second]
 **boolean_format** | **str**|  | [optional] [default to TrueFalseLowercase]
 **monetary_amount_format** | **str**|  | [optional] [default to NoCommasPeriod2DP]
 **meta_column_account** | [**list[str]**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_affiliate_charge_report**
> get_affiliate_charge_report(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.ReportsApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
recognition_start = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
recognition_end = billforward.SimpleDateParam() # SimpleDateParam |  (optional)

try:
    api_instance.get_affiliate_charge_report(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end)
except ApiException as e:
    print("Exception when calling ReportsApi->get_affiliate_charge_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **recognition_start** | [**SimpleDateParam**](.md)|  | [optional] 
 **recognition_end** | [**SimpleDateParam**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupon_report**
> get_coupon_report(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.ReportsApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
recognition_start = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
recognition_end = billforward.SimpleDateParam() # SimpleDateParam |  (optional)

try:
    api_instance.get_coupon_report(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end)
except ApiException as e:
    print("Exception when calling ReportsApi->get_coupon_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **recognition_start** | [**SimpleDateParam**](.md)|  | [optional] 
 **recognition_end** | [**SimpleDateParam**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_csv_report_invoice_line_payments_bucketed**
> get_csv_report_invoice_line_payments_bucketed(organizations=organizations, payment_direction=payment_direction, bucket_type=bucket_type, date_discriminator=date_discriminator, recognition_start=recognition_start, recognition_end=recognition_end, include_gateway=include_gateway, exclude_gateway=exclude_gateway, accounts=accounts, subscriptions=subscriptions, date_interval_inclusivity=date_interval_inclusivity, date_time_format=date_time_format, date_granularity=date_granularity, boolean_format=boolean_format, monetary_amount_format=monetary_amount_format, meta_column_account=meta_column_account, meta_column_sub_child=meta_column_sub_child)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.ReportsApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
payment_direction = 'All' # str |  (optional) (default to All)
bucket_type = 'DebitActualAmount' # str |  (optional) (default to DebitActualAmount)
date_discriminator = 'PeriodStart' # str |  (optional) (default to PeriodStart)
recognition_start = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
recognition_end = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
include_gateway = ['include_gateway_example'] # list[str] |  (optional)
exclude_gateway = ['exclude_gateway_example'] # list[str] |  (optional)
accounts = ['accounts_example'] # list[str] |  (optional)
subscriptions = ['subscriptions_example'] # list[str] |  (optional)
date_interval_inclusivity = 'Exclusive' # str |  (optional) (default to Exclusive)
date_time_format = 'UTCExcel' # str |  (optional) (default to UTCExcel)
date_granularity = 'Second' # str |  (optional) (default to Second)
boolean_format = 'TrueFalseLowercase' # str |  (optional) (default to TrueFalseLowercase)
monetary_amount_format = 'NoCommasPeriod2DP' # str |  (optional) (default to NoCommasPeriod2DP)
meta_column_account = ['meta_column_account_example'] # list[str] |  (optional)
meta_column_sub_child = ['meta_column_sub_child_example'] # list[str] |  (optional)

try:
    api_instance.get_csv_report_invoice_line_payments_bucketed(organizations=organizations, payment_direction=payment_direction, bucket_type=bucket_type, date_discriminator=date_discriminator, recognition_start=recognition_start, recognition_end=recognition_end, include_gateway=include_gateway, exclude_gateway=exclude_gateway, accounts=accounts, subscriptions=subscriptions, date_interval_inclusivity=date_interval_inclusivity, date_time_format=date_time_format, date_granularity=date_granularity, boolean_format=boolean_format, monetary_amount_format=monetary_amount_format, meta_column_account=meta_column_account, meta_column_sub_child=meta_column_sub_child)
except ApiException as e:
    print("Exception when calling ReportsApi->get_csv_report_invoice_line_payments_bucketed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **payment_direction** | **str**|  | [optional] [default to All]
 **bucket_type** | **str**|  | [optional] [default to DebitActualAmount]
 **date_discriminator** | **str**|  | [optional] [default to PeriodStart]
 **recognition_start** | [**SimpleDateParam**](.md)|  | [optional] 
 **recognition_end** | [**SimpleDateParam**](.md)|  | [optional] 
 **include_gateway** | [**list[str]**](str.md)|  | [optional] 
 **exclude_gateway** | [**list[str]**](str.md)|  | [optional] 
 **accounts** | [**list[str]**](str.md)|  | [optional] 
 **subscriptions** | [**list[str]**](str.md)|  | [optional] 
 **date_interval_inclusivity** | **str**|  | [optional] [default to Exclusive]
 **date_time_format** | **str**|  | [optional] [default to UTCExcel]
 **date_granularity** | **str**|  | [optional] [default to Second]
 **boolean_format** | **str**|  | [optional] [default to TrueFalseLowercase]
 **monetary_amount_format** | **str**|  | [optional] [default to NoCommasPeriod2DP]
 **meta_column_account** | [**list[str]**](str.md)|  | [optional] 
 **meta_column_sub_child** | [**list[str]**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_csv_report_invoice_line_payments_raw**
> get_csv_report_invoice_line_payments_raw(organizations=organizations, payment_direction=payment_direction, date_discriminator=date_discriminator, recognition_start=recognition_start, recognition_end=recognition_end, include_gateway=include_gateway, exclude_gateway=exclude_gateway, accounts=accounts, subscriptions=subscriptions, date_interval_inclusivity=date_interval_inclusivity, date_time_format=date_time_format, date_granularity=date_granularity, boolean_format=boolean_format, monetary_amount_format=monetary_amount_format, meta_column_account=meta_column_account, meta_column_sub_child=meta_column_sub_child)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.ReportsApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
payment_direction = 'All' # str |  (optional) (default to All)
date_discriminator = 'PeriodStart' # str |  (optional) (default to PeriodStart)
recognition_start = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
recognition_end = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
include_gateway = ['include_gateway_example'] # list[str] |  (optional)
exclude_gateway = ['exclude_gateway_example'] # list[str] |  (optional)
accounts = ['accounts_example'] # list[str] |  (optional)
subscriptions = ['subscriptions_example'] # list[str] |  (optional)
date_interval_inclusivity = 'Exclusive' # str |  (optional) (default to Exclusive)
date_time_format = 'UTCExcel' # str |  (optional) (default to UTCExcel)
date_granularity = 'Second' # str |  (optional) (default to Second)
boolean_format = 'TrueFalseLowercase' # str |  (optional) (default to TrueFalseLowercase)
monetary_amount_format = 'NoCommasPeriod2DP' # str |  (optional) (default to NoCommasPeriod2DP)
meta_column_account = ['meta_column_account_example'] # list[str] |  (optional)
meta_column_sub_child = ['meta_column_sub_child_example'] # list[str] |  (optional)

try:
    api_instance.get_csv_report_invoice_line_payments_raw(organizations=organizations, payment_direction=payment_direction, date_discriminator=date_discriminator, recognition_start=recognition_start, recognition_end=recognition_end, include_gateway=include_gateway, exclude_gateway=exclude_gateway, accounts=accounts, subscriptions=subscriptions, date_interval_inclusivity=date_interval_inclusivity, date_time_format=date_time_format, date_granularity=date_granularity, boolean_format=boolean_format, monetary_amount_format=monetary_amount_format, meta_column_account=meta_column_account, meta_column_sub_child=meta_column_sub_child)
except ApiException as e:
    print("Exception when calling ReportsApi->get_csv_report_invoice_line_payments_raw: %s\n" % e)
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
 **accounts** | [**list[str]**](str.md)|  | [optional] 
 **subscriptions** | [**list[str]**](str.md)|  | [optional] 
 **date_interval_inclusivity** | **str**|  | [optional] [default to Exclusive]
 **date_time_format** | **str**|  | [optional] [default to UTCExcel]
 **date_granularity** | **str**|  | [optional] [default to Second]
 **boolean_format** | **str**|  | [optional] [default to TrueFalseLowercase]
 **monetary_amount_format** | **str**|  | [optional] [default to NoCommasPeriod2DP]
 **meta_column_account** | [**list[str]**](str.md)|  | [optional] 
 **meta_column_sub_child** | [**list[str]**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_csv_report_revenue_attributions_bucketed**
> get_csv_report_revenue_attributions_bucketed(organizations=organizations, date_discriminator=date_discriminator, recognition_start=recognition_start, recognition_end=recognition_end, date_interval_inclusivity=date_interval_inclusivity, date_time_format=date_time_format, date_granularity=date_granularity, boolean_format=boolean_format, monetary_amount_format=monetary_amount_format, meta_column_account=meta_column_account, meta_column_sub_child=meta_column_sub_child)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.ReportsApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
date_discriminator = 'PeriodStart' # str |  (optional) (default to PeriodStart)
recognition_start = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
recognition_end = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
date_interval_inclusivity = 'Exclusive' # str |  (optional) (default to Exclusive)
date_time_format = 'UTCExcel' # str |  (optional) (default to UTCExcel)
date_granularity = 'Second' # str |  (optional) (default to Second)
boolean_format = 'TrueFalseLowercase' # str |  (optional) (default to TrueFalseLowercase)
monetary_amount_format = 'NoCommasPeriod2DP' # str |  (optional) (default to NoCommasPeriod2DP)
meta_column_account = ['meta_column_account_example'] # list[str] |  (optional)
meta_column_sub_child = ['meta_column_sub_child_example'] # list[str] |  (optional)

try:
    api_instance.get_csv_report_revenue_attributions_bucketed(organizations=organizations, date_discriminator=date_discriminator, recognition_start=recognition_start, recognition_end=recognition_end, date_interval_inclusivity=date_interval_inclusivity, date_time_format=date_time_format, date_granularity=date_granularity, boolean_format=boolean_format, monetary_amount_format=monetary_amount_format, meta_column_account=meta_column_account, meta_column_sub_child=meta_column_sub_child)
except ApiException as e:
    print("Exception when calling ReportsApi->get_csv_report_revenue_attributions_bucketed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **date_discriminator** | **str**|  | [optional] [default to PeriodStart]
 **recognition_start** | [**SimpleDateParam**](.md)|  | [optional] 
 **recognition_end** | [**SimpleDateParam**](.md)|  | [optional] 
 **date_interval_inclusivity** | **str**|  | [optional] [default to Exclusive]
 **date_time_format** | **str**|  | [optional] [default to UTCExcel]
 **date_granularity** | **str**|  | [optional] [default to Second]
 **boolean_format** | **str**|  | [optional] [default to TrueFalseLowercase]
 **monetary_amount_format** | **str**|  | [optional] [default to NoCommasPeriod2DP]
 **meta_column_account** | [**list[str]**](str.md)|  | [optional] 
 **meta_column_sub_child** | [**list[str]**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_csv_report_revenue_attributions_raw**
> get_csv_report_revenue_attributions_raw(organizations=organizations, date_discriminator=date_discriminator, recognition_start=recognition_start, recognition_end=recognition_end, date_interval_inclusivity=date_interval_inclusivity, date_time_format=date_time_format, date_granularity=date_granularity, boolean_format=boolean_format, monetary_amount_format=monetary_amount_format, meta_column_account=meta_column_account, meta_column_sub_child=meta_column_sub_child, include_zero_value=include_zero_value)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.ReportsApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
date_discriminator = 'PeriodStart' # str |  (optional) (default to PeriodStart)
recognition_start = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
recognition_end = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
date_interval_inclusivity = 'Exclusive' # str |  (optional) (default to Exclusive)
date_time_format = 'UTCExcel' # str |  (optional) (default to UTCExcel)
date_granularity = 'Second' # str |  (optional) (default to Second)
boolean_format = 'TrueFalseLowercase' # str |  (optional) (default to TrueFalseLowercase)
monetary_amount_format = 'NoCommasPeriod2DP' # str |  (optional) (default to NoCommasPeriod2DP)
meta_column_account = ['meta_column_account_example'] # list[str] |  (optional)
meta_column_sub_child = ['meta_column_sub_child_example'] # list[str] |  (optional)
include_zero_value = true # bool |  (optional)

try:
    api_instance.get_csv_report_revenue_attributions_raw(organizations=organizations, date_discriminator=date_discriminator, recognition_start=recognition_start, recognition_end=recognition_end, date_interval_inclusivity=date_interval_inclusivity, date_time_format=date_time_format, date_granularity=date_granularity, boolean_format=boolean_format, monetary_amount_format=monetary_amount_format, meta_column_account=meta_column_account, meta_column_sub_child=meta_column_sub_child, include_zero_value=include_zero_value)
except ApiException as e:
    print("Exception when calling ReportsApi->get_csv_report_revenue_attributions_raw: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **date_discriminator** | **str**|  | [optional] [default to PeriodStart]
 **recognition_start** | [**SimpleDateParam**](.md)|  | [optional] 
 **recognition_end** | [**SimpleDateParam**](.md)|  | [optional] 
 **date_interval_inclusivity** | **str**|  | [optional] [default to Exclusive]
 **date_time_format** | **str**|  | [optional] [default to UTCExcel]
 **date_granularity** | **str**|  | [optional] [default to Second]
 **boolean_format** | **str**|  | [optional] [default to TrueFalseLowercase]
 **monetary_amount_format** | **str**|  | [optional] [default to NoCommasPeriod2DP]
 **meta_column_account** | [**list[str]**](str.md)|  | [optional] 
 **meta_column_sub_child** | [**list[str]**](str.md)|  | [optional] 
 **include_zero_value** | **bool**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_csv_revenue_schedule**
> get_csv_revenue_schedule(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end, include_gateway=include_gateway, exclude_gateway=exclude_gateway, bucket_by=bucket_by, group_by=group_by, pivot_by_dates=pivot_by_dates, include_detailed_lines=include_detailed_lines, accounts=accounts, subscriptions=subscriptions, plans=plans)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.ReportsApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
recognition_start = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
recognition_end = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
include_gateway = ['include_gateway_example'] # list[str] |  (optional)
exclude_gateway = ['exclude_gateway_example'] # list[str] |  (optional)
bucket_by = 'day' # str |  (optional) (default to day)
group_by = ['group_by_example'] # list[str] |  (optional)
pivot_by_dates = false # bool |  (optional) (default to false)
include_detailed_lines = false # bool |  (optional) (default to false)
accounts = ['accounts_example'] # list[str] |  (optional)
subscriptions = ['subscriptions_example'] # list[str] |  (optional)
plans = ['plans_example'] # list[str] |  (optional)

try:
    api_instance.get_csv_revenue_schedule(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end, include_gateway=include_gateway, exclude_gateway=exclude_gateway, bucket_by=bucket_by, group_by=group_by, pivot_by_dates=pivot_by_dates, include_detailed_lines=include_detailed_lines, accounts=accounts, subscriptions=subscriptions, plans=plans)
except ApiException as e:
    print("Exception when calling ReportsApi->get_csv_revenue_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **recognition_start** | [**SimpleDateParam**](.md)|  | [optional] 
 **recognition_end** | [**SimpleDateParam**](.md)|  | [optional] 
 **include_gateway** | [**list[str]**](str.md)|  | [optional] 
 **exclude_gateway** | [**list[str]**](str.md)|  | [optional] 
 **bucket_by** | **str**|  | [optional] [default to day]
 **group_by** | [**list[str]**](str.md)|  | [optional] 
 **pivot_by_dates** | **bool**|  | [optional] [default to false]
 **include_detailed_lines** | **bool**|  | [optional] [default to false]
 **accounts** | [**list[str]**](str.md)|  | [optional] 
 **subscriptions** | [**list[str]**](str.md)|  | [optional] 
 **plans** | [**list[str]**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_transactions**
> get_payment_transactions(organizations=organizations, date_discriminator=date_discriminator, recognition_start=recognition_start, recognition_end=recognition_end, include_gateway=include_gateway, exclude_gateway=exclude_gateway, date_interval_inclusivity=date_interval_inclusivity, date_time_format=date_time_format, date_granularity=date_granularity, boolean_format=boolean_format, monetary_amount_format=monetary_amount_format, meta_column_account=meta_column_account, meta_column_sub_child=meta_column_sub_child)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.ReportsApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
date_discriminator = 'PaymentReceived' # str |  (optional) (default to PaymentReceived)
recognition_start = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
recognition_end = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
include_gateway = ['include_gateway_example'] # list[str] |  (optional)
exclude_gateway = ['exclude_gateway_example'] # list[str] |  (optional)
date_interval_inclusivity = 'Exclusive' # str |  (optional) (default to Exclusive)
date_time_format = 'UTCExcel' # str |  (optional) (default to UTCExcel)
date_granularity = 'Second' # str |  (optional) (default to Second)
boolean_format = 'TrueFalseLowercase' # str |  (optional) (default to TrueFalseLowercase)
monetary_amount_format = 'NoCommasPeriod2DP' # str |  (optional) (default to NoCommasPeriod2DP)
meta_column_account = ['meta_column_account_example'] # list[str] |  (optional)
meta_column_sub_child = ['meta_column_sub_child_example'] # list[str] |  (optional)

try:
    api_instance.get_payment_transactions(organizations=organizations, date_discriminator=date_discriminator, recognition_start=recognition_start, recognition_end=recognition_end, include_gateway=include_gateway, exclude_gateway=exclude_gateway, date_interval_inclusivity=date_interval_inclusivity, date_time_format=date_time_format, date_granularity=date_granularity, boolean_format=boolean_format, monetary_amount_format=monetary_amount_format, meta_column_account=meta_column_account, meta_column_sub_child=meta_column_sub_child)
except ApiException as e:
    print("Exception when calling ReportsApi->get_payment_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **date_discriminator** | **str**|  | [optional] [default to PaymentReceived]
 **recognition_start** | [**SimpleDateParam**](.md)|  | [optional] 
 **recognition_end** | [**SimpleDateParam**](.md)|  | [optional] 
 **include_gateway** | [**list[str]**](str.md)|  | [optional] 
 **exclude_gateway** | [**list[str]**](str.md)|  | [optional] 
 **date_interval_inclusivity** | **str**|  | [optional] [default to Exclusive]
 **date_time_format** | **str**|  | [optional] [default to UTCExcel]
 **date_granularity** | **str**|  | [optional] [default to Second]
 **boolean_format** | **str**|  | [optional] [default to TrueFalseLowercase]
 **monetary_amount_format** | **str**|  | [optional] [default to NoCommasPeriod2DP]
 **meta_column_account** | [**list[str]**](str.md)|  | [optional] 
 **meta_column_sub_child** | [**list[str]**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_refunds_as_csv**
> get_refunds_as_csv(organizations=organizations, completed_start=completed_start, completed_end=completed_end, offset=offset, records=records, order_by=order_by, order=order)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.ReportsApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
completed_start = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
completed_end = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
offset = 56 # int |  (optional)
records = 56 # int |  (optional)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)

try:
    api_instance.get_refunds_as_csv(organizations=organizations, completed_start=completed_start, completed_end=completed_end, offset=offset, records=records, order_by=order_by, order=order)
except ApiException as e:
    print("Exception when calling ReportsApi->get_refunds_as_csv: %s\n" % e)
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

# **get_shipments_report**
> get_shipments_report(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.ReportsApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
recognition_start = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
recognition_end = billforward.SimpleDateParam() # SimpleDateParam |  (optional)

try:
    api_instance.get_shipments_report(organizations=organizations, recognition_start=recognition_start, recognition_end=recognition_end)
except ApiException as e:
    print("Exception when calling ReportsApi->get_shipments_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **recognition_start** | [**SimpleDateParam**](.md)|  | [optional] 
 **recognition_end** | [**SimpleDateParam**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscriptions_overview**
> get_subscriptions_overview(organizations=organizations, date_discriminator=date_discriminator, recognition_start=recognition_start, recognition_end=recognition_end, date_interval_inclusivity=date_interval_inclusivity, date_time_format=date_time_format, date_granularity=date_granularity, boolean_format=boolean_format, monetary_amount_format=monetary_amount_format, meta_column_account=meta_column_account, meta_column_sub=meta_column_sub, account_id=account_id, subscription_id=subscription_id, parent_sub_id=parent_sub_id, product_id=product_id, rate_plan_id=rate_plan_id, exclude_child_subs=exclude_child_subs, exclude_parentless_subs=exclude_parentless_subs)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.ReportsApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
date_discriminator = 'AccountCreated' # str |  (optional) (default to AccountCreated)
recognition_start = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
recognition_end = billforward.SimpleDateParam() # SimpleDateParam |  (optional)
date_interval_inclusivity = 'Exclusive' # str |  (optional) (default to Exclusive)
date_time_format = 'UTCExcel' # str |  (optional) (default to UTCExcel)
date_granularity = 'Second' # str |  (optional) (default to Second)
boolean_format = 'TrueFalseLowercase' # str |  (optional) (default to TrueFalseLowercase)
monetary_amount_format = 'NoCommasPeriod2DP' # str |  (optional) (default to NoCommasPeriod2DP)
meta_column_account = ['meta_column_account_example'] # list[str] |  (optional)
meta_column_sub = ['meta_column_sub_example'] # list[str] |  (optional)
account_id = ['account_id_example'] # list[str] |  (optional)
subscription_id = ['subscription_id_example'] # list[str] |  (optional)
parent_sub_id = ['parent_sub_id_example'] # list[str] |  (optional)
product_id = ['product_id_example'] # list[str] |  (optional)
rate_plan_id = ['rate_plan_id_example'] # list[str] |  (optional)
exclude_child_subs = false # bool |  (optional) (default to false)
exclude_parentless_subs = false # bool |  (optional) (default to false)

try:
    api_instance.get_subscriptions_overview(organizations=organizations, date_discriminator=date_discriminator, recognition_start=recognition_start, recognition_end=recognition_end, date_interval_inclusivity=date_interval_inclusivity, date_time_format=date_time_format, date_granularity=date_granularity, boolean_format=boolean_format, monetary_amount_format=monetary_amount_format, meta_column_account=meta_column_account, meta_column_sub=meta_column_sub, account_id=account_id, subscription_id=subscription_id, parent_sub_id=parent_sub_id, product_id=product_id, rate_plan_id=rate_plan_id, exclude_child_subs=exclude_child_subs, exclude_parentless_subs=exclude_parentless_subs)
except ApiException as e:
    print("Exception when calling ReportsApi->get_subscriptions_overview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **date_discriminator** | **str**|  | [optional] [default to AccountCreated]
 **recognition_start** | [**SimpleDateParam**](.md)|  | [optional] 
 **recognition_end** | [**SimpleDateParam**](.md)|  | [optional] 
 **date_interval_inclusivity** | **str**|  | [optional] [default to Exclusive]
 **date_time_format** | **str**|  | [optional] [default to UTCExcel]
 **date_granularity** | **str**|  | [optional] [default to Second]
 **boolean_format** | **str**|  | [optional] [default to TrueFalseLowercase]
 **monetary_amount_format** | **str**|  | [optional] [default to NoCommasPeriod2DP]
 **meta_column_account** | [**list[str]**](str.md)|  | [optional] 
 **meta_column_sub** | [**list[str]**](str.md)|  | [optional] 
 **account_id** | [**list[str]**](str.md)|  | [optional] 
 **subscription_id** | [**list[str]**](str.md)|  | [optional] 
 **parent_sub_id** | [**list[str]**](str.md)|  | [optional] 
 **product_id** | [**list[str]**](str.md)|  | [optional] 
 **rate_plan_id** | [**list[str]**](str.md)|  | [optional] 
 **exclude_child_subs** | **bool**|  | [optional] [default to false]
 **exclude_parentless_subs** | **bool**|  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

