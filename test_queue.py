import myqueue
import unittest

q = myqueue.MyQueue()

class TestQueueMethods(unittest.TestCase):
    def test_newQueueIsInstance(self):
        assert(isinstance(q,myqueue.MyQueue))

    def test_newQueueIsEmpty(self):
        assert(q.isEmpty() is True)

    def test_popEmptyQueue(self):
        q.clear()
        with self.assertRaises(IndexError):
            q.pop()

    def test_pushOneItemTestSize(self):
        q.clear()
        q.push(-1)
        assert (q.size() == 1)

    def test_pushOneItemTestPopOneItem(self):
        q.clear()
        q.push(-1)
        assert (q.pop() == -1)
        
    def test_twoPushesTwoPops(self):
        q.clear()
        q.push(-1)
        q.push(1)
        firstIn = q.pop()
        lastIn = q.pop()
        assert(firstIn == -1 and lastIn == 1)
        
if __name__ == '__main__':
    unittest.main()
