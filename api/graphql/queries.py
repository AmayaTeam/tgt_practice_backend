import graphene
from django.contrib.auth.models import Group
from api.graphql.decorators import query_permission_required

from .types import (
    ToolModuleGroupObject,
    ToolModuleTypeObject,
    ToolModuleObject,
    ToolSensorTypeObject,
    ToolInstalledSensorObject,
    UserType,
    GroupType,
)
from api.models import (
    ToolModuleGroup,
    ToolModuleType,
    ToolModule,
    ToolSensorType,
    ToolInstalledSensor,
)


class Query(graphene.ObjectType):
    tool_module_groups = graphene.List(ToolModuleGroupObject)
    tool_module_types = graphene.List(ToolModuleTypeObject)
    tool_modules = graphene.List(ToolModuleObject)
    tool_sensor_types = graphene.List(ToolSensorTypeObject)
    tool_installed_sensors = graphene.List(ToolInstalledSensorObject)

    tool_modules_by_id = graphene.Field(ToolModuleObject, id=graphene.String())

    me = graphene.Field(UserType)
    groups = graphene.List(GroupType)

    def resolve_me(self, info):
        user = info.context.user
        return user

    def resolve_groups(self, info, **kwargs):
        return Group.objects.all()

    @query_permission_required("api.view_toolmodulegroup")
    def resolve_tool_module_groups(self, info, **kwargs):
        return ToolModuleGroup.objects.all()

    @query_permission_required("api.view_toolmoduletype")
    def resolve_tool_module_types(self, info, **kwargs):
        return ToolModuleType.objects.all()

    @query_permission_required("api.view_toolmodule")
    def resolve_tool_modules(self, info, **kwargs):
        return ToolModule.objects.all()

    @query_permission_required("api.view_toolmodule")
    def resolve_tool_modules_by_id(self, info, id):
        # Querying a single question
        return ToolModule.objects.get(pk=id)

    @query_permission_required("api.view_toolmoduletype")
    def resolve_tool_sensor_types(self, info, **kwargs):
        return ToolSensorType.objects.all()

    @query_permission_required("api.view_toolinstalledsensor")
    def resolve_tool_installed_sensors(self, info, **kwargs):
        return ToolInstalledSensor.objects.all()
