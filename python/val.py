import time
import types
import collections
from dateutil.parser import parse 
class Val(object):
    def is_num(self,numbers):
        print(numbers)
        print(type(numbers))
        if type(numbers) == int:
            print("its integer",numbers)
            return True
        elif type(numbers) == float:
            print("its float",numbers)
            return True
        elif type(numbers) == complex :
            print("its complex",numbers)
            return True
#    elif type(numbers) == __pow__():
#        import unicodedata
#        unicodedata.numberic(numbers)
#        return True
        else:
            return False
#is_num()
    def is_string(self,strings):
        print(strings)
        try:
            if type(strings) == str:
                print("its a string",strings)
                if len(strings) > 0:
                    print(strings,bool(str(strings)))
                    return True
                elif len(strings) == 0 or strings == "":
                    print("empty")
                    return False
        except ValueError:
            raise
    
    def is_list(self,listing):
        if type(listing) is list:
            if len(listing) == 0:
                print("list empty")
                return False
            else:
                print(listing,bool(str(listing)))
                return True

    def is_tuple(self,tple):
        if type(tple) is tuple:
            if len(tple) > 0:
                print(tple, bool(str(tple)) )
                return True
            else:
                print("empty")
                return False
    
    def is_all(self,listin):
        print(listin)
        if type(listin) is list:
            if len(listin) == 0:
                print("list empty")
            else:
                print("yes, it's a list",listin,bool(type(listin)))
                return True
        elif type(listin) is tuple:
            if len(listin) == 0:
                print("tuple is empty")
            else:
                print("yes it's a tuple",listin,bool(type(listin)))
                return True
        elif type(listin) is dict:
            if len(listin) == 0:
                print("dict is empty")
            else:
                print("yes it's a dict",listin,bool(type(listin)))
                return True
    def datetime(self,dtime):
        try:
            parse(dtime)
            print(dtime)
            return True
        except ValueError:
            print('valueerror')
            return False
    
    def funtest(self):
        try:
            print(bool(str(isinstance(self,types.FunctionType))),'its function')
        except NameError:
            print('its not correct fun name')
            raise


    def ctest(self):
        print('class test')
        try:
            import inspect
            if inspect.isclass(Val):
                print(bool(str(Val)),Val)
                return True
            else:
                print('not a class')
                return False
        except NameError:
            print("please give valid class name")

            


v=Val()
v.is_num(12)
v.is_string('er')
v.is_list([132,452,435])
v.is_tuple((1234,452,356))
v.datetime('24 March 2016')
v.funtest()
v.is_all([])
v.ctest()
