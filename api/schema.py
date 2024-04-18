import graphene

from .types import *
from .models import *
from .inputs import *
from .payloads import *


class CreateToolInstalledSensor(graphene.Mutation):
    class Arguments:
        input = CreateToolInstalledSensorInput(required=True)

    Output = ToolInstalledSensorPayload

    @classmethod
    def mutate(cls, root, info, input):
        try:
            tool_module = ToolModule.objects.get(pk=input.r_toolmodule_id)
        except ToolModule.DoesNotExist:
            raise Exception("Tool module not found")

        try:
            tool_sensor_type = ToolSensorType.objects.get(pk=input.r_toolsensortype_id)
        except ToolSensorType.DoesNotExist:
            raise Exception("Tool sensor type not found")

        tool_installed_sensor = ToolInstalledSensor.objects.create(
            r_toolmodule_id=tool_module,
            r_toolsensortype_id=tool_sensor_type,
            record_point=input.record_point,
        )
        return ToolInstalledSensorPayload(tool_installed_sensor=tool_installed_sensor)


class UpdateToolInstalledSensor(graphene.Mutation):
    class Arguments:
        input = UpdateToolInstalledSensorInput(required=True)

    Output = ToolInstalledSensorPayload

    @classmethod
    def mutate(cls, root, info, input):
        try:
            tool_installed_sensor = ToolInstalledSensor.objects.get(pk=input.id)
        except ToolInstalledSensor.DoesNotExist:
            raise Exception("Tool installed sensor not found")

        tool_installed_sensor.record_point = input.record_point
        tool_installed_sensor.save()

        return ToolInstalledSensorPayload(tool_installed_sensor=tool_installed_sensor)


class DeleteToolInstalledSensor(graphene.Mutation):
    class Arguments:
        input = DeleteToolInstalledSensorInput(required=True)

    Output = DeleteToolInstalledSensorPayload

    @classmethod
    def mutate(cls, root, info, input):
        try:
            tool_installed_sensor = ToolInstalledSensor.objects.get(pk=input.id)
            tool_installed_sensor.delete()
            return DeleteToolInstalledSensorPayload(success=True)
        except ToolInstalledSensor.DoesNotExist:
            return DeleteToolInstalledSensorPayload(success=False)


class CreateToolModule(graphene.Mutation):
    class Arguments:
        input = CreateToolModuleInput(required=True)

    Output = CreateToolModulePayload

    @classmethod
    def mutate(cls, root, info, input):
        try:
            tool_module_type = ToolModuleType.objects.get(pk=input.r_module_type_id)
        except ToolModuleType.DoesNotExist:
            raise Exception("Tool module type not found")

        tool_module = ToolModule.objects.create(
            r_module_type_id=tool_module_type,
            sn=input.sn,
            dbsn=input.dbsn,
            dbtname=input.dbtname,
            dbdate=input.dbdate,
            dbversion=input.dbversion,
            dbcomment=input.dbcomment,
            dbtlength=input.dbtlength,
            dbtweight=input.dbtweight,
            dbtmax_od=input.dbtmax_od,
            dbtmax_od_collapsed=input.dbtmax_od_collapsed,
            dbtmax_od_opened=input.dbtmax_od_opened,
            dbtimage_h_shift=input.dbtimage_h_shift,
            dbtimage_h_scale=input.dbtimage_h_scale,
            dbtimage_h_y1=input.dbtimage_h_y1,
            dbtimage_h_y2=input.dbtimage_h_y2,
            dbtcomp_str=input.dbtcomp_str,
            image=input.image
        )
        return CreateToolModulePayload(tool_module=tool_module)


class Mutation(graphene.ObjectType):
    create_tool_installed_sensor = CreateToolInstalledSensor.Field()
    update_tool_installed_sensor = UpdateToolInstalledSensor.Field()
    delete_tool_installed_sensor = DeleteToolInstalledSensor.Field()

    create_tool_module = CreateToolModule.Field()


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


schema = graphene.Schema(query=Query, mutation=Mutation)
