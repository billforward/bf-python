# swagger_client.PasswordsApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_password**](PasswordsApi.md#create_password) | **POST** /passwords | Create


# **create_password**
> PasswordPagedMetadata create_password(password)

Create

{\"nickname\":\"Create\",\"request\":\"createPasswordRequest.html\",\"response\":\"createPasswordResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PasswordsApi()
password = swagger_client.Password() # Password | The password object to be created.

try: 
    # Create
    api_response = api_instance.create_password(password)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PasswordsApi->create_password: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password** | [**Password**](Password.md)| The password object to be created. | 

### Return type

[**PasswordPagedMetadata**](PasswordPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

