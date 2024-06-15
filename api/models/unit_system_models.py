import uuid

from django.db import models


class ResourceString(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    en = models.TextField(null=True, blank=True)
    ru = models.TextField(null=True, blank=True)
    es = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.ru)


class Unit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.ForeignKey(
        ResourceString, on_delete=models.CASCADE, related_name="name", null=True, blank=True
    )
    html_name = models.ForeignKey(ResourceString, on_delete=models.CASCADE, null=True, blank=True)
    id_unisum = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.name.ru)


class UnitSystem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.ForeignKey(ResourceString, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name.ru)


class Measure(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.ForeignKey(ResourceString, on_delete=models.CASCADE)
    default_unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True, blank=True)
    id_unisum = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.name.ru)


class MeasureUnit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    measure = models.ForeignKey(Measure, on_delete=models.CASCADE, null=True, blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class UnitSystemMeasureUnit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE)
    unit_system = models.ForeignKey(UnitSystem, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class ConversionFactor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    from_unit = models.ForeignKey(
        Unit, on_delete=models.CASCADE, related_name="from_units"
    )
    to_unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="to_units")
    factor_1 = models.FloatField(null=True, blank=True)
    factor_2 = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(f"{self.factor_1} {self.factor_2}" "")
