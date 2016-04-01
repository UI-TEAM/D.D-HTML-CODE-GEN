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

    def _test_is_num(self):

        try:
            numbers=[1,2,3,'sree']
            for i in numbers:
                if i == len(numbers):
                    method=Val.is_num('self',numbers=i)
                    self.assertFalse(method)
                else:
                    method=Val.is_num(self,numbers=i)
                    self.assertTrue(method)


        except:
            self.assertFalse(True,self.error_message)
            traceback.print_exc()

    def _test_is_string(self):
        try:
            strings=['hi','how','are','you',89]
            for i in strings:
                if i == len(strings):
                    method=Val.is_string('strng check',strings=i)
                    self.assertFalse(method)
                else:
                    method= Val.is_string('strn check',strings=i)
                    self.assertTrue(method)

        except:
            self.assertFalse(True,self.error_message)
            traceback.print_exc()

    def _test_is_list(self):
        try:
            listing=[[1,2,3],[1],(4)]
            for i in listing:
                if i == len(listing):
                    method=Val.is_list('list check',listing=i)
                    self.assertFalse(method)
                else:
                    method = Val.is_list('list check',listing=i)
                    self.assertTrue(method)
        except:
            self.assertFalse(True,self.error_message)
            traceback.print_exc()

    def _test_is_tuple(self):
        try:
            tple=[(1,2,3),{1:1}]
            for i in tple:
                if i == len(tple):
                    method=Val.is_tuple('tuple check',tple=i)
                    self.assertFalse(method)
                else:
                    method=Val.is_tuple('tuple check',tple=i)
                    self.assertTrue(method)
        except:
            self.assertFalse(True,"exception raised")
            traceback.print_exc()

    def _test_is_all(self):
        try:

            listin=[{1:'one',2:2},(1,2,3),[1,3,5]]
            for i in listin:
                if i == len(listin):
                    method=Val.is_all('check all',listin=i)
                    self.assertFalse(method)
                else:
                    method=Val.is_all('check all',listin=i)
                    self.assertTrue(method)
        except:
            self.assertFalse(True,"exception raised")
            traceback.print_exc()

    def test_datetime(self):
        try:
            self.assertTrue(Val.datetime('date check',"26 jan 1950"))
        except:
            self.assertFalse(True,"exception raised")
            traceback.print_exc()

    def _test_funtest(self):
        try:
            print('88',self)
            self.assertTrue(Val.funtest())
        except:
            self.assertFalse(True,"exception raised")
            traceback.print_exc()

    def _test_ctest(self):
        try:
            self.assertTrue(Val.ctest(simpletest_case))
        except:
            self.assertFalse(True,"exception raised")
            traceback.print_exc()

if __name__ == '__main__':
    unittest.main()
