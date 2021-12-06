# billforward.TaxesApi

All URIs are relative to *https://app.billforward.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_taxation_strategy**](TaxesApi.md#create_taxation_strategy) | **POST** /taxation-strategies | 
[**get_all_taxation_strategies**](TaxesApi.md#get_all_taxation_strategies) | **GET** /taxation-strategies | 
[**get_taxation_strategy_by_consistent_id**](TaxesApi.md#get_taxation_strategy_by_consistent_id) | **GET** /taxation-strategies/{taxation-strategy-ID} | 
[**get_taxation_strategy_by_country**](TaxesApi.md#get_taxation_strategy_by_country) | **GET** /taxation-strategies/country/{country} | 
[**get_taxation_strategy_by_currency**](TaxesApi.md#get_taxation_strategy_by_currency) | **GET** /taxation-strategies/currency/{currency} | 
[**get_taxation_strategy_by_province**](TaxesApi.md#get_taxation_strategy_by_province) | **GET** /taxation-strategies/province/{province} | 
[**get_taxation_strategy_by_version_id**](TaxesApi.md#get_taxation_strategy_by_version_id) | **GET** /taxation-strategies/version/{version-ID} | 
[**retire_taxation_strategy**](TaxesApi.md#retire_taxation_strategy) | **DELETE** /taxation-strategies/version/{version-ID} | 
[**update_taxation_strategy**](TaxesApi.md#update_taxation_strategy) | **PUT** /taxation-strategies | 

# **create_taxation_strategy**
> InlineResponseDefault78 create_taxation_strategy(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TaxesApi(billforward.ApiClient(configuration))
body = billforward.TaxationStrategy() # TaxationStrategy |  (optional)

try:
    api_response = api_instance.create_taxation_strategy(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxesApi->create_taxation_strategy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TaxationStrategy**](TaxationStrategy.md)|  | [optional] 

### Return type

[**InlineResponseDefault78**](InlineResponseDefault78.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_taxation_strategies**
> InlineResponseDefault77 get_all_taxation_strategies(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TaxesApi(billforward.ApiClient(configuration))
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_all_taxation_strategies(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxesApi->get_all_taxation_strategies: %s\n" % e)
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

[**InlineResponseDefault77**](InlineResponseDefault77.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_taxation_strategy_by_consistent_id**
> InlineResponseDefault77 get_taxation_strategy_by_consistent_id(taxation_strategy_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TaxesApi(billforward.ApiClient(configuration))
taxation_strategy_id = 'taxation_strategy_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_taxation_strategy_by_consistent_id(taxation_strategy_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxesApi->get_taxation_strategy_by_consistent_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxation_strategy_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to false]

### Return type

[**InlineResponseDefault77**](InlineResponseDefault77.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_taxation_strategy_by_country**
> InlineResponseDefault77 get_taxation_strategy_by_country(country, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TaxesApi(billforward.ApiClient(configuration))
country = 'country_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_taxation_strategy_by_country(country, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxesApi->get_taxation_strategy_by_country: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to false]

### Return type

[**InlineResponseDefault77**](InlineResponseDefault77.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_taxation_strategy_by_currency**
> InlineResponseDefault77 get_taxation_strategy_by_currency(currency, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TaxesApi(billforward.ApiClient(configuration))
currency = 'currency_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_taxation_strategy_by_currency(currency, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxesApi->get_taxation_strategy_by_currency: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to false]

### Return type

[**InlineResponseDefault77**](InlineResponseDefault77.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_taxation_strategy_by_province**
> InlineResponseDefault77 get_taxation_strategy_by_province(province, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TaxesApi(billforward.ApiClient(configuration))
province = 'province_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)
include_retired = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_taxation_strategy_by_province(province, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxesApi->get_taxation_strategy_by_province: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **province** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]
 **include_retired** | **bool**|  | [optional] [default to false]

### Return type

[**InlineResponseDefault77**](InlineResponseDefault77.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_taxation_strategy_by_version_id**
> InlineResponseDefault78 get_taxation_strategy_by_version_id(version_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TaxesApi(billforward.ApiClient(configuration))
version_id = 'version_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_taxation_strategy_by_version_id(version_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxesApi->get_taxation_strategy_by_version_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault78**](InlineResponseDefault78.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retire_taxation_strategy**
> InlineResponseDefault78 retire_taxation_strategy(version_id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TaxesApi(billforward.ApiClient(configuration))
version_id = 'version_id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.retire_taxation_strategy(version_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxesApi->retire_taxation_strategy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault78**](InlineResponseDefault78.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_taxation_strategy**
> InlineResponseDefault78 update_taxation_strategy(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.TaxesApi(billforward.ApiClient(configuration))
body = billforward.TaxationStrategy() # TaxationStrategy |  (optional)

try:
    api_response = api_instance.update_taxation_strategy(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxesApi->update_taxation_strategy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TaxationStrategy**](TaxationStrategy.md)|  | [optional] 

### Return type

[**InlineResponseDefault78**](InlineResponseDefault78.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

