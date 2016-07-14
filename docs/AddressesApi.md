# swagger_client.AddressesApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_address**](AddressesApi.md#create_address) | **POST** /addresses | Create
[**update_address**](AddressesApi.md#update_address) | **PUT** /addresses | Update


# **create_address**
> AddressPagedMetadata create_address(request)

Create

{\"nickname\":\"Create a new address\",\"response\":\"createAddressResponse.html\",\"request\":\"createAddressRequest.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AddressesApi()
request = swagger_client.CreateAddressRequest() # CreateAddressRequest | The address object to be created.

try: 
    # Create
    api_response = api_instance.create_address(request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AddressesApi->create_address: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreateAddressRequest**](CreateAddressRequest.md)| The address object to be created. | 

### Return type

[**AddressPagedMetadata**](AddressPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_address**
> AddressPagedMetadata update_address(request)

Update

{\"nickname\":\"Update an address\",\"response\":\"updateAddressResponse.html\",\"request\":\"updateAddressRequest.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AddressesApi()
request = swagger_client.UpdateAddressRequest() # UpdateAddressRequest | The address object to be created.

try: 
    # Update
    api_response = api_instance.update_address(request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AddressesApi->update_address: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**UpdateAddressRequest**](UpdateAddressRequest.md)| The address object to be created. | 

### Return type

[**AddressPagedMetadata**](AddressPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

