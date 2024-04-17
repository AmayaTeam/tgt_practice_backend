import graphene

from .types import *
from .models import *


class Query(graphene.ObjectType):
    tool_module_groups = graphene.List(ToolModuleGroupT)
    tool_module_types = graphene.List(ToolModuleTypeT)
    tool_modules = graphene.List(ToolModuleT)
    tool_sensor_types = graphene.List(ToolSensorTypeT)
    tool_installed_sensors = graphene.List(ToolInstalledSensorT)

    def resolve_tool_module_groups(self, info, **kwargs):
        return ToolModuleGroup.objects.all()

    def resolve_tool_module_types(self, info, **kwargs):
        return ToolModuleType.objects.all()

    def resolve_tool_modules(self, info, **kwargs):
        return ToolModule.objects.all()

    def resolve_tool_sensor_types(self, info, **kwargs):
        return ToolSensorType.objects.all()

    def resolve_tool_installed_sensors(self, info, **kwargs):
        return ToolInstalledSensor.objects.all()


schema = graphene.Schema(query=Query)
