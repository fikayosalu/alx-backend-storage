#!/usr/bin/env python3
""" Contains a function that inserts a document in MongoDB
using pymongo """


def insert_school(mongo_collection, **kwargs):
    """ This function is used to insert a document in a collection
    and returns the id of the inserted document """
    item = mongo_collection.insert_one(kwargs)
    return item.inserted_id
