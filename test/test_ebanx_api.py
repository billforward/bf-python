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
from billforward.api.ebanx_api import EBANXApi  # noqa: E501
from billforward.rest import ApiException


class TestEBANXApi(unittest.TestCase):
    """EBANXApi unit test stubs"""

    def setUp(self):
        self.api = EBANXApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_configuration1(self):
        """Test case for delete_configuration1

        """
        pass

    def test_get_configuration1(self):
        """Test case for get_configuration1

        """
        pass

    def test_handle_webhook(self):
        """Test case for handle_webhook

        """
        pass

    def test_upsert_configuration1(self):
        """Test case for upsert_configuration1

        """
        pass


if __name__ == '__main__':
    unittest.main()
