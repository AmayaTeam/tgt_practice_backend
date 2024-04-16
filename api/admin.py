from django.contrib import admin
from .models import ToolModuleGroup, ToolModuleType, ToolModule, ToolSensorType, ToolInstalledSensor


@admin.register(ToolModuleGroup)
class ToolModuleGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_display_links = ('name',)


@admin.register(ToolModuleType)
class ToolModuleTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'r_modules_group_id', 'module_type_id', 'hash_code')
    search_fields = ('name', 'hash_code')
    list_display_links = ('name',)


@admin.register(ToolModule)
class ToolModuleAdmin(admin.ModelAdmin):
    list_display = (
        'sn', 'image', 'r_module_type_id', 'dbdate', 'dbversion', 'dbsn', 'dbcomment', 'dbtname', 'dbtlength', 'dbtweight',
        'dbtmax_od', 'dbtmax_od_collapsed', 'dbtmax_od_opened', 'dbtimage2d', 'dbtimage_h_shift', 'dbtimage_h_scale',
        'dbtimage_h_y1', 'dbtimage_h_y2', 'dbtcomp_str')
    search_fields = (
        'sn', 'dbdate', 'dbversion', 'dbsn', 'dbcomment', 'dbtname', 'dbtlength', 'dbtweight',
        'dbtmax_od', 'dbtmax_od_collapsed', 'dbtmax_od_opened', 'dbtimage2d', 'dbtimage_h_shift', 'dbtimage_h_scale',
        'dbtimage_h_y1', 'dbtimage_h_y2', 'dbtcomp_str')
    list_display_links = ('sn',)


@admin.register(ToolSensorType)
class ToolSensorTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'sensor_id')
    search_fields = ('name',)
    list_display_links = ('name',)


@admin.register(ToolInstalledSensor)
class ToolInstalledSensorAdmin(admin.ModelAdmin):
    list_display = ('r_toolmodule_id', 'r_toolsensortype_id', 'record_point')
    search_fields = ('r_toolmodule_id', 'r_toolsensortype_id', 'record_point')
    list_display_links = ('r_toolmodule_id', 'r_toolsensortype_id')
