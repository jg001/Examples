import stack
import unittest

s = stack.Stack()

class Test_StackMethods(unittest.TestCase):

    def test_newStackIsInstance(self):
        assert(isinstance(s,stack.Stack))

    def test_newStackIsEmpty(self):
        assert(s.isEmpty() is True)

    def test_popEmptyStack(self):
        s.clear()
        with self.assertRaises(IndexError):
            s.pop()

    def test_pushOneItemTestSize(self):
        s.clear()
        original_size = s.size()
        s.push(-1)
        assert (s.size() - original_size == 1)

    def test_pushOneItemTestPopOneItem(self):
        s.clear()
        s.push(-1)
        assert (s.pop() == -1)

    def test_pushTwoItemsPopTwoItems(self):
        s.clear()
        s.push(-1)
        s.push(1)
        assert(s.pop() == 1 and s.pop() == -1)

if __name__ == '__main__':
    unittest.main()
