import graphene
from .types import ToolInstalledSensorT


class ToolInstalledSensorPayload(graphene.ObjectType):
    tool_installed_sensor = graphene.Field(ToolInstalledSensorT)


class DeleteToolInstalledSensorPayload(graphene.ObjectType):
    success = graphene.Boolean()
