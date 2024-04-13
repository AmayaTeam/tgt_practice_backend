import uuid

from django.db import models


# TODO: TextField?
class ToolModuleGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(null=True, blank=True)


class ToolModuleType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    r_modules_group_id = models.ForeignKey(ToolModuleGroup, on_delete=models.CASCADE)  # TODO: module(s)?
    name = models.TextField(null=True, blank=True)
    # TODO: module_type_id?
    hash_code = models.TextField(null=True, blank=True)  # TODO: для чего, зачем


class ToolModule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    r_module_type_id = models.ForeignKey(ToolModuleType, on_delete=models.CASCADE)
    sn_ = models.TextField(max_length=255, null=True, blank=True)
    dbdate_ = models.DateField(null=True, blank=True)
    dbversion_ = models.DateField(null=True, blank=True)
    dbsn_ = models.TextField(null=True, blank=True)
    dbcomment_ = models.TextField(null=True, blank=True)
    dbtname_ = models.TextField(null=True, blank=True)
    dbtlength_ = models.FloatField(null=True, blank=True)
    dbtweight_ = models.FloatField(null=True, blank=True)
    dbtmax_od_ = models.FloatField(null=True, blank=True)
    dbtmax_od_collapsed_ = models.FloatField(null=True, blank=True)
    dbtmax_od_opened_ = models.FloatField(null=True, blank=True)
    dbtimage2d_ = models.FloatField(null=True, blank=True)
    dbtimage_h_shift = models.FloatField(null=True, blank=True)
    dbtimage_h_scale = models.FloatField(null=True, blank=True)
    dbtimage_h_y1 = models.FloatField(null=True, blank=True)
    dbtimage_h_y2 = models.FloatField(null=True, blank=True)
    dbtcomp_str = models.FloatField(null=True, blank=True)


class ToolSensorType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(null=True, blank=True)
    # TODO: sensor_id?


class ToolInstalledSensor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    r_toolmodule_id = models.ForeignKey(ToolModule, on_delete=models.CASCADE)
    r_toolsensortype_id = models.ForeignKey(ToolSensorType, on_delete=models.CASCADE)
    record_point_ = models.FloatField(null=True, blank=True)
