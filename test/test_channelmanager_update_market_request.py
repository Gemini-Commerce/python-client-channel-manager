# coding: utf-8

"""
    Channel Manager Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from channelmanager.models.channelmanager_update_market_request import ChannelmanagerUpdateMarketRequest

class TestChannelmanagerUpdateMarketRequest(unittest.TestCase):
    """ChannelmanagerUpdateMarketRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChannelmanagerUpdateMarketRequest:
        """Test ChannelmanagerUpdateMarketRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChannelmanagerUpdateMarketRequest`
        """
        model = ChannelmanagerUpdateMarketRequest()
        if include_optional:
            return ChannelmanagerUpdateMarketRequest(
                tenant_id = '',
                id = '',
                payload = channelmanager.models.channelmanager_update_market_request_payload.channelmanagerUpdateMarketRequestPayload(
                    name = '', 
                    description = '', 
                    countries = [
                        'COUNTRY_CODE_UNKNOWN'
                        ], ),
                payload_mask = ''
            )
        else:
            return ChannelmanagerUpdateMarketRequest(
                tenant_id = '',
                id = '',
        )
        """

    def testChannelmanagerUpdateMarketRequest(self):
        """Test ChannelmanagerUpdateMarketRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
