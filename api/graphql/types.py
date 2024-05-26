from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, Group
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
        model = get_user_model()
        fields = ('id', 'username', 'first_name', 'last_name', 'email', "groups")  # Include necessary fields


class GroupType(DjangoObjectType):
    class Meta:
        model = Group
        fields = ("id", "name")