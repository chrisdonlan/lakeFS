# coding: utf-8

"""
    lakeFS API

    lakeFS HTTP API

    The version of the OpenAPI document: 0.1.0
    Contact: services@treeverse.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictBool, StrictStr

from typing import Optional

from lakefs_sdk.models.object_stats import ObjectStats
from lakefs_sdk.models.staging_location import StagingLocation
from lakefs_sdk.models.staging_metadata import StagingMetadata

from lakefs_sdk.api_client import ApiClient
from lakefs_sdk.api_response import ApiResponse
from lakefs_sdk.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class StagingApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_physical_address(self, repository : StrictStr, branch : StrictStr, path : Annotated[StrictStr, Field(..., description="relative to the branch")], presign : Optional[StrictBool] = None, **kwargs) -> StagingLocation:  # noqa: E501
        """generate an address to which the client can upload an object  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_physical_address(repository, branch, path, presign, async_req=True)
        >>> result = thread.get()

        :param repository: (required)
        :type repository: str
        :param branch: (required)
        :type branch: str
        :param path: relative to the branch (required)
        :type path: str
        :param presign:
        :type presign: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: StagingLocation
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_physical_address_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_physical_address_with_http_info(repository, branch, path, presign, **kwargs)  # noqa: E501

    @validate_arguments
    def get_physical_address_with_http_info(self, repository : StrictStr, branch : StrictStr, path : Annotated[StrictStr, Field(..., description="relative to the branch")], presign : Optional[StrictBool] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """generate an address to which the client can upload an object  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_physical_address_with_http_info(repository, branch, path, presign, async_req=True)
        >>> result = thread.get()

        :param repository: (required)
        :type repository: str
        :param branch: (required)
        :type branch: str
        :param path: relative to the branch (required)
        :type path: str
        :param presign:
        :type presign: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(StagingLocation, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'repository',
            'branch',
            'path',
            'presign'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_physical_address" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['repository']:
            _path_params['repository'] = _params['repository']

        if _params['branch']:
            _path_params['branch'] = _params['branch']


        # process the query parameters
        _query_params = []
        if _params.get('path') is not None:  # noqa: E501
            _query_params.append(('path', _params['path']))

        if _params.get('presign') is not None:  # noqa: E501
            _query_params.append(('presign', _params['presign']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basic_auth', 'cookie_auth', 'oidc_auth', 'saml_auth', 'jwt_token']  # noqa: E501

        _response_types_map = {
            '200': "StagingLocation",
            '401': "Error",
            '404': "Error",
        }

        return self.api_client.call_api(
            '/repositories/{repository}/branches/{branch}/staging/backing', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def link_physical_address(self, repository : StrictStr, branch : StrictStr, path : Annotated[StrictStr, Field(..., description="relative to the branch")], staging_metadata : StagingMetadata, **kwargs) -> ObjectStats:  # noqa: E501
        """associate staging on this physical address with a path  # noqa: E501

        Link the physical address with the path in lakeFS, creating an uncommitted change. The given address can be one generated by getPhysicalAddress, or an address outside the repository's storage namespace.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.link_physical_address(repository, branch, path, staging_metadata, async_req=True)
        >>> result = thread.get()

        :param repository: (required)
        :type repository: str
        :param branch: (required)
        :type branch: str
        :param path: relative to the branch (required)
        :type path: str
        :param staging_metadata: (required)
        :type staging_metadata: StagingMetadata
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ObjectStats
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the link_physical_address_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.link_physical_address_with_http_info(repository, branch, path, staging_metadata, **kwargs)  # noqa: E501

    @validate_arguments
    def link_physical_address_with_http_info(self, repository : StrictStr, branch : StrictStr, path : Annotated[StrictStr, Field(..., description="relative to the branch")], staging_metadata : StagingMetadata, **kwargs) -> ApiResponse:  # noqa: E501
        """associate staging on this physical address with a path  # noqa: E501

        Link the physical address with the path in lakeFS, creating an uncommitted change. The given address can be one generated by getPhysicalAddress, or an address outside the repository's storage namespace.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.link_physical_address_with_http_info(repository, branch, path, staging_metadata, async_req=True)
        >>> result = thread.get()

        :param repository: (required)
        :type repository: str
        :param branch: (required)
        :type branch: str
        :param path: relative to the branch (required)
        :type path: str
        :param staging_metadata: (required)
        :type staging_metadata: StagingMetadata
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ObjectStats, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'repository',
            'branch',
            'path',
            'staging_metadata'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method link_physical_address" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['repository']:
            _path_params['repository'] = _params['repository']

        if _params['branch']:
            _path_params['branch'] = _params['branch']


        # process the query parameters
        _query_params = []
        if _params.get('path') is not None:  # noqa: E501
            _query_params.append(('path', _params['path']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['staging_metadata'] is not None:
            _body_params = _params['staging_metadata']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['basic_auth', 'cookie_auth', 'oidc_auth', 'saml_auth', 'jwt_token']  # noqa: E501

        _response_types_map = {
            '200': "ObjectStats",
            '400': "Error",
            '401': "Error",
            '404': "Error",
            '409': "StagingLocation",
        }

        return self.api_client.call_api(
            '/repositories/{repository}/branches/{branch}/staging/backing', 'PUT',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
