import graphene
from .types import ToolInstalledSensorT

class CreateToolInstalledSensorPayload(graphene.ObjectType):
    tool_installed_sensor = graphene.Field(ToolInstalledSensorT)
