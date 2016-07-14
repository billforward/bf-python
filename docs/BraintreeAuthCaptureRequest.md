# BraintreeAuthCaptureRequest

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
**payment_method_nonce** | **str** | {\&quot;description\&quot;:\&quot;One-use cryptographic nonce &lt;a href&#x3D;\\\&quot;https://developers.braintreepayments.com/javascript+node/start/overview\\\&quot;&gt;provided by Braintree&#39;s client-side card capture SDK&lt;/a&gt;, in response to your capturing a card into the Braintree vault. This nonce will be used by BillForward to find the tokenized card within the Braintree vault &amp;mdash; precursory to linking a BillForward PaymentMethod to that tokenized card\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;]} | 
**device_data** | **str** | {\&quot;description\&quot;:\&quot;(Required when vaulting a PayPal payment method; otherwise optional)&lt;br&gt;A JSON string providing information about the device your customer used to fill out the card capture form. This information is inserted into your form by &lt;a href&#x3D;\\\&quot;https://developers.braintreepayments.com/javascript+node/guides/advanced-fraud-tools/client-side\\\&quot;&gt;braintree-data.js&lt;/a&gt; &amp;mdash; if and only if you use Braintree&#39;s drop-in form integrations. You should ideally provide it if you have one (it aids with fraud detection), but it is only mandatory in the case of PayPal payment method vaulting.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;]} | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

