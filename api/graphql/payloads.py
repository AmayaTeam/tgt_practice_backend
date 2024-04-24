import graphene
from .types import (
    ToolInstalledSensorObject,
    ToolModuleObject,
    ToolModuleGroupObject,
    ToolModuleTypeObject,
)


class ToolInstalledSensorPayload(graphene.ObjectType):
    tool_installed_sensor = graphene.Field(ToolInstalledSensorObject)


class ToolModuleGroupPayload(graphene.ObjectType):
    tool_module_group = graphene.Field(ToolModuleGroupObject)


class DeletePayload(graphene.ObjectType):
    success = graphene.Boolean()


class ToolModulePayload(graphene.ObjectType):
    tool_module = graphene.Field(ToolModuleObject)


class ToolModuleTypePayload(graphene.ObjectType):
    tool_module_type = graphene.Field(ToolModuleTypeObject)
