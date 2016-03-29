import unittest
import sys
sys.path.append(r'/home/mobigesture/Desktop/ramyasree/D.D-HTML-CODE-GEN1/python')
from validate import Val
import traceback
#from validate import Val
class simpletest_case(unittest.TestCase):
    def setUp(self):
        #setting up for the test
        pass
    def tearDown(self):
        pass
    
    def test_is_num(self):
        try:
            self.assertTrue(True,Val.is_num('num check',12))
        except:
            self.assertFalse(False,"exception raise")
            traceback.print_exc()
        
    def test_is_string(self):
        try:
            self.assertTrue(True,Val.is_string('num check','adfsk'))
        except:
            self.assertFalse(False,"exception raise")
            traceback.print_exc()
    def test_is_list(self):
        try:
            self.assertTrue(True,Val.is_list('num check',[12,32,34]))
        except:
            self.assertFalse(False,"exception raise")
            traceback.print_exc()

    def test_is_tuple(self):
        try:
            self.assertTrue(True,Val.is_tuple('num check',(12,34,21)))
        except:
            self.assertFalse(False,"exception raise")
            traceback.print_exc()

    def test_is_all(self):
        try:
            self.assertTrue(True,Val.is_all('num check',{12:1,23:3}))
        except:
            self.assertFalse(False,"exception raise")
            traceback.print_exc()

    def test_datetime(self):
        try:
            self.assertTrue(True,Val.datetime('check',"26 jan 1950"))
        except:
            self.assertFalse(False,"exception raise")
            traceback.print_exc()

    def _test_funtest(self):
        try:
            self.assertTrue(True,Val.funtest('setUp'))
        except:
            self.assertFalse(False,"exception raise")
            traceback.print_exc()

    def test_ctest(self):
        try:
            self.assertTrue(True,Val.ctest(simpletest_case))
        except:
            self.assertFalse(False,"exception raise")
            traceback.print_exc()

if __name__ == '__main__':
    unittest.main()
