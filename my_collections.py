"""
myCollections.py

uses a CollectionsFactory to return the proper collection
type to the caller

"""

import stack, myqueue

class CollectionsFactory:
    def get_collection(self, collection):
        if collection == 'Stack':
            return stack.Stack()
        elif collection == 'Queue':
            return myqueue.MyQueue()
        else:
            raise ValueError(collection)

        