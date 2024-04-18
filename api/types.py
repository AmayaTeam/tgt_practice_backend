import graphene
from graphene_django import DjangoObjectType
from .models import *


class ToolModuleGroupT(DjangoObjectType):
    class Meta:
        model = ToolModuleGroup


class ToolModuleGroupConnection(graphene.relay.Connection):
    class Meta:
        node = ToolModuleGroupT


class ToolModuleTypeT(DjangoObjectType):
    class Meta:
        model = ToolModuleType


class ToolModuleTypeConnection(graphene.relay.Connection):
    class Meta:
        node = ToolModuleTypeT


class ToolModuleT(DjangoObjectType):
    class Meta:
        model = ToolModule


class ToolModuleConnection(graphene.relay.Connection):
    class Meta:
        node = ToolModuleT


class ToolSensorTypeT(DjangoObjectType):
    class Meta:
        model = ToolSensorType


class ToolSensorTypeConnection(graphene.relay.Connection):
    class Meta:
        node = ToolSensorTypeT


class ToolInstalledSensorT(DjangoObjectType):
    class Meta:
        model = ToolInstalledSensor


class ToolInstalledSensorConnection(graphene.relay.Connection):
    class Meta:
        node = ToolInstalledSensorT
