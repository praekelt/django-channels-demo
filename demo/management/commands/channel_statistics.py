import importlib
from pprint import pprint

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from channels.asgi import get_channel_layer

class Command(BaseCommand):
    help = "Display Django channels global statistics"

    def handle(self, *args, **kwargs):
        layer = get_channel_layer()
        if "statistics" in layer.extensions:
            pprint(layer.global_statistics())
        else:
            print("The statistics extension is not supported")

        pprint(dir(layer))
