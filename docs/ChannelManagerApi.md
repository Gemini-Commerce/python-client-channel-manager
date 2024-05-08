# channelmanager.ChannelManagerApi

All URIs are relative to *https://channel.api.gogemini.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**channel_manager_create_association**](ChannelManagerApi.md#channel_manager_create_association) | **POST** /channelmanager.ChannelManager/CreateAssociation | CreateAssociation
[**channel_manager_create_channel**](ChannelManagerApi.md#channel_manager_create_channel) | **POST** /channelmanager.ChannelManager/CreateChannel | CreateChannel
[**channel_manager_create_market**](ChannelManagerApi.md#channel_manager_create_market) | **POST** /channelmanager.ChannelManager/CreateMarket | CreateMarket
[**channel_manager_delete_association**](ChannelManagerApi.md#channel_manager_delete_association) | **POST** /channelmanager.ChannelManager/DeleteAssociation | DeleteAssociation
[**channel_manager_delete_channel**](ChannelManagerApi.md#channel_manager_delete_channel) | **POST** /channelmanager.ChannelManager/DeleteChannel | DeleteChannel
[**channel_manager_delete_market**](ChannelManagerApi.md#channel_manager_delete_market) | **POST** /channelmanager.ChannelManager/DeleteMarket | DeleteMarket
[**channel_manager_get_channel**](ChannelManagerApi.md#channel_manager_get_channel) | **POST** /channelmanager.ChannelManager/GetChannel | GetChannel
[**channel_manager_get_channel_with_associations**](ChannelManagerApi.md#channel_manager_get_channel_with_associations) | **POST** /channelmanager.ChannelManager/GetChannelWithAssociations | GetChannelWithAssociations
[**channel_manager_get_market**](ChannelManagerApi.md#channel_manager_get_market) | **POST** /channelmanager.ChannelManager/GetMarket | GetMarket
[**channel_manager_get_market_with_associations**](ChannelManagerApi.md#channel_manager_get_market_with_associations) | **POST** /channelmanager.ChannelManager/GetMarketWithAssociations | GetMarketWithAssociations
[**channel_manager_list_channels**](ChannelManagerApi.md#channel_manager_list_channels) | **POST** /channelmanager.ChannelManager/ListChannels | ListChannels
[**channel_manager_list_channels_with_associations**](ChannelManagerApi.md#channel_manager_list_channels_with_associations) | **POST** /channelmanager.ChannelManager/ListChannelsWithAssociations | ListChannelsWithAssociations
[**channel_manager_list_markets**](ChannelManagerApi.md#channel_manager_list_markets) | **POST** /channelmanager.ChannelManager/ListMarkets | ListMarkets
[**channel_manager_list_markets_with_associations**](ChannelManagerApi.md#channel_manager_list_markets_with_associations) | **POST** /channelmanager.ChannelManager/ListMarketsWithAssociations | ListMarketsWithAssociations
[**channel_manager_update_channel**](ChannelManagerApi.md#channel_manager_update_channel) | **POST** /channelmanager.ChannelManager/UpdateChannel | UpdateChannel
[**channel_manager_update_market**](ChannelManagerApi.md#channel_manager_update_market) | **POST** /channelmanager.ChannelManager/UpdateMarket | UpdateMarket


# **channel_manager_create_association**
> ChannelmanagerAssociationResponse channel_manager_create_association(body)

CreateAssociation

Create a new association between a channel and a market or entities

### Example


```python
import time
import os
import channelmanager
from channelmanager.models.channelmanager_association_response import ChannelmanagerAssociationResponse
from channelmanager.models.channelmanager_create_association_request import ChannelmanagerCreateAssociationRequest
from channelmanager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://channel.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = channelmanager.Configuration(
    host = "https://channel.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with channelmanager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channelmanager.ChannelManagerApi(api_client)
    body = channelmanager.ChannelmanagerCreateAssociationRequest() # ChannelmanagerCreateAssociationRequest | 

    try:
        # CreateAssociation
        api_response = api_instance.channel_manager_create_association(body)
        print("The response of ChannelManagerApi->channel_manager_create_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelManagerApi->channel_manager_create_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChannelmanagerCreateAssociationRequest**](ChannelmanagerCreateAssociationRequest.md)|  | 

### Return type

[**ChannelmanagerAssociationResponse**](ChannelmanagerAssociationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channel_manager_create_channel**
> ChannelmanagerChannelResponse channel_manager_create_channel(body)

CreateChannel

Create a new channel

### Example


```python
import time
import os
import channelmanager
from channelmanager.models.channelmanager_channel_response import ChannelmanagerChannelResponse
from channelmanager.models.channelmanager_create_channel_request import ChannelmanagerCreateChannelRequest
from channelmanager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://channel.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = channelmanager.Configuration(
    host = "https://channel.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with channelmanager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channelmanager.ChannelManagerApi(api_client)
    body = channelmanager.ChannelmanagerCreateChannelRequest() # ChannelmanagerCreateChannelRequest | 

    try:
        # CreateChannel
        api_response = api_instance.channel_manager_create_channel(body)
        print("The response of ChannelManagerApi->channel_manager_create_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelManagerApi->channel_manager_create_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChannelmanagerCreateChannelRequest**](ChannelmanagerCreateChannelRequest.md)|  | 

### Return type

[**ChannelmanagerChannelResponse**](ChannelmanagerChannelResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channel_manager_create_market**
> ChannelmanagerMarketResponse channel_manager_create_market(body)

CreateMarket

Create a new market

### Example


```python
import time
import os
import channelmanager
from channelmanager.models.channelmanager_create_market_request import ChannelmanagerCreateMarketRequest
from channelmanager.models.channelmanager_market_response import ChannelmanagerMarketResponse
from channelmanager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://channel.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = channelmanager.Configuration(
    host = "https://channel.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with channelmanager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channelmanager.ChannelManagerApi(api_client)
    body = channelmanager.ChannelmanagerCreateMarketRequest() # ChannelmanagerCreateMarketRequest | 

    try:
        # CreateMarket
        api_response = api_instance.channel_manager_create_market(body)
        print("The response of ChannelManagerApi->channel_manager_create_market:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelManagerApi->channel_manager_create_market: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChannelmanagerCreateMarketRequest**](ChannelmanagerCreateMarketRequest.md)|  | 

### Return type

[**ChannelmanagerMarketResponse**](ChannelmanagerMarketResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channel_manager_delete_association**
> object channel_manager_delete_association(body)

DeleteAssociation

Delete an existing association between a channel and a market or entities

### Example


```python
import time
import os
import channelmanager
from channelmanager.models.channelmanager_delete_association_request import ChannelmanagerDeleteAssociationRequest
from channelmanager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://channel.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = channelmanager.Configuration(
    host = "https://channel.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with channelmanager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channelmanager.ChannelManagerApi(api_client)
    body = channelmanager.ChannelmanagerDeleteAssociationRequest() # ChannelmanagerDeleteAssociationRequest | 

    try:
        # DeleteAssociation
        api_response = api_instance.channel_manager_delete_association(body)
        print("The response of ChannelManagerApi->channel_manager_delete_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelManagerApi->channel_manager_delete_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChannelmanagerDeleteAssociationRequest**](ChannelmanagerDeleteAssociationRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channel_manager_delete_channel**
> object channel_manager_delete_channel(body)

DeleteChannel

Soft delete an existing channel

### Example


```python
import time
import os
import channelmanager
from channelmanager.models.channelmanager_delete_channel_request import ChannelmanagerDeleteChannelRequest
from channelmanager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://channel.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = channelmanager.Configuration(
    host = "https://channel.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with channelmanager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channelmanager.ChannelManagerApi(api_client)
    body = channelmanager.ChannelmanagerDeleteChannelRequest() # ChannelmanagerDeleteChannelRequest | 

    try:
        # DeleteChannel
        api_response = api_instance.channel_manager_delete_channel(body)
        print("The response of ChannelManagerApi->channel_manager_delete_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelManagerApi->channel_manager_delete_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChannelmanagerDeleteChannelRequest**](ChannelmanagerDeleteChannelRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channel_manager_delete_market**
> object channel_manager_delete_market(body)

DeleteMarket

Soft delete an existing market

### Example


```python
import time
import os
import channelmanager
from channelmanager.models.channelmanager_delete_market_request import ChannelmanagerDeleteMarketRequest
from channelmanager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://channel.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = channelmanager.Configuration(
    host = "https://channel.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with channelmanager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channelmanager.ChannelManagerApi(api_client)
    body = channelmanager.ChannelmanagerDeleteMarketRequest() # ChannelmanagerDeleteMarketRequest | 

    try:
        # DeleteMarket
        api_response = api_instance.channel_manager_delete_market(body)
        print("The response of ChannelManagerApi->channel_manager_delete_market:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelManagerApi->channel_manager_delete_market: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChannelmanagerDeleteMarketRequest**](ChannelmanagerDeleteMarketRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channel_manager_get_channel**
> ChannelmanagerChannelResponse channel_manager_get_channel(body)

GetChannel

Get an existing channel

### Example


```python
import time
import os
import channelmanager
from channelmanager.models.channelmanager_channel_response import ChannelmanagerChannelResponse
from channelmanager.models.channelmanager_get_channel_request import ChannelmanagerGetChannelRequest
from channelmanager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://channel.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = channelmanager.Configuration(
    host = "https://channel.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with channelmanager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channelmanager.ChannelManagerApi(api_client)
    body = channelmanager.ChannelmanagerGetChannelRequest() # ChannelmanagerGetChannelRequest | 

    try:
        # GetChannel
        api_response = api_instance.channel_manager_get_channel(body)
        print("The response of ChannelManagerApi->channel_manager_get_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelManagerApi->channel_manager_get_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChannelmanagerGetChannelRequest**](ChannelmanagerGetChannelRequest.md)|  | 

### Return type

[**ChannelmanagerChannelResponse**](ChannelmanagerChannelResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channel_manager_get_channel_with_associations**
> ChannelmanagerChannelResponseWithAssociations channel_manager_get_channel_with_associations(body)

GetChannelWithAssociations

Get an existing channel with associations

### Example


```python
import time
import os
import channelmanager
from channelmanager.models.channelmanager_channel_response_with_associations import ChannelmanagerChannelResponseWithAssociations
from channelmanager.models.channelmanager_get_channel_with_associations_request import ChannelmanagerGetChannelWithAssociationsRequest
from channelmanager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://channel.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = channelmanager.Configuration(
    host = "https://channel.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with channelmanager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channelmanager.ChannelManagerApi(api_client)
    body = channelmanager.ChannelmanagerGetChannelWithAssociationsRequest() # ChannelmanagerGetChannelWithAssociationsRequest | 

    try:
        # GetChannelWithAssociations
        api_response = api_instance.channel_manager_get_channel_with_associations(body)
        print("The response of ChannelManagerApi->channel_manager_get_channel_with_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelManagerApi->channel_manager_get_channel_with_associations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChannelmanagerGetChannelWithAssociationsRequest**](ChannelmanagerGetChannelWithAssociationsRequest.md)|  | 

### Return type

[**ChannelmanagerChannelResponseWithAssociations**](ChannelmanagerChannelResponseWithAssociations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channel_manager_get_market**
> ChannelmanagerMarketResponse channel_manager_get_market(body)

GetMarket

Get an existing market

### Example


```python
import time
import os
import channelmanager
from channelmanager.models.channelmanager_get_market_request import ChannelmanagerGetMarketRequest
from channelmanager.models.channelmanager_market_response import ChannelmanagerMarketResponse
from channelmanager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://channel.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = channelmanager.Configuration(
    host = "https://channel.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with channelmanager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channelmanager.ChannelManagerApi(api_client)
    body = channelmanager.ChannelmanagerGetMarketRequest() # ChannelmanagerGetMarketRequest | 

    try:
        # GetMarket
        api_response = api_instance.channel_manager_get_market(body)
        print("The response of ChannelManagerApi->channel_manager_get_market:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelManagerApi->channel_manager_get_market: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChannelmanagerGetMarketRequest**](ChannelmanagerGetMarketRequest.md)|  | 

### Return type

[**ChannelmanagerMarketResponse**](ChannelmanagerMarketResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channel_manager_get_market_with_associations**
> ChannelmanagerMarketResponseWithAssociations channel_manager_get_market_with_associations(body)

GetMarketWithAssociations

Get an existing market with associations

### Example


```python
import time
import os
import channelmanager
from channelmanager.models.channelmanager_get_market_with_associations_request import ChannelmanagerGetMarketWithAssociationsRequest
from channelmanager.models.channelmanager_market_response_with_associations import ChannelmanagerMarketResponseWithAssociations
from channelmanager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://channel.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = channelmanager.Configuration(
    host = "https://channel.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with channelmanager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channelmanager.ChannelManagerApi(api_client)
    body = channelmanager.ChannelmanagerGetMarketWithAssociationsRequest() # ChannelmanagerGetMarketWithAssociationsRequest | 

    try:
        # GetMarketWithAssociations
        api_response = api_instance.channel_manager_get_market_with_associations(body)
        print("The response of ChannelManagerApi->channel_manager_get_market_with_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelManagerApi->channel_manager_get_market_with_associations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChannelmanagerGetMarketWithAssociationsRequest**](ChannelmanagerGetMarketWithAssociationsRequest.md)|  | 

### Return type

[**ChannelmanagerMarketResponseWithAssociations**](ChannelmanagerMarketResponseWithAssociations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channel_manager_list_channels**
> ChannelmanagerListChannelsResponse channel_manager_list_channels(body)

ListChannels

List all channels

### Example


```python
import time
import os
import channelmanager
from channelmanager.models.channelmanager_list_channels_request import ChannelmanagerListChannelsRequest
from channelmanager.models.channelmanager_list_channels_response import ChannelmanagerListChannelsResponse
from channelmanager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://channel.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = channelmanager.Configuration(
    host = "https://channel.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with channelmanager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channelmanager.ChannelManagerApi(api_client)
    body = channelmanager.ChannelmanagerListChannelsRequest() # ChannelmanagerListChannelsRequest | 

    try:
        # ListChannels
        api_response = api_instance.channel_manager_list_channels(body)
        print("The response of ChannelManagerApi->channel_manager_list_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelManagerApi->channel_manager_list_channels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChannelmanagerListChannelsRequest**](ChannelmanagerListChannelsRequest.md)|  | 

### Return type

[**ChannelmanagerListChannelsResponse**](ChannelmanagerListChannelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channel_manager_list_channels_with_associations**
> ChannelmanagerListChannelsWithAssociationsResponse channel_manager_list_channels_with_associations(body)

ListChannelsWithAssociations

List all channels with associations

### Example


```python
import time
import os
import channelmanager
from channelmanager.models.channelmanager_list_channels_with_associations_request import ChannelmanagerListChannelsWithAssociationsRequest
from channelmanager.models.channelmanager_list_channels_with_associations_response import ChannelmanagerListChannelsWithAssociationsResponse
from channelmanager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://channel.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = channelmanager.Configuration(
    host = "https://channel.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with channelmanager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channelmanager.ChannelManagerApi(api_client)
    body = channelmanager.ChannelmanagerListChannelsWithAssociationsRequest() # ChannelmanagerListChannelsWithAssociationsRequest | 

    try:
        # ListChannelsWithAssociations
        api_response = api_instance.channel_manager_list_channels_with_associations(body)
        print("The response of ChannelManagerApi->channel_manager_list_channels_with_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelManagerApi->channel_manager_list_channels_with_associations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChannelmanagerListChannelsWithAssociationsRequest**](ChannelmanagerListChannelsWithAssociationsRequest.md)|  | 

### Return type

[**ChannelmanagerListChannelsWithAssociationsResponse**](ChannelmanagerListChannelsWithAssociationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channel_manager_list_markets**
> ChannelmanagerListMarketsResponse channel_manager_list_markets(body)

ListMarkets

List all markets

### Example


```python
import time
import os
import channelmanager
from channelmanager.models.channelmanager_list_markets_request import ChannelmanagerListMarketsRequest
from channelmanager.models.channelmanager_list_markets_response import ChannelmanagerListMarketsResponse
from channelmanager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://channel.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = channelmanager.Configuration(
    host = "https://channel.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with channelmanager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channelmanager.ChannelManagerApi(api_client)
    body = channelmanager.ChannelmanagerListMarketsRequest() # ChannelmanagerListMarketsRequest | 

    try:
        # ListMarkets
        api_response = api_instance.channel_manager_list_markets(body)
        print("The response of ChannelManagerApi->channel_manager_list_markets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelManagerApi->channel_manager_list_markets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChannelmanagerListMarketsRequest**](ChannelmanagerListMarketsRequest.md)|  | 

### Return type

[**ChannelmanagerListMarketsResponse**](ChannelmanagerListMarketsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channel_manager_list_markets_with_associations**
> ChannelmanagerListMarketsWithAssociationsResponse channel_manager_list_markets_with_associations(body)

ListMarketsWithAssociations

List all markets with associations

### Example


```python
import time
import os
import channelmanager
from channelmanager.models.channelmanager_list_markets_with_associations_request import ChannelmanagerListMarketsWithAssociationsRequest
from channelmanager.models.channelmanager_list_markets_with_associations_response import ChannelmanagerListMarketsWithAssociationsResponse
from channelmanager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://channel.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = channelmanager.Configuration(
    host = "https://channel.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with channelmanager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channelmanager.ChannelManagerApi(api_client)
    body = channelmanager.ChannelmanagerListMarketsWithAssociationsRequest() # ChannelmanagerListMarketsWithAssociationsRequest | 

    try:
        # ListMarketsWithAssociations
        api_response = api_instance.channel_manager_list_markets_with_associations(body)
        print("The response of ChannelManagerApi->channel_manager_list_markets_with_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelManagerApi->channel_manager_list_markets_with_associations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChannelmanagerListMarketsWithAssociationsRequest**](ChannelmanagerListMarketsWithAssociationsRequest.md)|  | 

### Return type

[**ChannelmanagerListMarketsWithAssociationsResponse**](ChannelmanagerListMarketsWithAssociationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channel_manager_update_channel**
> ChannelmanagerChannelResponse channel_manager_update_channel(body)

UpdateChannel

Update an existing channel

### Example


```python
import time
import os
import channelmanager
from channelmanager.models.channelmanager_channel_response import ChannelmanagerChannelResponse
from channelmanager.models.channelmanager_update_channel_request import ChannelmanagerUpdateChannelRequest
from channelmanager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://channel.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = channelmanager.Configuration(
    host = "https://channel.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with channelmanager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channelmanager.ChannelManagerApi(api_client)
    body = channelmanager.ChannelmanagerUpdateChannelRequest() # ChannelmanagerUpdateChannelRequest | 

    try:
        # UpdateChannel
        api_response = api_instance.channel_manager_update_channel(body)
        print("The response of ChannelManagerApi->channel_manager_update_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelManagerApi->channel_manager_update_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChannelmanagerUpdateChannelRequest**](ChannelmanagerUpdateChannelRequest.md)|  | 

### Return type

[**ChannelmanagerChannelResponse**](ChannelmanagerChannelResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channel_manager_update_market**
> ChannelmanagerMarketResponse channel_manager_update_market(body)

UpdateMarket

Update an existing market

### Example


```python
import time
import os
import channelmanager
from channelmanager.models.channelmanager_market_response import ChannelmanagerMarketResponse
from channelmanager.models.channelmanager_update_market_request import ChannelmanagerUpdateMarketRequest
from channelmanager.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://channel.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = channelmanager.Configuration(
    host = "https://channel.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with channelmanager.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channelmanager.ChannelManagerApi(api_client)
    body = channelmanager.ChannelmanagerUpdateMarketRequest() # ChannelmanagerUpdateMarketRequest | 

    try:
        # UpdateMarket
        api_response = api_instance.channel_manager_update_market(body)
        print("The response of ChannelManagerApi->channel_manager_update_market:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelManagerApi->channel_manager_update_market: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChannelmanagerUpdateMarketRequest**](ChannelmanagerUpdateMarketRequest.md)|  | 

### Return type

[**ChannelmanagerMarketResponse**](ChannelmanagerMarketResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

