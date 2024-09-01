#!/usr/bin/env python3
"""
This script provides statistics about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient

def nginx_stats():
     """
    Retrieves and prints statistics about Nginx logs stored in MongoDB.
    """
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    collection = db.nginx

    # Count the total number of logs
    log_count = collection.count_documents({})

    # Count the number of logs for each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents({"method": method}) for method in methods}

    # Count the number of logs for GET requests to /status
    status_check = collection.count_documents({"method": "GET", "path": "/status"})

    # Output the statistics
    print(f"{log_count} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")
    print(f"{status_check} status check")

if __name__ == "__main__":
    nginx_stats()
