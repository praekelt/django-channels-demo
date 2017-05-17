import json
import logging

from django.core import serializers
from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http

from demo.constants import SUBSCRIBER_GROUP_NAME
from demo.models import Article

logger = logging.getLogger()


@channel_session_user_from_http
def ws_connect(message):
    """
    A user connecting via websocket is sent the latest N articles and added to
    the subscriber group.
    :param message: 
    :return: 
    """
    logger.debug("User '{}' connected via websocket".format(
        message.user.username))

    # Send the last 5 articles to the user
    message.reply_channel.send({
        "text": serializers.serialize("json",
            reversed(Article.objects.all().order_by("-id")[:5])
        )
    })
    # Add the user to the subscriber group
    Group(SUBSCRIBER_GROUP_NAME).add(message.reply_channel)


@channel_session_user
def ws_disconnect(message):
    """
    A user disconnected from the websocket is removed from the subscriber group.
    :param message: 
    :return: 
    """
    logger.debug("User '{} disconnected from websocket".format(
        message.user.username))
    Group(SUBSCRIBER_GROUP_NAME).discard(message.reply_channel)
