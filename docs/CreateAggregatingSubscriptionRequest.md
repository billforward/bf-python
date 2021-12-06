# CreateAggregatingSubscriptionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] 
**account_id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**start** | **datetime** |  | [optional] 
**end** | **datetime** |  | [optional] 
**state** | **str** |  | [optional] 
**product_rate_plan** | **str** |  | [optional] 
**duration** | **int** |  | [optional] 
**duration_period** | **str** |  | [optional] 
**product_type** | **str** |  | [optional] 
**aggregating_components** | [**list[CreateAggregatingComponentRequest]**](CreateAggregatingComponentRequest.md) |  | [optional] 
**aggregate_all_subscriptions_on_account** | **bool** |  | [optional] 
**currency** | [**CreditNoteCurrency**](CreditNoteCurrency.md) |  | [optional] 
**failed_payment_behaviour** | **str** |  | [optional] 
**payment_terms** | **int** |  | [optional] 
**purchase_order** | **str** |  | [optional] 
**align_period_with_aggregating_subscription** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

