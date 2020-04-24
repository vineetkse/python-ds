import unittest
import time
from queue.queue import queue
class queuetest(unittest.TestCase):

    def __init__(self, methodName):
        super().__init__(methodName)

    def setUp(self):
        self.start_time = time.time()
        self.que = queue()
        self.que.enqueue(3)
        self.que.enqueue(5)

    def tearDown(self):
        t = time.time() - self.start_time
        print('%s: %.3f' % (self.id(), t))
    
    def test_enqueue(self):
        self.que.enqueue(9)
        self.assertEqual(self.que.size(), 3)

    def test_dequeue(self):
        self.assertEqual(self.que.dequeue(), 3)

    def test_size(self):
        self.assertEqual(self.que.size(), 2)

    def test_is_empty(self):
        self.assertEqual(self.que.is_empty(), False)

if __name__ == '__main__':
    unittest.main()