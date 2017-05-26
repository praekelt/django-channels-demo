import importlib
from pprint import pprint

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Display Django channels global statistics"

    def handle(self, *args, **kwargs):
        backend_class_path = settings.CHANNEL_LAYERS["default"]["BACKEND"]
        module_name, class_name = backend_class_path.rsplit(".", 1)
        module = importlib.import_module(module_name)
        klass = getattr(module, class_name)
        instance = klass()
        pprint(instance.global_statistics())
        print("Global statistics expiry: {}".format(
            instance.global_statistics_expiry)
        )

