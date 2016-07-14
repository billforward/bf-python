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


class Email(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, created=None, changed_by=None, updated=None, id=None, account_id=None, subscription_id=None, invoice_id=None, _from=None, to=None, cc=None, bcc=None, subject=None, html=None, attachment_filename=None, attachment_html=None, plain=None, sent=None, state=None, deleted=False, header_url=None, salutation=None, paragraph1=None, paragraph2=None, footer_information=None, signoff=None, emai_subscription_type=None, notification_id=None, organization_id=None):
        """
        Email - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'created': 'datetime',
            'changed_by': 'str',
            'updated': 'datetime',
            'id': 'str',
            'account_id': 'str',
            'subscription_id': 'str',
            'invoice_id': 'str',
            '_from': 'str',
            'to': 'str',
            'cc': 'str',
            'bcc': 'str',
            'subject': 'str',
            'html': 'str',
            'attachment_filename': 'str',
            'attachment_html': 'str',
            'plain': 'str',
            'sent': 'datetime',
            'state': 'str',
            'deleted': 'bool',
            'header_url': 'str',
            'salutation': 'str',
            'paragraph1': 'str',
            'paragraph2': 'str',
            'footer_information': 'str',
            'signoff': 'str',
            'emai_subscription_type': 'str',
            'notification_id': 'str',
            'organization_id': 'str'
        }

        self.attribute_map = {
            'created': 'created',
            'changed_by': 'changedBy',
            'updated': 'updated',
            'id': 'id',
            'account_id': 'accountID',
            'subscription_id': 'subscriptionID',
            'invoice_id': 'invoiceID',
            '_from': 'from',
            'to': 'to',
            'cc': 'cc',
            'bcc': 'bcc',
            'subject': 'subject',
            'html': 'html',
            'attachment_filename': 'attachmentFilename',
            'attachment_html': 'attachmentHtml',
            'plain': 'plain',
            'sent': 'sent',
            'state': 'state',
            'deleted': 'deleted',
            'header_url': 'headerURL',
            'salutation': 'salutation',
            'paragraph1': 'paragraph1',
            'paragraph2': 'paragraph2',
            'footer_information': 'footerInformation',
            'signoff': 'signoff',
            'emai_subscription_type': 'emaiSubscriptionType',
            'notification_id': 'notificationID',
            'organization_id': 'organizationID'
        }

        self._created = created
        self._changed_by = changed_by
        self._updated = updated
        self._id = id
        self._account_id = account_id
        self._subscription_id = subscription_id
        self._invoice_id = invoice_id
        self.__from = _from
        self._to = to
        self._cc = cc
        self._bcc = bcc
        self._subject = subject
        self._html = html
        self._attachment_filename = attachment_filename
        self._attachment_html = attachment_html
        self._plain = plain
        self._sent = sent
        self._state = state
        self._deleted = deleted
        self._header_url = header_url
        self._salutation = salutation
        self._paragraph1 = paragraph1
        self._paragraph2 = paragraph2
        self._footer_information = footer_information
        self._signoff = signoff
        self._emai_subscription_type = emai_subscription_type
        self._notification_id = notification_id
        self._organization_id = organization_id

    @property
    def created(self):
        """
        Gets the created of this Email.
        { \"description\" : \"The UTC DateTime when the object was created.\", \"verbs\":[] }

        :return: The created of this Email.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this Email.
        { \"description\" : \"The UTC DateTime when the object was created.\", \"verbs\":[] }

        :param created: The created of this Email.
        :type: datetime
        """

        self._created = created

    @property
    def changed_by(self):
        """
        Gets the changed_by of this Email.
        { \"description\" : \"ID of the user who last updated the entity.\", \"verbs\":[] }

        :return: The changed_by of this Email.
        :rtype: str
        """
        return self._changed_by

    @changed_by.setter
    def changed_by(self, changed_by):
        """
        Sets the changed_by of this Email.
        { \"description\" : \"ID of the user who last updated the entity.\", \"verbs\":[] }

        :param changed_by: The changed_by of this Email.
        :type: str
        """

        self._changed_by = changed_by

    @property
    def updated(self):
        """
        Gets the updated of this Email.
        { \"description\" : \"The UTC DateTime when the object was last updated.\", \"verbs\":[] }

        :return: The updated of this Email.
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """
        Sets the updated of this Email.
        { \"description\" : \"The UTC DateTime when the object was last updated.\", \"verbs\":[] }

        :param updated: The updated of this Email.
        :type: datetime
        """

        self._updated = updated

    @property
    def id(self):
        """
        Gets the id of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :return: The id of this Email.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :param id: The id of this Email.
        :type: str
        """

        self._id = id

    @property
    def account_id(self):
        """
        Gets the account_id of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :return: The account_id of this Email.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :param account_id: The account_id of this Email.
        :type: str
        """

        self._account_id = account_id

    @property
    def subscription_id(self):
        """
        Gets the subscription_id of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :return: The subscription_id of this Email.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """
        Sets the subscription_id of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :param subscription_id: The subscription_id of this Email.
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def invoice_id(self):
        """
        Gets the invoice_id of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :return: The invoice_id of this Email.
        :rtype: str
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """
        Sets the invoice_id of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :param invoice_id: The invoice_id of this Email.
        :type: str
        """

        self._invoice_id = invoice_id

    @property
    def _from(self):
        """
        Gets the _from of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :return: The _from of this Email.
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """
        Sets the _from of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :param _from: The _from of this Email.
        :type: str
        """

        self.__from = _from

    @property
    def to(self):
        """
        Gets the to of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :return: The to of this Email.
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """
        Sets the to of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :param to: The to of this Email.
        :type: str
        """

        self._to = to

    @property
    def cc(self):
        """
        Gets the cc of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :return: The cc of this Email.
        :rtype: str
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        """
        Sets the cc of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :param cc: The cc of this Email.
        :type: str
        """

        self._cc = cc

    @property
    def bcc(self):
        """
        Gets the bcc of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :return: The bcc of this Email.
        :rtype: str
        """
        return self._bcc

    @bcc.setter
    def bcc(self, bcc):
        """
        Sets the bcc of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :param bcc: The bcc of this Email.
        :type: str
        """

        self._bcc = bcc

    @property
    def subject(self):
        """
        Gets the subject of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :return: The subject of this Email.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :param subject: The subject of this Email.
        :type: str
        """

        self._subject = subject

    @property
    def html(self):
        """
        Gets the html of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :return: The html of this Email.
        :rtype: str
        """
        return self._html

    @html.setter
    def html(self, html):
        """
        Sets the html of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :param html: The html of this Email.
        :type: str
        """

        self._html = html

    @property
    def attachment_filename(self):
        """
        Gets the attachment_filename of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :return: The attachment_filename of this Email.
        :rtype: str
        """
        return self._attachment_filename

    @attachment_filename.setter
    def attachment_filename(self, attachment_filename):
        """
        Sets the attachment_filename of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :param attachment_filename: The attachment_filename of this Email.
        :type: str
        """

        self._attachment_filename = attachment_filename

    @property
    def attachment_html(self):
        """
        Gets the attachment_html of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :return: The attachment_html of this Email.
        :rtype: str
        """
        return self._attachment_html

    @attachment_html.setter
    def attachment_html(self, attachment_html):
        """
        Sets the attachment_html of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :param attachment_html: The attachment_html of this Email.
        :type: str
        """

        self._attachment_html = attachment_html

    @property
    def plain(self):
        """
        Gets the plain of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :return: The plain of this Email.
        :rtype: str
        """
        return self._plain

    @plain.setter
    def plain(self, plain):
        """
        Sets the plain of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :param plain: The plain of this Email.
        :type: str
        """

        self._plain = plain

    @property
    def sent(self):
        """
        Gets the sent of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :return: The sent of this Email.
        :rtype: datetime
        """
        return self._sent

    @sent.setter
    def sent(self, sent):
        """
        Sets the sent of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :param sent: The sent of this Email.
        :type: datetime
        """

        self._sent = sent

    @property
    def state(self):
        """
        Gets the state of this Email.
        { \"description\" : \".\", \"verbs\":[\"GET\"] }

        :return: The state of this Email.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this Email.
        { \"description\" : \".\", \"verbs\":[\"GET\"] }

        :param state: The state of this Email.
        :type: str
        """
        allowed_values = ["Pending", "Unsent", "Sent"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def deleted(self):
        """
        Gets the deleted of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :return: The deleted of this Email.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """
        Sets the deleted of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :param deleted: The deleted of this Email.
        :type: bool
        """

        self._deleted = deleted

    @property
    def header_url(self):
        """
        Gets the header_url of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :return: The header_url of this Email.
        :rtype: str
        """
        return self._header_url

    @header_url.setter
    def header_url(self, header_url):
        """
        Sets the header_url of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :param header_url: The header_url of this Email.
        :type: str
        """

        self._header_url = header_url

    @property
    def salutation(self):
        """
        Gets the salutation of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :return: The salutation of this Email.
        :rtype: str
        """
        return self._salutation

    @salutation.setter
    def salutation(self, salutation):
        """
        Sets the salutation of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :param salutation: The salutation of this Email.
        :type: str
        """

        self._salutation = salutation

    @property
    def paragraph1(self):
        """
        Gets the paragraph1 of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :return: The paragraph1 of this Email.
        :rtype: str
        """
        return self._paragraph1

    @paragraph1.setter
    def paragraph1(self, paragraph1):
        """
        Sets the paragraph1 of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :param paragraph1: The paragraph1 of this Email.
        :type: str
        """

        self._paragraph1 = paragraph1

    @property
    def paragraph2(self):
        """
        Gets the paragraph2 of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :return: The paragraph2 of this Email.
        :rtype: str
        """
        return self._paragraph2

    @paragraph2.setter
    def paragraph2(self, paragraph2):
        """
        Sets the paragraph2 of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :param paragraph2: The paragraph2 of this Email.
        :type: str
        """

        self._paragraph2 = paragraph2

    @property
    def footer_information(self):
        """
        Gets the footer_information of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :return: The footer_information of this Email.
        :rtype: str
        """
        return self._footer_information

    @footer_information.setter
    def footer_information(self, footer_information):
        """
        Sets the footer_information of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :param footer_information: The footer_information of this Email.
        :type: str
        """

        self._footer_information = footer_information

    @property
    def signoff(self):
        """
        Gets the signoff of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :return: The signoff of this Email.
        :rtype: str
        """
        return self._signoff

    @signoff.setter
    def signoff(self, signoff):
        """
        Sets the signoff of this Email.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :param signoff: The signoff of this Email.
        :type: str
        """

        self._signoff = signoff

    @property
    def emai_subscription_type(self):
        """
        Gets the emai_subscription_type of this Email.


        :return: The emai_subscription_type of this Email.
        :rtype: str
        """
        return self._emai_subscription_type

    @emai_subscription_type.setter
    def emai_subscription_type(self, emai_subscription_type):
        """
        Sets the emai_subscription_type of this Email.


        :param emai_subscription_type: The emai_subscription_type of this Email.
        :type: str
        """
        allowed_values = ["FailedPayment", "InvoicePaid", "SubscriptionCancellation", "SubscriptionCancelled", "SubscriptionPlanMigrated", "SubscriptionPlanMigrating", "CardExpired", "CardExpiring"]
        if emai_subscription_type not in allowed_values:
            raise ValueError(
                "Invalid value for `emai_subscription_type` ({0}), must be one of {1}"
                .format(emai_subscription_type, allowed_values)
            )

        self._emai_subscription_type = emai_subscription_type

    @property
    def notification_id(self):
        """
        Gets the notification_id of this Email.
        { \"description\" : \"\", \"verbs\":[] }

        :return: The notification_id of this Email.
        :rtype: str
        """
        return self._notification_id

    @notification_id.setter
    def notification_id(self, notification_id):
        """
        Sets the notification_id of this Email.
        { \"description\" : \"\", \"verbs\":[] }

        :param notification_id: The notification_id of this Email.
        :type: str
        """

        self._notification_id = notification_id

    @property
    def organization_id(self):
        """
        Gets the organization_id of this Email.
        { \"description\" : \"\", \"verbs\":[] }

        :return: The organization_id of this Email.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """
        Sets the organization_id of this Email.
        { \"description\" : \"\", \"verbs\":[] }

        :param organization_id: The organization_id of this Email.
        :type: str
        """

        self._organization_id = organization_id

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
