# swagger_client.AnalyticsApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_debts**](AnalyticsApi.md#get_account_debts) | **POST** /analytics/payments/accounts/outstanding | Gets outstanding debts per account, within a date range.
[**get_account_ltv**](AnalyticsApi.md#get_account_ltv) | **GET** /analytics/account-ltv/{account-id}/{end-datetime} | Gets an account&#39;s life-time value, as of a given end date.
[**get_account_payments**](AnalyticsApi.md#get_account_payments) | **POST** /analytics/payments/accounts | Gets hourly payments per product, within a date range.
[**get_billforward_managed_payments**](AnalyticsApi.md#get_billforward_managed_payments) | **GET** /analytics/billforward-managed-payments/{start-datetime}/{end-datetime} | Gets all payments managed by BillForward, within a date range.
[**get_churn**](AnalyticsApi.md#get_churn) | **GET** /analytics/churn/{start-datetime}/{end-datetime} | Gets churn, within a date range.
[**get_debts**](AnalyticsApi.md#get_debts) | **GET** /analytics/payments/outstanding/{start-datetime}/{end-datetime} | Gets debts within a date range.
[**get_payments**](AnalyticsApi.md#get_payments) | **GET** /analytics/payments/{start-datetime}/{end-datetime} | Gets payments within a date range.
[**get_product_payments**](AnalyticsApi.md#get_product_payments) | **POST** /analytics/payments-per-product | Gets hourly payments per product, within a date range.
[**get_product_rate_plan_payments**](AnalyticsApi.md#get_product_rate_plan_payments) | **POST** /analytics/payments/product-rate-plan | Gets hourly payments per product, within a date range.
[**get_subscription_ltv**](AnalyticsApi.md#get_subscription_ltv) | **GET** /analytics/subscription-ltv/{subscription-id}/{end-datetime} | Gets a subscription&#39;s life-time value, as of a given end date.
[**get_upgrades**](AnalyticsApi.md#get_upgrades) | **GET** /analytics/upgrades/{start-datetime}/{end-datetime} | Gets upgrades, within a date range.


# **get_account_debts**
> AccountPaymentsResultPagedMetadata get_account_debts(debts_per_account)

Gets outstanding debts per account, within a date range.

{\"nickname\" : \"Get account debts\",\"response\" : \"getAccountDebts.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalyticsApi()
debts_per_account = swagger_client.BillingEntityBase() # BillingEntityBase | The payments-per-account object.

try: 
    # Gets outstanding debts per account, within a date range.
    api_response = api_instance.get_account_debts(debts_per_account)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_account_debts: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **debts_per_account** | [**BillingEntityBase**](BillingEntityBase.md)| The payments-per-account object. | 

### Return type

[**AccountPaymentsResultPagedMetadata**](AccountPaymentsResultPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_ltv**
> AccountLTVResultPagedMetadata get_account_ltv(account_id, end_datetime, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Gets an account's life-time value, as of a given end date.

{\"nickname\":\"Get account life-time value\",\"response\":\"getAccountLTV.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalyticsApi()
account_id = 'account_id_example' # str | The id of the account.
end_datetime = 'end_datetime_example' # str | The UTC DateTime specifying the end of the result period.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first amendment to return. (optional) (default to 0)
records = 8766 # int | The maximum number of amendments to return. (optional) (default to 8766)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'ASC' # str | The direction of any ordering, either ASC or DESC. (optional) (default to ASC)

try: 
    # Gets an account's life-time value, as of a given end date.
    api_response = api_instance.get_account_ltv(account_id, end_datetime, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_account_ltv: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The id of the account. | 
 **end_datetime** | **str**| The UTC DateTime specifying the end of the result period. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first amendment to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of amendments to return. | [optional] [default to 8766]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| The direction of any ordering, either ASC or DESC. | [optional] [default to ASC]

### Return type

[**AccountLTVResultPagedMetadata**](AccountLTVResultPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_payments**
> AccountPaymentsResultPagedMetadata get_account_payments(payments_per_account)

Gets hourly payments per product, within a date range.

{\"nickname\" : \"Get payments per account\",\"response\" : \"getAccountPayments.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalyticsApi()
payments_per_account = swagger_client.BillingEntityBase() # BillingEntityBase | The payments-per-account object.

try: 
    # Gets hourly payments per product, within a date range.
    api_response = api_instance.get_account_payments(payments_per_account)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_account_payments: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payments_per_account** | [**BillingEntityBase**](BillingEntityBase.md)| The payments-per-account object. | 

### Return type

[**AccountPaymentsResultPagedMetadata**](AccountPaymentsResultPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billforward_managed_payments**
> BillforwardManagedPaymentsResultPagedMetadata get_billforward_managed_payments(start_datetime, end_datetime, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Gets all payments managed by BillForward, within a date range.

{\"nickname\":\"Get managed payments\",\"response\":\"getManagedPayments.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalyticsApi()
start_datetime = 'start_datetime_example' # str | The UTC DateTime specifying the start of the result period.
end_datetime = 'end_datetime_example' # str | The UTC DateTime specifying the end of the result period.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first amendment to return. (optional) (default to 0)
records = 8766 # int | The maximum number of amendments to return. (optional) (default to 8766)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'ASC' # str | The direction of any ordering, either ASC or DESC. (optional) (default to ASC)

try: 
    # Gets all payments managed by BillForward, within a date range.
    api_response = api_instance.get_billforward_managed_payments(start_datetime, end_datetime, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_billforward_managed_payments: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_datetime** | **str**| The UTC DateTime specifying the start of the result period. | 
 **end_datetime** | **str**| The UTC DateTime specifying the end of the result period. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first amendment to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of amendments to return. | [optional] [default to 8766]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| The direction of any ordering, either ASC or DESC. | [optional] [default to ASC]

### Return type

[**BillforwardManagedPaymentsResultPagedMetadata**](BillforwardManagedPaymentsResultPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_churn**
> CassChurnResultPagedMetadata get_churn(start_datetime, end_datetime, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Gets churn, within a date range.

{\"nickname\":\"Get churn\",\"response\":\"getChurn.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalyticsApi()
start_datetime = 'start_datetime_example' # str | The UTC DateTime specifying the start of the result period.
end_datetime = 'end_datetime_example' # str | The UTC DateTime specifying the end of the result period.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first amendment to return. (optional) (default to 0)
records = 8766 # int | The maximum number of amendments to return. (optional) (default to 8766)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'ASC' # str | The direction of any ordering, either ASC or DESC. (optional) (default to ASC)

try: 
    # Gets churn, within a date range.
    api_response = api_instance.get_churn(start_datetime, end_datetime, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_churn: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_datetime** | **str**| The UTC DateTime specifying the start of the result period. | 
 **end_datetime** | **str**| The UTC DateTime specifying the end of the result period. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first amendment to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of amendments to return. | [optional] [default to 8766]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| The direction of any ordering, either ASC or DESC. | [optional] [default to ASC]

### Return type

[**CassChurnResultPagedMetadata**](CassChurnResultPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debts**
> DebtsResultPagedMetadata get_debts(start_datetime, end_datetime, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Gets debts within a date range.

{\"nickname\":\"Get debts\",\"response\":\"getDebts.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalyticsApi()
start_datetime = 'start_datetime_example' # str | The UTC DateTime specifying the start of the result period.
end_datetime = 'end_datetime_example' # str | The UTC DateTime specifying the end of the result period.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first amendment to return. (optional) (default to 0)
records = 8766 # int | The maximum number of amendments to return. (optional) (default to 8766)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'ASC' # str | The direction of any ordering, either ASC or DESC. (optional) (default to ASC)

try: 
    # Gets debts within a date range.
    api_response = api_instance.get_debts(start_datetime, end_datetime, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_debts: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_datetime** | **str**| The UTC DateTime specifying the start of the result period. | 
 **end_datetime** | **str**| The UTC DateTime specifying the end of the result period. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first amendment to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of amendments to return. | [optional] [default to 8766]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| The direction of any ordering, either ASC or DESC. | [optional] [default to ASC]

### Return type

[**DebtsResultPagedMetadata**](DebtsResultPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payments**
> CassPaymentResultPagedMetadata get_payments(start_datetime, end_datetime, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Gets payments within a date range.

{\"nickname\":\"Get all payments\",\"response\":\"getPayments.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalyticsApi()
start_datetime = 'start_datetime_example' # str | The UTC DateTime specifying the start of the result period.
end_datetime = 'end_datetime_example' # str | The UTC DateTime specifying the end of the result period.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first amendment to return. (optional) (default to 0)
records = 8766 # int | The maximum number of amendments to return. (optional) (default to 8766)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'ASC' # str | The direction of any ordering, either ASC or DESC. (optional) (default to ASC)

try: 
    # Gets payments within a date range.
    api_response = api_instance.get_payments(start_datetime, end_datetime, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_payments: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_datetime** | **str**| The UTC DateTime specifying the start of the result period. | 
 **end_datetime** | **str**| The UTC DateTime specifying the end of the result period. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first amendment to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of amendments to return. | [optional] [default to 8766]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| The direction of any ordering, either ASC or DESC. | [optional] [default to ASC]

### Return type

[**CassPaymentResultPagedMetadata**](CassPaymentResultPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_payments**
> ProductPaymentsResultPagedMetadata get_product_payments(payments_per_product)

Gets hourly payments per product, within a date range.

{\"nickname\" : \"Get payments per product\",\"response\" : \"getProductPayments.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalyticsApi()
payments_per_product = swagger_client.BillingEntityBase() # BillingEntityBase | The payments-per-product object.

try: 
    # Gets hourly payments per product, within a date range.
    api_response = api_instance.get_product_payments(payments_per_product)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_product_payments: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payments_per_product** | [**BillingEntityBase**](BillingEntityBase.md)| The payments-per-product object. | 

### Return type

[**ProductPaymentsResultPagedMetadata**](ProductPaymentsResultPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_rate_plan_payments**
> ProductRatePlanPaymentsResultPagedMetadata get_product_rate_plan_payments(payments_per_product_rate_plan)

Gets hourly payments per product, within a date range.

{\"nickname\" : \"Get payments per rate plan\",\"response\" : \"getRatePlanPayments.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalyticsApi()
payments_per_product_rate_plan = swagger_client.BillingEntityBase() # BillingEntityBase | The payments-per-product-rate-plan object.

try: 
    # Gets hourly payments per product, within a date range.
    api_response = api_instance.get_product_rate_plan_payments(payments_per_product_rate_plan)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_product_rate_plan_payments: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payments_per_product_rate_plan** | [**BillingEntityBase**](BillingEntityBase.md)| The payments-per-product-rate-plan object. | 

### Return type

[**ProductRatePlanPaymentsResultPagedMetadata**](ProductRatePlanPaymentsResultPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_ltv**
> SubscriptionLTVResultPagedMetadata get_subscription_ltv(subscription_id, end_datetime, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Gets a subscription's life-time value, as of a given end date.

{\"nickname\":\"Get sub life-time value\",\"response\":\"getSubscriptionLTV.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalyticsApi()
subscription_id = 'subscription_id_example' # str | The id of the subscription.
end_datetime = 'end_datetime_example' # str | The UTC DateTime specifying the end of the result period.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first amendment to return. (optional) (default to 0)
records = 8766 # int | The maximum number of amendments to return. (optional) (default to 8766)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'ASC' # str | The direction of any ordering, either ASC or DESC. (optional) (default to ASC)

try: 
    # Gets a subscription's life-time value, as of a given end date.
    api_response = api_instance.get_subscription_ltv(subscription_id, end_datetime, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_subscription_ltv: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| The id of the subscription. | 
 **end_datetime** | **str**| The UTC DateTime specifying the end of the result period. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first amendment to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of amendments to return. | [optional] [default to 8766]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| The direction of any ordering, either ASC or DESC. | [optional] [default to ASC]

### Return type

[**SubscriptionLTVResultPagedMetadata**](SubscriptionLTVResultPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upgrades**
> CassUpgradeResultPagedMetadata get_upgrades(start_datetime, end_datetime, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Gets upgrades, within a date range.

{\"nickname\":\"Get upgrades\",\"response\":\"getUpgrades.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AnalyticsApi()
start_datetime = 'start_datetime_example' # str | The UTC DateTime specifying the start of the result period.
end_datetime = 'end_datetime_example' # str | The UTC DateTime specifying the end of the result period.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first amendment to return. (optional) (default to 0)
records = 8766 # int | The maximum number of amendments to return. (optional) (default to 8766)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'ASC' # str | The direction of any ordering, either ASC or DESC. (optional) (default to ASC)

try: 
    # Gets upgrades, within a date range.
    api_response = api_instance.get_upgrades(start_datetime, end_datetime, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_upgrades: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_datetime** | **str**| The UTC DateTime specifying the start of the result period. | 
 **end_datetime** | **str**| The UTC DateTime specifying the end of the result period. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first amendment to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of amendments to return. | [optional] [default to 8766]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| The direction of any ordering, either ASC or DESC. | [optional] [default to ASC]

### Return type

[**CassUpgradeResultPagedMetadata**](CassUpgradeResultPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

