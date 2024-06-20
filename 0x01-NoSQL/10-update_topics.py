#!/usr/bin/env python3
""" NoSQL Project """


def update_topics(mongo_collection, name, topics):
    """
    Function that changes all topics of a school document based on the name

    Args:
        mongo_collection: pymongo collection object
        name: (string) the school name to update
        topics: (list of strings) the list of topics approached in the school

    Returns:
        Nothing
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
