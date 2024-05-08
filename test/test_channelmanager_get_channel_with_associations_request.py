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

from channelmanager.models.channelmanager_get_channel_with_associations_request import ChannelmanagerGetChannelWithAssociationsRequest

class TestChannelmanagerGetChannelWithAssociationsRequest(unittest.TestCase):
    """ChannelmanagerGetChannelWithAssociationsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChannelmanagerGetChannelWithAssociationsRequest:
        """Test ChannelmanagerGetChannelWithAssociationsRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChannelmanagerGetChannelWithAssociationsRequest`
        """
        model = ChannelmanagerGetChannelWithAssociationsRequest()
        if include_optional:
            return ChannelmanagerGetChannelWithAssociationsRequest(
                tenant_id = '',
                id = ''
            )
        else:
            return ChannelmanagerGetChannelWithAssociationsRequest(
                tenant_id = '',
                id = '',
        )
        """

    def testChannelmanagerGetChannelWithAssociationsRequest(self):
        """Test ChannelmanagerGetChannelWithAssociationsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
