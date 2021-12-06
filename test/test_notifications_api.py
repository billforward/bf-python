# coding: utf-8

"""
    Billforward API

    This is documentation for the Billforward API. You can find out more at billforward.io.  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: team@billforward.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import billforward
from billforward.api.notifications_api import NotificationsApi  # noqa: E501
from billforward.rest import ApiException


class TestNotificationsApi(unittest.TestCase):
    """NotificationsApi unit test stubs"""

    def setUp(self):
        self.api = NotificationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_all_notifications(self):
        """Test case for get_all_notifications

        """
        pass

    def test_get_notification_by_entity_id(self):
        """Test case for get_notification_by_entity_id

        """
        pass

    def test_get_notification_by_id(self):
        """Test case for get_notification_by_id

        """
        pass

    def test_get_notifications_by_webhook_id(self):
        """Test case for get_notifications_by_webhook_id

        """
        pass

    def test_get_notifications_within_date_range(self):
        """Test case for get_notifications_within_date_range

        """
        pass

    def test_resend_notification(self):
        """Test case for resend_notification

        """
        pass


if __name__ == '__main__':
    unittest.main()
