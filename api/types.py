import graphene
from graphene_django import DjangoObjectType
from .models import *


class ToolModuleGroupType(DjangoObjectType):
    class Meta:
        model = ToolModuleGroup


class ToolModuleGroupConnection(graphene.relay.Connection):
    class Meta:
        node = ToolModuleGroupType


class ToolModuleTypeType(DjangoObjectType):
    class Meta:
        model = ToolModuleType


class ToolModuleTypeConnection(graphene.relay.Connection):
    class Meta:
        node = ToolModuleTypeType


class ToolModuleTypeType(DjangoObjectType):
    class Meta:
        model = ToolModuleType


class ToolModuleTypeConnection(graphene.relay.Connection):
    class Meta:
        node = ToolModuleTypeType


class ToolModuleType(DjangoObjectType):
    class Meta:
        model = ToolModule


class ToolModuleConnection(graphene.relay.Connection):
    class Meta:
        node = ToolModuleType


class ToolSensorTypeType(DjangoObjectType):
    class Meta:
        model = ToolSensorType


class ToolSensorTypeConnection(graphene.relay.Connection):
    class Meta:
        node = ToolSensorTypeType


class ToolInstalledSensorType(DjangoObjectType):
    class Meta:
        model = ToolInstalledSensor


class ToolInstalledSensorConnection(graphene.relay.Connection):
    class Meta:
        node = ToolInstalledSensorType
