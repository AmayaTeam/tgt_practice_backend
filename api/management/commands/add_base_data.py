from django.core.management import BaseCommand
import json
from api.models import *


class Command(BaseCommand):
    help = 'add_base_data'

    def add_tool_module_group(self, tool_module_group_data):
        for tool_module_group_element in tool_module_group_data:
            id = tool_module_group_element["id"]
            name = tool_module_group_element["name"]
            ToolModuleGroup.objects.create(
                id=id,
                name=name
            )

    def add_tool_module_type(self, tool_module_type_data):
        for tool_module_type_element in tool_module_type_data:
            id = tool_module_type_element["id"]
            name = tool_module_type_element["name"]
            r_modules_group_id = tool_module_type_element["r_modules_group_id"]
            tool_module_group = ToolModuleGroup.objects.filter(id=r_modules_group_id).first()
            # пока эти поля не нужны
            module_type_id = tool_module_type_element["module_type_id"]
            hash_code = tool_module_type_element["hash_code"]
            ToolModuleType.objects.create(
                id=id,
                name=name,
                module_type_id=module_type_id,
                hash_code=hash_code,
                r_modules_group_id=tool_module_group,
            )

    def add_tool_sensor_type(self, tool_sensor_type_data):
        for tool_sensor_type_element in tool_sensor_type_data:
            id = tool_sensor_type_element["id"]
            name = tool_sensor_type_element["name"]
            sensor_type_id = tool_sensor_type_element["sensor_type_id"]
            ToolSensorType.objects.create(
                id=id,
                name=name,
                sensor_type_id=sensor_type_id,
            )

    def add_tool_module(self, tool_module_data):
        for tool_module_element in tool_module_data:
            id = tool_module_element["id"]
            r_module_type_id = tool_module_element["r_module_type_id"]
            sn_ = tool_module_element["sn_"]
            dbdate_ = tool_module_element["dbdate_"]
            dbversion_ = tool_module_element["dbversion_"]
            dbsn_ = tool_module_element["dbsn_"]
            dbcomment_ = tool_module_element["dbcomment_"]
            dbtname_ = tool_module_element["dbtname_"]
            dbtlength_ = tool_module_element["dbtlength_"]
            dbtweight_ = tool_module_element["dbtweight_"]
            dbtmax_od_ = tool_module_element["dbtmax_od_"]
            dbtmax_od_collapsed_ = tool_module_element["dbtmax_od_collapsed_"]
            dbtmax_od_opened_ = tool_module_element["dbtmax_od_opened_"]
            dbtimage2d_ = tool_module_element["dbtimage2d_"]
            dbtimage_h_shift = tool_module_element["dbtimage_h_shift"]
            dbtimage_h_scale = tool_module_element["dbtimage_h_scale"]
            dbtimage_h_y1 = tool_module_element["dbtimage_h_y1"]
            dbtimage_h_y2 = tool_module_element["dbtimage_h_y2"]
            dbtcomp_str = tool_module_element["dbtcomp_str"]
            image = tool_module_element["image"]
            ToolModule.objects.create(
                id=id,
                r_module_type_id=r_module_type_id,
                sn=sn_,
                dbdate=dbdate_,
                dbversion=dbversion_,
                dbsn=dbsn_,
                dbcomment=dbcomment_,
                dbtname=dbtname_,
                dbtlength=dbtlength_,
                dbtweight=dbtweight_,
                dbtmax_od=dbtmax_od_,
                dbtmax_od_collapsed=dbtmax_od_collapsed_,
                dbtmax_od_opened=dbtmax_od_opened_,
                dbtimage2d=dbtimage2d_,
                dbtimage_h_shift=dbtimage_h_shift,
                dbtimage_h_scale=dbtimage_h_scale,
                dbtimage_h_y1=dbtimage_h_y1,
                dbtimage_h_y2=dbtimage_h_y2,
                dbtcomp_str=dbtcomp_str,
                image=image,
            )

    def add_tool_installed_sensor(self, tool_installed_sensor_data):
        for tool_installed_sensor_element in tool_installed_sensor_data:
            id = tool_installed_sensor_element["id"]
            r_toolmodule_id = tool_installed_sensor_element["r_toolmodule_id"]
            r_toolsensortype_id = tool_installed_sensor_element["r_toolsensortype_id"]
            record_point_ = tool_installed_sensor_element["record_point_"]
            ToolInstalledSensor.objects.create(
                id=id,
                r_toolmodule_id=r_toolmodule_id,
                r_toolsensortype_id=r_toolsensortype_id,
                record_point=record_point_,
            )


    def handle(self, *args, **kwargs):
        tool_module_group_filepath = "api/management/data/tool_module_group.json"
        tool_module_type_filepath = "api/management/data/tool_module_type.json"
        tool_sensor_type_filepath = "api/management/data/tool_sensor_type.json"
        tool_module_filepath = "api/management/data/tool_module.json"

        with open(tool_module_group_filepath, "r", encoding="utf-8") as tool_module_group_file:
            tool_module_group_data = json.load(tool_module_group_file)

        with open(tool_module_type_filepath, "r", encoding="utf-8") as tool_module_type_file:
            tool_module_type_data = json.load(tool_module_type_file)

        with open(tool_sensor_type_filepath, "r", encoding="utf-8") as tool_sensor_type_file:
            tool_sensor_type_data = json.load(tool_sensor_type_file)

        with open(tool_module_filepath, "r", encoding="utf-8") as tool_module_file:
            tool_module_data = json.load(tool_module_file)

        self.add_tool_module_group(tool_module_group_data)
        self.add_tool_module_type(tool_module_type_data)
        self.add_tool_sensor_type(tool_sensor_type_data)
        self.add_tool_module(tool_module_data)
