#!/usr/bin/env python3
"""
This module defines a function to insert a new document into a MongoDB collection.
"""

from pymongo import collection
from typing import Any

def insert_school(mongo_collection: collection.Collection, **kwargs: Any) -> Any:
    """
    Inserts a new document into the given MongoDB collection based on the provided keyword arguments.
    
    :param mongo_collection: The pymongo collection object.
    :param kwargs: The key-value pairs to be inserted as a document.
    :return: The _id of the newly inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
