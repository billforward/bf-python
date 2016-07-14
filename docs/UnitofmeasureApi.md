# billforward.UnitofmeasureApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_unit_of_measure**](UnitofmeasureApi.md#create_unit_of_measure) | **POST** /units-of-measure | Create a unit-of-measure.
[**get_all_units_of_measure**](UnitofmeasureApi.md#get_all_units_of_measure) | **GET** /units-of-measure | Returns a collection of all unit-of-measure objects. By default 10 values are returned. Records are returned in natural order.
[**get_unit_of_measure_by_id**](UnitofmeasureApi.md#get_unit_of_measure_by_id) | **GET** /units-of-measure/{unit-of-measure-identifier} | Returns a single unit-of-measure corresponding to the unique id or name specified.
[**update_unit_of_measure**](UnitofmeasureApi.md#update_unit_of_measure) | **PUT** /units-of-measure | Update a unit-of-measure.


# **create_unit_of_measure**
> UnitOfMeasurePagedMetadata create_unit_of_measure(unit_of_measure)

Create a unit-of-measure.

{\"nickname\":\"Create a new unit of measure\",\"request\":\"createUnitOfMeasureRequest.html\",\"response\":\"createUnitOfMeasureResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.UnitofmeasureApi()
unit_of_measure = billforward.UnitOfMeasure() # UnitOfMeasure | The unit-of-measure object to be created.

try: 
    # Create a unit-of-measure.
    api_response = api_instance.create_unit_of_measure(unit_of_measure)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UnitofmeasureApi->create_unit_of_measure: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unit_of_measure** | [**UnitOfMeasure**](UnitOfMeasure.md)| The unit-of-measure object to be created. | 

### Return type

[**UnitOfMeasurePagedMetadata**](UnitOfMeasurePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_units_of_measure**
> UnitOfMeasurePagedMetadata get_all_units_of_measure(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)

Returns a collection of all unit-of-measure objects. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get all units of measure\",\"response\":\"getUnitOfMeasureAll.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.UnitofmeasureApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first taxation-link to return. (optional) (default to 0)
records = 10 # int | The maximum number of taxation-links to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)
include_retired = true # bool | Whether retired products should be returned. (optional) (default to true)

try: 
    # Returns a collection of all unit-of-measure objects. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_units_of_measure(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order, include_retired=include_retired)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UnitofmeasureApi->get_all_units_of_measure: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first taxation-link to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of taxation-links to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]
 **include_retired** | **bool**| Whether retired products should be returned. | [optional] [default to true]

### Return type

[**UnitOfMeasurePagedMetadata**](UnitOfMeasurePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unit_of_measure_by_id**
> UnitOfMeasurePagedMetadata get_unit_of_measure_by_id(unit_of_measure_identifier, organizations=organizations)

Returns a single unit-of-measure corresponding to the unique id or name specified.

{\"nickname\":\"Retrieve an existing unit of measure\",\"response\":\"getUnitOfMeasureByID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.UnitofmeasureApi()
unit_of_measure_identifier = 'unit_of_measure_identifier_example' # str | The unique id or name of the unit-of-measure.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single unit-of-measure corresponding to the unique id or name specified.
    api_response = api_instance.get_unit_of_measure_by_id(unit_of_measure_identifier, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UnitofmeasureApi->get_unit_of_measure_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unit_of_measure_identifier** | **str**| The unique id or name of the unit-of-measure. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**UnitOfMeasurePagedMetadata**](UnitOfMeasurePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_unit_of_measure**
> UnitOfMeasurePagedMetadata update_unit_of_measure(unit_of_measure)

Update a unit-of-measure.

{\"nickname\":\"Update a unit of measure\",\"request\":\"updateUnitOfMeasureRequest.html\",\"response\":\"updateUnitOfMeasureResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.UnitofmeasureApi()
unit_of_measure = billforward.UnitOfMeasure() # UnitOfMeasure | The unit-of-measure object to be updated.

try: 
    # Update a unit-of-measure.
    api_response = api_instance.update_unit_of_measure(unit_of_measure)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UnitofmeasureApi->update_unit_of_measure: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unit_of_measure** | [**UnitOfMeasure**](UnitOfMeasure.md)| The unit-of-measure object to be updated. | 

### Return type

[**UnitOfMeasurePagedMetadata**](UnitOfMeasurePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

