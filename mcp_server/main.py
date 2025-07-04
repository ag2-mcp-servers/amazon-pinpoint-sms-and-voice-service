# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T13:51:06+00:00



import argparse
import json
import os
from typing import *
from typing import Optional, Union

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import APIKeyHeader, BaseSecurity
from fastapi import Header, Path, Query

from models import (
    AlreadyExistsException,
    BadRequestException,
    CreateConfigurationSetEventDestinationResponse,
    CreateConfigurationSetResponse,
    DeleteConfigurationSetEventDestinationResponse,
    DeleteConfigurationSetResponse,
    GetConfigurationSetEventDestinationsResponse,
    InternalServiceErrorException,
    LimitExceededException,
    ListConfigurationSetsResponse,
    NotFoundException,
    SendVoiceMessageResponse,
    TooManyRequestsException,
    UpdateConfigurationSetEventDestinationResponse,
    V1SmsVoiceConfigurationSetsConfigurationSetNameEventDestinationsEventDestinationNamePutRequest,
    V1SmsVoiceConfigurationSetsConfigurationSetNameEventDestinationsPostRequest,
    V1SmsVoiceConfigurationSetsPostRequest,
    V1SmsVoiceVoiceMessagePostRequest,
)

app = MCPProxy(
    contact={
        'email': 'mike.ralphson@gmail.com',
        'name': 'Mike Ralphson',
        'url': 'https://github.com/mermade/aws2openapi',
        'x-twitter': 'PermittedSoc',
    },
    description='Pinpoint SMS and Voice Messaging public facing APIs',
    license={'name': 'Apache 2.0 License', 'url': 'http://www.apache.org/licenses/'},
    termsOfService='https://aws.amazon.com/service-terms/',
    title='Amazon Pinpoint SMS and Voice Service',
    version='2018-09-05',
    servers=[
        {
            'description': 'The Pinpoint SMS Voice multi-region endpoint',
            'url': 'http://sms-voice.pinpoint.{region}.amazonaws.com',
            'variables': {
                'region': {
                    'default': 'us-east-1',
                    'description': 'The AWS region',
                    'enum': [
                        'us-east-1',
                        'us-east-2',
                        'us-west-1',
                        'us-west-2',
                        'us-gov-west-1',
                        'us-gov-east-1',
                        'ca-central-1',
                        'eu-north-1',
                        'eu-west-1',
                        'eu-west-2',
                        'eu-west-3',
                        'eu-central-1',
                        'eu-south-1',
                        'af-south-1',
                        'ap-northeast-1',
                        'ap-northeast-2',
                        'ap-northeast-3',
                        'ap-southeast-1',
                        'ap-southeast-2',
                        'ap-east-1',
                        'ap-south-1',
                        'sa-east-1',
                        'me-south-1',
                    ],
                }
            },
        },
        {
            'description': 'The Pinpoint SMS Voice multi-region endpoint',
            'url': 'https://sms-voice.pinpoint.{region}.amazonaws.com',
            'variables': {
                'region': {
                    'default': 'us-east-1',
                    'description': 'The AWS region',
                    'enum': [
                        'us-east-1',
                        'us-east-2',
                        'us-west-1',
                        'us-west-2',
                        'us-gov-west-1',
                        'us-gov-east-1',
                        'ca-central-1',
                        'eu-north-1',
                        'eu-west-1',
                        'eu-west-2',
                        'eu-west-3',
                        'eu-central-1',
                        'eu-south-1',
                        'af-south-1',
                        'ap-northeast-1',
                        'ap-northeast-2',
                        'ap-northeast-3',
                        'ap-southeast-1',
                        'ap-southeast-2',
                        'ap-east-1',
                        'ap-south-1',
                        'sa-east-1',
                        'me-south-1',
                    ],
                }
            },
        },
        {
            'description': 'The Pinpoint SMS Voice endpoint for China (Beijing) and China (Ningxia)',
            'url': 'http://sms-voice.pinpoint.{region}.amazonaws.com.cn',
            'variables': {
                'region': {
                    'default': 'cn-north-1',
                    'description': 'The AWS region',
                    'enum': ['cn-north-1', 'cn-northwest-1'],
                }
            },
        },
        {
            'description': 'The Pinpoint SMS Voice endpoint for China (Beijing) and China (Ningxia)',
            'url': 'https://sms-voice.pinpoint.{region}.amazonaws.com.cn',
            'variables': {
                'region': {
                    'default': 'cn-north-1',
                    'description': 'The AWS region',
                    'enum': ['cn-north-1', 'cn-northwest-1'],
                }
            },
        },
    ],
)


@app.get(
    '/v1/sms-voice/configuration-sets',
    description=""" List all of the configuration sets associated with your Amazon Pinpoint account in the current region. """,
    tags=['configuration_set_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def list_configuration_sets(
    next_token: Optional[str] = Query(None, alias='NextToken'),
    page_size: Optional[str] = Query(None, alias='PageSize'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/sms-voice/configuration-sets',
    description=""" Create a new configuration set. After you create the configuration set, you can add one or more event destinations to it. """,
    tags=['configuration_set_management', 'voice_message_delivery'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def create_configuration_set(
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: V1SmsVoiceConfigurationSetsPostRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.delete(
    '/v1/sms-voice/configuration-sets/{ConfigurationSetName}',
    description=""" Deletes an existing configuration set. """,
    tags=['configuration_set_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def delete_configuration_set(
    configuration_set_name: str = Path(..., alias='ConfigurationSetName'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/sms-voice/configuration-sets/{ConfigurationSetName}/event-destinations',
    description=""" Obtain information about an event destination, including the types of events it reports, the Amazon Resource Name (ARN) of the destination, and the name of the event destination. """,
    tags=['configuration_set_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def get_configuration_set_event_destinations(
    configuration_set_name: str = Path(..., alias='ConfigurationSetName'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/sms-voice/configuration-sets/{ConfigurationSetName}/event-destinations',
    description=""" Create a new event destination in a configuration set. """,
    tags=['configuration_set_management', 'voice_message_delivery'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def create_configuration_set_event_destination(
    configuration_set_name: str = Path(..., alias='ConfigurationSetName'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: V1SmsVoiceConfigurationSetsConfigurationSetNameEventDestinationsPostRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.delete(
    '/v1/sms-voice/configuration-sets/{ConfigurationSetName}/event-destinations/{EventDestinationName}',
    description=""" Deletes an event destination in a configuration set. """,
    tags=['configuration_set_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def delete_configuration_set_event_destination(
    configuration_set_name: str = Path(..., alias='ConfigurationSetName'),
    event_destination_name: str = Path(..., alias='EventDestinationName'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.put(
    '/v1/sms-voice/configuration-sets/{ConfigurationSetName}/event-destinations/{EventDestinationName}',
    description=""" Update an event destination in a configuration set. An event destination is a location that you publish information about your voice calls to. For example, you can log an event to an Amazon CloudWatch destination when a call fails. """,
    tags=['configuration_set_management', 'voice_message_delivery'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def update_configuration_set_event_destination(
    configuration_set_name: str = Path(..., alias='ConfigurationSetName'),
    event_destination_name: str = Path(..., alias='EventDestinationName'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: V1SmsVoiceConfigurationSetsConfigurationSetNameEventDestinationsEventDestinationNamePutRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/sms-voice/voice/message',
    description=""" Create a new voice message and send it to a recipient's phone number. """,
    tags=['voice_message_delivery'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def send_voice_message(
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: V1SmsVoiceVoiceMessagePostRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
