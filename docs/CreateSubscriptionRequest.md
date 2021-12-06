# CreateSubscriptionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] 
**account_id** | **str** |  | [optional] 
**product** | **str** |  | [optional] 
**product_rate_plan** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**contract_start** | **datetime** |  | [optional] 
**start** | **datetime** |  | [optional] 
**end** | **datetime** |  | [optional] 
**state** | **str** |  | [optional] 
**trial_end** | **datetime** |  | [optional] 
**type** | **str** |  | [optional] 
**failed_payment_behaviour** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**exclude_from_auto_aggregation** | **bool** |  | [optional] 
**aggregate_all_subscriptions_on_account** | **bool** |  | [optional] 
**allow_subscription_wihtout_rate_plan** | **bool** |  | [optional] 
**dont_create_default_fixed_term** | **bool** |  | [optional] 
**align_period_with_aggregating_subscription** | **bool** |  | [optional] 
**parent_should_copy_child_period_end** | **bool** |  | [optional] 
**pricing_component_quantities** | [**list[CreatePricingComponentQuantityRequest]**](CreatePricingComponentQuantityRequest.md) |  | [optional] 
**payment_terms** | **int** |  | [optional] 
**purchase_order** | **str** |  | [optional] 
**coupon_codes** | **list[str]** |  | [optional] 
**prepayment_amount** | **float** |  | [optional] 
**extras** | [**Extras**](Extras.md) |  | [optional] 
**termed_subscription** | **bool** |  | [optional] 
**term_periods** | **int** |  | [optional] 
**term_expiry_behaviour** | **str** |  | [optional] 
**subsequent_product_rate_plan** | **str** |  | [optional] 
**metadata** | **dict(str, object)** |  | [optional] 
**ignore_first_period_usage** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

