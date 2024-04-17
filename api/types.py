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
