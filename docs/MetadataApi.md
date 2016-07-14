# billforward.MetadataApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_metadata_key_values**](MetadataApi.md#delete_metadata_key_values) | **DELETE** /metadata | Remove any associated metadata.
[**get_metadata_key_values**](MetadataApi.md#get_metadata_key_values) | **GET** /metadata | Retrieve any associated metadata.
[**set_metadata_key_values**](MetadataApi.md#set_metadata_key_values) | **POST** /metadata | Remove any existing metadata keys and create the provided data.
[**upsert_metadata_key_values**](MetadataApi.md#upsert_metadata_key_values) | **PUT** /metadata | Update any existing metadata key-values and insert any new key-values, no keys will be removed.


# **delete_metadata_key_values**
> DynamicMetadata delete_metadata_key_values(organizations=organizations)

Remove any associated metadata.

{\"nickname\":\"Clear metadata from organization\",\"request\" :\"deleteOrganizationMetadataRequest.html\",\"response\":\"deleteOrganizationMetadataResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.MetadataApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Remove any associated metadata.
    api_response = api_instance.delete_metadata_key_values(organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MetadataApi->delete_metadata_key_values: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**DynamicMetadata**](DynamicMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_key_values**
> DynamicMetadata get_metadata_key_values(organizations=organizations)

Retrieve any associated metadata.

{\"nickname\":\"Retrieve metadata on organization\",\"request\":\"getOrganizationMetadataRequest.html\",\"response\":\"getOrganizationMetadataResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.MetadataApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Retrieve any associated metadata.
    api_response = api_instance.get_metadata_key_values(organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MetadataApi->get_metadata_key_values: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**DynamicMetadata**](DynamicMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_metadata_key_values**
> DynamicMetadata set_metadata_key_values(metadata, organizations=organizations)

Remove any existing metadata keys and create the provided data.

{\"nickname\":\"Set metadata on organization\",\"request\":\"setOrganizationMetadataRequest.html\",\"response\":\"setOrganizationMetadataResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.MetadataApi()
metadata = billforward.DynamicMetadata() # DynamicMetadata | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Remove any existing metadata keys and create the provided data.
    api_response = api_instance.set_metadata_key_values(metadata, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MetadataApi->set_metadata_key_values: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata** | [**DynamicMetadata**](DynamicMetadata.md)|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**DynamicMetadata**](DynamicMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_metadata_key_values**
> DynamicMetadata upsert_metadata_key_values(metadata, organizations=organizations)

Update any existing metadata key-values and insert any new key-values, no keys will be removed.

{\"nickname\":\"Upsert metadata on organization\",\"request\":\"upsertOrganizationMetadataRequest.html\",\"response\":\"upsertOrganizationMetadataResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.MetadataApi()
metadata = billforward.DynamicMetadata() # DynamicMetadata | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Update any existing metadata key-values and insert any new key-values, no keys will be removed.
    api_response = api_instance.upsert_metadata_key_values(metadata, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MetadataApi->upsert_metadata_key_values: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata** | [**DynamicMetadata**](DynamicMetadata.md)|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**DynamicMetadata**](DynamicMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

