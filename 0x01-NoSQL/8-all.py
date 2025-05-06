#!/usr/bin/env python3
""" This script uses pymongo to query a database """


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Args:
    mongo_collection: pymongo collection object

    Returns: A list of documents,
    or an empty list if no documents exist.
    """
    return list(mongo_collection.find())
