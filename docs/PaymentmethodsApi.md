# swagger_client.PaymentmethodsApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_method**](PaymentmethodsApi.md#create_payment_method) | **POST** /payment-methods | Create a payment-method.
[**delete_payment_method**](PaymentmethodsApi.md#delete_payment_method) | **DELETE** /payment-methods/{payment-method-ID} | Deletes the payment-method specified by the payment-method-ID parameter.
[**get_all_payment_methods**](PaymentmethodsApi.md#get_all_payment_methods) | **GET** /payment-methods | Returns a collection of all payment-methods. By default 10 values are returned. Records are returned in natural order.
[**get_payment_method_by_account_id**](PaymentmethodsApi.md#get_payment_method_by_account_id) | **GET** /payment-methods/account/{account-ID} | Returns a collection of payment-methods, specified by the account-ID parameter. By default 10 values are returned. Records are returned in natural order.
[**get_payment_method_by_id**](PaymentmethodsApi.md#get_payment_method_by_id) | **GET** /payment-methods/{payment-method-ID} | Returns a single payment-method, specified by the payment-method-ID parameter.
[**get_payment_method_by_link_id**](PaymentmethodsApi.md#get_payment_method_by_link_id) | **GET** /payment-methods/link-id/{linkID} | Returns a single payment-method, specified by the linkID parameter.
[**get_payment_method_by_payment_gateway**](PaymentmethodsApi.md#get_payment_method_by_payment_gateway) | **GET** /payment-methods/gateway/{gateway} | Returns a collection of payment-methods, specified by the gateway parameter. By default 10 values are returned. Records are returned in natural order.
[**update_payment_method**](PaymentmethodsApi.md#update_payment_method) | **PUT** /payment-methods | Update a payment-method.


# **create_payment_method**
> PaymentMethodPagedMetadata create_payment_method(payment_method)

Create a payment-method.

{\"nickname\":\"Create a new payment method\",\"request\":\"createPaymentMethodRequest.html\",\"response\":\"createPaymentMethodResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentmethodsApi()
payment_method = swagger_client.PaymentMethod() # PaymentMethod | The payment-method object to be updated.

try: 
    # Create a payment-method.
    api_response = api_instance.create_payment_method(payment_method)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PaymentmethodsApi->create_payment_method: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method** | [**PaymentMethod**](PaymentMethod.md)| The payment-method object to be updated. | 

### Return type

[**PaymentMethodPagedMetadata**](PaymentMethodPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_payment_method**
> PaymentMethodPagedMetadata delete_payment_method(payment_method_id, organizations=organizations)

Deletes the payment-method specified by the payment-method-ID parameter.

{\"nickname\":\"Delete payment method\",\"response\":\"deletePaymentMethod.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentmethodsApi()
payment_method_id = 'payment_method_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Deletes the payment-method specified by the payment-method-ID parameter.
    api_response = api_instance.delete_payment_method(payment_method_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PaymentmethodsApi->delete_payment_method: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**PaymentMethodPagedMetadata**](PaymentMethodPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_payment_methods**
> PaymentMethodPagedMetadata get_all_payment_methods(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of all payment-methods. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get all payment methods\",\"response\":\"getPaymentMethodAll.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentmethodsApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first payment-method to return. (optional) (default to 0)
records = 10 # int | The maximum number of payment-methods to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)

try: 
    # Returns a collection of all payment-methods. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_payment_methods(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PaymentmethodsApi->get_all_payment_methods: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first payment-method to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of payment-methods to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]

### Return type

[**PaymentMethodPagedMetadata**](PaymentMethodPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_method_by_account_id**
> PaymentMethodPagedMetadata get_payment_method_by_account_id(account_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, default_only=default_only)

Returns a collection of payment-methods, specified by the account-ID parameter. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by account\",\"response\":\"getPaymentMethodByAccount.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentmethodsApi()
account_id = 'account_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first payment-method to return. (optional) (default to 0)
records = 10 # int | The maximum number of payment-methods to return. (optional) (default to 10)
order_by = 'id' # str | Specify a field used to order the result set. (optional) (default to id)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)
default_only = false # bool | Whether only the defualt payment method should be returned. (optional) (default to false)

try: 
    # Returns a collection of payment-methods, specified by the account-ID parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_payment_method_by_account_id(account_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, default_only=default_only)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PaymentmethodsApi->get_payment_method_by_account_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first payment-method to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of payment-methods to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to id]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]
 **default_only** | **bool**| Whether only the defualt payment method should be returned. | [optional] [default to false]

### Return type

[**PaymentMethodPagedMetadata**](PaymentMethodPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_method_by_id**
> PaymentMethodPagedMetadata get_payment_method_by_id(payment_method_id, organizations=organizations)

Returns a single payment-method, specified by the payment-method-ID parameter.

{\"nickname\":\"Get existing payment method\",\"response\":\"getPaymentMethodByID.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentmethodsApi()
payment_method_id = 'payment_method_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single payment-method, specified by the payment-method-ID parameter.
    api_response = api_instance.get_payment_method_by_id(payment_method_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PaymentmethodsApi->get_payment_method_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**PaymentMethodPagedMetadata**](PaymentMethodPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_method_by_link_id**
> PaymentMethodPagedMetadata get_payment_method_by_link_id(link_id, organizations=organizations)

Returns a single payment-method, specified by the linkID parameter.

{\"nickname\":\"Retrieve by subscription link\",\"response\":\"getPaymentMethodByLinkID.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentmethodsApi()
link_id = 'link_id_example' # str | The link-id of the payment-method.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single payment-method, specified by the linkID parameter.
    api_response = api_instance.get_payment_method_by_link_id(link_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PaymentmethodsApi->get_payment_method_by_link_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_id** | **str**| The link-id of the payment-method. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**PaymentMethodPagedMetadata**](PaymentMethodPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_method_by_payment_gateway**
> PaymentMethodPagedMetadata get_payment_method_by_payment_gateway(gateway, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of payment-methods, specified by the gateway parameter. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by gateway\",\"response\":\"getPaymentMethodByGateway.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentmethodsApi()
gateway = 'gateway_example' # str | The payment-method gateway which generated the payment-method.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first payment-method to return. (optional) (default to 0)
records = 10 # int | The maximum number of payment-methods to return. (optional) (default to 10)
order_by = 'id' # str | Specify a field used to order the result set. (optional) (default to id)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)

try: 
    # Returns a collection of payment-methods, specified by the gateway parameter. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_payment_method_by_payment_gateway(gateway, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PaymentmethodsApi->get_payment_method_by_payment_gateway: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway** | **str**| The payment-method gateway which generated the payment-method. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first payment-method to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of payment-methods to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to id]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]

### Return type

[**PaymentMethodPagedMetadata**](PaymentMethodPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payment_method**
> PaymentMethodPagedMetadata update_payment_method(payment_method)

Update a payment-method.

{\"nickname\":\"Update a payment-method\",\"request\":\"updatePaymentMethodRequest.html\",\"response\":\"updatePaymentMethodResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentmethodsApi()
payment_method = swagger_client.PaymentMethod() # PaymentMethod | The payment-method object to be updated.

try: 
    # Update a payment-method.
    api_response = api_instance.update_payment_method(payment_method)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PaymentmethodsApi->update_payment_method: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method** | [**PaymentMethod**](PaymentMethod.md)| The payment-method object to be updated. | 

### Return type

[**PaymentMethodPagedMetadata**](PaymentMethodPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

