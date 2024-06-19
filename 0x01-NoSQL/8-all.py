#!/usr/bin/env python3
""" NoSQL Project """


def list_all(mongo_collection):
    """
    list all documents in a collection

    Args:
        mongo_collection: pymongo collection object

    Returns:
        Empty list if no document in the collection
        Otherwise, a list of documents in the collection
    """
    if mongo_collection is None:
        return []

    return list(mongo_collection.find())
