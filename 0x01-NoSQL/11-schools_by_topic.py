#!/usr/bin/env python3
" Contains a function that returns a list of school "


def schools_by_topic(mongo_collection, topic):
    " Returns a list of school having a specific topic "
    return list(mongo_collection.find({"topics": topic}))
