import unittest
from linkedlist.linkedlist import linkedlist
import time

class linkedlisttest(unittest.TestCase):
    def __init__(self, methodName):
        super().__init__(methodName)

    def setUp(self):
        self.start_time = time.time()
        self.sll = linkedlist()
        self.sll.prepend(3)
        self.sll.prepend(5)

    def tearDown(self):
        t = time.time() - self.start_time
        print('%s: %.3f' % (self.id(), t))

    def test_size(self):
        self.assertEqual(self.sll.size(), 2)

if __name__ == '__main__':
    unittest.main()