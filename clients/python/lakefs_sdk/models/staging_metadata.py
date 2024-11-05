# coding: utf-8

"""
    lakeFS API

    lakeFS HTTP API

    The version of the OpenAPI document: 1.0.0
    Contact: services@treeverse.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Dict, Optional
try:
    from pydantic.v1 import BaseModel, Field, StrictBool, StrictInt, StrictStr
except ImportError:
    from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from lakefs_sdk.models.staging_location import StagingLocation

class StagingMetadata(BaseModel):
    """
    information about uploaded object
    """
    staging: StagingLocation = Field(...)
    checksum: StrictStr = Field(..., description="unique identifier of object content on backing store (typically ETag)")
    size_bytes: StrictInt = Field(...)
    user_metadata: Optional[Dict[str, StrictStr]] = None
    content_type: Optional[StrictStr] = Field(None, description="Object media type")
    mtime: Optional[StrictInt] = Field(None, description="Unix Epoch in seconds.  May be ignored by server.")
    force: Optional[StrictBool] = False
    __properties = ["staging", "checksum", "size_bytes", "user_metadata", "content_type", "mtime", "force"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> StagingMetadata:
        """Create an instance of StagingMetadata from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of staging
        if self.staging:
            _dict['staging'] = self.staging.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StagingMetadata:
        """Create an instance of StagingMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StagingMetadata.parse_obj(obj)

        _obj = StagingMetadata.parse_obj({
            "staging": StagingLocation.from_dict(obj.get("staging")) if obj.get("staging") is not None else None,
            "checksum": obj.get("checksum"),
            "size_bytes": obj.get("size_bytes"),
            "user_metadata": obj.get("user_metadata"),
            "content_type": obj.get("content_type"),
            "mtime": obj.get("mtime"),
            "force": obj.get("force") if obj.get("force") is not None else False
        })
        return _obj


