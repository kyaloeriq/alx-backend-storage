#!/usr/bin/env python3
"""
Module that defines a function to insert a new document into a MongoDB collection.

The `insert_school` function inserts a document into the provided collection based on
the keyword arguments (`**kwargs`). It returns the `_id` of the newly inserted document.
"""

from pymongo.collection import Collection
from typing import Any

def insert_school(mongo_collection: Collection, **kwargs: Any) -> str:
    """
    Inserts a new document into the specified MongoDB collection.

    This function inserts a document into the collection using the keyword arguments
    provided. It returns the `_id` of the newly inserted document.

    Args:
        mongo_collection (Collection): The pymongo collection object. This object
        represents the collection within a MongoDB database where the document will be inserted.
        **kwargs: Arbitrary keyword arguments that represent the fields and values of the document.

    Returns:
        str: The `_id` of the newly inserted document.

    Example:
        >>> from pymongo import MongoClient
        >>> client = MongoClient('mongodb://localhost:27017/')
        >>> db = client.myDatabase
        >>> collection = db.school
        >>> new_id = insert_school(collection, name="Holberton School", address="972 Mission Street")
        >>> print(new_id)
    """
    # Insert the document into the collection and return the new document's _id
    result = mongo_collection.insert_one(kwargs)
    return str(result.inserted_id)
