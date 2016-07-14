# AuditEntry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changed_by** | **str** | { \&quot;description\&quot; : \&quot;ID of the user who made the change.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**id** | **str** | { \&quot;description\&quot; : \&quot;ID of the audit-entry.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**organization_id** | **str** | { \&quot;description\&quot; : \&quot;ID of the organization associated with the audit-entry.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**entity** | **str** | { \&quot;description\&quot; : \&quot;The entity type.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**entity_id** | **str** | { \&quot;description\&quot; : \&quot;ID of the entity.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**audit_action** | **str** | { \&quot;description\&quot; : \&quot;update, insert\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**field_changes** | **list[str]** | { \&quot;description\&quot; : \&quot;A description of the changes.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**new_entity** | **list[str]** |  | 
**state** | **str** | { \&quot;description\&quot; : \&quot;The state of the audit entry.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**created** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was created.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


