import time
import collections
from dateutil.parser import parse 
def is_num(numbers):
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
is_num()
def is_string(strings):
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

is_string("")

def is_list(listin):
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
is_list([])

def datetime(dtime):
    try:
        parse(dtime)
        print(dtime)
        return True
    except ValueError:
        print('valueerror')
        return False
datetime('20132')

def funtest():
    print(type(funtest))
    isinstance(funtest,collections.Callable)
    return True
funtest()
"""
def ctest():
    import inspect
    inspect.isclass("classname")
ctest()
"""
