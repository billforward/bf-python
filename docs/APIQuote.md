# ApiQuote

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] 
**changed_by** | **str** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**id** | **str** |  | [optional] 
**subtotal** | **float** |  | [optional] 
**subtotal_excluding_tax** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**total_excluding_tax** | **float** |  | [optional] 
**tax** | **float** |  | [optional] 
**discount** | **float** |  | [optional] 
**discount_excluding_tax** | **float** |  | [optional] 
**currency** | [**CreditNoteCurrency**](CreditNoteCurrency.md) |  | [optional] 
**product_name** | **str** |  | [optional] 
**public_product_name** | **str** |  | [optional] 
**product_rate_plan_name** | **str** |  | [optional] 
**public_product_rate_plan_name** | **str** |  | [optional] 
**product_id** | **str** |  | [optional] 
**product_rate_plan_id** | **str** |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 
**quantities** | [**list[APIQuoteResponseQuantity]**](APIQuoteResponseQuantity.md) |  | [optional] 
**discounts** | [**list[CouponWrapperResponse]**](CouponWrapperResponse.md) |  | [optional] 
**quote_for** | **str** |  | [optional] 
**period_start** | **datetime** |  | 
**period_end** | **datetime** |  | 
**total_periods** | **float** |  | [optional] 
**proration_enabled** | **bool** |  | [optional] 
**uplift** | **float** |  | [optional] 
**coupon_codes** | **list[str]** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**same_product_period** | **bool** |  | [optional] 
**purchase_order** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

