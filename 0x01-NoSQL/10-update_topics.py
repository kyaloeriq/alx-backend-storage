#!/usr/bin/env python3
"""
This module defines a function to update the topics of a school document in a MongoDB collection.
"""

from pymongo import collection
from typing import List

def update_topics(mongo_collection: collection.Collection, name: str, topics: List[str]) -> None:
    """
    Updates the topics of a school document in the collection based on the given school name.
    
    :param mongo_collection: The pymongo collection object.
    :param name: The name of the school to update.
    :param topics: The list of topics to set for the school document.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
