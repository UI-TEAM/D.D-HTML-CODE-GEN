import unittest
from python.validate import Val
import traceback
class simpletest_case(unittest.TestCase):

    def setUp(self):

        #test_method= self.id()
        #test_method= test_method.split('.')[-1]

        #setting up for thet
        pass
    def tearDown(self):
        pass

    def test_is_num(self):
        try:
            method=Val.is_num('num check',numbers='123')
        except:
            traceback.print_exc()
            raise

if __name__ == '__main__':
    unittest.main()