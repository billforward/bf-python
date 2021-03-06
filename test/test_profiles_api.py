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

from __future__ import absolute_import

import os
import sys
import unittest

import billforward
from billforward.rest import ApiException
from billforward.apis.profiles_api import ProfilesApi


class TestProfilesApi(unittest.TestCase):
    """ ProfilesApi unit test stubs """

    def setUp(self):
        self.api = billforward.apis.profiles_api.ProfilesApi()

    def tearDown(self):
        pass

    def test_get_all_profiles(self):
        """
        Test case for get_all_profiles

        Returns a collection of all profiles. By default 10 values are returned. Records are returned in natural order
        """
        pass

    def test_get_profile(self):
        """
        Test case for get_profile

        Returns a single profile, specified by the ID parameter.
        """
        pass

    def test_get_profile_by_account_id(self):
        """
        Test case for get_profile_by_account_id

        Returns a collection of profiles, specified by the account-ID parameter. By default 10 values are returned. Records are returned in natural order
        """
        pass

    def test_get_profile_by_email_address(self):
        """
        Test case for get_profile_by_email_address

        Returns a single profile, specified by the email parameter.
        """
        pass

    def test_update_profile(self):
        """
        Test case for update_profile

        Update a profile
        """
        pass


if __name__ == '__main__':
    unittest.main()
