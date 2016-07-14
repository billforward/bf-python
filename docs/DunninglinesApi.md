# swagger_client.DunninglinesApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dunning_line**](DunninglinesApi.md#create_dunning_line) | **POST** /dunning-lines | Create a dunning-line.
[**get_all_dunning_lines**](DunninglinesApi.md#get_all_dunning_lines) | **GET** /dunning-lines | Returns a collection of all dunning-lines. By default 10 values are returned. Records are returned in natural order.
[**get_dunning_line_by_attempt_index**](DunninglinesApi.md#get_dunning_line_by_attempt_index) | **GET** /dunning-lines/attempt-index/{index} | Returns a collection of dunning-lines specified by the index parameter. By default 10 values are returned. Records are returned in natural order.
[**get_dunning_line_by_id**](DunninglinesApi.md#get_dunning_line_by_id) | **GET** /dunning-lines/{dunning-line-ID} | Returns a single dunning-line, specified by the dunning-line-ID parameter.
[**retire_dunning_line**](DunninglinesApi.md#retire_dunning_line) | **DELETE** /dunning-lines/{dunning-line-ID} | Retires the specified dunning-line.
[**update_dunning_line**](DunninglinesApi.md#update_dunning_line) | **PUT** /dunning-lines | Update a dunning-line.


# **create_dunning_line**
> DunningLinePagedMetadata create_dunning_line(dunning_line)

Create a dunning-line.

{\"nickname\":\"Create a new dunning line\",\"request\":\"createDunningLineRequest.html\",\"response\":\"createDunningLineResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DunninglinesApi()
dunning_line = swagger_client.DunningLine() # DunningLine | The Dunning-Line object to be updated.

try: 
    # Create a dunning-line.
    api_response = api_instance.create_dunning_line(dunning_line)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DunninglinesApi->create_dunning_line: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dunning_line** | [**DunningLine**](DunningLine.md)| The Dunning-Line object to be updated. | 

### Return type

[**DunningLinePagedMetadata**](DunningLinePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_dunning_lines**
> DunningLinePagedMetadata get_all_dunning_lines(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of all dunning-lines. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get all dunning lines\",\"response\":\"getDunningLineByID.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DunninglinesApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first invoice to return. (optional) (default to 0)
records = 10 # int | The maximum number of invoices to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)

try: 
    # Returns a collection of all dunning-lines. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_dunning_lines(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DunninglinesApi->get_all_dunning_lines: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first invoice to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of invoices to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]

### Return type

[**DunningLinePagedMetadata**](DunningLinePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dunning_line_by_attempt_index**
> DunningLinePagedMetadata get_dunning_line_by_attempt_index(index, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of dunning-lines specified by the index parameter. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by attempt\",\"response\":\"getDunningLineByID.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DunninglinesApi()
index = 56 # int | The attempt index of the dunning-line.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first invoice to return. (optional) (default to 0)
records = 10 # int | The maximum number of invoices to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)

try: 
    # Returns a collection of dunning-lines specified by the index parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_dunning_line_by_attempt_index(index, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DunninglinesApi->get_dunning_line_by_attempt_index: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| The attempt index of the dunning-line. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first invoice to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of invoices to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]

### Return type

[**DunningLinePagedMetadata**](DunningLinePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dunning_line_by_id**
> DunningLinePagedMetadata get_dunning_line_by_id(dunning_line_id, organizations=organizations)

Returns a single dunning-line, specified by the dunning-line-ID parameter.

{\"nickname\":\"Retrieve an existing dunning line\",\"response\":\"getDunningLineByID.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DunninglinesApi()
dunning_line_id = 'dunning_line_id_example' # str | ID of the dunning-line.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single dunning-line, specified by the dunning-line-ID parameter.
    api_response = api_instance.get_dunning_line_by_id(dunning_line_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DunninglinesApi->get_dunning_line_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dunning_line_id** | **str**| ID of the dunning-line. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**DunningLinePagedMetadata**](DunningLinePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retire_dunning_line**
> DunningLinePagedMetadata retire_dunning_line(dunning_line_id, organizations)

Retires the specified dunning-line.

{\"nickname\":\"Delete a dunning line\",\"response\":\"deleteDunningLine.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DunninglinesApi()
dunning_line_id = 'dunning_line_id_example' # str | ID of the dunning-line.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls.

try: 
    # Retires the specified dunning-line.
    api_response = api_instance.retire_dunning_line(dunning_line_id, organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DunninglinesApi->retire_dunning_line: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dunning_line_id** | **str**| ID of the dunning-line. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | 

### Return type

[**DunningLinePagedMetadata**](DunningLinePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dunning_line**
> DunningLinePagedMetadata update_dunning_line(dunning_line)

Update a dunning-line.

{\"nickname\":\"Update a dunning line\",\"request\":\"updateDunningLineRequest.html\",\"response\":\"updateDunningLineResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DunninglinesApi()
dunning_line = swagger_client.DunningLine() # DunningLine | The Dunning-Line object to be updated.

try: 
    # Update a dunning-line.
    api_response = api_instance.update_dunning_line(dunning_line)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DunninglinesApi->update_dunning_line: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dunning_line** | [**DunningLine**](DunningLine.md)| The Dunning-Line object to be updated. | 

### Return type

[**DunningLinePagedMetadata**](DunningLinePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

