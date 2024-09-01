#!/usr/bin/env python3
"""
Module defines a function to return a list of schools having a specific topic
"""

from pymongo import collection
from typing import List, Dict


def schools_by_topic(
        mongo_collection: collection.Collection, topic: str
        ) -> List[Dict]:
    """
    Returns the list of schools having a specific topic.
    """
    schools = mongo_collection.find({"topics": topic})
    return list(schools)
