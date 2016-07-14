# coding: utf-8

"""
    BillForward REST API


    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class PricingComponentValueChangeAmendment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, created=None, changed_by=None, updated=None, type=None, id=None, organization_id=None, subscription_id=None, amendment_type=None, actioning_time=None, actioned_time=None, state=None, deleted=False, invoicing_type=None, invoice_id=None, component_changes=None):
        """
        PricingComponentValueChangeAmendment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'created': 'datetime',
            'changed_by': 'str',
            'updated': 'datetime',
            'type': 'str',
            'id': 'str',
            'organization_id': 'str',
            'subscription_id': 'str',
            'amendment_type': 'str',
            'actioning_time': 'datetime',
            'actioned_time': 'datetime',
            'state': 'str',
            'deleted': 'bool',
            'invoicing_type': 'str',
            'invoice_id': 'str',
            'component_changes': 'list[ComponentChange]'
        }

        self.attribute_map = {
            'created': 'created',
            'changed_by': 'changedBy',
            'updated': 'updated',
            'type': '@type',
            'id': 'id',
            'organization_id': 'organizationID',
            'subscription_id': 'subscriptionID',
            'amendment_type': 'amendmentType',
            'actioning_time': 'actioningTime',
            'actioned_time': 'actionedTime',
            'state': 'state',
            'deleted': 'deleted',
            'invoicing_type': 'invoicingType',
            'invoice_id': 'invoiceID',
            'component_changes': 'componentChanges'
        }

        self._created = created
        self._changed_by = changed_by
        self._updated = updated
        self._type = type
        self._id = id
        self._organization_id = organization_id
        self._subscription_id = subscription_id
        self._amendment_type = amendment_type
        self._actioning_time = actioning_time
        self._actioned_time = actioned_time
        self._state = state
        self._deleted = deleted
        self._invoicing_type = invoicing_type
        self._invoice_id = invoice_id
        self._component_changes = component_changes

    @property
    def created(self):
        """
        Gets the created of this PricingComponentValueChangeAmendment.
        { \"description\" : \"The UTC DateTime when the object was created.\", \"verbs\":[] }

        :return: The created of this PricingComponentValueChangeAmendment.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this PricingComponentValueChangeAmendment.
        { \"description\" : \"The UTC DateTime when the object was created.\", \"verbs\":[] }

        :param created: The created of this PricingComponentValueChangeAmendment.
        :type: datetime
        """

        self._created = created

    @property
    def changed_by(self):
        """
        Gets the changed_by of this PricingComponentValueChangeAmendment.
        { \"description\" : \"ID of the user who last updated the entity.\", \"verbs\":[] }

        :return: The changed_by of this PricingComponentValueChangeAmendment.
        :rtype: str
        """
        return self._changed_by

    @changed_by.setter
    def changed_by(self, changed_by):
        """
        Sets the changed_by of this PricingComponentValueChangeAmendment.
        { \"description\" : \"ID of the user who last updated the entity.\", \"verbs\":[] }

        :param changed_by: The changed_by of this PricingComponentValueChangeAmendment.
        :type: str
        """

        self._changed_by = changed_by

    @property
    def updated(self):
        """
        Gets the updated of this PricingComponentValueChangeAmendment.
        { \"description\" : \"The UTC DateTime when the object was last updated.\", \"verbs\":[] }

        :return: The updated of this PricingComponentValueChangeAmendment.
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """
        Sets the updated of this PricingComponentValueChangeAmendment.
        { \"description\" : \"The UTC DateTime when the object was last updated.\", \"verbs\":[] }

        :param updated: The updated of this PricingComponentValueChangeAmendment.
        :type: datetime
        """

        self._updated = updated

    @property
    def type(self):
        """
        Gets the type of this PricingComponentValueChangeAmendment.
        { \"description\" : \"\", \"default\" : \"\", \"verbs\":[\"POST\",\"GET\"] }

        :return: The type of this PricingComponentValueChangeAmendment.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this PricingComponentValueChangeAmendment.
        { \"description\" : \"\", \"default\" : \"\", \"verbs\":[\"POST\",\"GET\"] }

        :param type: The type of this PricingComponentValueChangeAmendment.
        :type: str
        """
        allowed_values = ["InvoiceOutstandingChargesAmendment", "IssueInvoiceAmendment", "PricingComponentValueAmendment", "InvoiceRecalculationAmendment", "CancellationAmendment", "InvoiceNextExecutionAttemptAmendment", "FixedTermExpiryAmendment", "EndTrialAmendment", "ProductRatePlanMigrationAmendment", "AmendmentDiscardAmendment", "UpdateComponentValueAmendment", "ServiceEndAmendment", "ResumeSubscriptionAmendment", "CreateSubscriptionChargeAmendment", "TimerAmendment"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def id(self):
        """
        Gets the id of this PricingComponentValueChangeAmendment.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :return: The id of this PricingComponentValueChangeAmendment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PricingComponentValueChangeAmendment.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :param id: The id of this PricingComponentValueChangeAmendment.
        :type: str
        """

        self._id = id

    @property
    def organization_id(self):
        """
        Gets the organization_id of this PricingComponentValueChangeAmendment.
        { \"description\" : \"\", \"verbs\":[\"\"] }

        :return: The organization_id of this PricingComponentValueChangeAmendment.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """
        Sets the organization_id of this PricingComponentValueChangeAmendment.
        { \"description\" : \"\", \"verbs\":[\"\"] }

        :param organization_id: The organization_id of this PricingComponentValueChangeAmendment.
        :type: str
        """

        self._organization_id = organization_id

    @property
    def subscription_id(self):
        """
        Gets the subscription_id of this PricingComponentValueChangeAmendment.
        { \"description\" : \"\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The subscription_id of this PricingComponentValueChangeAmendment.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """
        Sets the subscription_id of this PricingComponentValueChangeAmendment.
        { \"description\" : \"\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param subscription_id: The subscription_id of this PricingComponentValueChangeAmendment.
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def amendment_type(self):
        """
        Gets the amendment_type of this PricingComponentValueChangeAmendment.
        { \"description\" : \"Type of amendment\", \"verbs\":[\"POST\",\"GET\"] }

        :return: The amendment_type of this PricingComponentValueChangeAmendment.
        :rtype: str
        """
        return self._amendment_type

    @amendment_type.setter
    def amendment_type(self, amendment_type):
        """
        Sets the amendment_type of this PricingComponentValueChangeAmendment.
        { \"description\" : \"Type of amendment\", \"verbs\":[\"POST\",\"GET\"] }

        :param amendment_type: The amendment_type of this PricingComponentValueChangeAmendment.
        :type: str
        """
        allowed_values = ["InvoiceNextExecutionAttempt", "Cancellation", "PricingComponentValue", "AmendmentDiscard", "Compound", "FixedTermExpiry", "InvoiceRecalculation", "EndTrial", "InvoiceOutstandingCharges", "IssueInvoice", "ProductRatePlanMigration", "UpdateComponentValue", "ServiceEnd", "ResumeSubscription", "CreateSubscriptionCharge", "Timer"]
        if amendment_type not in allowed_values:
            raise ValueError(
                "Invalid value for `amendment_type` ({0}), must be one of {1}"
                .format(amendment_type, allowed_values)
            )

        self._amendment_type = amendment_type

    @property
    def actioning_time(self):
        """
        Gets the actioning_time of this PricingComponentValueChangeAmendment.
        { \"description\" : \"When the amendment will run\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The actioning_time of this PricingComponentValueChangeAmendment.
        :rtype: datetime
        """
        return self._actioning_time

    @actioning_time.setter
    def actioning_time(self, actioning_time):
        """
        Sets the actioning_time of this PricingComponentValueChangeAmendment.
        { \"description\" : \"When the amendment will run\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param actioning_time: The actioning_time of this PricingComponentValueChangeAmendment.
        :type: datetime
        """

        self._actioning_time = actioning_time

    @property
    def actioned_time(self):
        """
        Gets the actioned_time of this PricingComponentValueChangeAmendment.
        { \"description\" : \"The time the amendment completed.\", \"verbs\":[\"GET\"] }

        :return: The actioned_time of this PricingComponentValueChangeAmendment.
        :rtype: datetime
        """
        return self._actioned_time

    @actioned_time.setter
    def actioned_time(self, actioned_time):
        """
        Sets the actioned_time of this PricingComponentValueChangeAmendment.
        { \"description\" : \"The time the amendment completed.\", \"verbs\":[\"GET\"] }

        :param actioned_time: The actioned_time of this PricingComponentValueChangeAmendment.
        :type: datetime
        """

        self._actioned_time = actioned_time

    @property
    def state(self):
        """
        Gets the state of this PricingComponentValueChangeAmendment.
        Whether the subscription-amendment is: pending (to be actioned in the future), succeeded (actioning completed), failed (actioning was attempted but no effect was made) or discarded (the amendment had been cancelled before being actioned). Default: Pending

        :return: The state of this PricingComponentValueChangeAmendment.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this PricingComponentValueChangeAmendment.
        Whether the subscription-amendment is: pending (to be actioned in the future), succeeded (actioning completed), failed (actioning was attempted but no effect was made) or discarded (the amendment had been cancelled before being actioned). Default: Pending

        :param state: The state of this PricingComponentValueChangeAmendment.
        :type: str
        """
        allowed_values = ["Pending", "Succeeded", "Failed", "Discarded"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def deleted(self):
        """
        Gets the deleted of this PricingComponentValueChangeAmendment.
        { \"description\" : \"Is the amendment deleted.\", \"verbs\":[\"GET\"] }

        :return: The deleted of this PricingComponentValueChangeAmendment.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """
        Sets the deleted of this PricingComponentValueChangeAmendment.
        { \"description\" : \"Is the amendment deleted.\", \"verbs\":[\"GET\"] }

        :param deleted: The deleted of this PricingComponentValueChangeAmendment.
        :type: bool
        """

        self._deleted = deleted

    @property
    def invoicing_type(self):
        """
        Gets the invoicing_type of this PricingComponentValueChangeAmendment.
        { \"description\" : \"<span class=\\\"label label-default\\\">Immediate</span> generates an invoice straight away for any costs arising from this change, for example upgrade charge. <span class=\\\"label label-default\\\">Aggregated</span> add any upgrade charges to the next invoice, generally this would be at the next period end.\",  \"default\" : \"Aggregated\", \"verbs\":[\"POST\",\"GET\"] }

        :return: The invoicing_type of this PricingComponentValueChangeAmendment.
        :rtype: str
        """
        return self._invoicing_type

    @invoicing_type.setter
    def invoicing_type(self, invoicing_type):
        """
        Sets the invoicing_type of this PricingComponentValueChangeAmendment.
        { \"description\" : \"<span class=\\\"label label-default\\\">Immediate</span> generates an invoice straight away for any costs arising from this change, for example upgrade charge. <span class=\\\"label label-default\\\">Aggregated</span> add any upgrade charges to the next invoice, generally this would be at the next period end.\",  \"default\" : \"Aggregated\", \"verbs\":[\"POST\",\"GET\"] }

        :param invoicing_type: The invoicing_type of this PricingComponentValueChangeAmendment.
        :type: str
        """
        allowed_values = ["Immediate", "Aggregated"]
        if invoicing_type not in allowed_values:
            raise ValueError(
                "Invalid value for `invoicing_type` ({0}), must be one of {1}"
                .format(invoicing_type, allowed_values)
            )

        self._invoicing_type = invoicing_type

    @property
    def invoice_id(self):
        """
        Gets the invoice_id of this PricingComponentValueChangeAmendment.
        { \"description\" : \"Identifer of the invoice with the charges for this change.\", \"verbs\":[\"GET\"] }

        :return: The invoice_id of this PricingComponentValueChangeAmendment.
        :rtype: str
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """
        Sets the invoice_id of this PricingComponentValueChangeAmendment.
        { \"description\" : \"Identifer of the invoice with the charges for this change.\", \"verbs\":[\"GET\"] }

        :param invoice_id: The invoice_id of this PricingComponentValueChangeAmendment.
        :type: str
        """

        self._invoice_id = invoice_id

    @property
    def component_changes(self):
        """
        Gets the component_changes of this PricingComponentValueChangeAmendment.
        { \"description\" : \"Changes to perform, for example upgrade\", \"verbs\":[\"POST\",\"GET\"] }

        :return: The component_changes of this PricingComponentValueChangeAmendment.
        :rtype: list[ComponentChange]
        """
        return self._component_changes

    @component_changes.setter
    def component_changes(self, component_changes):
        """
        Sets the component_changes of this PricingComponentValueChangeAmendment.
        { \"description\" : \"Changes to perform, for example upgrade\", \"verbs\":[\"POST\",\"GET\"] }

        :param component_changes: The component_changes of this PricingComponentValueChangeAmendment.
        :type: list[ComponentChange]
        """

        self._component_changes = component_changes

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
