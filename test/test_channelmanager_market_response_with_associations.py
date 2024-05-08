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

from channelmanager.models.channelmanager_market_response_with_associations import ChannelmanagerMarketResponseWithAssociations

class TestChannelmanagerMarketResponseWithAssociations(unittest.TestCase):
    """ChannelmanagerMarketResponseWithAssociations unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChannelmanagerMarketResponseWithAssociations:
        """Test ChannelmanagerMarketResponseWithAssociations
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChannelmanagerMarketResponseWithAssociations`
        """
        model = ChannelmanagerMarketResponseWithAssociations()
        if include_optional:
            return ChannelmanagerMarketResponseWithAssociations(
                id = '',
                grn = '',
                name = '',
                description = '',
                countries = [
                    'COUNTRY_CODE_UNKNOWN'
                    ],
                associations = [
                    channelmanager.models.channelmanager_market_response_with_associations_association.channelmanagerMarketResponseWithAssociationsAssociation(
                        channel = channelmanager.models.channelmanager_channel_response.channelmanagerChannelResponse(
                            id = '', 
                            grn = '', 
                            code = '', 
                            image = '', 
                            name = '', 
                            default_language = 'LANGUAGE_CODE_UNKNOWN', 
                            settings = channelmanager.models.channelmanager_channel_settings.channelmanagerChannelSettings(
                                hide_oos_products = True, 
                                hide_priceless_products = True, ), 
                            website = channelmanager.models.channelmanager_channel_type_website.channelmanagerChannelTypeWebsite(
                                domain = '', ), 
                            status = 'CH_STATUS_UNKNOWN', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), )
                    ],
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return ChannelmanagerMarketResponseWithAssociations(
        )
        """

    def testChannelmanagerMarketResponseWithAssociations(self):
        """Test ChannelmanagerMarketResponseWithAssociations"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
