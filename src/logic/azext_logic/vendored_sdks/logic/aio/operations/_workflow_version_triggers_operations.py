# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._workflow_version_triggers_operations import build_list_callback_url_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class WorkflowVersionTriggersOperations:
    """WorkflowVersionTriggersOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.logic.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def list_callback_url(
        self,
        resource_group_name: str,
        workflow_name: str,
        version_id: str,
        trigger_name: str,
        parameters: Optional["_models.GetCallbackUrlParameters"] = None,
        **kwargs: Any
    ) -> "_models.WorkflowTriggerCallbackUrl":
        """Get the callback url for a trigger of a workflow version.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param workflow_name: The workflow name.
        :type workflow_name: str
        :param version_id: The workflow versionId.
        :type version_id: str
        :param trigger_name: The workflow trigger name.
        :type trigger_name: str
        :param parameters: The callback URL parameters. Default value is None.
        :type parameters: ~azure.mgmt.logic.models.GetCallbackUrlParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: WorkflowTriggerCallbackUrl, or the result of cls(response)
        :rtype: ~azure.mgmt.logic.models.WorkflowTriggerCallbackUrl
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.WorkflowTriggerCallbackUrl"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2019-05-01")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        if parameters is not None:
            _json = self._serialize.body(parameters, 'GetCallbackUrlParameters')
        else:
            _json = None

        request = build_list_callback_url_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            workflow_name=workflow_name,
            version_id=version_id,
            trigger_name=trigger_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.list_callback_url.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('WorkflowTriggerCallbackUrl', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_callback_url.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/versions/{versionId}/triggers/{triggerName}/listCallbackUrl"}  # type: ignore
