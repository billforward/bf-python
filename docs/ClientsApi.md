# swagger_client.ClientsApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client**](ClientsApi.md#create_client) | **POST** /clients | Create a client.
[**get_all_clients**](ClientsApi.md#get_all_clients) | **GET** /clients | Returns a collection of clients.
[**get_client_by_id**](ClientsApi.md#get_client_by_id) | **GET** /clients/{client-ID} | Returns a single client, specified by the client-ID parameter.
[**update_client**](ClientsApi.md#update_client) | **PUT** /clients | Update a client.


# **create_client**
> ClientPagedMetadata create_client(client)

Create a client.

{\"nickname\":\"Create\",\"request\":\"createClientRequest.html\",\"response\":\"createClientResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientsApi()
client = swagger_client.Client() # Client | The client object to be updated.

try: 
    # Create a client.
    api_response = api_instance.create_client(client)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClientsApi->create_client: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client** | [**Client**](Client.md)| The client object to be updated. | 

### Return type

[**ClientPagedMetadata**](ClientPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_clients**
> ClientPagedMetadata get_all_clients(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of clients.

{\"nickname\":\"Get All\",\"response\":\"getClientAll.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientsApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first client to return. (optional) (default to 0)
records = 10 # int | The maximum number of clients to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)

try: 
    # Returns a collection of clients.
    api_response = api_instance.get_all_clients(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClientsApi->get_all_clients: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first client to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of clients to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]

### Return type

[**ClientPagedMetadata**](ClientPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_by_id**
> ClientPagedMetadata get_client_by_id(client_id, organizations=organizations)

Returns a single client, specified by the client-ID parameter.

{\"nickname\":\"Retrieve by id\",\"response\":\"getClientByID.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientsApi()
client_id = 'client_id_example' # str | The string ID of the client.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single client, specified by the client-ID parameter.
    api_response = api_instance.get_client_by_id(client_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClientsApi->get_client_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The string ID of the client. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**ClientPagedMetadata**](ClientPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client**
> ClientPagedMetadata update_client(client)

Update a client.

{\"nickname\":\"Update\",\"request\":\"updateClientRequest.html\",\"response\":\"updateClientResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientsApi()
client = swagger_client.Client() # Client | The client object to be updated.

try: 
    # Update a client.
    api_response = api_instance.update_client(client)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClientsApi->update_client: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client** | [**Client**](Client.md)| The client object to be updated. | 

### Return type

[**ClientPagedMetadata**](ClientPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

