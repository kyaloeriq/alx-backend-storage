#!/usr/bin/env python3
"""
This module defines a function to list all documents in a MongoDB collection.
"""

from pymongo import collection

def list_all(mongo_collection: collection.Collection) -> list:
    """
    Lists all documents in the given MongoDB collection.
    
    :param mongo_collection: The pymongo collection object.
    :return: A list of all documents in the collection. Returns an empty list if no documents are found.
    """
    documents = list(mongo_collection.find())
    return documents if documents else []
