# Role

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was created.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**changed_by** | **str** | { \&quot;description\&quot; : \&quot;ID of the user who last updated the entity.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**updated** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was last updated.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**id** | **str** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**organization_id** | **str** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[\&quot;\&quot;] } | [optional] 
**name** | **str** | { \&quot;description\&quot; : \&quot;Friendly name of the role.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;,\&quot;POST\&quot;,\&quot;PUT\&quot;] } | [optional] 
**description** | **str** | { \&quot;description\&quot; : \&quot;Friendly description of the role.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;,\&quot;POST\&quot;,\&quot;PUT\&quot;] } | [optional] 
**revoked** | **datetime** | { \&quot;description\&quot; : \&quot;If a role is deleted it is set as revoked from this date. Any account in the role will no longer have its permissions.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;,\&quot;POST\&quot;,\&quot;PUT\&quot;] } | [optional] 
**deleted** | **bool** | { \&quot;default\&quot; : \&quot;false\&quot;, \&quot;description\&quot; : \&quot;If a role is deleted any account in the role will no longer have its permissions.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;,\&quot;POST\&quot;,\&quot;PUT\&quot;] } | [optional] [default to False]
**default_role** | **bool** | { \&quot;default\&quot; : \&quot;false\&quot;, \&quot;description\&quot; : \&quot;If set this role will become the default role for the organization. Any accounts without an explicitly set role will have this applied.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;,\&quot;POST\&quot;,\&quot;PUT\&quot;] } | [optional] [default to False]
**default_returned** | **bool** | { \&quot;default\&quot; : \&quot;false\&quot;, \&quot;description\&quot; : \&quot;When returning the list of roles for an account, this indicates if the role was returned due to defaulting.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;,\&quot;POST\&quot;,\&quot;PUT\&quot;] } | [optional] [default to False]
**permissions** | [**list[BFPermission]**](BFPermission.md) | { \&quot;description\&quot; : \&quot;List of permissions in this role.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;,\&quot;POST\&quot;,\&quot;PUT\&quot;] } | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


