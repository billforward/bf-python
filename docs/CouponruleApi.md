# billforward.CouponruleApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_coupon_rule**](CouponruleApi.md#create_coupon_rule) | **POST** /coupon-rules | Create a coupon-rule.
[**delete_coupon_rule**](CouponruleApi.md#delete_coupon_rule) | **DELETE** /coupon-rules/{coupon-rule-ID} | Retire a coupon-rule, specified by the coupon-rule-ID parameter.
[**get_all_coupon_rules**](CouponruleApi.md#get_all_coupon_rules) | **GET** /coupon-rules | Returns a collection of coupon-rules. By default 10 values are returned. Records are returned in natural order.
[**get_coupon_rule_by_coupon_definition_id**](CouponruleApi.md#get_coupon_rule_by_coupon_definition_id) | **GET** /coupon-rules/coupon-definition/{coupon-definition-ID} | Returns a single coupon-definition, specified by the coupon-definition-ID parameter.
[**get_coupon_rule_by_id**](CouponruleApi.md#get_coupon_rule_by_id) | **GET** /coupon-rules/{coupon-rule-ID} | Returns a single coupon-rule, specified by the coupon-rule-ID parameter.


# **create_coupon_rule**
> CouponRulePagedMetadata create_coupon_rule(coupon_rule)

Create a coupon-rule.

{\"nickname\":\"Create a new rule\", \"request\" : \"createCouponRuleRequest.html\" ,\"response\" : \"createCouponRuleResponse.html\" }

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.CouponruleApi()
coupon_rule = billforward.CouponRule() # CouponRule | The coupon-rule object to be created.

try: 
    # Create a coupon-rule.
    api_response = api_instance.create_coupon_rule(coupon_rule)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponruleApi->create_coupon_rule: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_rule** | [**CouponRule**](CouponRule.md)| The coupon-rule object to be created. | 

### Return type

[**CouponRulePagedMetadata**](CouponRulePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_coupon_rule**
> CouponRulePagedMetadata delete_coupon_rule(coupon_rule_id, organizations=organizations)

Retire a coupon-rule, specified by the coupon-rule-ID parameter.

{\"nickname\":\"Delete a rule\",\"response\" : \"deleteCouponRuleByID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.CouponruleApi()
coupon_rule_id = 'coupon_rule_id_example' # str | ID of the coupon-rule.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Retire a coupon-rule, specified by the coupon-rule-ID parameter.
    api_response = api_instance.delete_coupon_rule(coupon_rule_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponruleApi->delete_coupon_rule: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_rule_id** | **str**| ID of the coupon-rule. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**CouponRulePagedMetadata**](CouponRulePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_coupon_rules**
> CouponRulePagedMetadata get_all_coupon_rules(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)

Returns a collection of coupon-rules. By default 10 values are returned. Records are returned in natural order.

{\"nickname\":\"Get all rules\",\"response\" : \"getCouponRuleAll.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.CouponruleApi()
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)
offset = 0 # int | The offset from the first product-rate-plan to return. (optional) (default to 0)
records = 10 # int | The maximum number of product-rate-plans to return. (optional) (default to 10)
order_by = 'created' # str | Specify a field used to order the result set. (optional) (default to created)
order = 'DESC' # str | Ihe direction of any ordering, either ASC or DESC. (optional) (default to DESC)

try: 
    # Returns a collection of coupon-rules. By default 10 values are returned. Records are returned in natural order.
    api_response = api_instance.get_all_coupon_rules(organizations=organizations, offset=offset, records=records, order_by=order_by, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponruleApi->get_all_coupon_rules: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 
 **offset** | **int**| The offset from the first product-rate-plan to return. | [optional] [default to 0]
 **records** | **int**| The maximum number of product-rate-plans to return. | [optional] [default to 10]
 **order_by** | **str**| Specify a field used to order the result set. | [optional] [default to created]
 **order** | **str**| Ihe direction of any ordering, either ASC or DESC. | [optional] [default to DESC]

### Return type

[**CouponRulePagedMetadata**](CouponRulePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupon_rule_by_coupon_definition_id**
> CouponRulePagedMetadata get_coupon_rule_by_coupon_definition_id(coupon_definition_id, organizations=organizations)

Returns a single coupon-definition, specified by the coupon-definition-ID parameter.

{\"nickname\":\"Retrieve by coupon definition\",\"response\" : \"getCouponRuleByCouponDefinitionID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.CouponruleApi()
coupon_definition_id = 'coupon_definition_id_example' # str | ID of the coupon-definition.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single coupon-definition, specified by the coupon-definition-ID parameter.
    api_response = api_instance.get_coupon_rule_by_coupon_definition_id(coupon_definition_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponruleApi->get_coupon_rule_by_coupon_definition_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_definition_id** | **str**| ID of the coupon-definition. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**CouponRulePagedMetadata**](CouponRulePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupon_rule_by_id**
> CouponRulePagedMetadata get_coupon_rule_by_id(coupon_rule_id, organizations=organizations)

Returns a single coupon-rule, specified by the coupon-rule-ID parameter.

{\"nickname\":\"Retrieve an existing rule\",\"response\" : \"getCouponRuleByID.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.CouponruleApi()
coupon_rule_id = 'coupon_rule_id_example' # str | ID of the coupon-rule.
organizations = ['organizations_example'] # list[str] | A list of organization-IDs used to restrict the scope of API calls. (optional)

try: 
    # Returns a single coupon-rule, specified by the coupon-rule-ID parameter.
    api_response = api_instance.get_coupon_rule_by_id(coupon_rule_id, organizations=organizations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CouponruleApi->get_coupon_rule_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_rule_id** | **str**| ID of the coupon-rule. | 
 **organizations** | [**list[str]**](str.md)| A list of organization-IDs used to restrict the scope of API calls. | [optional] 

### Return type

[**CouponRulePagedMetadata**](CouponRulePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

