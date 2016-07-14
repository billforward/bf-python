# billforward.TimeApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_time_swagger**](TimeApi.md#get_time_swagger) | **GET** /time/swagger-end-point | 


# **get_time_swagger**
> TimeResponsePagedMetadata get_time_swagger(request)



{\"nickname\":\"\",\"request\":\"advanceSubscriptionRequest.html\",\"response\":\"advanceSubscription.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.TimeApi()
request = billforward.TimeRequest() # TimeRequest | The request

try: 
    # 
    api_response = api_instance.get_time_swagger(request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TimeApi->get_time_swagger: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**TimeRequest**](TimeRequest.md)| The request | 

### Return type

[**TimeResponsePagedMetadata**](TimeResponsePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

