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
from swagger_client.apis.auditlogs_api import AuditlogsApi


class TestAuditlogsApi(unittest.TestCase):
    """ AuditlogsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.auditlogs_api.AuditlogsApi()

    def tearDown(self):
        pass

    def test_get_all_audit_entries(self):
        """
        Test case for get_all_audit_entries

        Returns a collection of all audit-log objects. By default 10 values are returned. Records are returned in natural order.
        """
        pass

    def test_get_audit_entries_by_created_date(self):
        """
        Test case for get_audit_entries_by_created_date

        Returns a collection of audit-log objects with created times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.
        """
        pass

    def test_get_audit_entry_by_entity_id(self):
        """
        Test case for get_audit_entry_by_entity_id

        Returns a collection of audit-log entries, specified by the entity-ID parameter. By default 10 values are returned. Records are returned in natural order.
        """
        pass

    def test_get_audit_entry_by_entity_type(self):
        """
        Test case for get_audit_entry_by_entity_type

        Returns a collection of audit-log entries, specified by the entity-type parameter. By default 10 values are returned. Records are returned in natural order.
        """
        pass

    def test_get_audit_entry_by_id(self):
        """
        Test case for get_audit_entry_by_id

        Returns a single audit-log entry, specified by the audit-ID parameter.
        """
        pass


if __name__ == '__main__':
    unittest.main()
