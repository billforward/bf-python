# User

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] 
**changed_by** | **str** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**id** | **str** |  | [optional] 
**organization_id** | **str** |  | 
**password** | [**list[Password]**](Password.md) |  | [optional] 
**username** | [**list[Username]**](Username.md) |  | [optional] 
**open_id_identifier** | **str** |  | [optional] 
**password_reset_code** | **str** |  | [optional] 
**password_reset_attempts** | **int** |  | [optional] 
**password_reset_valid_till** | **datetime** |  | [optional] 
**last_successful_login** | **datetime** |  | [optional] 
**successful_logins** | **int** |  | [optional] 
**bf_admin** | **bool** |  | [optional] 
**enabled** | **bool** |  | 
**timezone** | [**UserTimezone**](UserTimezone.md) |  | 
**flexcheck_user** | **bool** |  | 
**two_fa** | **bool** |  | [optional] 
**email** | **str** |  | [optional] 
**main_username** | [**Username**](Username.md) |  | [optional] 
**active_usernames** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

