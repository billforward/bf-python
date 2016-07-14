# UpdateRoleRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was created.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**organization_id** | **str** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[\&quot;\&quot;] } | [optional] 
**id** | **str** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;, \&quot;PUT\&quot;] } | 
**name** | **str** | { \&quot;description\&quot; : \&quot;Friendly name of the role.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;,\&quot;POST\&quot;,\&quot;PUT\&quot;] } | [optional] 
**description** | **str** | { \&quot;description\&quot; : \&quot;Friendly description of the role.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;,\&quot;POST\&quot;,\&quot;PUT\&quot;] } | [optional] 
**default_role** | **bool** | { \&quot;description\&quot; : \&quot;If set this role will become the default role for the organization unsetting any existing role. Any accounts without an explicitly set role will have this applied.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;,\&quot;POST\&quot;,\&quot;PUT\&quot;] } | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


