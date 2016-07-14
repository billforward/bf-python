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
from swagger_client.apis.pricingcomponents_api import PricingcomponentsApi


class TestPricingcomponentsApi(unittest.TestCase):
    """ PricingcomponentsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.pricingcomponents_api.PricingcomponentsApi()

    def tearDown(self):
        pass

    def test_create_pricing_component(self):
        """
        Test case for create_pricing_component

        Create a pricing-component.
        """
        pass

    def test_get_all_pricing_components(self):
        """
        Test case for get_all_pricing_components

        Returns a collection of pricing-components. By default 10 values are returned. Records are returned in natural order.
        """
        pass

    def test_get_pricing_component(self):
        """
        Test case for get_pricing_component

        Returns a collection of pricing-components, specified by the pricing-component-ID parameter. By default 10 values are returned. Records are returned in natural order.
        """
        pass

    def test_get_pricing_component_by_product_rate_plan_id(self):
        """
        Test case for get_pricing_component_by_product_rate_plan_id

        Returns a collection of pricing-components, specified by the product-rate-plan-ID parameter. By default 10 values are returned. Records are returned in natural order.
        """
        pass

    def test_retire_pricing_component(self):
        """
        Test case for retire_pricing_component

        Retires the pricing-component specified by the pricing-component-ID parameter.
        """
        pass

    def test_update_pricing_component(self):
        """
        Test case for update_pricing_component

        Update a pricing-component.
        """
        pass


if __name__ == '__main__':
    unittest.main()
