from django.core.management import BaseCommand
from api.models import *


class Command(BaseCommand):
    help = 'delete_data'

    def handle(self, *args, **kwargs):
        ToolInstalledSensor.objects.all().delete()
        ToolModule.objects.all().delete()
        ToolModuleGroup.objects.all().delete()
        ToolSensorType.objects.all().delete()
        ToolSensorType.objects.all().delete()
