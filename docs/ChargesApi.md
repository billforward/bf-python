# billforward.ChargesApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_subscription_charges**](ChargesApi.md#get_all_subscription_charges) | **GET** /charges | Retrieves a collection of all charges. By default 10 values are returned. Records are returned in natural order.
[**get_subscription_charge_by_account_id**](ChargesApi.md#get_subscription_charge_by_account_id) | **GET** /charges/account/{account-ID} | Retrieves a collection of charges, specified by the account-ID parameter. By default 10 values are returned. Records are returned in natural order.
[**get_subscription_charge_by_id**](ChargesApi.md#get_subscription_charge_by_id) | **GET** /charges/{charge-id} | Retrieves a single charge, specified by the charge-id parameter.
[**get_subscription_charge_by_state**](ChargesApi.md#get_subscription_charge_by_state) | **GET** /charges/state/{state} | Retrieves a collection of charges, specified by the state parameter. By default 10 values are returned. Records are returned in natural order.
[**get_subscription_charge_by_version_id**](ChargesApi.md#get_subscription_charge_by_version_id) | **GET** /charges/version/{version-ID} | Retrieves a single charge, specified by the version-ID parameter.
[**recalculate_subscription_charge**](ChargesApi.md#recalculate_subscription_charge) | **POST** /charges/{charge-ID}/recalculate | Recalculate a charge.
[**void_subscription_charge**](ChargesApi.md#void_subscription_charge) | **DELETE** /charges/{charge-id} | Void the charge with the specified charge-ID.


# **get_all_subscription_charges**
> SubscriptionChargePagedMetadata get_all_subscription_charges(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Retrieves a collection of all charges. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve all charges\",\"response\":\"getChargeAll.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.ChargesApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first subscription to return. (optional) (default to 0)
records = 10 # int | The maximum number of subscriptions to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired subscriptions should be returned. (optional) (default to false)

try: 
    # Retrieves a collection of all charges. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_subscription_charges(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ChargesApi->get_all_subscription_charges: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first subscription to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of subscriptions to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired subscriptions should be returned. | [optional] [default to false]

### Return type

[**SubscriptionChargePagedMetadata**](SubscriptionChargePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_charge_by_account_id**
> SubscriptionChargePagedMetadata get_subscription_charge_by_account_id(account_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Retrieves a collection of charges, specified by the account-ID parameter. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by account\",\"response\":\"getChargeByAccount.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.ChargesApi()
account_id = 'account_id_example' # str | The string ID of the account
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first subscription to return. (optional) (default to 0)
records = 10 # int | The maximum number of subscriptions to return. (optional) (default to 10)
order_by = 'id' # str | Specify a field used to order the result set. (optional) (default to id)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired subscriptions should be returned. (optional) (default to false)

try: 
    # Retrieves a collection of charges, specified by the account-ID parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_subscription_charge_by_account_id(account_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ChargesApi->get_subscription_charge_by_account_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The string ID of the account | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first subscription to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of subscriptions to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to id]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired subscriptions should be returned. | [optional] [default to false]

### Return type

[**SubscriptionChargePagedMetadata**](SubscriptionChargePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_charge_by_id**
> SubscriptionChargePagedMetadata get_subscription_charge_by_id(charge_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Retrieves a single charge, specified by the charge-id parameter.

{\"nickname\":\"Retrieve a charge\",\"response\":\"getChargeByID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.ChargesApi()
charge_id = 'charge_id_example' # str | The unique string-ID of the subscription.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first subscription to return. (optional) (default to 0)
records = 10 # int | The maximum number of subscriptions to return. (optional) (default to 10)
order_by = 'id' # str | Specify a field used to order the result set. (optional) (default to id)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired subscriptions should be returned. (optional) (default to false)

try: 
    # Retrieves a single charge, specified by the charge-id parameter.
    api_response = api_instance.get_subscription_charge_by_id(charge_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ChargesApi->get_subscription_charge_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charge_id** | **str**| The unique string-ID of the subscription. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first subscription to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of subscriptions to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to id]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired subscriptions should be returned. | [optional] [default to false]

### Return type

[**SubscriptionChargePagedMetadata**](SubscriptionChargePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_charge_by_state**
> SubscriptionChargePagedMetadata get_subscription_charge_by_state(state, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Retrieves a collection of charges, specified by the state parameter. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by state\",\"response\":\"getChargeByState.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.ChargesApi()
state = 'state_example' # str | The current state of the charge
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first subscription to return. (optional) (default to 0)
records = 10 # int | The maximum number of subscriptions to return. (optional) (default to 10)
order_by = 'id' # str | Specify a field used to order the result set. (optional) (default to id)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired subscriptions should be returned. (optional) (default to false)

try: 
    # Retrieves a collection of charges, specified by the state parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_subscription_charge_by_state(state, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ChargesApi->get_subscription_charge_by_state: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| The current state of the charge | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first subscription to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of subscriptions to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to id]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired subscriptions should be returned. | [optional] [default to false]

### Return type

[**SubscriptionChargePagedMetadata**](SubscriptionChargePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_charge_by_version_id**
> SubscriptionChargePagedMetadata get_subscription_charge_by_version_id(version_id, organizations=organizations)

Retrieves a single charge, specified by the version-ID parameter.

{\"nickname\":\"Retrieve by version\",\"response\":\"getChargeByVersionID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.ChargesApi()
version_id = 'version_id_example' # str | The version-ID of the charge.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Retrieves a single charge, specified by the version-ID parameter.
    api_response = api_instance.get_subscription_charge_by_version_id(version_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ChargesApi->get_subscription_charge_by_version_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | **str**| The version-ID of the charge. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**SubscriptionChargePagedMetadata**](SubscriptionChargePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recalculate_subscription_charge**
> SubscriptionChargePagedMetadata recalculate_subscription_charge(charge_id, charge)

Recalculate a charge.

{\"nickname\":\"Re-calculate a charge\",\"request\":\"recalculateChargeRequest.html\",\"response\":\"recalculateChargeResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.ChargesApi()
charge_id = 'charge_id_example' # str | Unique id of the charge.
charge = billforward.RecalculateChargeRequest() # RecalculateChargeRequest | The charge to be re-calculated.

try: 
    # Recalculate a charge.
    api_response = api_instance.recalculate_subscription_charge(charge_id, charge)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ChargesApi->recalculate_subscription_charge: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charge_id** | **str**| Unique id of the charge. | 
 **charge** | [**RecalculateChargeRequest**](RecalculateChargeRequest.md)| The charge to be re-calculated. | 

### Return type

[**SubscriptionChargePagedMetadata**](SubscriptionChargePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **void_subscription_charge**
> SubscriptionChargePagedMetadata void_subscription_charge(charge_id, organizations=organizations)

Void the charge with the specified charge-ID.

{\"nickname\":\"Void charge\",\"response\":\"deleteCharge.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.ChargesApi()
charge_id = 'charge_id_example' # str | Unique id of the charge.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Void the charge with the specified charge-ID.
    api_response = api_instance.void_subscription_charge(charge_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ChargesApi->void_subscription_charge: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charge_id** | **str**| Unique id of the charge. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**SubscriptionChargePagedMetadata**](SubscriptionChargePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

