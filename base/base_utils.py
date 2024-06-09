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
from base.base_constants import SystemVersions

# random methods


def get_ver() -> str:
    return SystemVersions.Latest


def get_random_uid() -> str:
    return str(uuid.uuid4())


def get_random_uid_with_prefix(prefix: str) -> str:
    return prefix + "_" + str(datetime.datetime.now())[:10].replace("-", "_") + "_" + str(
        uuid.uuid4())[:13].replace("-", "_")


def get_random_uid_long_with_prefix(prefix: str) -> str:
    return prefix + "_" + str(datetime.datetime.now())[:19].replace("-", "_").replace(":", "_").replace(" ", "_") + "_" + str(
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


def tuple_to_dict(tup: tuple) -> dict:
    di = {}
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di

def create_object_by_class() -> any:
    #globals()[class_name]
    try:
        #type(class_name)()
        return "" # eval(class_name)
    except:
        return None


def create_empty_list() -> list:
    return []


def create_empty_tuple() -> tuple:
    return ()
