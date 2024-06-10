import uuid

from django.contrib.auth.models import User
from django.db import models

from .unit_system_models import UnitSystem


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    unitsystem_id = models.ForeignKey(UnitSystem, on_delete=models.CASCADE)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    language = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.user_id