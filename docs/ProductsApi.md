# billforward.ProductsApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_product**](ProductsApi.md#create_product) | **POST** /products | Create a product.
[**delete_metadata_for_product**](ProductsApi.md#delete_metadata_for_product) | **DELETE** /products/{product-ID}/metadata | Remove any associated metadata.
[**get_all_products**](ProductsApi.md#get_all_products) | **GET** /products | Returns a collection of products. By default 10 values are returned. Records are returned in natural order.
[**get_metadata_for_product**](ProductsApi.md#get_metadata_for_product) | **GET** /products/{product-ID}/metadata | Retrieve any associated metadata.
[**get_product_by_id**](ProductsApi.md#get_product_by_id) | **GET** /products/{product-ID} | Returns a single product, specified by the product-ID parameter.
[**retire_product**](ProductsApi.md#retire_product) | **DELETE** /products/{product-ID} | Deletes the product specified by the product-ID parameter. Any existing subscriptions will continue; it is a soft delete.
[**set_metadata_for_product**](ProductsApi.md#set_metadata_for_product) | **POST** /products/{product-ID}/metadata | Remove any existing metadata keys and create the provided data.
[**update_product**](ProductsApi.md#update_product) | **PUT** /products | Update a product.
[**upsert_metadata_for_product**](ProductsApi.md#upsert_metadata_for_product) | **PUT** /products/{product-ID}/metadata | Update any existing metadata key-values and insert any new key-values, no keys will be removed.


# **create_product**
> ProductPagedMetadata create_product(product)

Create a product.

{\"nickname\":\"Create a new product\",\"request\":\"createProductRequest.html\",\"response\":\"createProductResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.ProductsApi()
product = billforward.Product() # Product | The product object to be updated.

try: 
    # Create a product.
    api_response = api_instance.create_product(product)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProductsApi->create_product: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | [**Product**](Product.md)| The product object to be updated. | 

### Return type

[**ProductPagedMetadata**](ProductPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_metadata_for_product**
> DynamicMetadata delete_metadata_for_product(product_id, organizations=organizations)

Remove any associated metadata.

{\"nickname\":\"Clear metadata from product\",\"request\" :\"deleteProductMetadataRequest.html\",\"response\":\"deleteProductMetadataResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.ProductsApi()
product_id = 'product_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Remove any associated metadata.
    api_response = api_instance.delete_metadata_for_product(product_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProductsApi->delete_metadata_for_product: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**DynamicMetadata**](DynamicMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_products**
> ProductPagedMetadata get_all_products(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, metadata=metadata)

Returns a collection of products. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get all products\",\"response\":\"getProductAll.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.ProductsApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first product to return. (optional) (default to 0)
records = 10 # int | The maximum number of products to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)
metadata = 'metadata_example' # str |  (optional)

try: 
    # Returns a collection of products. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_products(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired, metadata=metadata)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProductsApi->get_all_products: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first product to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of products to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]
 **metadata** | **str**|  | [optional] 

### Return type

[**ProductPagedMetadata**](ProductPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_for_product**
> DynamicMetadata get_metadata_for_product(product_id, organizations=organizations)

Retrieve any associated metadata.

{\"nickname\":\"Retrieve metadata on product\",\"request\":\"getProductMetadataRequest.html\",\"response\":\"getProductMetadataResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.ProductsApi()
product_id = 'product_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Retrieve any associated metadata.
    api_response = api_instance.get_metadata_for_product(product_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProductsApi->get_metadata_for_product: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**DynamicMetadata**](DynamicMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_by_id**
> ProductPagedMetadata get_product_by_id(product_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a single product, specified by the product-ID parameter.

{\"nickname\":\"Retrieve an existing product\",\"response\":\"getProductByID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.ProductsApi()
product_id = 'product_id_example' # str | ID or name of the product.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first product-rate-plan to return. (optional) (default to 0)
records = 10 # int | The maximum number of product-rate-plans to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)

try: 
    # Returns a single product, specified by the product-ID parameter.
    api_response = api_instance.get_product_by_id(product_id, organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProductsApi->get_product_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID or name of the product. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first product-rate-plan to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of product-rate-plans to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]

### Return type

[**ProductPagedMetadata**](ProductPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retire_product**
> ProductPagedMetadata retire_product(product_id, organizations=organizations)

Deletes the product specified by the product-ID parameter. Any existing subscriptions will continue; it is a soft delete.

{\"nickname\":\"Delete a product\",\"response\":\"deleteProduct.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.ProductsApi()
product_id = 'product_id_example' # str | ID of the Product.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Deletes the product specified by the product-ID parameter. Any existing subscriptions will continue; it is a soft delete.
    api_response = api_instance.retire_product(product_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProductsApi->retire_product: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of the Product. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**ProductPagedMetadata**](ProductPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_metadata_for_product**
> DynamicMetadata set_metadata_for_product(metadata, product_id, organizations=organizations)

Remove any existing metadata keys and create the provided data.

{\"nickname\":\"Set metadata on product\",\"request\":\"setProductMetadataRequest.html\",\"response\":\"setProductMetadataResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.ProductsApi()
metadata = billforward.DynamicMetadata() # DynamicMetadata | 
product_id = 'product_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Remove any existing metadata keys and create the provided data.
    api_response = api_instance.set_metadata_for_product(metadata, product_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProductsApi->set_metadata_for_product: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata** | [**DynamicMetadata**](DynamicMetadata.md)|  | 
 **product_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**DynamicMetadata**](DynamicMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_product**
> ProductPagedMetadata update_product(product)

Update a product.

{\"nickname\":\"Update a product\",\"request\":\"updateProductRequest.html\",\"response\":\"updateProductResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.ProductsApi()
product = billforward.Product() # Product | The product object to be updated.

try: 
    # Update a product.
    api_response = api_instance.update_product(product)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProductsApi->update_product: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | [**Product**](Product.md)| The product object to be updated. | 

### Return type

[**ProductPagedMetadata**](ProductPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_metadata_for_product**
> DynamicMetadata upsert_metadata_for_product(metadata, product_id, organizations=organizations)

Update any existing metadata key-values and insert any new key-values, no keys will be removed.

{\"nickname\":\"Upsert metadata on product\",\"request\":\"upsertProductMetadataRequest.html\",\"response\":\"upsertProductMetadataResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.ProductsApi()
metadata = billforward.DynamicMetadata() # DynamicMetadata | 
product_id = 'product_id_example' # str | 
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Update any existing metadata key-values and insert any new key-values, no keys will be removed.
    api_response = api_instance.upsert_metadata_for_product(metadata, product_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProductsApi->upsert_metadata_for_product: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata** | [**DynamicMetadata**](DynamicMetadata.md)|  | 
 **product_id** | **str**|  | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**DynamicMetadata**](DynamicMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

