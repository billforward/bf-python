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


class CouponRule(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, parent_rule_id=None, created=None, changed_by=None, updated=None, id=None, organization_id=None, coupon_definition_id=None, subject=None, polarity=None, verb=None, preposition=None, parameter=None, object=None, rule_validation_strategy=None, specifier=None, deleted=False, child_rules=None):
        """
        CouponRule - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'parent_rule_id': 'str',
            'created': 'datetime',
            'changed_by': 'str',
            'updated': 'datetime',
            'id': 'str',
            'organization_id': 'str',
            'coupon_definition_id': 'str',
            'subject': 'str',
            'polarity': 'str',
            'verb': 'str',
            'preposition': 'str',
            'parameter': 'str',
            'object': 'str',
            'rule_validation_strategy': 'str',
            'specifier': 'str',
            'deleted': 'bool',
            'child_rules': 'list[CouponRule]'
        }

        self.attribute_map = {
            'parent_rule_id': 'parentRuleID',
            'created': 'created',
            'changed_by': 'changedBy',
            'updated': 'updated',
            'id': 'id',
            'organization_id': 'organizationID',
            'coupon_definition_id': 'couponDefinitionID',
            'subject': 'subject',
            'polarity': 'polarity',
            'verb': 'verb',
            'preposition': 'preposition',
            'parameter': 'parameter',
            'object': 'object',
            'rule_validation_strategy': 'ruleValidationStrategy',
            'specifier': 'specifier',
            'deleted': 'deleted',
            'child_rules': 'childRules'
        }

        self._parent_rule_id = parent_rule_id
        self._created = created
        self._changed_by = changed_by
        self._updated = updated
        self._id = id
        self._organization_id = organization_id
        self._coupon_definition_id = coupon_definition_id
        self._subject = subject
        self._polarity = polarity
        self._verb = verb
        self._preposition = preposition
        self._parameter = parameter
        self._object = object
        self._rule_validation_strategy = rule_validation_strategy
        self._specifier = specifier
        self._deleted = deleted
        self._child_rules = child_rules

    @property
    def parent_rule_id(self):
        """
        Gets the parent_rule_id of this CouponRule.
        { \"description\" : \"ID of the parent of this coupon-rule.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The parent_rule_id of this CouponRule.
        :rtype: str
        """
        return self._parent_rule_id

    @parent_rule_id.setter
    def parent_rule_id(self, parent_rule_id):
        """
        Sets the parent_rule_id of this CouponRule.
        { \"description\" : \"ID of the parent of this coupon-rule.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param parent_rule_id: The parent_rule_id of this CouponRule.
        :type: str
        """

        self._parent_rule_id = parent_rule_id

    @property
    def created(self):
        """
        Gets the created of this CouponRule.
        { \"description\" : \"The UTC DateTime when the object was created.\", \"verbs\":[] }

        :return: The created of this CouponRule.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this CouponRule.
        { \"description\" : \"The UTC DateTime when the object was created.\", \"verbs\":[] }

        :param created: The created of this CouponRule.
        :type: datetime
        """

        self._created = created

    @property
    def changed_by(self):
        """
        Gets the changed_by of this CouponRule.
        { \"description\" : \"ID of the user who last updated the entity.\", \"verbs\":[] }

        :return: The changed_by of this CouponRule.
        :rtype: str
        """
        return self._changed_by

    @changed_by.setter
    def changed_by(self, changed_by):
        """
        Sets the changed_by of this CouponRule.
        { \"description\" : \"ID of the user who last updated the entity.\", \"verbs\":[] }

        :param changed_by: The changed_by of this CouponRule.
        :type: str
        """

        self._changed_by = changed_by

    @property
    def updated(self):
        """
        Gets the updated of this CouponRule.
        { \"description\" : \"The UTC DateTime when the object was last updated.\", \"verbs\":[] }

        :return: The updated of this CouponRule.
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """
        Sets the updated of this CouponRule.
        { \"description\" : \"The UTC DateTime when the object was last updated.\", \"verbs\":[] }

        :param updated: The updated of this CouponRule.
        :type: datetime
        """

        self._updated = updated

    @property
    def id(self):
        """
        Gets the id of this CouponRule.
        { \"description\" : \"ID of the coupon-rule.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The id of this CouponRule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CouponRule.
        { \"description\" : \"ID of the coupon-rule.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param id: The id of this CouponRule.
        :type: str
        """

        self._id = id

    @property
    def organization_id(self):
        """
        Gets the organization_id of this CouponRule.
        { \"description\" : \"ID of the organization associated with the coupon-rule.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The organization_id of this CouponRule.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """
        Sets the organization_id of this CouponRule.
        { \"description\" : \"ID of the organization associated with the coupon-rule.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param organization_id: The organization_id of this CouponRule.
        :type: str
        """

        self._organization_id = organization_id

    @property
    def coupon_definition_id(self):
        """
        Gets the coupon_definition_id of this CouponRule.
        { \"description\" : \"ID of the coupon-definition associated with the coupon-rule.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The coupon_definition_id of this CouponRule.
        :rtype: str
        """
        return self._coupon_definition_id

    @coupon_definition_id.setter
    def coupon_definition_id(self, coupon_definition_id):
        """
        Sets the coupon_definition_id of this CouponRule.
        { \"description\" : \"ID of the coupon-definition associated with the coupon-rule.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param coupon_definition_id: The coupon_definition_id of this CouponRule.
        :type: str
        """

        self._coupon_definition_id = coupon_definition_id

    @property
    def subject(self):
        """
        Gets the subject of this CouponRule.
        { \"description\" : \"The subject of the coupon-rule. The coupon-rule can operate on either the user or subscription that the coupon-instance is associated with.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The subject of this CouponRule.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this CouponRule.
        { \"description\" : \"The subject of the coupon-rule. The coupon-rule can operate on either the user or subscription that the coupon-instance is associated with.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param subject: The subject of this CouponRule.
        :type: str
        """
        allowed_values = ["user", "current_subscription", "child_rules"]
        if subject not in allowed_values:
            raise ValueError(
                "Invalid value for `subject` ({0}), must be one of {1}"
                .format(subject, allowed_values)
            )

        self._subject = subject

    @property
    def polarity(self):
        """
        Gets the polarity of this CouponRule.
        { \"description\" : \"Specifies whether the rule's result will affect the application of the coupon-instance positively or negatively.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The polarity of this CouponRule.
        :rtype: str
        """
        return self._polarity

    @polarity.setter
    def polarity(self, polarity):
        """
        Sets the polarity of this CouponRule.
        { \"description\" : \"Specifies whether the rule's result will affect the application of the coupon-instance positively or negatively.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param polarity: The polarity of this CouponRule.
        :type: str
        """
        allowed_values = ["does", "does_not"]
        if polarity not in allowed_values:
            raise ValueError(
                "Invalid value for `polarity` ({0}), must be one of {1}"
                .format(polarity, allowed_values)
            )

        self._polarity = polarity

    @property
    def verb(self):
        """
        Gets the verb of this CouponRule.
        { \"description\" : \"The verb of the coupon-rule. coupon-rules can check whether the user or subscription has a certain property.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The verb of this CouponRule.
        :rtype: str
        """
        return self._verb

    @verb.setter
    def verb(self, verb):
        """
        Sets the verb of this CouponRule.
        { \"description\" : \"The verb of the coupon-rule. coupon-rules can check whether the user or subscription has a certain property.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param verb: The verb of this CouponRule.
        :type: str
        """
        allowed_values = ["have"]
        if verb not in allowed_values:
            raise ValueError(
                "Invalid value for `verb` ({0}), must be one of {1}"
                .format(verb, allowed_values)
            )

        self._verb = verb

    @property
    def preposition(self):
        """
        Gets the preposition of this CouponRule.
        { \"description\" : \"This is the comparison operator of the coupon-rule's parameter and the subject's object.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The preposition of this CouponRule.
        :rtype: str
        """
        return self._preposition

    @preposition.setter
    def preposition(self, preposition):
        """
        Sets the preposition of this CouponRule.
        { \"description\" : \"This is the comparison operator of the coupon-rule's parameter and the subject's object.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param preposition: The preposition of this CouponRule.
        :type: str
        """
        allowed_values = ["less_than", "less_than_or_equal_to", "greater_than", "greater_than_or_equal_to", "equal_to"]
        if preposition not in allowed_values:
            raise ValueError(
                "Invalid value for `preposition` ({0}), must be one of {1}"
                .format(preposition, allowed_values)
            )

        self._preposition = preposition

    @property
    def parameter(self):
        """
        Gets the parameter of this CouponRule.
        { \"description\" : \"The parameter for the coupon-rule. This specifies the ID or the quantity for the object of the subject.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The parameter of this CouponRule.
        :rtype: str
        """
        return self._parameter

    @parameter.setter
    def parameter(self, parameter):
        """
        Sets the parameter of this CouponRule.
        { \"description\" : \"The parameter for the coupon-rule. This specifies the ID or the quantity for the object of the subject.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param parameter: The parameter of this CouponRule.
        :type: str
        """

        self._parameter = parameter

    @property
    def object(self):
        """
        Gets the object of this CouponRule.
        { \"description\" : \"The property of the subject of the coupon-rule. e.g. When the subject is 'subscription' and the object is 'product-ID', the coupon-rule will observe the product-ID for that subscription.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The object of this CouponRule.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this CouponRule.
        { \"description\" : \"The property of the subject of the coupon-rule. e.g. When the subject is 'subscription' and the object is 'product-ID', the coupon-rule will observe the product-ID for that subscription.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param object: The object of this CouponRule.
        :type: str
        """
        allowed_values = ["subscription", "unit_of_measure", "satisfaction", "product_rate_plan_id", "product_id"]
        if object not in allowed_values:
            raise ValueError(
                "Invalid value for `object` ({0}), must be one of {1}"
                .format(object, allowed_values)
            )

        self._object = object

    @property
    def rule_validation_strategy(self):
        """
        Gets the rule_validation_strategy of this CouponRule.
        { \"description\" : \"The rule-validation-strategy object associated with the coupon-rule.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The rule_validation_strategy of this CouponRule.
        :rtype: str
        """
        return self._rule_validation_strategy

    @rule_validation_strategy.setter
    def rule_validation_strategy(self, rule_validation_strategy):
        """
        Sets the rule_validation_strategy of this CouponRule.
        { \"description\" : \"The rule-validation-strategy object associated with the coupon-rule.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param rule_validation_strategy: The rule_validation_strategy of this CouponRule.
        :type: str
        """
        allowed_values = ["only_at_initialisation", "while_recurring_or_initialisation", "only_while_recurring"]
        if rule_validation_strategy not in allowed_values:
            raise ValueError(
                "Invalid value for `rule_validation_strategy` ({0}), must be one of {1}"
                .format(rule_validation_strategy, allowed_values)
            )

        self._rule_validation_strategy = rule_validation_strategy

    @property
    def specifier(self):
        """
        Gets the specifier of this CouponRule.
        { \"description\" : \"When the subject is subscription, the specifier is used to define which unit of measure the coupon rule will operate on. When the subject is user, the specifier defines which property of the user's account it will operate on.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The specifier of this CouponRule.
        :rtype: str
        """
        return self._specifier

    @specifier.setter
    def specifier(self, specifier):
        """
        Sets the specifier of this CouponRule.
        { \"description\" : \"When the subject is subscription, the specifier is used to define which unit of measure the coupon rule will operate on. When the subject is user, the specifier defines which property of the user's account it will operate on.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param specifier: The specifier of this CouponRule.
        :type: str
        """

        self._specifier = specifier

    @property
    def deleted(self):
        """
        Gets the deleted of this CouponRule.
        { \"description\" : \"Has the coupon-modifier been deleted.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The deleted of this CouponRule.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """
        Sets the deleted of this CouponRule.
        { \"description\" : \"Has the coupon-modifier been deleted.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param deleted: The deleted of this CouponRule.
        :type: bool
        """

        self._deleted = deleted

    @property
    def child_rules(self):
        """
        Gets the child_rules of this CouponRule.
        { \"description\" : \"The collection of child coupon-rules associated with the coupon-rule.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The child_rules of this CouponRule.
        :rtype: list[CouponRule]
        """
        return self._child_rules

    @child_rules.setter
    def child_rules(self, child_rules):
        """
        Sets the child_rules of this CouponRule.
        { \"description\" : \"The collection of child coupon-rules associated with the coupon-rule.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param child_rules: The child_rules of this CouponRule.
        :type: list[CouponRule]
        """

        self._child_rules = child_rules

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
