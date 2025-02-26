# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import sys
from typing import Any, List, Optional, TYPE_CHECKING, Union

from ... import _serialization

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object


class Resource(_serialization.Model):
    """Describes an Azure resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
    }

    def __init__(self, **kwargs):
        """ """
        super().__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class Application(Resource):
    """Security Application over a given scope.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar display_name: display name of the application.
    :vartype display_name: str
    :ivar description: description of the application.
    :vartype description: str
    :ivar source_resource_type: The application source, what it affects, e.g. Assessments.
     "Assessments"
    :vartype source_resource_type: str or
     ~azure.mgmt.security.v2022_07_01_preview.models.ApplicationSourceResourceType
    :ivar condition_sets: The application conditionSets - see examples.
    :vartype condition_sets: list[JSON]
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "display_name": {"key": "properties.displayName", "type": "str"},
        "description": {"key": "properties.description", "type": "str"},
        "source_resource_type": {"key": "properties.sourceResourceType", "type": "str"},
        "condition_sets": {"key": "properties.conditionSets", "type": "[object]"},
    }

    def __init__(
        self,
        *,
        display_name: Optional[str] = None,
        description: Optional[str] = None,
        source_resource_type: Optional[Union[str, "_models.ApplicationSourceResourceType"]] = None,
        condition_sets: Optional[List[JSON]] = None,
        **kwargs
    ):
        """
        :keyword display_name: display name of the application.
        :paramtype display_name: str
        :keyword description: description of the application.
        :paramtype description: str
        :keyword source_resource_type: The application source, what it affects, e.g. Assessments.
         "Assessments"
        :paramtype source_resource_type: str or
         ~azure.mgmt.security.v2022_07_01_preview.models.ApplicationSourceResourceType
        :keyword condition_sets: The application conditionSets - see examples.
        :paramtype condition_sets: list[JSON]
        """
        super().__init__(**kwargs)
        self.display_name = display_name
        self.description = description
        self.source_resource_type = source_resource_type
        self.condition_sets = condition_sets


class ApplicationCondition(_serialization.Model):
    """Application's condition.

    :ivar property: The application Condition's Property, e.g. ID, see examples.
    :vartype property: str
    :ivar value: The application Condition's Value like IDs that contain some string, see examples.
    :vartype value: str
    :ivar operator: The application Condition's Operator, for example Contains for id or In for
     list of possible IDs, see examples. Known values are: "Contains", "Equals", and "In".
    :vartype operator: str or
     ~azure.mgmt.security.v2022_07_01_preview.models.ApplicationConditionOperator
    """

    _attribute_map = {
        "property": {"key": "property", "type": "str"},
        "value": {"key": "value", "type": "str"},
        "operator": {"key": "operator", "type": "str"},
    }

    def __init__(
        self,
        *,
        property: Optional[str] = None,
        value: Optional[str] = None,
        operator: Optional[Union[str, "_models.ApplicationConditionOperator"]] = None,
        **kwargs
    ):
        """
        :keyword property: The application Condition's Property, e.g. ID, see examples.
        :paramtype property: str
        :keyword value: The application Condition's Value like IDs that contain some string, see
         examples.
        :paramtype value: str
        :keyword operator: The application Condition's Operator, for example Contains for id or In for
         list of possible IDs, see examples. Known values are: "Contains", "Equals", and "In".
        :paramtype operator: str or
         ~azure.mgmt.security.v2022_07_01_preview.models.ApplicationConditionOperator
        """
        super().__init__(**kwargs)
        self.property = property
        self.value = value
        self.operator = operator


class ApplicationsList(_serialization.Model):
    """Page of a security applications list.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: Collection of applications in this page.
    :vartype value: list[~azure.mgmt.security.v2022_07_01_preview.models.Application]
    :ivar next_link: The URI to fetch the next page.
    :vartype next_link: str
    """

    _validation = {
        "value": {"readonly": True},
        "next_link": {"readonly": True},
    }

    _attribute_map = {
        "value": {"key": "value", "type": "[Application]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(self, **kwargs):
        """ """
        super().__init__(**kwargs)
        self.value = None
        self.next_link = None


class CloudErrorBody(_serialization.Model):
    """The error detail.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~azure.mgmt.security.v2022_07_01_preview.models.CloudErrorBody]
    :ivar additional_info: The error additional info.
    :vartype additional_info:
     list[~azure.mgmt.security.v2022_07_01_preview.models.ErrorAdditionalInfo]
    """

    _validation = {
        "code": {"readonly": True},
        "message": {"readonly": True},
        "target": {"readonly": True},
        "details": {"readonly": True},
        "additional_info": {"readonly": True},
    }

    _attribute_map = {
        "code": {"key": "code", "type": "str"},
        "message": {"key": "message", "type": "str"},
        "target": {"key": "target", "type": "str"},
        "details": {"key": "details", "type": "[CloudErrorBody]"},
        "additional_info": {"key": "additionalInfo", "type": "[ErrorAdditionalInfo]"},
    }

    def __init__(self, **kwargs):
        """ """
        super().__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class ErrorAdditionalInfo(_serialization.Model):
    """The resource management error additional info.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: JSON
    """

    _validation = {
        "type": {"readonly": True},
        "info": {"readonly": True},
    }

    _attribute_map = {
        "type": {"key": "type", "type": "str"},
        "info": {"key": "info", "type": "object"},
    }

    def __init__(self, **kwargs):
        """ """
        super().__init__(**kwargs)
        self.type = None
        self.info = None
