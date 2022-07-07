from typing import Any, Mapping
from pymongo.database import Database


def Collection(database: Database):
    def decorate(classDef):
        classDef.__meta_collection__ = classDef.__name__
        classDef.__meta_database__ = database

        def insert(document: Mapping[str, Any]):
            database = classDef.__meta_database__
            collection_name = classDef.__meta_collection__

            if classDef.validator is not None:
                classDef.validator.validate(
                    classDef.validator, classDef.__name__, document
                )

            return database.get_collection(collection_name).insert_one(document)

        def find(*args, **kwargs):
            database = classDef.__meta_database__
            collection_name = classDef.__meta_collection__

            return database.get_collection(collection_name).find(*args, **kwargs)

        def update_one(filter: Mapping[str, Any], update: Mapping[str, Any]):
            database = classDef.__meta_database__
            collection_name = classDef.__meta_collection__

            return database.get_collection(collection_name).update_one(filter, update)

        def update_many(filter: Mapping[str, Any], update: Mapping[str, Any]):
            database = classDef.__meta_database__
            collection_name = classDef.__meta_collection__

            return database.get_collection(collection_name).update_many(filter, update)

        def delete_one(filter: Mapping[str, Any]):
            database = classDef.__meta_database__
            collection_name = classDef.__meta_collection__

            return database.get_collection(collection_name).delete_one(filter)

        def delete_many(filter: Mapping[str, Any]):
            database = classDef.__meta_database__
            collection_name = classDef.__meta_collection__

            return database.get_collection(collection_name).delete_many(filter)

        classDef.insert = insert
        classDef.find = find
        classDef.update_one = update_one
        classDef.update_many = update_many
        classDef.delete_one = delete_one
        classDef.delete_many = delete_many

        return classDef

    return decorate
