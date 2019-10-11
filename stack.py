class Stack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not self.items

    def size(self):
        return len(self.items)

    def pop(self):
        if not self.isEmpty():
            item = self.items.pop(0)
            return item
        else:
            raise IndexError('stack is empty')

    def push(self, item):
        self.items.insert(0,item)

    def clear(self):
        self.items = []

    
