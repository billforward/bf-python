# BFPermission

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was created.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**changed_by** | **str** | { \&quot;description\&quot; : \&quot;ID of the user who last updated the entity.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**updated** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was last updated.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**id** | **str** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | [optional] 
**role_id** | **str** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;, \&quot;POST\&quot;] } | [optional] 
**role_name** | **str** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;, \&quot;POST\&quot;] } | [optional] 
**resource** | **str** | { \&quot;description\&quot; : \&quot;BillForward resource associated with this permission.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;,\&quot;POST\&quot;,\&quot;PUT\&quot;] } | [optional] 
**action** | **str** | { \&quot;description\&quot; : \&quot;Action they may be performed on the associated resource.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;,\&quot;POST\&quot;,\&quot;PUT\&quot;] } | [optional] 
**revoked** | **datetime** | { \&quot;description\&quot; : \&quot;If a permission is deleted it is set as revoked from this date. The role with this permission will no longer have its applied.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;,\&quot;POST\&quot;,\&quot;PUT\&quot;] } | [optional] 
**deleted** | **bool** | { \&quot;default\&quot; : \&quot;false\&quot;, \&quot;description\&quot; : \&quot;If a permission is deleted the role with this permission will no longer have its applied.\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;,\&quot;POST\&quot;,\&quot;PUT\&quot;] } | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


