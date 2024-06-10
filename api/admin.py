from django.contrib import admin
from .models import (
    ToolModuleGroup,
    ToolModuleType,
    ToolModule,
    ToolSensorType,
    ToolInstalledSensor,
)


@admin.register(ToolModuleGroup)
class ToolModuleGroupAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_display_links = ("name",)


@admin.register(ToolModuleType)
class ToolModuleTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "r_modules_group", "module_type", "hash_code")
    search_fields = ("name", "hash_code")
    list_display_links = ("name",)


@admin.register(ToolModule)
class ToolModuleAdmin(admin.ModelAdmin):
    list_display = (
        "sn",
        "image",
        "r_module_type",
        "dbdate",
        "dbversion",
        "dbsn",
        "dbcomment",
        "dbtname",
    )
    search_fields = (
        "sn",
        "dbdate",
        "dbversion",
        "dbsn",
        "dbcomment",
        "dbtname",
    )
    list_display_links = ("sn",)


@admin.register(ToolSensorType)
class ToolSensorTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "sensor")
    search_fields = ("name",)
    list_display_links = ("name",)


@admin.register(ToolInstalledSensor)
class ToolInstalledSensorAdmin(admin.ModelAdmin):
    list_display = ("r_toolmodule", "r_toolsensortype", "record_point")
    search_fields = ("r_toolmodule", "r_toolsensortype", "record_point")
    list_display_links = ("r_toolmodule", "r_toolsensortype")
