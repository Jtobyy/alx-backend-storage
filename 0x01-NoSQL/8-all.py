#!/usr/bin/env python3
'''
Lists all documents in a collection
'''


def list_all(mongo_collection):
    '''Return list of documents in collection'''
    return list(mongo_collection.find())
