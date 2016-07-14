# swagger_client.CouponbookApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_coupon_book**](CouponbookApi.md#create_coupon_book) | **POST** /coupon-books | Create a coupon-book.
[**delete_coupon_book**](CouponbookApi.md#delete_coupon_book) | **DELETE** /coupon-books/{coupon-book-ID} | Retire a coupon-book, specified by the coupon-book-ID parameter.
[**get_all_attachable_coupon_books**](CouponbookApi.md#get_all_attachable_coupon_books) | **GET** /coupon-books/attachable/{attachableness}/{has_code} | Returns a collection of attachable coupon-books. An attachable coupon-book has at least one remaining use, and is not deleted. By default 10 values are returned. Records are returned in natural order.
[**get_all_coupon_books**](CouponbookApi.md#get_all_coupon_books) | **GET** /coupon-books | Returns a collection of coupon-books. By default 10 values are returned. Records are returned in natural order.
[**get_coupon_book_by_book_code**](CouponbookApi.md#get_coupon_book_by_book_code) | **GET** /coupon-books/book-code/{book-code} | Returns a single coupon-book, specified by the book-code parameter.
[**get_coupon_book_by_coupon_book_definition_id**](CouponbookApi.md#get_coupon_book_by_coupon_book_definition_id) | **GET** /coupon-books/coupon-book-definition/{coupon-book-definition-ID} | Returns a collection of coupon-books, specified by coupon-book-definition-ID parameter. By default 10 coupon-books are returned. Records are returned in natural order.
[**get_coupon_book_by_coupon_code**](CouponbookApi.md#get_coupon_book_by_coupon_code) | **GET** /coupon-books/coupon/{coupon-code} | Returns a single coupon-book, specified by the coupon-code parameter.
[**get_coupon_book_by_id**](CouponbookApi.md#get_coupon_book_by_id) | **GET** /coupon-books/{coupon-book-ID} | Returns a single coupon-book, specified by the coupon-book-ID parameter.
[**update_coupon_book**](CouponbookApi.md#update_coupon_book) | **PUT** /coupon-books | Update a coupon-book.


# **create_coupon_book**
> CouponBookPagedMetadata create_coupon_book(coupon_book)

Create a coupon-book.

{\"nickname\":\"Create a new coupon book\",\"request\":\"createCouponBookRequest.html\",\"response\":\"createCouponBookResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CouponbookApi()
coupon_book = swagger_client.CouponBook() # CouponBook | The coupon-book object to be created.

try: 
    # Create a coupon-book.
    api_response = api_instance.create_coupon_book(coupon_book)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponbookApi->create_coupon_book: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_book** | [**CouponBook**](CouponBook.md)| The coupon-book object to be created. | 

### Return type

[**CouponBookPagedMetadata**](CouponBookPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_coupon_book**
> CouponBookPagedMetadata delete_coupon_book(coupon_book_id, organizations=organizations)

Retire a coupon-book, specified by the coupon-book-ID parameter.

{\"nickname\":\"Delete coupon book\",\"response\":\"deleteCouponBookByID.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CouponbookApi()
coupon_book_id = 'coupon_book_id_example' # str | ID of the coupon-book.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Retire a coupon-book, specified by the coupon-book-ID parameter.
    api_response = api_instance.delete_coupon_book(coupon_book_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponbookApi->delete_coupon_book: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_book_id** | **str**| ID of the coupon-book. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**CouponBookPagedMetadata**](CouponBookPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_attachable_coupon_books**
> CouponBookPagedMetadata get_all_attachable_coupon_books(attachableness, has_code, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Returns a collection of attachable coupon-books. An attachable coupon-book has at least one remaining use, and is not deleted. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get all attachable coupon books\",\"response\":\"getCouponBookAllAttachable.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CouponbookApi()
attachableness = true # bool | The attachableness of the coupon-book.
has_code = true # bool | Whether the coupon-books have book codes or not.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first coupon-book to return. (optional) (default to 0)
records = 10 # int | The maximum number of coupon-books to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Returns a collection of attachable coupon-books. An attachable coupon-book has at least one remaining use, and is not deleted. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_attachable_coupon_books(attachableness, has_code, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponbookApi->get_all_attachable_coupon_books: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachableness** | **bool**| The attachableness of the coupon-book. | 
 **has_code** | **bool**| Whether the coupon-books have book codes or not. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first coupon-book to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of coupon-books to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**CouponBookPagedMetadata**](CouponBookPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_coupon_books**
> CouponBookPagedMetadata get_all_coupon_books(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of coupon-books. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get all coupon books\",\"response\":\"getCouponBookAll.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CouponbookApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first coupon-books to return. (optional) (default to 0)
records = 10 # int | The maximum number of coupon-books to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired coupon-books should be returned. (optional) (default to true)

try: 
    # Returns a collection of coupon-books. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_coupon_books(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponbookApi->get_all_coupon_books: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first coupon-books to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of coupon-books to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired coupon-books should be returned. | [optional] [default to true]

### Return type

[**CouponBookPagedMetadata**](CouponBookPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupon_book_by_book_code**
> CouponBookPagedMetadata get_coupon_book_by_book_code(book_code, organizations=organizations)

Returns a single coupon-book, specified by the book-code parameter.

{\"nickname\":\"Retrieve by book code\",\"response\":\"getCouponBookByBookCode.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CouponbookApi()
book_code = 'book_code_example' # str | The unique coupon-book-code.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single coupon-book, specified by the book-code parameter.
    api_response = api_instance.get_coupon_book_by_book_code(book_code, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponbookApi->get_coupon_book_by_book_code: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_code** | **str**| The unique coupon-book-code. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**CouponBookPagedMetadata**](CouponBookPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupon_book_by_coupon_book_definition_id**
> CouponBookPagedMetadata get_coupon_book_by_coupon_book_definition_id(coupon_book_definition_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of coupon-books, specified by coupon-book-definition-ID parameter. By default 10 coupon-books are returned. Records are returned in natural order.

{\"nickname\":\"Retrieve by coupon book definition\",\"response\":\"getCouponBookByCouponBookDefinitionID.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CouponbookApi()
coupon_book_definition_id = 'coupon_book_definition_id_example' # str | The string coupon-book-definition-ID of the coupon-book.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first coupon-book to return. (optional) (default to 0)
records = 10 # int | The maximum number of coupon-books to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired coupon-books should be returned. (optional) (default to true)

try: 
    # Returns a collection of coupon-books, specified by coupon-book-definition-ID parameter. By default 10 coupon-books are returned. Records are returned in natural order.
    api_response = api_instance.get_coupon_book_by_coupon_book_definition_id(coupon_book_definition_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponbookApi->get_coupon_book_by_coupon_book_definition_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_book_definition_id** | **str**| The string coupon-book-definition-ID of the coupon-book. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first coupon-book to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of coupon-books to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired coupon-books should be returned. | [optional] [default to true]

### Return type

[**CouponBookPagedMetadata**](CouponBookPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupon_book_by_coupon_code**
> CouponBookPagedMetadata get_coupon_book_by_coupon_code(coupon_code, organizations=organizations)

Returns a single coupon-book, specified by the coupon-code parameter.

{\"nickname\":\"Retrieve by coupon code\",\"response\":\"getCouponBookByBookCode.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CouponbookApi()
coupon_code = 'coupon_code_example' # str | The unique coupon-code.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single coupon-book, specified by the coupon-code parameter.
    api_response = api_instance.get_coupon_book_by_coupon_code(coupon_code, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponbookApi->get_coupon_book_by_coupon_code: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_code** | **str**| The unique coupon-code. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**CouponBookPagedMetadata**](CouponBookPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupon_book_by_id**
> CouponBookPagedMetadata get_coupon_book_by_id(coupon_book_id, organizations=organizations)

Returns a single coupon-book, specified by the coupon-book-ID parameter.

{\"nickname\":\"Retrieve an existing coupon book\",\"response\":\"getCouponBookByID.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CouponbookApi()
coupon_book_id = 'coupon_book_id_example' # str | ID of the coupon-book.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single coupon-book, specified by the coupon-book-ID parameter.
    api_response = api_instance.get_coupon_book_by_id(coupon_book_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponbookApi->get_coupon_book_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_book_id** | **str**| ID of the coupon-book. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**CouponBookPagedMetadata**](CouponBookPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_coupon_book**
> CouponBookPagedMetadata update_coupon_book(coupon_book)

Update a coupon-book.

{\"nickname\":\"Update a coupon book\",\"request\":\"updateCouponBookRequest.html\",\"response\":\"updateCouponBookResponse.html\"}

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CouponbookApi()
coupon_book = swagger_client.CouponBook() # CouponBook | The coupon-book object to be updated.

try: 
    # Update a coupon-book.
    api_response = api_instance.update_coupon_book(coupon_book)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponbookApi->update_coupon_book: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_book** | [**CouponBook**](CouponBook.md)| The coupon-book object to be updated. | 

### Return type

[**CouponBookPagedMetadata**](CouponBookPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

