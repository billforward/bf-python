# billforward.QuotesApi

All URIs are relative to *https://app.billforward.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_quotes**](QuotesApi.md#get_all_quotes) | **GET** /quotes | 
[**get_quote_by_id**](QuotesApi.md#get_quote_by_id) | **GET** /quotes/{id} | 
[**quote**](QuotesApi.md#quote) | **POST** /quotes | 

# **get_all_quotes**
> InlineResponseDefault52 get_all_quotes(account_id=account_id, subscription_id=subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.QuotesApi(billforward.ApiClient(configuration))
account_id = ['account_id_example'] # list[str] |  (optional)
subscription_id = ['subscription_id_example'] # list[str] |  (optional)
organizations = ['organizations_example'] # list[str] |  (optional)
offset = 0 # int |  (optional) (default to 0)
records = 10 # int |  (optional) (default to 10)
order_by = 'created' # str |  (optional) (default to created)
order = 'DESC' # str |  (optional) (default to DESC)

try:
    api_response = api_instance.get_all_quotes(account_id=account_id, subscription_id=subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->get_all_quotes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**list[str]**](str.md)|  | [optional] 
 **subscription_id** | [**list[str]**](str.md)|  | [optional] 
 **organizations** | [**list[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **records** | **int**|  | [optional] [default to 10]
 **order_by** | **str**|  | [optional] [default to created]
 **order** | **str**|  | [optional] [default to DESC]

### Return type

[**InlineResponseDefault52**](InlineResponseDefault52.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quote_by_id**
> InlineResponseDefault53 get_quote_by_id(id, organizations=organizations)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.QuotesApi(billforward.ApiClient(configuration))
id = 'id_example' # str | 
organizations = ['organizations_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_quote_by_id(id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->get_quote_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponseDefault53**](InlineResponseDefault53.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote**
> InlineResponseDefault53 quote(body=body)



### Example
```python
from __future__ import print_function
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = billforward.QuotesApi(billforward.ApiClient(configuration))
body = billforward.QuoteRequest() # QuoteRequest |  (optional)

try:
    api_response = api_instance.quote(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->quote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuoteRequest**](QuoteRequest.md)|  | [optional] 

### Return type

[**InlineResponseDefault53**](InlineResponseDefault53.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

