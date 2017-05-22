import logging
import json
from datetime import timedelta
from celery.task import periodic_task
from celery.schedules import crontab
from channels import Group

from .constants import SUBSCRIBER_GROUP_NAME

logger = logging.getLogger()


@periodic_task(run_every=timedelta(seconds=10), ignore_result=True)
def ping():
    logger.debug("ping")
    Group(SUBSCRIBER_GROUP_NAME).send({"text": json.dumps({"ping": True})})
