import unittest
import time
from stack.stack import stack
class stacktest(unittest.TestCase):

    def __init__(self, methodName):
        super().__init__(methodName)

    def setUp(self):
        self.start_time = time.time()
        self.stk = stack()
        self.stk.push(3)
        self.stk.push(5)

    def tearDown(self):
        t = time.time() - self.start_time
        print('%s: %.3f' % (self.id(), t))
    
    def test_push(self):
        self.stk.push(9)
        self.assertEqual(self.stk.size(), 3)

    def test_pop(self):
        self.assertEqual(self.stk.pop(), 5)

    def test_peek(self):
        self.assertEqual(self.stk.peek(), 5)

    def test_size(self):
        self.assertEqual(self.stk.size(), 2)

    def test_is_empty(self):
        self.assertEqual(self.stk.is_empty(), False)

if __name__ == '__main__':
    unittest.main()