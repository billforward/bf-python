# CreateSubscriptionChargeAmendment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was created.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**changed_by** | **str** | { \&quot;description\&quot; : \&quot;ID of the user who last updated the entity.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**updated** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was last updated.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**type** | **str** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;default\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;] } | 
**id** | **str** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**organization_id** | **str** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[\&quot;\&quot;] } | [optional] 
**subscription_id** | **str** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**amendment_type** | **str** | { \&quot;description\&quot; : \&quot;Type of amendment\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;] } | 
**actioning_time** | **datetime** | { \&quot;description\&quot; : \&quot;When the amendment will run\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**actioned_time** | **datetime** | { \&quot;description\&quot; : \&quot;The time the amendment completed.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**state** | **str** | Whether the subscription-amendment is: pending (to be actioned in the future), succeeded (actioning completed), failed (actioning was attempted but no effect was made) or discarded (the amendment had been cancelled before being actioned). Default: Pending | 
**deleted** | **bool** | { \&quot;description\&quot; : \&quot;Is the amendment deleted.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [default to False]
**subscription_charge_id** | **str** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**description** | **str** | { \&quot;description\&quot; : \&quot;.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;] } | [optional] 
**amount** | **float** | { \&quot;description\&quot; : \&quot;Monetary value to charge in the same currency as the subscription.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;] } | 
**discount** | **float** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**type** | **str** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;default\&quot; : \&quot;Manual\&quot;,  \&quot;verbs\&quot;:[] } | 
**invoicing_type** | **str** | { \&quot;description\&quot; : \&quot;&lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;Immediate&lt;/span&gt; invoicing will result in an invoice being issued immediately for the charge. &lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;Aggregated&lt;/span&gt; invoicing will generate a charge to be added to the next issued invoice, for example at the current billing period end.\&quot;, \&quot;default\&quot; : \&quot;Aggregated\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**tax_status** | **str** | { \&quot;description\&quot; : \&quot;Whether the amount specified is &lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;inclusive&lt;/span&gt; or &lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;exclusive&lt;/span&gt; of tax\&quot;,  \&quot;default\&quot; : \&quot;inclusive\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**subscription_charge** | [**SubscriptionCharge**](SubscriptionCharge.md) | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**pricing_component_value_change** | [**InsertableBillingEntity**](InsertableBillingEntity.md) | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**pricing_component_id** | **str** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[] } | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


