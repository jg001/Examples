"""
main.py

implements a collection of objects based
on factory method 

"""

import my_collections

factory = my_collections.CollectionsFactory()

# using queue (vs stack)
collection = factory.get_collection('Queue')

print('Queue : pushing 1, then 2')

collection.push(1)
collection.push(2)

print('pop twice')
print(collection.pop())  # the 1 was first
print(collection.pop())  # then the 2


# using stack
collection = factory.get_collection('Stack')

print('\nStack : pushing 1 then 2')

collection.push(1)
collection.push(2)

print('pop twice')
print(collection.pop())  # the 2 was last
print(collection.pop())  # then the 1