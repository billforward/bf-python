# billforward.QuotesApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quote**](QuotesApi.md#quote) | **POST** /quotes | Returns a quote.


# **quote**
> APIQuotePagedMetadata quote(quote_request)

Returns a quote.

{\"nickname\":\"Returns a quote\",\"request\":\"PriceRequest.html\",\"response\":\"PriceCalculation.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.QuotesApi()
quote_request = billforward.QuoteRequest() # QuoteRequest | A quote request

try: 
    # Returns a quote.
    api_response = api_instance.quote(quote_request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling QuotesApi->quote: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_request** | [**QuoteRequest**](QuoteRequest.md)| A quote request | 

### Return type

[**APIQuotePagedMetadata**](APIQuotePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

