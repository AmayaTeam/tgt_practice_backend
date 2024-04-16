from django.core.management import BaseCommand
from api.models import *


class Command(BaseCommand):
    help = "delete_data"

    def handle(self, *args, **kwargs):
        ToolInstalledSensor.objects.all().delete()
        print("ToolInstalledSensors Deleted")
        ToolModule.objects.all().delete()
        print("ToolModules Deleted")
        ToolModuleGroup.objects.all().delete()
        print("ToolModuleGroups Deleted")
        ToolModuleType.objects.all().delete()
        print("ToolModuleType Deleted")
        ToolSensorType.objects.all().delete()
        print("ToolSensorTypes Deleted")
