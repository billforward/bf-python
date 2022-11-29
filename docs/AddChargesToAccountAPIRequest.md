# AddChargesToAccountAPIRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**purchase_order** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**currency** | [**CreditNoteCurrency**](CreditNoteCurrency.md) |  | [optional] 
**invoicing_type** | **str** |  | [optional] 
**payment_terms** | **int** |  | [optional] 
**remaining_credit_behaviour** | **str** |  | 
**invoice_state** | **str** |  | [optional] 
**charges** | [**list[NestedChargeRequest]**](NestedChargeRequest.md) |  | [optional] 
**adhoc_charges** | [**list[NestedAdhocChargeRequest]**](NestedAdhocChargeRequest.md) |  | [optional] 
**dry_run** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

