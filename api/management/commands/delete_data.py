from django.core.management import BaseCommand
from api.models import *


class Command(BaseCommand):
    help = 'delete_data'

    def handle(self, *args, **kwargs):
        ToolModuleGroup.objects.all().delete()

