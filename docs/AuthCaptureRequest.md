# AuthCaptureRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**account_id** | **str** | {\&quot;description\&quot;:\&quot;ID of the BillForward Account with which you would like to associate the created payment method.&lt;br&gt;If omitted, BillForward will associate the created PaymentMethod with a newly-created Account, whose Profile details will be populated using billing information from the funding instrument.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;]} | [optional] 
**gateway** | **str** | {\&quot;description\&quot;:\&quot;The gateway with which your funding instrument has been vaulted.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;]} | [optional] 
**company_name** | **str** | {\&quot;description\&quot;:\&quot;The name of the company of the customer from whose card a PaymentMethod is being produced. If provided: this metadata will be used to populate a Profile &amp;mdash; should a BillForward Account be created by this request.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;]} | [optional] 
**email** | **str** | {\&quot;description\&quot;:\&quot;The email address of the customer from whose card a PaymentMethod is being produced. If provided: this metadata will be used to populate a Profile &amp;mdash; should a BillForward Account be created by this request.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;]} | [optional] 
**first_name** | **str** | {\&quot;description\&quot;:\&quot;The first name of the customer from whose card a PaymentMethod is being produced. If provided: this metadata will be used to populate a Profile &amp;mdash; should a BillForward Account be created by this request.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;]} | [optional] 
**last_name** | **str** | {\&quot;description\&quot;:\&quot;The last name of the customer from whose card a PaymentMethod is being produced. If provided: this metadata will be used to populate a Profile &amp;mdash; should a BillForward Account be created by this request.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;]} | [optional] 
**mobile** | **str** | {\&quot;description\&quot;:\&quot;The mobile phone number of the customer from whose card a PaymentMethod is being produced. If provided: this metadata will be used to populate a Profile &amp;mdash; should a BillForward Account be created by this request.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;]} | [optional] 
**default_payment_method** | **bool** | {\&quot;default\&quot;:false,\&quot;description\&quot;:\&quot;Whether the PaymentMethod produced by this request should be elected as the &#39;default&#39; payment method for the concerned BillForward Account. Whichever PaymentMethod is elected as an Account&#39;s default payment method, will be consulted whenever payment is demanded of that Account (i.e. upon the execution of any of the Account&#39;s invoices).\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;]} | [optional] [default to False]
**organization_id** | **str** | {\&quot;description\&quot;:\&quot;ID of the BillForward Organization within which the requested PaymentMethod should be created. If omitted, this will be auto-populated using your authentication credentials.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;]} | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


