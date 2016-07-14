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

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.models.usage_paged_metadata import UsagePagedMetadata


class TestUsagePagedMetadata(unittest.TestCase):
    """ UsagePagedMetadata unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUsagePagedMetadata(self):
        """
        Test UsagePagedMetadata
        """
        model = swagger_client.models.usage_paged_metadata.UsagePagedMetadata()


if __name__ == '__main__':
    unittest.main()
