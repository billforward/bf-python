# Subscription

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] 
**changed_by** | **str** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**metadata** | **dict(str, object)** |  | [optional] 
**id** | **str** |  | 
**version_id** | **str** |  | [optional] 
**crm_id** | **str** |  | [optional] 
**account_id** | **str** |  | 
**organization_id** | **str** |  | 
**product_id** | **str** |  | [optional] 
**product_rate_plan_id** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**state** | **str** |  | 
**active** | **bool** |  | [optional] 
**current_period_start** | **datetime** |  | [optional] 
**current_period_end** | **datetime** |  | [optional] 
**contract_start** | **datetime** |  | [optional] 
**subscription_end** | **datetime** |  | [optional] 
**current_period_end_explicit** | **datetime** |  | [optional] 
**initial_period_start** | **datetime** |  | [optional] 
**successful_periods** | **int** |  | [optional] 
**total_periods** | **int** |  | [optional] 
**total_version_periods** | **int** |  | [optional] 
**trial_end** | **datetime** |  | [optional] 
**dunning** | **bool** |  | [optional] 
**locked** | **str** |  | [optional] 
**managed_by** | **str** |  | [optional] 
**version_start** | **datetime** |  | 
**version_end** | **datetime** |  | [optional] 
**version_number** | **int** |  | 
**credit_enabled** | **bool** |  | [optional] 
**aggregate_all_subscriptions_on_account** | **bool** |  | [optional] 
**failed_payment_behaviour** | **str** |  | [optional] 
**pricing_component_values** | [**list[PricingComponentValue]**](PricingComponentValue.md) |  | [optional] 
**payment_method_subscription_links** | [**list[PaymentMethodSubscriptionLink]**](PaymentMethodSubscriptionLink.md) |  | [optional] 
**fixed_terms** | [**list[FixedTerm]**](FixedTerm.md) |  | [optional] 
**contracts** | [**list[Contract]**](Contract.md) |  | [optional] 
**square_subscription** | [**SquareSubscription**](SquareSubscription.md) |  | [optional] 
**execution_info** | [**ExecutionResponse**](ExecutionResponse.md) |  | [optional] 
**current_time** | **datetime** |  | [optional] 
**time_offset** | **int** |  | [optional] 
**revive** | [**SubscriptionRevivePartialRequest**](SubscriptionRevivePartialRequest.md) |  | [optional] 
**payment_terms** | **int** |  | [optional] 
**purchase_order** | **str** |  | [optional] 
**affiliate_subscription_relationship** | [**list[AffiliateSubscriptionRelationship]**](AffiliateSubscriptionRelationship.md) |  | [optional] 
**fixed_term** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

