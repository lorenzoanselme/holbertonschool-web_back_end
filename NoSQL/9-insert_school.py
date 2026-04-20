#!/usr/bin/env python3
"""Module that inserts a new document in a MongoDB collection."""


def insert_school(mongo_collection, **kwargs):
    """Insert a new document in a collection and return its new id."""
    return mongo_collection.insert_one(kwargs).inserted_id
