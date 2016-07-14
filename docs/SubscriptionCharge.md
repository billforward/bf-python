# SubscriptionCharge

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was created.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**changed_by** | **str** | { \&quot;description\&quot; : \&quot;ID of the user who last updated the entity.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**updated** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was last updated.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**id** | **str** | {\&quot;description\&quot;:\&quot;The ID of the charge.\&quot;,\&quot;verbs\&quot;:[\&quot;GET\&quot;]} | [optional] 
**crm_id** | **str** | {\&quot;description\&quot;:\&quot;Customer-relationship-management ID of the charge.\&quot;,\&quot;verbs\&quot;:[\&quot;GET\&quot;,\&quot;PUT\&quot;,\&quot;POST\&quot;]} | [optional] 
**account_id** | **str** | {\&quot;description\&quot;:\&quot;ID of the account owning the subscription for which the charge was generated.\&quot;,\&quot;verbs\&quot;:[\&quot;GET\&quot;,\&quot;POST\&quot;]} | [optional] 
**subscription_id** | **str** | {\&quot;description\&quot;:\&quot;ID of the subscription for which the charge was generated.\&quot;,\&quot;verbs\&quot;:[\&quot;GET\&quot;,\&quot;POST\&quot;]} | [optional] 
**subscription_version_id** | **str** | {\&quot;description\&quot;:\&quot;Version ID of the subscription for which the charge was generated.\&quot;,\&quot;verbs\&quot;:[\&quot;GET\&quot;,\&quot;POST\&quot;]} | [optional] 
**invoice_id** | **str** | {\&quot;description\&quot;:\&quot;ID of the invoice to which this charge applies (if the charge targets a specific invoice).\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | [optional] 
**name** | **str** | {\&quot;description\&quot;:\&quot;Friendly name given to the charge to help identify it.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;,\&quot;PUT\&quot;]} | [optional] 
**description** | **str** | {\&quot;description\&quot;:\&quot;Description given to the charge.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;,\&quot;PUT\&quot;]} | [optional] 
**amount** | **float** | {\&quot;description\&quot;:\&quot;Monetary amount of the charge &amp;mdash; including any tax applied to the final amount.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | [optional] 
**amount_excluding_tax** | **float** | {\&quot;description\&quot;:\&quot;Monetary amount of the charge &amp;mdash; excluding any tax applied to the final amount.\&quot;,\&quot;verbs\&quot;:[\&quot;GET\&quot;]} | [optional] 
**currency** | **str** | { \&quot;description\&quot; : \&quot;Currency of the invoice specified by a three character ISO 4217 currency code.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**period_start** | **datetime** | {\&quot;default\&quot;:\&quot;(Now)\&quot;,\&quot;description\&quot;:\&quot;The time-beginning of the interval to which the charge applies. This can be used to apply a charge across partial or multiple periods,to pro-rate its price.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | [optional] 
**period_end** | **datetime** | {\&quot;default\&quot;:\&quot;(End of current period)\&quot;,\&quot;description\&quot;:\&quot;The time-ending of the interval to which the charge applies. This can be used to apply a charge across partial or multiple periods,to pro-rate its price.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | [optional] 
**type** | **str** | {\&quot;description\&quot;:\&quot;A type describing the nature of the charge.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | 
**invoicing_type** | **str** | {\&quot;default\&quot;:\&quot;&lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;Aggregated&lt;/span&gt;\&quot;,\&quot;description\&quot;:\&quot;The strategy for how this charge will raise invoices.&lt;br&gt;&lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;Immediate&lt;/span&gt; &amp;mdash; Generate straight-away an invoice containing this charge.&lt;br&gt;&lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;Aggregated&lt;/span&gt; &amp;mdash; Add this charge to the next invoice which is generated naturally &amp;mdash; i.e. the invoice raised at the current period&#39;s end.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | 
**state** | **str** | {\&quot;default\&quot;:\&quot;&lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;Pending&lt;/span&gt;\&quot;,\&quot;description\&quot;:\&quot;The current state of the charge.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;,\&quot;PUT\&quot;]} | 
**charge_type** | **str** | {\&quot;default\&quot;:\&quot;&lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;Debit&lt;/span&gt;\&quot;,\&quot;description\&quot;:\&quot;Whether this charge represents money given to or taken from the customer.&lt;br&gt;&lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;Credit&lt;/span&gt; &amp;mdash; This is a charge for money given to the customer.&lt;br&gt;&lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;Debit&lt;/span&gt; &amp;mdash; This is a charge for money taken from the customer.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | 
**calculation** | **str** | {\&quot;default\&quot;:\&quot;(Empty string)\&quot;,\&quot;description\&quot;:\&quot;A human-readable explanation of how the value of the charge was calculated.\&quot;,\&quot;verbs\&quot;:[\&quot;GET\&quot;]} | [optional] 
**remaining_credit_behaviour** | **str** | {\&quot;default\&quot;:\&quot;&lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;Rollover&lt;/span&gt;\&quot;,\&quot;description\&quot;:\&quot;Defines the behaviour applied to any outstanding credit resulting from the application of the charge..&lt;br&gt;&lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;Rollover&lt;/span&gt; &amp;mdash; Outstanding credit is returned to the accounts credit pool.&lt;br&gt;&lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;Discard&lt;/span&gt; &amp;mdash; Outstanding credit is lost.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | 
**trial** | **bool** | {\&quot;default\&quot;:\&quot;false\&quot;,\&quot;description\&quot;:\&quot;(Applicable only if any of [&#x60;pricingComponentName&#x60;, &#x60;pricingComponentID&#x60;] are defined)&lt;br&gt;Whether the charge was created for a subscription whilst in a trial period.&lt;br&gt;&lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;false&lt;/span&gt; &amp;mdash; This is a non-trial charge, so funds will be sought from the customer.&lt;br&gt;&lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;true&lt;/span&gt; &amp;mdash; This is a trial charge, soThe charge can be considered &#39;Paid&#39; without taking any funds from the customer.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | [optional] [default to False]
**version_id** | **str** | {\&quot;description\&quot;:\&quot;The version ID of the charge.\&quot;,\&quot;verbs\&quot;:[\&quot;GET\&quot;]} | [optional] 
**version_number** | **int** | {\&quot;description\&quot;:\&quot;The version number of the charge. The first version of a charge is version number 1.\&quot;,\&quot;verbs\&quot;:[\&quot;GET\&quot;]} | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

