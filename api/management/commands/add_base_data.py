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

    def handle(self, *args, **kwargs):
        tool_module_group_filepath = "api/management/data/tool_module_group.json"
        tool_module_type_filepath = "api/management/data/tool_module_type.json"

        with open(tool_module_group_filepath, "r", encoding="utf-8") as tool_module_group_file:
            tool_module_group_data = json.load(tool_module_group_file)

        with open(tool_module_type_filepath, "r", encoding="utf-8") as tool_module_type_file:
            tool_module_type_data = json.load(tool_module_type_file)

        self.add_tool_module_group(tool_module_group_data)
        self.add_tool_module_type(tool_module_type_data)
