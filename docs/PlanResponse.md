# PlanResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**currency** | [**CreditNoteCurrency**](CreditNoteCurrency.md) |  | [optional] 
**tax_status** | **str** |  | [optional] 
**failed_payment_behaviour** | **str** |  | [optional] 
**duration** | **int** |  | [optional] 
**duration_period** | **str** |  | [optional] 
**trial** | **int** |  | [optional] 
**trial_period** | **str** |  | [optional] 
**pro_rata_mode** | **str** |  | [optional] 
**localised_tax** | **bool** |  | [optional] 
**create_zero_valued_invoices** | **bool** |  | [optional] 
**migration_behaviour** | **str** |  | [optional] 
**invoice_issue_type** | **str** |  | [optional] 
**issue_duration** | **int** |  | [optional] 
**issue_period** | **str** |  | [optional] 
**payment_terms** | **int** |  | [optional] 
**generate_service_end_invoice** | **bool** |  | [optional] 
**fixed_term** | [**FixedTerm**](FixedTerm.md) |  | [optional] 
**taxation_strategies** | **list[str]** |  | [optional] 
**pricing** | [**PricingComponentsByChargeType**](PricingComponentsByChargeType.md) |  | [optional] 
**valid_from** | **datetime** |  | [optional] 
**valid_till** | **datetime** |  | [optional] 
**metadata** | **dict(str, object)** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
