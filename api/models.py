import uuid

from django.db import models


class ToolModuleGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class ToolModuleType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    r_modules_group_id = models.ForeignKey(ToolModuleGroup, on_delete=models.CASCADE)
    name = models.TextField(null=True, blank=True)
    module_type_id = models.TextField(null=True, blank=True)
    hash_code = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class ToolModule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    r_module_type_id = models.ForeignKey(ToolModuleType, on_delete=models.CASCADE)
    sn = models.TextField(max_length=255, null=True, blank=True)
    dbdate = models.DateField(null=True, blank=True)
    dbversion = models.TextField(null=True, blank=True)
    dbsn = models.TextField(null=True, blank=True)
    dbcomment = models.TextField(null=True, blank=True)
    dbtname = models.TextField(null=True, blank=True)
    dbtlength = models.FloatField(null=True, blank=True)
    dbtweight = models.FloatField(null=True, blank=True)
    dbtmax_od = models.FloatField(null=True, blank=True)
    dbtmax_od_collapsed = models.FloatField(null=True, blank=True)
    dbtmax_od_opened = models.FloatField(null=True, blank=True)
    dbtimage_h_shift = models.FloatField(null=True, blank=True)
    dbtimage_h_scale = models.FloatField(null=True, blank=True)
    dbtimage_h_y1 = models.FloatField(null=True, blank=True)
    dbtimage_h_y2 = models.FloatField(null=True, blank=True)
    dbtcomp_str = models.FloatField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.sn

    class Meta:
        ordering = ("sn",)


class ToolSensorType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(null=True, blank=True)
    sensor_id = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class ToolInstalledSensor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    r_toolmodule_id = models.ForeignKey(ToolModule, on_delete=models.CASCADE)
    r_toolsensortype_id = models.ForeignKey(ToolSensorType, on_delete=models.CASCADE)
    record_point = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.record_point)
