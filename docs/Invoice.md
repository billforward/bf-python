# Invoice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was created.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**changed_by** | **str** | { \&quot;description\&quot; : \&quot;ID of the user who last updated the entity.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**updated** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was last updated.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**version_id** | **str** | { \&quot;description\&quot; : \&quot;Version identifier of the invoice.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**id** | **str** | { \&quot;description\&quot; : \&quot;Unique identifier for the invoice.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**crm_id** | **str** | { \&quot;description\&quot; : \&quot;CRM identifier of the invoice.\&quot;, \&quot;verbs\&quot;:[\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**subscription_id** | **str** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**subscription_version_id** | **str** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | 
**account_id** | **str** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | 
**organization_id** | **str** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[] } | 
**parent_invoice_id** | **str** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**name** | **str** | { \&quot;description\&quot; : \&quot;The name of the invoice\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**description** | **str** | { \&quot;description\&quot; : \&quot;The description of the invoice\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**state** | **str** | { \&quot;description\&quot; : \&quot;Initially an invoice is set as unpaid. Once payment for the full value of the invoice has been received it is marked as paid. An invoice may be paid from various sources including cards, coupons or manual payments.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | 
**issued** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the invoice was first issued.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**period_start** | **datetime** | { \&quot;description\&quot; : \&quot;Start of the period being billed by this invoice, UTC DateTime\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**period_end** | **datetime** | { \&quot;description\&quot; : \&quot;End of the period being billed by this invoice, UTC DateTime.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**due** | **datetime** | { \&quot;description\&quot; : \&quot;Date this invoice is due, UTC DateTime.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**deleted** | **bool** | { \&quot;description\&quot; : \&quot;Indicates if an invoice has been retired. If an invoice has been retired it can still be retrieved using the appropriate flag on API requests. Generally invoices will not be retired.\&quot;, \&quot;verbs\&quot;:[] } | [default to False]
**total_execution_attempts** | **int** | { \&quot;description\&quot; : \&quot;Number of payment attempts for this invoice. This includes any manual execution attempts.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**last_execution_attempt** | **datetime** | { \&quot;description\&quot; : \&quot;UTC DateTime of the invoice&#39;s last execution attempt. This was the last time an attempt was made to take payment for this invoice.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**next_execution_attempt** | **datetime** | { \&quot;description\&quot; : \&quot;UTC DateTime of the invoice&#39;s next execution attempt. If the next execution attempt is greater than the period end for this invoice, the invoice will not receive another automatic execution attempt.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**final_execution_attempt** | **datetime** | { \&quot;description\&quot; : \&quot;UTC DateTime of the invoice&#39;s final execution attempt. The final execution attempt. This may be less than the next execution attempt if the next execution attempt never occurred.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**payment_received** | **datetime** | { \&quot;description\&quot; : \&quot;UTC DateTime specifying when payment was received for the invoice.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**currency** | **str** | { \&quot;description\&quot; : \&quot;Currency of the invoice specified by a three character ISO 4217 currency code.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | 
**cost_excluding_tax** | **float** | { \&quot;description\&quot; : \&quot;Cost of the invoice exclusive of tax.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | 
**invoice_cost** | **float** | { \&quot;description\&quot; : \&quot;Cost of the invoice inclusive of tax.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | 
**non_discounted_cost** | **float** | Cost of the invoice before discounts, inclusive of tax. | 
**non_discounted_cost_excluding_tax** | **float** | Cost of the invoice before discounts, inclusive of tax. | 
**invoice_paid** | **float** | { \&quot;description\&quot; : \&quot;Total amount of the invoice currently paid for. As the invoice may be paid by multiple payments, for example partly paid for by a voucher and then paid for by a card, this indicates the current paid amount of the invoice.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**discount_amount** | **float** | { \&quot;description\&quot; : \&quot;The amount of discounts for the invoice.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**discount_amount_excluding_tax** | **float** | { \&quot;description\&quot; : \&quot;The amount of discounts for the invoice excluding tax.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**invoice_refunded** | **float** | { \&quot;description\&quot; : \&quot;Total amount of the invoice refunded.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**credit_rolled_over** | **float** | { \&quot;description\&quot; : \&quot;The amount of credit to be returned to the pool.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | 
**credit_rolled_over_excluding_tax** | **float** | { \&quot;description\&quot; : \&quot;The amount of credit to be returned to the pool excluding tax.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**type** | **str** | { \&quot;description\&quot; : \&quot;The type of the invoice. A subscription invoice is raised every time a subscription recurs. An amendment is created for intra-contract changes. An Adhoc invoice is created for payment that is taken out-of-band of a subscription. Finally the invoice generated for a trial period is marked as Trial.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | 
**locked** | **str** | { \&quot;description\&quot; : \&quot;If the subscription is locked, it will not be processed by the system\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**managed_by** | **str** | { \&quot;description\&quot; : \&quot;Which system is responsible for managing the subscription.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**initial_invoice** | **bool** | { \&quot;description\&quot; : \&quot;Is this an initial invoice. An initial invoice is the first invoice generated for a subscription. Initial invoices will not have dunning applied to them and as such will only have a single payment attempt. For trial periods, the trial invoice is the initial invoice.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [default to False]
**version_number** | **int** | { \&quot;description\&quot; : \&quot;The version number of the Invoice.  The first version of an Invoice is version number 1\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | 
**invoice_lines** | [**list[InvoiceLine]**](InvoiceLine.md) | { \&quot;description\&quot; : \&quot;The collection of invoice-lines associated with the invoice.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**tax_lines** | [**list[InsertableBillingEntity]**](InsertableBillingEntity.md) |  | [optional] 
**invoice_payments** | [**list[InvoicePayment]**](InvoicePayment.md) | { \&quot;description\&quot; : \&quot;Payments used for this invoice. Multiple payments may be associated with the invoice.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**invoice_refunds** | [**list[Refund]**](Refund.md) | { \&quot;description\&quot; : \&quot;Refunds associated with this invoice. Multiple refunds may be associated with the invoice.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**invoice_credit_notes** | [**list[CreditNote]**](CreditNote.md) | { \&quot;description\&quot; : \&quot;Credit Notes associated with this invoice. Multiple credit notes may be associated with the invoice.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**charges** | [**list[SubscriptionCharge]**](SubscriptionCharge.md) |  | [optional] 
**children** | [**list[Invoice]**](Invoice.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


