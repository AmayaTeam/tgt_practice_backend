from django.contrib.auth.models import User
from graphene_django import DjangoObjectType
from api.models import (
    ToolModuleGroup,
    ToolModuleType,
    ToolModule,
    ToolSensorType,
    ToolInstalledSensor,
)


class ToolModuleGroupObject(DjangoObjectType):
    class Meta:
        model = ToolModuleGroup


class ToolModuleTypeObject(DjangoObjectType):
    class Meta:
        model = ToolModuleType


class ToolModuleObject(DjangoObjectType):
    class Meta:
        model = ToolModule


class ToolSensorTypeObject(DjangoObjectType):
    class Meta:
        model = ToolSensorType


class ToolInstalledSensorObject(DjangoObjectType):
    class Meta:
        model = ToolInstalledSensor


class UserType(DjangoObjectType):
    class Meta:
        model = User