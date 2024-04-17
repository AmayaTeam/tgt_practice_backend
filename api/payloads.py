import graphene
from .types import ToolInstalledSensorT

class ToolInstalledSensorPayload(graphene.ObjectType):
    tool_installed_sensor = graphene.Field(ToolInstalledSensorT)
