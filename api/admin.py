from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from .models import (
    ToolModuleGroup,
    ToolModuleType,
    ToolModule,
    ToolSensorType,
    ToolInstalledSensor,
)


manager_group, created = Group.objects.get_or_create(name='manager')
user_group, created = Group.objects.get_or_create(name='user')
# CRUD для manager
permissions = Permission.objects.filter(content_type__app_label='api')
manager_group.permissions.set(permissions)

# Только чтение для user
user_permissions = Permission.objects.filter(content_type__app_label='api', codename__startswith='view')
user_group.permissions.set(user_permissions)


@admin.register(ToolModuleGroup)
class ToolModuleGroupAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_display_links = ("name",)


@admin.register(ToolModuleType)
class ToolModuleTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "r_modules_group_id", "module_type_id", "hash_code")
    search_fields = ("name", "hash_code")
    list_display_links = ("name",)


@admin.register(ToolModule)
class ToolModuleAdmin(admin.ModelAdmin):
    list_display = (
        "sn",
        "image",
        "r_module_type_id",
        "dbdate",
        "dbversion",
        "dbsn",
        "dbcomment",
        "dbtname",
        "dbtlength",
        "dbtweight",
        "dbtmax_od",
        "dbtmax_od_collapsed",
        "dbtmax_od_opened",
        "dbtimage_h_shift",
        "dbtimage_h_scale",
        "dbtimage_h_y1",
        "dbtimage_h_y2",
        "dbtcomp_str",
    )
    search_fields = (
        "sn",
        "dbdate",
        "dbversion",
        "dbsn",
        "dbcomment",
        "dbtname",
        "dbtlength",
        "dbtweight",
        "dbtmax_od",
        "dbtmax_od_collapsed",
        "dbtmax_od_opened",
        "dbtimage_h_shift",
        "dbtimage_h_scale",
        "dbtimage_h_y1",
        "dbtimage_h_y2",
        "dbtcomp_str",
    )
    list_display_links = ("sn",)


@admin.register(ToolSensorType)
class ToolSensorTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "sensor_id")
    search_fields = ("name",)
    list_display_links = ("name",)


@admin.register(ToolInstalledSensor)
class ToolInstalledSensorAdmin(admin.ModelAdmin):
    list_display = ("r_toolmodule_id", "r_toolsensortype_id", "record_point")
    search_fields = ("r_toolmodule_id", "r_toolsensortype_id", "record_point")
    list_display_links = ("r_toolmodule_id", "r_toolsensortype_id")
