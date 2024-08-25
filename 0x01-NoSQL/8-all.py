#!/usr/bin/env python3
"""
Module that defines a function to list all documents in a MongoDB collection.
This function will return a list of all documents found in the provided collection.
If the collection is empty, an empty list will be returned.
"""

from pymongo.collection import Collection
from typing import List, Dict

def list_all(mongo_collection: Collection) -> List[Dict]:
    """
    Lists all documents in the specified MongoDB collection.

    This function connects to the provided MongoDB collection and retrieves all
    documents stored in that collection. If the collection is empty, it returns
    an empty list.

    Args:
        mongo_collection (Collection): The pymongo collection object. This object
        represents the collection within a MongoDB database from which documents
        will be retrieved.

    Returns:
        List[Dict]: A list of dictionaries, where each dictionary corresponds
        to a document in the collection. If the collection contains no documents,
        the function returns an empty list.

    Example:
        >>> from pymongo import MongoClient
        >>> client = MongoClient('mongodb://localhost:27017/')
        >>> db = client.myDatabase
        >>> collection = db.school
        >>> documents = list_all(collection)
        >>> for doc in documents:
        >>>     print(doc)
    """
    # Retrieve all documents from the collection using the find() method
    documents = mongo_collection.find()

    # Convert the cursor to a list and return it, or return an empty list if no documents are found
    return list(documents)
