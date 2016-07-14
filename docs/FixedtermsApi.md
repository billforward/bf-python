# billforward.FixedtermsApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_fixed_term**](FixedtermsApi.md#update_fixed_term) | **PUT** /fixed-terms | Update


# **update_fixed_term**
> FixedTermPagedMetadata update_fixed_term(payment_method)

Update

{\"nickname\":\"Update a fixed term\",\"request\":\"updateFixedTermRequest.html\",\"response\":\"updateFixedTermResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.FixedtermsApi()
payment_method = billforward.FixedTerm() # FixedTerm | The payment-method object to be updated.

try: 
    # Update
    api_response = api_instance.update_fixed_term(payment_method)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FixedtermsApi->update_fixed_term: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method** | [**FixedTerm**](FixedTerm.md)| The payment-method object to be updated. | 

### Return type

[**FixedTermPagedMetadata**](FixedTermPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

