# SubscriptionCancellation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] 
**changed_by** | **str** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**id** | **str** |  | [optional] 
**subscription_id** | **str** |  | 
**organization_id** | **str** |  | 
**source** | **str** |  | [optional] 
**service_end** | **str** |  | 
**revive** | [**SubscriptionRevivePartialRequest**](SubscriptionRevivePartialRequest.md) |  | [optional] 
**cancellation_credit** | **str** |  | 
**credit_note_description** | **str** |  | [optional] 
**pre_cancellation_state** | **str** |  | [optional] 
**state** | **str** |  | 
**cancel_children** | **bool** |  | [optional] 
**cancel_empty_parent** | **bool** |  | [optional] 
**associated_refunds** | [**list[Refund]**](Refund.md) |  | [optional] 
**discardable** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

