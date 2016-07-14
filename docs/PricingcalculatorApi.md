# billforward.PricingcalculatorApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_amendment_cost**](PricingcalculatorApi.md#get_amendment_cost) | **POST** /pricing-calculator/amendment-cost | Calculates the price of a subscription&#39;s upgrading/downgrading to a new pricing component value.
[**get_coupon_instance_initialisation_cost**](PricingcalculatorApi.md#get_coupon_instance_initialisation_cost) | **POST** /pricing-calculator/coupon-instance/initialisation | Calculates the price of a subscription to a rate plan, at specified values of pricing component values, and with the specified coupon applied.
[**get_product_rate_plan_costs**](PricingcalculatorApi.md#get_product_rate_plan_costs) | **POST** /pricing-calculator/product-rate-plan | Calculates the price of a subscription to a rate plan, at specified values of pricing component values.


# **get_amendment_cost**
> AmendmentPriceNTimePagedMetadata get_amendment_cost(ammendment_price_request)

Calculates the price of a subscription's upgrading/downgrading to a new pricing component value.

{ \"nickname\" : \"Calculate upgrade price\", \"request\" : \"AmendmentPriceRequest.html\" ,\"response\" : \"AmendmentPriceNTime.html\" }

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.PricingcalculatorApi()
ammendment_price_request = billforward.BillingEntityBase() # BillingEntityBase | An amendment pricing request

try: 
    # Calculates the price of a subscription's upgrading/downgrading to a new pricing component value.
    api_response = api_instance.get_amendment_cost(ammendment_price_request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PricingcalculatorApi->get_amendment_cost: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ammendment_price_request** | [**BillingEntityBase**](BillingEntityBase.md)| An amendment pricing request | 

### Return type

[**AmendmentPriceNTimePagedMetadata**](AmendmentPriceNTimePagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupon_instance_initialisation_cost**
> PriceCalculationPagedMetadata get_coupon_instance_initialisation_cost(coupon_instance_initialisation_request)

Calculates the price of a subscription to a rate plan, at specified values of pricing component values, and with the specified coupon applied.

{ \"nickname\" : \"Calculate price with a coupon\",\"request\" : \"PriceRequestWithCoupon.html\" ,\"response\" : \"PriceCalculationWithCoupon.html\" }

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.PricingcalculatorApi()
coupon_instance_initialisation_request = billforward.BillingEntityBase() # BillingEntityBase | A coupon instance initialisation request

try: 
    # Calculates the price of a subscription to a rate plan, at specified values of pricing component values, and with the specified coupon applied.
    api_response = api_instance.get_coupon_instance_initialisation_cost(coupon_instance_initialisation_request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PricingcalculatorApi->get_coupon_instance_initialisation_cost: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_instance_initialisation_request** | [**BillingEntityBase**](BillingEntityBase.md)| A coupon instance initialisation request | 

### Return type

[**PriceCalculationPagedMetadata**](PriceCalculationPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_rate_plan_costs**
> PriceCalculationPagedMetadata get_product_rate_plan_costs(price_request)

Calculates the price of a subscription to a rate plan, at specified values of pricing component values.

{ \"nickname\" : \"Calculate price\", \"request\" : \"PriceRequest.html\" ,\"response\" : \"PriceCalculation.html\" }

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.PricingcalculatorApi()
price_request = billforward.BillingEntityBase() # BillingEntityBase | A price request

try: 
    # Calculates the price of a subscription to a rate plan, at specified values of pricing component values.
    api_response = api_instance.get_product_rate_plan_costs(price_request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PricingcalculatorApi->get_product_rate_plan_costs: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_request** | [**BillingEntityBase**](BillingEntityBase.md)| A price request | 

### Return type

[**PriceCalculationPagedMetadata**](PriceCalculationPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

