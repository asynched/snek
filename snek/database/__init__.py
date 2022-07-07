from typing import Any, Mapping
from pymongo import MongoClient
from pymongo.database import Database

from snek.validators.decorators import Validator


class Model:
    validator: Validator = None
    __meta_database__: Database = None
    __meta_collection__: str = None

    def insert(document: Mapping[str, Any]):
        ...

    def find(*args, **kwargs):
        ...

    def update_one(filter: Mapping[str, Any], update: Mapping[str, Any]):
        ...

    def update_many(filter: Mapping[str, Any], update: Mapping[str, Any]):
        ...

    def delete_one(filter: Mapping[str, Any]):
        ...

    def delete_many(filter: Mapping[str, Any]):
        ...
