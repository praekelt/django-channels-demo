import json
import logging

from django.core import serializers
from channels import Group
# Use the following decorators if you want to add user information to the
# websocket messages.
from channels.auth import channel_session_user, channel_session_user_from_http

from demo.constants import SUBSCRIBER_GROUP_NAME
from demo.models import Article

logger = logging.getLogger()

# Rough estimator of the subscriber pool
SUBSCRIBER_COUNT = 0

# Convenient switch for disabling authentication checks, predominantly for
# use with the Tsung load tests.
REQUIRES_AUTHENTICATION = False


@channel_session_user_from_http
def ws_connect(message):
    """
    A user connecting via websocket is sent the latest N articles and added to
    the subscriber group.
    :param message: 
    :return: 
    """
    if not REQUIRES_AUTHENTICATION or message.user.is_authenticated:
        global SUBSCRIBER_COUNT
        # Send the last 5 articles to the user
        message.reply_channel.send({
            "text": serializers.serialize(
                "json", reversed(Article.objects.all().order_by("-id")[:5])
            )
        })
        # Add the user to the subscriber group
        Group(SUBSCRIBER_GROUP_NAME).add(message.reply_channel)
        SUBSCRIBER_COUNT += 1
        print("Connect: Group size = {}".format(SUBSCRIBER_COUNT))
        message.reply_channel.send({"accept": True})
    else:
        message.reply_channel.send({"close": True})


@channel_session_user
def ws_disconnect(message):
    """
    A user disconnected from the websocket is removed from the subscriber group.
    :param message: 
    :return: 
    """
    if not REQUIRES_AUTHENTICATION or message.user.is_authenticated:
        global SUBSCRIBER_COUNT
        Group(SUBSCRIBER_GROUP_NAME).discard(message.reply_channel)
        SUBSCRIBER_COUNT -= 1
        print("Disconnect: Group size = {}".format(SUBSCRIBER_COUNT))
    else:
        message.reply_channel.send({"close": True})


@channel_session_user
def ws_receive(message):
    if not REQUIRES_AUTHENTICATION or message.user.is_authenticated:
        if "text" in message.content:
            data = json.loads(message.content["text"])
            print("Someone said: '{}'".format(data["greeting"]))
    else:
        message.reply_channel.send({"close": True})
