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

class DataSyncJobResponse(object):
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
        'created': 'datetime',
        'organization_id': 'str',
        'id': 'str',
        'config_id': 'str',
        'state': 'str',
        'type': 'str',
        'scope': 'str',
        'target': 'str',
        'name': 'str',
        'description': 'str',
        'data_from': 'datetime',
        'data_till': 'datetime',
        'started': 'datetime',
        'stopped': 'datetime',
        'created_by': 'str',
        'max_retry_times': 'int',
        'retry_attempted': 'int',
        'deleted': 'bool',
        'latest_run_number': 'int',
        'errors': 'list[DataSyncJobErrorResponse]'
    }

    attribute_map = {
        'created': 'created',
        'organization_id': 'organizationID',
        'id': 'id',
        'config_id': 'configID',
        'state': 'state',
        'type': 'type',
        'scope': 'scope',
        'target': 'target',
        'name': 'name',
        'description': 'description',
        'data_from': 'dataFrom',
        'data_till': 'dataTill',
        'started': 'started',
        'stopped': 'stopped',
        'created_by': 'createdBy',
        'max_retry_times': 'maxRetryTimes',
        'retry_attempted': 'retryAttempted',
        'deleted': 'deleted',
        'latest_run_number': 'latestRunNumber',
        'errors': 'errors'
    }

    def __init__(self, created=None, organization_id=None, id=None, config_id=None, state=None, type=None, scope=None, target=None, name=None, description=None, data_from=None, data_till=None, started=None, stopped=None, created_by=None, max_retry_times=None, retry_attempted=None, deleted=None, latest_run_number=None, errors=None):  # noqa: E501
        """DataSyncJobResponse - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._organization_id = None
        self._id = None
        self._config_id = None
        self._state = None
        self._type = None
        self._scope = None
        self._target = None
        self._name = None
        self._description = None
        self._data_from = None
        self._data_till = None
        self._started = None
        self._stopped = None
        self._created_by = None
        self._max_retry_times = None
        self._retry_attempted = None
        self._deleted = None
        self._latest_run_number = None
        self._errors = None
        self.discriminator = None
        if created is not None:
            self.created = created
        if organization_id is not None:
            self.organization_id = organization_id
        if id is not None:
            self.id = id
        if config_id is not None:
            self.config_id = config_id
        if state is not None:
            self.state = state
        if type is not None:
            self.type = type
        if scope is not None:
            self.scope = scope
        if target is not None:
            self.target = target
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if data_from is not None:
            self.data_from = data_from
        if data_till is not None:
            self.data_till = data_till
        if started is not None:
            self.started = started
        if stopped is not None:
            self.stopped = stopped
        if created_by is not None:
            self.created_by = created_by
        if max_retry_times is not None:
            self.max_retry_times = max_retry_times
        if retry_attempted is not None:
            self.retry_attempted = retry_attempted
        if deleted is not None:
            self.deleted = deleted
        if latest_run_number is not None:
            self.latest_run_number = latest_run_number
        if errors is not None:
            self.errors = errors

    @property
    def created(self):
        """Gets the created of this DataSyncJobResponse.  # noqa: E501


        :return: The created of this DataSyncJobResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this DataSyncJobResponse.


        :param created: The created of this DataSyncJobResponse.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def organization_id(self):
        """Gets the organization_id of this DataSyncJobResponse.  # noqa: E501


        :return: The organization_id of this DataSyncJobResponse.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this DataSyncJobResponse.


        :param organization_id: The organization_id of this DataSyncJobResponse.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def id(self):
        """Gets the id of this DataSyncJobResponse.  # noqa: E501


        :return: The id of this DataSyncJobResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataSyncJobResponse.


        :param id: The id of this DataSyncJobResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def config_id(self):
        """Gets the config_id of this DataSyncJobResponse.  # noqa: E501


        :return: The config_id of this DataSyncJobResponse.  # noqa: E501
        :rtype: str
        """
        return self._config_id

    @config_id.setter
    def config_id(self, config_id):
        """Sets the config_id of this DataSyncJobResponse.


        :param config_id: The config_id of this DataSyncJobResponse.  # noqa: E501
        :type: str
        """

        self._config_id = config_id

    @property
    def state(self):
        """Gets the state of this DataSyncJobResponse.  # noqa: E501


        :return: The state of this DataSyncJobResponse.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DataSyncJobResponse.


        :param state: The state of this DataSyncJobResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["Pending", "Complete", "Failed", "Cancelled", "Processing"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def type(self):
        """Gets the type of this DataSyncJobResponse.  # noqa: E501


        :return: The type of this DataSyncJobResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DataSyncJobResponse.


        :param type: The type of this DataSyncJobResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["Incremental", "Full"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def scope(self):
        """Gets the scope of this DataSyncJobResponse.  # noqa: E501


        :return: The scope of this DataSyncJobResponse.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this DataSyncJobResponse.


        :param scope: The scope of this DataSyncJobResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["Manual", "Scheduled"]  # noqa: E501
        if scope not in allowed_values:
            raise ValueError(
                "Invalid value for `scope` ({0}), must be one of {1}"  # noqa: E501
                .format(scope, allowed_values)
            )

        self._scope = scope

    @property
    def target(self):
        """Gets the target of this DataSyncJobResponse.  # noqa: E501


        :return: The target of this DataSyncJobResponse.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this DataSyncJobResponse.


        :param target: The target of this DataSyncJobResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["Salesforce", "Quickbooks"]  # noqa: E501
        if target not in allowed_values:
            raise ValueError(
                "Invalid value for `target` ({0}), must be one of {1}"  # noqa: E501
                .format(target, allowed_values)
            )

        self._target = target

    @property
    def name(self):
        """Gets the name of this DataSyncJobResponse.  # noqa: E501


        :return: The name of this DataSyncJobResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DataSyncJobResponse.


        :param name: The name of this DataSyncJobResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this DataSyncJobResponse.  # noqa: E501


        :return: The description of this DataSyncJobResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DataSyncJobResponse.


        :param description: The description of this DataSyncJobResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def data_from(self):
        """Gets the data_from of this DataSyncJobResponse.  # noqa: E501


        :return: The data_from of this DataSyncJobResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._data_from

    @data_from.setter
    def data_from(self, data_from):
        """Sets the data_from of this DataSyncJobResponse.


        :param data_from: The data_from of this DataSyncJobResponse.  # noqa: E501
        :type: datetime
        """

        self._data_from = data_from

    @property
    def data_till(self):
        """Gets the data_till of this DataSyncJobResponse.  # noqa: E501


        :return: The data_till of this DataSyncJobResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._data_till

    @data_till.setter
    def data_till(self, data_till):
        """Sets the data_till of this DataSyncJobResponse.


        :param data_till: The data_till of this DataSyncJobResponse.  # noqa: E501
        :type: datetime
        """

        self._data_till = data_till

    @property
    def started(self):
        """Gets the started of this DataSyncJobResponse.  # noqa: E501


        :return: The started of this DataSyncJobResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._started

    @started.setter
    def started(self, started):
        """Sets the started of this DataSyncJobResponse.


        :param started: The started of this DataSyncJobResponse.  # noqa: E501
        :type: datetime
        """

        self._started = started

    @property
    def stopped(self):
        """Gets the stopped of this DataSyncJobResponse.  # noqa: E501


        :return: The stopped of this DataSyncJobResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._stopped

    @stopped.setter
    def stopped(self, stopped):
        """Sets the stopped of this DataSyncJobResponse.


        :param stopped: The stopped of this DataSyncJobResponse.  # noqa: E501
        :type: datetime
        """

        self._stopped = stopped

    @property
    def created_by(self):
        """Gets the created_by of this DataSyncJobResponse.  # noqa: E501


        :return: The created_by of this DataSyncJobResponse.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this DataSyncJobResponse.


        :param created_by: The created_by of this DataSyncJobResponse.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def max_retry_times(self):
        """Gets the max_retry_times of this DataSyncJobResponse.  # noqa: E501


        :return: The max_retry_times of this DataSyncJobResponse.  # noqa: E501
        :rtype: int
        """
        return self._max_retry_times

    @max_retry_times.setter
    def max_retry_times(self, max_retry_times):
        """Sets the max_retry_times of this DataSyncJobResponse.


        :param max_retry_times: The max_retry_times of this DataSyncJobResponse.  # noqa: E501
        :type: int
        """

        self._max_retry_times = max_retry_times

    @property
    def retry_attempted(self):
        """Gets the retry_attempted of this DataSyncJobResponse.  # noqa: E501


        :return: The retry_attempted of this DataSyncJobResponse.  # noqa: E501
        :rtype: int
        """
        return self._retry_attempted

    @retry_attempted.setter
    def retry_attempted(self, retry_attempted):
        """Sets the retry_attempted of this DataSyncJobResponse.


        :param retry_attempted: The retry_attempted of this DataSyncJobResponse.  # noqa: E501
        :type: int
        """

        self._retry_attempted = retry_attempted

    @property
    def deleted(self):
        """Gets the deleted of this DataSyncJobResponse.  # noqa: E501


        :return: The deleted of this DataSyncJobResponse.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this DataSyncJobResponse.


        :param deleted: The deleted of this DataSyncJobResponse.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def latest_run_number(self):
        """Gets the latest_run_number of this DataSyncJobResponse.  # noqa: E501


        :return: The latest_run_number of this DataSyncJobResponse.  # noqa: E501
        :rtype: int
        """
        return self._latest_run_number

    @latest_run_number.setter
    def latest_run_number(self, latest_run_number):
        """Sets the latest_run_number of this DataSyncJobResponse.


        :param latest_run_number: The latest_run_number of this DataSyncJobResponse.  # noqa: E501
        :type: int
        """

        self._latest_run_number = latest_run_number

    @property
    def errors(self):
        """Gets the errors of this DataSyncJobResponse.  # noqa: E501


        :return: The errors of this DataSyncJobResponse.  # noqa: E501
        :rtype: list[DataSyncJobErrorResponse]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this DataSyncJobResponse.


        :param errors: The errors of this DataSyncJobResponse.  # noqa: E501
        :type: list[DataSyncJobErrorResponse]
        """

        self._errors = errors

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
        if issubclass(DataSyncJobResponse, dict):
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
        if not isinstance(other, DataSyncJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
