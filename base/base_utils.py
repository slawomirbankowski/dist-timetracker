import datetime
from abc import abstractmethod
from dataclasses import dataclass
import uuid
import random
from random import randrange, uniform, randint
from typing import Iterable
from typing import Dict, Callable
import logging
from logging import config

application_start_date = datetime.datetime.now()
logging.config.fileConfig('logging.conf')
logging.info(f"=================================================== STARTING at {str(application_start_date)} ")
logging.info("Initializing Logging in application")
# random methods

def get_random_uid() -> str:
    return str(uuid.uuid4())

def get_random_uid_with_prefix(prefix: str) -> str:
    return prefix + "_" + str(datetime.datetime.now())[:10].replace("-", "_") + "_" + str(
        uuid.uuid4())[:13].replace("-", "_")

def get_random_uid_for_object(prefix: str, obj: any) -> str:
    return prefix + "_" + type(obj).__name__ + "_" + str(datetime.datetime.now())[:10].replace("-", "_") + "_" + str(
        uuid.uuid4())[:13].replace("-", "_")


def get_random_uid_with_name( prefix: str) -> str:
    return prefix + "_" + str(datetime.datetime.now())[:10].replace("-", "_") + "_" + str(uuid.uuid4())[:13].replace(
        "-", "_")


def get_random_int() -> int:
    return random.randint(0, 1000000)


def get_random_float() -> float:
    return random.uniform(0, 1000000)


def get_random_date() -> str:
    # TODO: generate random date and time
    return str(uuid.uuid4())
