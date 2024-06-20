#!/usr/bin/env python3
""" NoSQL Project """


def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document in a collection based on kwargs

    Args:
        mongo_collection: the pymongo collection object
        kwargs: key-value pairs to be inserted in the document

    Returns:
        the new _id
    """
    return mongo_collection.insert_one(kwargs).inserted_id
