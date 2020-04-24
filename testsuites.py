from stack.stacktest import stacktest 
from queue.queuetest import queuetest 
from linkedlist.linkedlisttest import linkedlisttest 
import unittest
import HtmlTestRunner

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite1 = loader.loadTestsFromTestCase(stacktest)
    suite2 = loader.loadTestsFromTestCase(queuetest)
    suite3 = loader.loadTestsFromTestCase(linkedlisttest)
    suite = unittest.TestSuite([suite1, suite2, suite3])
    runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="test_report", add_timestamp=False)
    runner.run(suite)