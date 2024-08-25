#!/usr/bin/env python3
"""
Module that defines a function to list all documents in a MongoDB collection.
"""

from pymongo.collection import Collection
from typing import List, Dict

def list_all(mongo_collection: Collection) -> List[Dict]:
    """
    Lists all documents in the specified MongoDB collection.
    """
    documents = mongo_collection.find()
    return list(documents) if documents.count() > 0 else []
