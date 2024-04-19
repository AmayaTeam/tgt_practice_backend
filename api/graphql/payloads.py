import graphene
from .types import ToolInstalledSensorObject, ToolModuleObject


class ToolInstalledSensorPayload(graphene.ObjectType):
    tool_installed_sensor = graphene.Field(ToolInstalledSensorObject)


class DeletePayload(graphene.ObjectType):
    success = graphene.Boolean()


class ToolModulePayload(graphene.ObjectType):
    tool_module = graphene.Field(ToolModuleObject)
