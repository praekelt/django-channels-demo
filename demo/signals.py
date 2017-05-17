from django.core import serializers
from django.db.models.signals import post_save
from django.dispatch import receiver
from demo.models import Article
from demo.constants import SUBSCRIBER_GROUP_NAME

from channels import Group


@receiver(post_save, sender=Article)
def publish(sender, instance, created, **kwargs):
    """
    We publish new articles to the subscriber group.
    :param sender: The sender class (Article in this case, because of the 
    filter applied in the @receiver decorator)
    :param instance: The Article instance that was saved
    :param created: A flag indicating whether the instance was created, 
    or already existed.
    :param kwargs: Miscellaneous keyword arguments
    """
    if created:
        Group(SUBSCRIBER_GROUP_NAME).send({
            "text": serializers.serialize("json", [instance])
        })