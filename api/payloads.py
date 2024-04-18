import graphene
from .types import *


class ToolInstalledSensorPayload(graphene.ObjectType):
    tool_installed_sensor = graphene.Field(ToolInstalledSensorT)


class DeleteToolInstalledSensorPayload(graphene.ObjectType):
    success = graphene.Boolean()


class CreateToolModulePayload(graphene.ObjectType):
    tool_module = graphene.Field(ToolModuleT)