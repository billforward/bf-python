# Invoice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] 
**changed_by** | **str** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**metadata** | **dict(str, object)** |  | [optional] 
**version_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**subscription_version_id** | **str** |  | [optional] 
**account_id** | **str** |  | 
**organization_id** | **str** |  | 
**parent_invoice_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**state** | **str** |  | 
**issued** | **datetime** |  | [optional] 
**due** | **datetime** |  | [optional] 
**period_start** | **datetime** |  | [optional] 
**period_end** | **datetime** |  | [optional] 
**deleted** | **bool** |  | 
**total_execution_attempts** | **int** |  | [optional] 
**last_execution_attempt** | **datetime** |  | [optional] 
**next_execution_attempt** | **datetime** |  | [optional] 
**final_execution_attempt** | **datetime** |  | [optional] 
**payment_received** | **datetime** |  | [optional] 
**currency** | [**CreditNoteCurrency**](CreditNoteCurrency.md) |  | 
**cost_excluding_tax** | **float** |  | 
**invoice_cost** | **float** |  | 
**non_discounted_cost** | **float** |  | [optional] 
**non_discounted_cost_excluding_tax** | **float** |  | [optional] 
**invoice_paid** | **float** |  | [optional] 
**discount_amount** | **float** |  | [optional] 
**discount_amount_excluding_tax** | **float** |  | [optional] 
**invoice_refunded** | **float** |  | [optional] 
**credit_rolled_over** | **float** |  | 
**credit_rolled_over_excluding_tax** | **float** |  | [optional] 
**type** | **str** |  | 
**locked** | **str** |  | [optional] 
**managed_by** | **str** |  | [optional] 
**initial_invoice** | **bool** |  | 
**processing** | **bool** |  | 
**purchase_order** | **str** |  | [optional] 
**version_number** | **int** |  | 
**invoice_lines** | [**list[InvoiceLines]**](InvoiceLines.md) |  | [optional] 
**tax_lines** | [**list[TaxLine]**](TaxLine.md) |  | [optional] 
**invoice_payments** | [**list[InvoicePayments]**](InvoicePayments.md) |  | [optional] 
**invoice_refunds** | [**list[Refund]**](Refund.md) |  | [optional] 
**invoice_credit_notes** | [**list[CreditNote]**](CreditNote.md) |  | [optional] 
**charges** | [**list[SubscriptionCharge]**](SubscriptionCharge.md) |  | [optional] 
**payment_terms** | **int** |  | [optional] 
**children** | [**list[Invoice]**](Invoice.md) |  | [optional] 
**executions** | [**list[ExecutionReceiptResponse]**](ExecutionReceiptResponse.md) |  | [optional] 
**total_invoice_cost** | **float** |  | [optional] 
**zero_cost** | **bool** |  | [optional] 
**c_rmid** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

