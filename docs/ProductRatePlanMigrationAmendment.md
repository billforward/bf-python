# ProductRatePlanMigrationAmendment

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
**product_rate_plan_id** | **str** | { \&quot;description\&quot; : \&quot;Identifier of the rate-plan the subscription to migrate to\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;] } | 
**invoicing_type** | **str** | { \&quot;description\&quot; : \&quot;&lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;Immediate&lt;/span&gt; invoicing will result in an invoice being issued immediately for migration charges. &lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;Aggregated&lt;/span&gt; invoicing will generate a charge to be added to the next issued invoice, for example at the current billing period end.\&quot;,  \&quot;default\&quot; : \&quot;Immediate\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;] } | 
**mappings** | [**list[PricingComponentValueMigrationAmendmentMapping]**](PricingComponentValueMigrationAmendmentMapping.md) | { \&quot;description\&quot; : \&quot;Mapping  of new rate-plans pricing-components to values\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;] } | [optional] 
**previous_subscription_id** | **str** | { \&quot;description\&quot; : \&quot;ID of the previous subscription.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**next_subscription_id** | **str** | { \&quot;description\&quot; : \&quot;ID of the next subscription.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**next_subscription_name** | **str** | { \&quot;description\&quot; : \&quot;User definable friendly name for the migrated subscription.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;] } | [optional] 
**next_subscription_description** | **str** | { \&quot;description\&quot; : \&quot;User definable description for the migrated subscription.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;] } | [optional] 
**pricing_behaviour** | **str** | { \&quot;description\&quot; : \&quot;Pricing behaviour defines how migration charges are calculated. &lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;DifferenceProRated&lt;/span&gt; calculates the difference between in-advance charges of the existing and new rate-plan, then pro-rates based on time remaining. &lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;None&lt;/span&gt; sets the migration charge as zero cost. &lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;Full&lt;/span&gt; sets the costs as the total of the new rate-plans in-advance charges.  &lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;Difference&lt;/span&gt; is the same calculation as &lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;DifferenceProRated&lt;/span&gt; but no pro-ration is applied.  &lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;ProRated&lt;/span&gt; differs depending on two cases; when moving to a rate-plan of the same duration it pro-rates the in-advance charges of the new rate-plan. If the duration is different, a credit-note will be issued any remaining time on the existing plans billing period.\&quot;, \&quot;default\&quot; : \&quot;DifferenceProRated\&quot;,  \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;] } | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


