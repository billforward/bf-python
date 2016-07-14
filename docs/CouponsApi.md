# swagger_client.CouponsApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_coupon**](CouponsApi.md#create_coupon) | **POST** /coupons | Create a coupon.
[**create_coupon_unique_codes**](CouponsApi.md#create_coupon_unique_codes) | **POST** /coupons/{code}/codes | Create a list of unique coupon codes that can be applied to a subscription.
[**get_all_coupons**](CouponsApi.md#get_all_coupons) | **GET** /coupons | Returns a collection of all coupons. By default 10 values are returned. Records are returned in natural order.
[**get_applied_coupons**](CouponsApi.md#get_applied_coupons) | **GET** /coupons/{code}/applied | Returns a list of unique coupons which have been applied.
[**get_available_coupon_codes_for_code**](CouponsApi.md#get_available_coupon_codes_for_code) | **GET** /coupons/{code}/codes | Returns a list of available unique coupon codes for the specified parent coupon code that can be applied to a subscription.
[**get_coupon_code**](CouponsApi.md#get_coupon_code) | **GET** /coupons/{code} | Returns the coupon for the specified code that can be applied to a subscription.
[**get_subscription_applications_of_coupons**](CouponsApi.md#get_subscription_applications_of_coupons) | **GET** /coupons/{code}/subscriptions | Retrieves a collection of the coupons by this coupon code which have been applied.
[**retire_coupon**](CouponsApi.md#retire_coupon) | **DELETE** /coupons/{code} | &lt;p&gt;This method has 2 main behaviours depending on what is passed in. If the parent coupon code, for example SUMMER, is given no new coupons can be issued or claimed from this code. Deleting will result in the deleted property being set to true.&lt;/p&gt;&lt;p&gt;If a unique coupon code, for example SUMMER-AGH8, is given this will stop the coupon from being applied to the subscription from that point onwards. When a coupon is deleted the validUntil property is set which is the date/time it stopped applying to the target.&lt;/p&gt;


# **create_coupon**
> CouponPagedMetadata create_coupon(code)

Create a coupon.

{\"nickname\":\"Create a new coupon\",\"request\":\"createCouponRequest.html\",\"response\":\"createCouponResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CouponsApi()
code = swagger_client.Coupon() # Coupon | The coupon object to be created.

try: 
    # Create a coupon.
    api_response = api_instance.create_coupon(code)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponsApi->create_coupon: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | [**Coupon**](Coupon.md)| The coupon object to be created. | 

### Return type

[**CouponPagedMetadata**](CouponPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_coupon_unique_codes**
> CouponUniqueCodesResponsePagedMetadata create_coupon_unique_codes(code, request=request)

Create a list of unique coupon codes that can be applied to a subscription.

{ \"nickname\":\"Create unique coupon codes\",\"request\":\"createUniqueCodesRequest.html\",\"response\":\"createUniqueCodesResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CouponsApi()
code = 'code_example' # str | The coupon code to use in the generation of the unique codes.
request = swagger_client.CouponUniqueCodesRequest() # CouponUniqueCodesRequest | The request object that specifies the number of codes to be created. (optional)

try: 
    # Create a list of unique coupon codes that can be applied to a subscription.
    api_response = api_instance.create_coupon_unique_codes(code, request=request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponsApi->create_coupon_unique_codes: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The coupon code to use in the generation of the unique codes. | 
 **request** | [**CouponUniqueCodesRequest**](CouponUniqueCodesRequest.md)| The request object that specifies the number of codes to be created. | [optional] 

### Return type

[**CouponUniqueCodesResponsePagedMetadata**](CouponUniqueCodesResponsePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_coupons**
> CouponPagedMetadata get_all_coupons(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of all coupons. By default 10 values are returned. Records are returned in natural order.

{ \"nickname\":\"Retrieve all coupons\",\"response\":\"getCouponAll.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CouponsApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first subscription to return. (optional) (default to 0)
records = 10 # int | The maximum number of subscriptions to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired subscriptions should be returned. (optional) (default to false)

try: 
    # Returns a collection of all coupons. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_coupons(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponsApi->get_all_coupons: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first subscription to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of subscriptions to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired subscriptions should be returned. | [optional] [default to false]

### Return type

[**CouponPagedMetadata**](CouponPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_applied_coupons**
> CouponPagedMetadata get_applied_coupons(code, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a list of unique coupons which have been applied.

{ \"nickname\":\"Retrieve used unique coupons\",\"response\":\"getAppliedCodesForCode.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CouponsApi()
code = 'code_example' # str | The base code to use in the generation of the unique codes.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first subscription to return. (optional) (default to 0)
records = 10 # int | The maximum number of subscriptions to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired subscriptions should be returned. (optional) (default to false)

try: 
    # Returns a list of unique coupons which have been applied.
    api_response = api_instance.get_applied_coupons(code, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponsApi->get_applied_coupons: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The base code to use in the generation of the unique codes. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first subscription to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of subscriptions to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired subscriptions should be returned. | [optional] [default to false]

### Return type

[**CouponPagedMetadata**](CouponPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_coupon_codes_for_code**
> CouponUniqueCodesResponsePagedMetadata get_available_coupon_codes_for_code(code, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a list of available unique coupon codes for the specified parent coupon code that can be applied to a subscription.

{ \"nickname\":\"Retrieve unused unique coupons\",\"response\":\"getAvailableCodesForCode.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CouponsApi()
code = 'code_example' # str | The base code to use in the generation of the unique codes.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first subscription to return. (optional) (default to 0)
records = 10 # int | The maximum number of subscriptions to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired subscriptions should be returned. (optional) (default to false)

try: 
    # Returns a list of available unique coupon codes for the specified parent coupon code that can be applied to a subscription.
    api_response = api_instance.get_available_coupon_codes_for_code(code, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponsApi->get_available_coupon_codes_for_code: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The base code to use in the generation of the unique codes. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first subscription to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of subscriptions to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired subscriptions should be returned. | [optional] [default to false]

### Return type

[**CouponUniqueCodesResponsePagedMetadata**](CouponUniqueCodesResponsePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupon_code**
> CouponUniqueCodesResponsePagedMetadata get_coupon_code(code, organizations=organizations)

Returns the coupon for the specified code that can be applied to a subscription.

{ \"nickname\":\"Retrieve coupon\",\"response\":\"getCouponByCode.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CouponsApi()
code = 'code_example' # str | The parent coupon code to use in the generation of the unique codes.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns the coupon for the specified code that can be applied to a subscription.
    api_response = api_instance.get_coupon_code(code, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponsApi->get_coupon_code: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The parent coupon code to use in the generation of the unique codes. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**CouponUniqueCodesResponsePagedMetadata**](CouponUniqueCodesResponsePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_applications_of_coupons**
> SubscriptionPagedMetadata get_subscription_applications_of_coupons(code, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Retrieves a collection of the coupons by this coupon code which have been applied.

{ \"nickname\":\"Retrieve subscriptions to which the given coupon code has been applied.\",\"response\":\"getSubscriptionApplications.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CouponsApi()
code = 'code_example' # str | Base code of the coupon.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first subscription to return. (optional) (default to 0)
records = 10 # int | The maximum number of subscriptions to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = false # bool | Whether retired subscriptions should be returned. (optional) (default to false)

try: 
    # Retrieves a collection of the coupons by this coupon code which have been applied.
    api_response = api_instance.get_subscription_applications_of_coupons(code, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponsApi->get_subscription_applications_of_coupons: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Base code of the coupon. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first subscription to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of subscriptions to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired subscriptions should be returned. | [optional] [default to false]

### Return type

[**SubscriptionPagedMetadata**](SubscriptionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retire_coupon**
> CouponPagedMetadata retire_coupon(code, organizations)

<p>This method has 2 main behaviours depending on what is passed in. If the parent coupon code, for example SUMMER, is given no new coupons can be issued or claimed from this code. Deleting will result in the deleted property being set to true.</p><p>If a unique coupon code, for example SUMMER-AGH8, is given this will stop the coupon from being applied to the subscription from that point onwards. When a coupon is deleted the validUntil property is set which is the date/time it stopped applying to the target.</p>

{ \"nickname\":\"Retire coupon\",\"response\":\"retireCoupon.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CouponsApi()
code = 'code_example' # str | ID of the coupon to remove.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls.

try: 
    # <p>This method has 2 main behaviours depending on what is passed in. If the parent coupon code, for example SUMMER, is given no new coupons can be issued or claimed from this code. Deleting will result in the deleted property being set to true.</p><p>If a unique coupon code, for example SUMMER-AGH8, is given this will stop the coupon from being applied to the subscription from that point onwards. When a coupon is deleted the validUntil property is set which is the date/time it stopped applying to the target.</p>
    api_response = api_instance.retire_coupon(code, organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponsApi->retire_coupon: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| ID of the coupon to remove. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | 

### Return type

[**CouponPagedMetadata**](CouponPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

