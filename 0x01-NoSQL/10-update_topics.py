#!/usr/bin/env python3
" Contains a function that updates a MongoDB Database "


def update_topics(mongo_collection, name, topics):
    " Changes all topics on a school document based on the name"
    mongo_collection.update_one(
            {"name": name},
            {"$set": {"topics": topics}}
            )
