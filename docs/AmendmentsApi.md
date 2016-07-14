# billforward.AmendmentsApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_amendment**](AmendmentsApi.md#create_amendment) | **POST** /amendments | Create an amendment.
[**get_all_amendments**](AmendmentsApi.md#get_all_amendments) | **GET** /amendments | Returns a collection of all amendments. By default 10 values are returned. Records are returned in natural order.
[**get_amendment_by_id**](AmendmentsApi.md#get_amendment_by_id) | **GET** /amendments/{amendment-ID} | Returns a single amendment, specified by the amendment-ID parameter.
[**get_amendment_by_state**](AmendmentsApi.md#get_amendment_by_state) | **GET** /amendments/state/{state} | Returns a collection of amendments, specified by the state parameter. By default 10 values are returned. Records are returned in natural order.
[**get_amendment_by_subscription_id**](AmendmentsApi.md#get_amendment_by_subscription_id) | **GET** /amendments/subscription/{subscription-ID} | Returns a collection of amendments, specified by the subscription-ID parameter. By default 10 values are returned. Records are returned in natural order.
[**get_amendment_swagger**](AmendmentsApi.md#get_amendment_swagger) | **GET** /amendments/swagger-end-point/{query-string} | 
[**get_amendments_by_actioning_time**](AmendmentsApi.md#get_amendments_by_actioning_time) | **GET** /amendments/actioning-time/{lower-threshold}/{upper-threshold} | Returns a collection of amendment objects with an actioning-time within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.
[**get_amendments_by_created_date**](AmendmentsApi.md#get_amendments_by_created_date) | **GET** /amendments/created/{lower-threshold}/{upper-threshold} | Returns a collection of amendment objects with created times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.
[**get_amendments_by_updated_date**](AmendmentsApi.md#get_amendments_by_updated_date) | **GET** /amendments/updated/{lower-threshold}/{upper-threshold} | Returns a collection of amendment objects with updated times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.
[**retire_amendment**](AmendmentsApi.md#retire_amendment) | **DELETE** /amendments/{amendment-ID} | Retires the amendment specified by the amendment-ID parameter. Retiring a amendment causes it to cancel based on the specificed retirement settings for the product.
[**update_amendment**](AmendmentsApi.md#update_amendment) | **PUT** /amendments | Update an amendment.


# **create_amendment**
> AmendmentPagedMetadata create_amendment(amendment)

Create an amendment.

{\"nickname\":\"Create a new amendment\",\"request\":\"createAmendmentRequest.html\",\"response\":\"createAmendmentResponse.html\" }

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.AmendmentsApi()
amendment = billforward.Amendment() # Amendment | The amendment object to be created.

try: 
    # Create an amendment.
    api_response = api_instance.create_amendment(amendment)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AmendmentsApi->create_amendment: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amendment** | [**Amendment**](Amendment.md)| The amendment object to be created. | 

### Return type

[**AmendmentPagedMetadata**](AmendmentPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_amendments**
> AmendmentPagedMetadata get_all_amendments(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, invoice_id=invoice_id, state=state, type=type)

Returns a collection of all amendments. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get all amendments\",\"response\":\"getAmendmentAll.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.AmendmentsApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first amendment to return. (optional) (default to 0)
records = 10 # int | The maximum number of amendments to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
invoice_id = 'invoice_id_example' # str | Ihe invoice ID associated with the amendment. (optional)
state = 'state_example' # str | Ihe state of the amendment. (optional)
type = 'type_example' # str | Ihe type of amendment. (optional)

try: 
    # Returns a collection of all amendments. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_amendments(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, invoice_id=invoice_id, state=state, type=type)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AmendmentsApi->get_all_amendments: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first amendment to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of amendments to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **invoice_id** | **str**| Ihe invoice ID associated with the amendment. | [optional] 
 **state** | **str**| Ihe state of the amendment. | [optional] 
 **type** | **str**| Ihe type of amendment. | [optional] 

### Return type

[**AmendmentPagedMetadata**](AmendmentPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_amendment_by_id**
> AmendmentPagedMetadata get_amendment_by_id(amendment_id, organizations=organizations)

Returns a single amendment, specified by the amendment-ID parameter.

{\"nickname\":\"Retrieve an existing amendment\",\"response\":\"getAmendmentByID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.AmendmentsApi()
amendment_id = 'amendment_id_example' # str | The unique string-ID of the amendment.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single amendment, specified by the amendment-ID parameter.
    api_response = api_instance.get_amendment_by_id(amendment_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AmendmentsApi->get_amendment_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amendment_id** | **str**| The unique string-ID of the amendment. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**AmendmentPagedMetadata**](AmendmentPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_amendment_by_state**
> AmendmentPagedMetadata get_amendment_by_state(state, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Returns a collection of amendments, specified by the state parameter. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by state\",\"response\":\"getAmendmentsByState.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.AmendmentsApi()
state = 'state_example' # str | The current state of the amendment, either pending, succeeded, failed or discarded
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first amendment to return. (optional) (default to 0)
records = 10 # int | The maximum number of amendments to return. (optional) (default to 10)
order_by = 'id' # str | Specify a field used to order the result set. (optional) (default to id)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Returns a collection of amendments, specified by the state parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_amendment_by_state(state, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AmendmentsApi->get_amendment_by_state: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| The current state of the amendment, either pending, succeeded, failed or discarded | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first amendment to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of amendments to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to id]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**AmendmentPagedMetadata**](AmendmentPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_amendment_by_subscription_id**
> AmendmentPagedMetadata get_amendment_by_subscription_id(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Returns a collection of amendments, specified by the subscription-ID parameter. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by subscription\",\"response\":\"getAmendmentsBySubscription.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.AmendmentsApi()
subscription_id = 'subscription_id_example' # str | ID of the subscription
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first amendment to return. (optional) (default to 0)
records = 10 # int | The maximum number of amendments to return. (optional) (default to 10)
order_by = 'id' # str | Specify a field used to order the result set. (optional) (default to id)
order = 'DESC' # str | The direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Returns a collection of amendments, specified by the subscription-ID parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_amendment_by_subscription_id(subscription_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AmendmentsApi->get_amendment_by_subscription_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| ID of the subscription | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first amendment to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of amendments to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to id]
 **order** | **str**| The direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**AmendmentPagedMetadata**](AmendmentPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_amendment_swagger**
> SwaggerTypeList get_amendment_swagger(query_string, organizations=organizations, offset=offset, records=records, wildcard=wildcard, entity=entity)



{\"nickname\":\"\",\"response\":\"\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.AmendmentsApi()
query_string = 'query_string_example' # str | The query string used to search.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The starting index of the search results. (optional) (default to 0)
records = 10 # int | The number of search results to return. (optional) (default to 10)
wildcard = false # bool | Toggle if we search for full words or whether a wildcard is used. (optional) (default to false)
entity = false # bool | Is an entity returned with the search results. (optional) (default to false)

try: 
    # 
    api_response = api_instance.get_amendment_swagger(query_string, organizations=organizations, offset=offset, records=records, wildcard=wildcard, entity=entity)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AmendmentsApi->get_amendment_swagger: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_string** | **str**| The query string used to search. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The starting index of the search results. | [optional] [default to 0]
 **records** | **int**| The number of search results to return. | [optional] [default to 10]
 **wildcard** | **bool**| Toggle if we search for full words or whether a wildcard is used. | [optional] [default to false]
 **entity** | **bool**| Is an entity returned with the search results. | [optional] [default to false]

### Return type

[**SwaggerTypeList**](SwaggerTypeList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_amendments_by_actioning_time**
> AmendmentPagedMetadata get_amendments_by_actioning_time(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Returns a collection of amendment objects with an actioning-time within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by actioning\",\"response\":\"getAmendmentByActioningTime.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.AmendmentsApi()
lower_threshold = 'lower_threshold_example' # str | The UTC DateTime specifying the start of the result period.
upper_threshold = 'upper_threshold_example' # str | The UTC DateTime specifying the end of the result period.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first amendment to return. (optional) (default to 0)
records = 10 # int | The maximum number of amendments to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Returns a collection of amendment objects with an actioning-time within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_amendments_by_actioning_time(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AmendmentsApi->get_amendments_by_actioning_time: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lower_threshold** | **str**| The UTC DateTime specifying the start of the result period. | 
 **upper_threshold** | **str**| The UTC DateTime specifying the end of the result period. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first amendment to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of amendments to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**AmendmentPagedMetadata**](AmendmentPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_amendments_by_created_date**
> AmendmentPagedMetadata get_amendments_by_created_date(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Returns a collection of amendment objects with created times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by creation\",\"response\":\"getAmendmentByCreated.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.AmendmentsApi()
lower_threshold = 'lower_threshold_example' # str | The UTC DateTime specifying the start of the result period.
upper_threshold = 'upper_threshold_example' # str | The UTC DateTime specifying the end of the result period.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first amendment to return. (optional) (default to 0)
records = 10 # int | The maximum number of amendments to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Returns a collection of amendment objects with created times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_amendments_by_created_date(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AmendmentsApi->get_amendments_by_created_date: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lower_threshold** | **str**| The UTC DateTime specifying the start of the result period. | 
 **upper_threshold** | **str**| The UTC DateTime specifying the end of the result period. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first amendment to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of amendments to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**AmendmentPagedMetadata**](AmendmentPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_amendments_by_updated_date**
> AmendmentPagedMetadata get_amendments_by_updated_date(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Returns a collection of amendment objects with updated times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by updated\",\"response\":\"getAmendmentByUpdated.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.AmendmentsApi()
lower_threshold = 'lower_threshold_example' # str | The UTC DateTime specifying the start of the result period.
upper_threshold = 'upper_threshold_example' # str | The UTC DateTime specifying the end of the result period.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first amendment to return. (optional) (default to 0)
records = 10 # int | The maximum number of amendments to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Returns a collection of amendment objects with updated times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_amendments_by_updated_date(lower_threshold, upper_threshold, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AmendmentsApi->get_amendments_by_updated_date: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lower_threshold** | **str**| The UTC DateTime specifying the start of the result period. | 
 **upper_threshold** | **str**| The UTC DateTime specifying the end of the result period. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first amendment to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of amendments to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**AmendmentPagedMetadata**](AmendmentPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retire_amendment**
> AmendmentPagedMetadata retire_amendment(amendment_id, organizations)

Retires the amendment specified by the amendment-ID parameter. Retiring a amendment causes it to cancel based on the specificed retirement settings for the product.

{\"nickname\":\"Delete an amendment\",\"response\":\"deleteAmendment.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.AmendmentsApi()
amendment_id = 'amendment_id_example' # str | ID of the amendment.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls.

try: 
    # Retires the amendment specified by the amendment-ID parameter. Retiring a amendment causes it to cancel based on the specificed retirement settings for the product.
    api_response = api_instance.retire_amendment(amendment_id, organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AmendmentsApi->retire_amendment: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amendment_id** | **str**| ID of the amendment. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | 

### Return type

[**AmendmentPagedMetadata**](AmendmentPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_amendment**
> AmendmentPagedMetadata update_amendment(amendment)

Update an amendment.

{\"nickname\":\"Update an amendment\",\"request\":\"updateAmendmentRequest.html\",\"response\":\"updateAmendmentResponse.html\" }

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.AmendmentsApi()
amendment = billforward.Amendment() # Amendment | The amendment object to be updated.

try: 
    # Update an amendment.
    api_response = api_instance.update_amendment(amendment)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AmendmentsApi->update_amendment: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amendment** | [**Amendment**](Amendment.md)| The amendment object to be updated. | 

### Return type

[**AmendmentPagedMetadata**](AmendmentPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

