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

from channelmanager.models.channelmanager_create_association_request import ChannelmanagerCreateAssociationRequest

class TestChannelmanagerCreateAssociationRequest(unittest.TestCase):
    """ChannelmanagerCreateAssociationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChannelmanagerCreateAssociationRequest:
        """Test ChannelmanagerCreateAssociationRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChannelmanagerCreateAssociationRequest`
        """
        model = ChannelmanagerCreateAssociationRequest()
        if include_optional:
            return ChannelmanagerCreateAssociationRequest(
                tenant_id = '',
                channel_grn = '',
                market_grn = ''
            )
        else:
            return ChannelmanagerCreateAssociationRequest(
        )
        """

    def testChannelmanagerCreateAssociationRequest(self):
        """Test ChannelmanagerCreateAssociationRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()