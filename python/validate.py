import time
import types
import collections
from dateutil.parser import parse 
class Val(object):

    def is_num(self,numbers):
        try:
            if type(numbers) == int:
                print("its a number of  integer",numbers,type(numbers))
                return True
            elif type(numbers) == float:
                print("its float",numbers)
                return True
            elif type(numbers) == complex :
                print("its complex",numbers)
                return True
            else:
                print(numbers,"not a num")
                return False
        except:
            raise

    def is_string(self,strings):
        try:
            if type(strings) == str:
                if len(strings) > 0:
                    print('its a string',strings,bool(str(strings)),type(strings))
                    return True
                elif len(strings) == 0 or strings == " ":
                    print("empty")
                    return False
            else:
                print("not a string")
                return False

        except:
            raise
    
    def is_list(self,listing):
        if type(listing) is list:
            if len(listing) == 0:
                print("list empty")
                return False
            else:
                print(' its a list',listing,bool(str(listing)))
                return True

    def is_tuple(self,tple):
        if type(tple) is tuple:
            if len(tple) > 0:
                print(' its a tuple',tple, bool(str(tple)) ,type(tple))
                return True
            else:
                print("empty",self)
                return False
    
    def is_all(self,listin):
        if type(listin) is list:
            if len(listin) == 0:
                print("list empty",listin,type(listin))
            else:
                print(" it's a list",listin,bool(type(listin)),type(listin))
                return True
        elif type(listin) is tuple:
            if len(listin) == 0:
                print("tuple is empty",listin,type(listin))
            else:
                print("it's a tuple",listin,bool(type(listin)))
                return True
        elif type(listin) is dict:
            if len(listin) == 0:
                print("dict is empty",listin)
            else:
                print("it's a dict",listin,bool(type(listin)))
                return True
        else:
            return False
    def datetime(self,dtime):
        try:
            parse(dtime)
            print('its a date',dtime,self)
            return True
        except ValueError:
            print('valueerror',self)
            return False
    
    def funtest(self):
        try:
            from inspect import isfunction
            print('*****',isfunction(self),self)
            if isfunction(self) == False:
                print('its a function',type(self),self)
            else:
                print('its not a function')
                
            #print(bool(str(isinstance(self,types.FunctionType))),'its function')
        except NameError:
            print('its not correct fun name')
            raise


    def ctest(self):
        try:
            import inspect
            if inspect.isclass(Val):
                print('its a class ',bool(str(Val)),Val,self)
                return True
            else:
                print('not a class',self)
                return False
        except NameError:
            print("please give valid class name")
