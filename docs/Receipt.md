# Receipt

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refund_id** | **str** |  | 
**created** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was created.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**changed_by** | **str** | { \&quot;description\&quot; : \&quot;ID of the user who last updated the entity.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**id** | **str** |  | [optional] 
**crm_id** | **str** | { \&quot;description\&quot; : \&quot;CRM ID of the subscription.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**invoice_id** | **str** |  | [optional] 
**gateway_reference_id** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 
**payment_id** | **str** |  | [optional] 
**payment_method_id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**cardholder_name** | **str** |  | [optional] 
**card_last_four** | **str** |  | [optional] 
**card_description** | **str** |  | [optional] 
**card_country** | **str** |  | [optional] 
**card_province** | **str** |  | [optional] 
**card_type** | **str** |  | [optional] 
**ip_address** | **str** | {\&quot;description\&quot;:\&quot;IP address associated with this payment method.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;]} | [optional] 
**ip_address_country** | **str** | {\&quot;description\&quot;:\&quot;Country of the IP address associated with this payment method.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;]} | [optional] 
**type** | **str** | { \&quot;description\&quot; : \&quot;Type of transaction.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**currency** | **str** | { \&quot;description\&quot; : \&quot;Currency of the invoice specified by a three character ISO 4217 currency code.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**value** | **float** |  | [optional] 
**payment_gateway** | **str** |  | [optional] 
**invoice_type** | **str** | { \&quot;description\&quot; : \&quot;The type of the invoice. A subscription invoice is raised every time a subscription recurs. An amendment is created for intra-contract changes. An Adhoc invoice is created for payment that is taken out-of-band of a subscription. Finally the invoice generated for a trial period is marked as Trial.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**execution_attempt** | **int** |  | [optional] 
**decision** | **str** |  | [optional] 
**reason_code** | **int** |  | [optional] 
**raw_reason_code** | **str** |  | [optional] 
**raw_data** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


