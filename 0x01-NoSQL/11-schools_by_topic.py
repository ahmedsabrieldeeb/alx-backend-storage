#!/usr/bin/env python3
""" NoSQL Project """


def schools_by_topic(mongo_collection, topic):
    """
    returns the list of school having a specific topic

    Args:
        mongo_collection: the pymongo collection object
        topic: topic searched

    Returns:
        list of schools having a specific topic
    """
    return mongo_collection.find({"topics": {"$in": [topic]}})
