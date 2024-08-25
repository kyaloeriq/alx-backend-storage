#!/usr/bin/env python3
"""
Module that defines a function to list all documents in a MongoDB collection.
"""

from pymongo.collection import Collection
from typing import List, Dict

def list_all(mongo_collection: Collection) -> List[Dict]:
    """
    Lists all documents in the specified MongoDB collection.

    Args:
        mongo_collection (Collection): The pymongo collection object.

    Returns:
        List[Dict]: A list of all documents in the collection.
                    Returns an empty list if no documents are found.
    """
    documents = mongo_collection.find()
    return list(documents) if documents.count() > 0 else []
