import uuid

from django.db import models


class ResourceString(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    en = models.TextField()
    ru = models.TextField()
    es = models.TextField()

    def __str__(self):
        return str(self.ru)

class Unit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_id = models.ForeignKey(ResourceString, on_delete=models.CASCADE, related_name='name')
    html_name = models.ForeignKey(ResourceString, on_delete=models.CASCADE)
    id_unisum = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.id)

class UnitSystem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_id = models.ForeignKey(ResourceString, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name_id)

class Measure(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_id = models.ForeignKey(ResourceString, on_delete=models.CASCADE)
    default_unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    id_unisum = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.name_id)

class MeasureUnit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    measure_id = models.ForeignKey(Measure, on_delete=models.CASCADE)
    unit_id = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class UnitSystemMeasureUnit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    measure_unit_id = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE)
    unit_system_id = models.ForeignKey(UnitSystem, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)