# billforward.TaxationstrategiesApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_taxation_strategy**](TaxationstrategiesApi.md#create_taxation_strategy) | **POST** /taxation-strategies | &lt;p&gt;Add a new tax or schedule changes in an existing tax.&lt;/p&gt;&lt;p&gt;Add a new tax by providing the location and tax percentage. To schedule a tax change specify the ID of the current Tax. A new version of the will be created &lt;i&gt;validFrom&lt;/i&gt; the specified date, the existing tax &lt;i&gt;validTill&lt;/i&gt; the start of this new tax.&lt;/p&gt;
[**get_all_taxation_strategies**](TaxationstrategiesApi.md#get_all_taxation_strategies) | **GET** /taxation-strategies | Returns a collection of all taxation-strategies. By default 10 values are returned. Records are returned in natural order.
[**get_taxation_strategy_by_consistent_id**](TaxationstrategiesApi.md#get_taxation_strategy_by_consistent_id) | **GET** /taxation-strategies/{taxation-strategy-ID} | Returns the tax currently being applied for the taxation-strategy-ID. To return schedule or historic tax changes the include_retired query parameter should be set to true.
[**get_taxation_strategy_by_country**](TaxationstrategiesApi.md#get_taxation_strategy_by_country) | **GET** /taxation-strategies/country/{country} | Returns a collection of taxation-strategies, specified by the country parameter. By default 10 values are returned. Records are returned in natural order. To return schedule or historic tax changes the include_retired query parameter should be set to true.
[**get_taxation_strategy_by_currency**](TaxationstrategiesApi.md#get_taxation_strategy_by_currency) | **GET** /taxation-strategies/currency/{currency} | Returns a collection of taxation-strategies, specified by the currency parameter. By default 10 values are returned. Records are returned in natural order.
[**get_taxation_strategy_by_province**](TaxationstrategiesApi.md#get_taxation_strategy_by_province) | **GET** /taxation-strategies/province/{province} | Returns a collection of taxation-strategies, specified by the province parameter. By default 10 values are returned. Records are returned in natural order.
[**get_taxation_strategy_by_version_id**](TaxationstrategiesApi.md#get_taxation_strategy_by_version_id) | **GET** /taxation-strategies/version/{version-ID} | Returns a single taxation-strategy, specified by the taxation-strategy-ID parameter.
[**retire_taxation_strategy**](TaxationstrategiesApi.md#retire_taxation_strategy) | **DELETE** /taxation-strategies/version/{version-ID} | Retires the taxation-strategy specified by taxation-strategy-ID parameter. Only the version of the tax which has an unbounded (null) validTill can be removed. Removing a tax change will make the previous tax come into effect. For example if you have a Tax in January and 5% and a new tax at 7% from February onwards, you can remove the February tax. Remove the February tax will re-instate the January tax.
[**update_taxation_strategy**](TaxationstrategiesApi.md#update_taxation_strategy) | **PUT** /taxation-strategies | Update a tax.


# **create_taxation_strategy**
> TaxationStrategyPagedMetadata create_taxation_strategy(taxation_strategy)

<p>Add a new tax or schedule changes in an existing tax.</p><p>Add a new tax by providing the location and tax percentage. To schedule a tax change specify the ID of the current Tax. A new version of the will be created <i>validFrom</i> the specified date, the existing tax <i>validTill</i> the start of this new tax.</p>

{\"nickname\":\"Create a tax\",\"request\":\"createTaxationStrategyRequest.html\",\"response\":\"createTaxationStrategyResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.TaxationstrategiesApi()
taxation_strategy = billforward.MutableBillingEntity() # MutableBillingEntity | The taxation-strategy object to be updated.

try: 
    # <p>Add a new tax or schedule changes in an existing tax.</p><p>Add a new tax by providing the location and tax percentage. To schedule a tax change specify the ID of the current Tax. A new version of the will be created <i>validFrom</i> the specified date, the existing tax <i>validTill</i> the start of this new tax.</p>
    api_response = api_instance.create_taxation_strategy(taxation_strategy)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TaxationstrategiesApi->create_taxation_strategy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxation_strategy** | [**MutableBillingEntity**](MutableBillingEntity.md)| The taxation-strategy object to be updated. | 

### Return type

[**TaxationStrategyPagedMetadata**](TaxationStrategyPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_taxation_strategies**
> TaxationStrategyPagedMetadata get_all_taxation_strategies(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of all taxation-strategies. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get all tax\",\"response\":\"getTaxationStrategyAll.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.TaxationstrategiesApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first taxation-strategy to return. (optional) (default to 0)
records = 10 # int | The maximum number of taxation-strategies to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired products should be returned. (optional) (default to false)

try: 
    # Returns a collection of all taxation-strategies. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_taxation_strategies(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TaxationstrategiesApi->get_all_taxation_strategies: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first taxation-strategy to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of taxation-strategies to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to false]

### Return type

[**TaxationStrategyPagedMetadata**](TaxationStrategyPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_taxation_strategy_by_consistent_id**
> TaxationStrategyPagedMetadata get_taxation_strategy_by_consistent_id(taxation_strategy_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns the tax currently being applied for the taxation-strategy-ID. To return schedule or historic tax changes the include_retired query parameter should be set to true.

{\"nickname\":\"Retrieve an existing tax \",\"response\":\"getTaxationStrategyByID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.TaxationstrategiesApi()
taxation_strategy_id = 'taxation_strategy_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first taxation-strategy to return. (optional) (default to 0)
records = 10 # int | The maximum number of taxation-strategies to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired products should be returned. (optional) (default to false)

try: 
    # Returns the tax currently being applied for the taxation-strategy-ID. To return schedule or historic tax changes the include_retired query parameter should be set to true.
    api_response = api_instance.get_taxation_strategy_by_consistent_id(taxation_strategy_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TaxationstrategiesApi->get_taxation_strategy_by_consistent_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxation_strategy_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first taxation-strategy to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of taxation-strategies to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to false]

### Return type

[**TaxationStrategyPagedMetadata**](TaxationStrategyPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_taxation_strategy_by_country**
> TaxationStrategyPagedMetadata get_taxation_strategy_by_country(country, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of taxation-strategies, specified by the country parameter. By default 10 values are returned. Records are returned in natural order. To return schedule or historic tax changes the include_retired query parameter should be set to true.

{\"nickname\":\"Retrieve by country\",\"response\":\"getTaxationStrategyByCountry.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.TaxationstrategiesApi()
country = 'country_example' # str | The country
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first taxation-strategy to return. (optional) (default to 0)
records = 10 # int | The maximum number of taxation-strategies to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired products should be returned. (optional) (default to false)

try: 
    # Returns a collection of taxation-strategies, specified by the country parameter. By default 10 values are returned. Records are returned in natural order. To return schedule or historic tax changes the include_retired query parameter should be set to true.
    api_response = api_instance.get_taxation_strategy_by_country(country, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TaxationstrategiesApi->get_taxation_strategy_by_country: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| The country | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first taxation-strategy to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of taxation-strategies to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to false]

### Return type

[**TaxationStrategyPagedMetadata**](TaxationStrategyPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_taxation_strategy_by_currency**
> TaxationStrategyPagedMetadata get_taxation_strategy_by_currency(currency, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of taxation-strategies, specified by the currency parameter. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by currency\",\"response\":\"getTaxationStrategyByProvince.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.TaxationstrategiesApi()
currency = 'currency_example' # str | The currency
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first taxation-strategy to return. (optional) (default to 0)
records = 10 # int | The maximum number of taxation-strategies to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired products should be returned. (optional) (default to false)

try: 
    # Returns a collection of taxation-strategies, specified by the currency parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_taxation_strategy_by_currency(currency, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TaxationstrategiesApi->get_taxation_strategy_by_currency: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| The currency | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first taxation-strategy to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of taxation-strategies to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to false]

### Return type

[**TaxationStrategyPagedMetadata**](TaxationStrategyPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_taxation_strategy_by_province**
> TaxationStrategyPagedMetadata get_taxation_strategy_by_province(province, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of taxation-strategies, specified by the province parameter. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by province\",\"response\":\"getTaxationStrategyByProvince.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.TaxationstrategiesApi()
province = 'province_example' # str | The province
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first taxation-strategy to return. (optional) (default to 0)
records = 10 # int | The maximum number of taxation-strategies to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired products should be returned. (optional) (default to false)

try: 
    # Returns a collection of taxation-strategies, specified by the province parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_taxation_strategy_by_province(province, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TaxationstrategiesApi->get_taxation_strategy_by_province: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **province** | **str**| The province | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first taxation-strategy to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of taxation-strategies to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to false]

### Return type

[**TaxationStrategyPagedMetadata**](TaxationStrategyPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_taxation_strategy_by_version_id**
> TaxationStrategyPagedMetadata get_taxation_strategy_by_version_id(version_id, organizations=organizations)

Returns a single taxation-strategy, specified by the taxation-strategy-ID parameter.

{\"nickname\":\"Retrieve by version\",\"response\":\"getTaxationStrategyByVersionID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.TaxationstrategiesApi()
version_id = 'version_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single taxation-strategy, specified by the taxation-strategy-ID parameter.
    api_response = api_instance.get_taxation_strategy_by_version_id(version_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TaxationstrategiesApi->get_taxation_strategy_by_version_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**TaxationStrategyPagedMetadata**](TaxationStrategyPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retire_taxation_strategy**
> TaxationStrategyPagedMetadata retire_taxation_strategy(version_id, organizations)

Retires the taxation-strategy specified by taxation-strategy-ID parameter. Only the version of the tax which has an unbounded (null) validTill can be removed. Removing a tax change will make the previous tax come into effect. For example if you have a Tax in January and 5% and a new tax at 7% from February onwards, you can remove the February tax. Remove the February tax will re-instate the January tax.

{\"nickname\":\"Remove a tax change\",\"response\":\"deleteSubscription.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.TaxationstrategiesApi()
version_id = 'version_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls.

try: 
    # Retires the taxation-strategy specified by taxation-strategy-ID parameter. Only the version of the tax which has an unbounded (null) validTill can be removed. Removing a tax change will make the previous tax come into effect. For example if you have a Tax in January and 5% and a new tax at 7% from February onwards, you can remove the February tax. Remove the February tax will re-instate the January tax.
    api_response = api_instance.retire_taxation_strategy(version_id, organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TaxationstrategiesApi->retire_taxation_strategy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | 

### Return type

[**TaxationStrategyPagedMetadata**](TaxationStrategyPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_taxation_strategy**
> TaxationStrategyPagedMetadata update_taxation_strategy(taxation_strategy)

Update a tax.

{\"nickname\":\"Update a tax\",\"request\":\"updateTaxationStrategyRequest.html\",\"response\":\"updateTaxationStrategyResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.TaxationstrategiesApi()
taxation_strategy = billforward.MutableBillingEntity() # MutableBillingEntity | The taxation-strategy object to be updated.

try: 
    # Update a tax.
    api_response = api_instance.update_taxation_strategy(taxation_strategy)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TaxationstrategiesApi->update_taxation_strategy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxation_strategy** | [**MutableBillingEntity**](MutableBillingEntity.md)| The taxation-strategy object to be updated. | 

### Return type

[**TaxationStrategyPagedMetadata**](TaxationStrategyPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

