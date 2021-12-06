# coding: utf-8

"""
    Billforward API

    This is documentation for the Billforward API. You can find out more at billforward.io.  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: team@billforward.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponseDefault92(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'execution_time': 'int',
        'results': 'list[UpdatePasswordResponse]'
    }

    attribute_map = {
        'execution_time': 'executionTime',
        'results': 'results'
    }

    def __init__(self, execution_time=None, results=None):  # noqa: E501
        """InlineResponseDefault92 - a model defined in Swagger"""  # noqa: E501
        self._execution_time = None
        self._results = None
        self.discriminator = None
        self.execution_time = execution_time
        self.results = results

    @property
    def execution_time(self):
        """Gets the execution_time of this InlineResponseDefault92.  # noqa: E501


        :return: The execution_time of this InlineResponseDefault92.  # noqa: E501
        :rtype: int
        """
        return self._execution_time

    @execution_time.setter
    def execution_time(self, execution_time):
        """Sets the execution_time of this InlineResponseDefault92.


        :param execution_time: The execution_time of this InlineResponseDefault92.  # noqa: E501
        :type: int
        """
        if execution_time is None:
            raise ValueError("Invalid value for `execution_time`, must not be `None`")  # noqa: E501

        self._execution_time = execution_time

    @property
    def results(self):
        """Gets the results of this InlineResponseDefault92.  # noqa: E501


        :return: The results of this InlineResponseDefault92.  # noqa: E501
        :rtype: list[UpdatePasswordResponse]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this InlineResponseDefault92.


        :param results: The results of this InlineResponseDefault92.  # noqa: E501
        :type: list[UpdatePasswordResponse]
        """
        if results is None:
            raise ValueError("Invalid value for `results`, must not be `None`")  # noqa: E501

        self._results = results

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(InlineResponseDefault92, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponseDefault92):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
