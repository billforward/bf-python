# InvoiceLine

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit_of_measure** | [**UnitOfMeasure**](UnitOfMeasure.md) | { \&quot;description\&quot; : \&quot;The unit-of-measure associated with the invoice-line.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**pricing_component_type** | **str** | { \&quot;description\&quot; : \&quot;The type of the pricing component associated with the invoice line.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**charge_type** | **str** | { \&quot;description\&quot; : \&quot;charge-type.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**period_start** | **datetime** | The period start of the charge. | 
**period_end** | **datetime** | The period end of the charge. | 
**created** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was created.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**changed_by** | **str** | { \&quot;description\&quot; : \&quot;ID of the user who last updated the entity.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**updated** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was last updated.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**id** | **str** | { \&quot;description\&quot; : \&quot;ID of the invoice-line.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**invoice_id** | **str** | { \&quot;description\&quot; : \&quot;invoice associated with the invoice-line.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**unit_of_measure_id** | **str** | { \&quot;description\&quot; : \&quot;unit-of-measure associated with the invoice-line.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**subscription_id** | **str** | { \&quot;description\&quot; : \&quot;the subscription ID associated with the invoice-line.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**product_rate_plan_id** | **str** | { \&quot;description\&quot; : \&quot;the product rate plan ID associated with the invoice-line.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**public_product_rate_plan_name** | **str** | { \&quot;description\&quot; : \&quot;the public product rate plan name associated with the invoice-line.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**product_rate_plan_name** | **str** | { \&quot;description\&quot; : \&quot;the product rate plan name associated with the invoice-line.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**product_id** | **str** | { \&quot;description\&quot; : \&quot;the product ID associated with the invoice-line.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**public_product_name** | **str** | { \&quot;description\&quot; : \&quot;the public product name associated with the invoice-line.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**product_name** | **str** | { \&quot;description\&quot; : \&quot;the product name associated with the invoice-line.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**organization_id** | **str** | { \&quot;description\&quot; : \&quot;ID of the organization associated with the invoice-line.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**name** | **str** | { \&quot;description\&quot; : \&quot;The human readable name of the invoice-line.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**description** | **str** | { \&quot;description\&quot; : \&quot;The human readable description of the invoice-line.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**calculation** | **str** | { \&quot;description\&quot; : \&quot;A human readable explanation of how the value of the invoice-line was calculated.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**cost** | **float** | { \&quot;description\&quot; : \&quot;The cost of the invoice-line including tax.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**tax** | **float** | { \&quot;description\&quot; : \&quot;The cumulative tax of the invoice-line.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**component_value** | **int** | { \&quot;description\&quot; : \&quot;The component value for the unit-of-measure that is associated with the invoice-line.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**pricing_component_id** | **str** | The ID of the pricing-component that is associated with the invoice-line. | 
**public_pricing_component_name** | **str** | The public name of the pricing-component that is associated with the invoice-line. | 
**pricing_component_name** | **str** | The name of the pricing-component that is associated with the invoice-line. | 
**subscription_charge_id** | **str** | The ID of the subscription-charge that is associated with the invoice-line. | 
**child_invoice_id** | **str** | The ID of the invoice that is associated with the invoice-line. | 
**type** | **str** | The type of the invoice-line. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


