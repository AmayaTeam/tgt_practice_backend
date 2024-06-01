import uuid
from django.db import models
from .tool_models import ToolModule

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