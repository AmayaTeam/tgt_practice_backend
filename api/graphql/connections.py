import graphene

from .types import (
    ToolModuleGroupObject,
    ToolModuleTypeObject,
    ToolModuleObject,
    ToolSensorTypeObject,
    ToolInstalledSensorObject,
)


class ToolModuleGroupConnection(graphene.relay.Connection):
    class Meta:
        node = ToolModuleGroupObject


class ToolModuleTypeConnection(graphene.relay.Connection):
    class Meta:
        node = ToolModuleTypeObject


class ToolModuleConnection(graphene.relay.Connection):
    class Meta:
        node = ToolModuleObject


class ToolSensorTypeConnection(graphene.relay.Connection):
    class Meta:
        node = ToolSensorTypeObject


class ToolInstalledSensorConnection(graphene.relay.Connection):
    class Meta:
        node = ToolInstalledSensorObject
