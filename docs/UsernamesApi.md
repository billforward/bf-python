# swagger_client.UsernamesApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_username**](UsernamesApi.md#create_username) | **POST** /usernames | Create a username.


# **create_username**
> UsernamePagedMetadata create_username(username)

Create a username.

{\"nickname\":\"Create\",\"request\":\"createUsernameRequest.html\",\"response\":\"createUsernameResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsernamesApi()
username = swagger_client.Username() # Username | The username object to be created.

try: 
    # Create a username.
    api_response = api_instance.create_username(username)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsernamesApi->create_username: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | [**Username**](Username.md)| The username object to be created. | 

### Return type

[**UsernamePagedMetadata**](UsernamePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

