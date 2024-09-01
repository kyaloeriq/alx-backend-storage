#!/usr/bin/env python3
"""
This script provides statistics about Nginx logs stored in MongoDB.

It connects to a MongoDB instance, retrieves logs from the 'nginx' collection
in the 'logs' database, and prints statistics about the logs.

Statistics include:
- Total number of logs
- Number of logs for each HTTP method (GET, POST, PUT, PATCH, DELETE)
- Number of logs with GET requests to the /status path
"""

from pymongo import MongoClient


def nginx_stats() -> None:
    """
    Retrieves and prints statistics about Nginx logs stored in MongoDB.
    The statistics are printed in a specific format:
    - First line: Total number of logs
    - Last line: Number of GET requests to the /status path
    """
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    collection = db.nginx

    # Count the total number of logs in the collection
    log_count = collection.count_documents({})
    # Define the list of HTTP methods to check
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    # Count the number of logs for each HTTP method
    method_counts = {
        method: collection.count_documents({"method": method})
        for method in methods
    }

    # Count the number of logs with GET method and /status path
    status_check = collection.count_documents(
            {"method": "GET", "path": "/status"}
            )

    # Print the total number of logs
    print(f"{log_count} logs")
    # Print the counts for each HTTP method
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")
    # Print the count of GET requests to /status
    print(f"{status_check} status check")


if __name__ == "__main__":
    nginx_stats()
