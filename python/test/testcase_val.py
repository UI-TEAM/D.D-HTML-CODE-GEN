import unittest
from python.validate import Val
import traceback

class simpletest_case(unittest.TestCase):
    my_fun_map={
    'test_is_num':'is_num',
    'test_is_string' : 'is_string',
    'test_is_list':'is_list',
    'test_is_tuple':'is_tuple',
    'test_is_all':'is_all',
    'test_datetime':'datetime',
    'test_funtest':'funtest',
    'test_ctest':'ctest'

}

    def setUp(self):
        test_method= self.id()
        test_method= test_method.split('.')[-1]
        #self.vari=my_fun_map.get(test_method)
        self.error_message = 'No values found for "%s" method.' %test_method
        #setting up for the test
        pass
    def tearDown(self):
        pass

    def test_is_num(self):

        try:
            method=Val.is_num('self',numbers=1)
            self.assertTrue(method)

        except:
            self.assertFalse(True,self.failureException)
            #self.assertFalse(False,"exception raise")
            traceback.print_exc()
            #self.assertTrue()
            raise self.failureException
    def test_is_string(self):
        try:
            self.assertTrue(True,Val.is_string('string check','adfsk'))

        except:
            self.assertFalse(False,"exception raise")
            traceback.print_exc()
    def test_is_list(self):
        try:
            self.assertTrue(True,Val.is_list('list check',[12,32,34]))
        except:
            self.assertFalse(False,"exception raise")
            traceback.print_exc()

    def test_is_tuple(self):
        try:
            self.assertTrue(Val.is_tuple('to check tuple',(12,34,21)),self.error_message)
        except:
            self.assertFalse(True,"sree")
            traceback.print_exc()

    def test_is_all(self):
        try:

            self.assertTrue(Val.is_all('all at once ',{12:1,23:3}))
        except:
            self.assertFalse(True,"exception raise")
            traceback.print_exc()

    def test_datetime(self):
        try:
            self.assertTrue(Val.datetime('date check',"26 jan 1950"))
        except:
            self.assertFalse(True,"exception raise")
            traceback.print_exc()

    def _test_funtest(self):
        try:
            self.assertTrue(Val.funtest('setUp'))
        except:
            self.assertFalse(True,"exception raise")
            traceback.print_exc()

    def test_ctest(self):
        try:
            self.assertTrue(Val.ctest(simpletest_case))
        except:
            self.assertFalse(True,"exception raise")
            traceback.print_exc()

if __name__ == '__main__':
    unittest.main()
