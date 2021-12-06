# MigrationResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**next_subscription_name** | **str** |  | [optional] 
**next_subscription_description** | **str** |  | [optional] 
**product** | **str** |  | [optional] 
**product_rate_plan** | **str** |  | [optional] 
**invoicing_type** | **str** |  | 
**mappings** | [**list[PricingComponentMigrationValue]**](PricingComponentMigrationValue.md) |  | [optional] 
**pricing_behaviour** | **str** |  | 
**void_existing_coupons** | **bool** |  | [optional] 
**force_trial_end** | **bool** |  | [optional] 
**dry_run** | **bool** |  | [optional] 
**new_subscription_id** | **str** |  | [optional] 
**new_subscription** | [**Subscription**](Subscription.md) |  | [optional] 
**previous_subscription** | [**Subscription**](Subscription.md) |  | [optional] 
**previous_product_rate_plan_id** | **str** |  | [optional] 
**previous_product_rate_plan_name** | **str** |  | [optional] 
**new_product_rate_plan_id** | **str** |  | [optional] 
**new_product_rate_plan_name** | **str** |  | [optional] 
**charge_type** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**tax** | **float** |  | [optional] 
**invoices** | [**list[Invoice]**](Invoice.md) |  | [optional] 
**amendment** | [**Amendment**](Amendment.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

