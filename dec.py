#run time life for a class in python
#from insepctt import getsource
#from insepctt import getfile[
##from insepctt import getline
#getsource(add)
from time import time
def timer1(func,x,y):
    before=time()
    rv=func(x,y)
    after =time()
    print ('a little better', after-before )
    return rv
def timer2(func):
    def f(*args,** kwargs):
        before=time()
        rv=func(*args,** kwargs)
        after =time()
        print ('a little better', after-before )
        return rv
    return f
def ntimes(n):
    def inner(f):
        def wrapper(*args,** kwargs):
            for _ in range(n):
                print ('running {.__name__} '.format(f) )
                rv = f(*args,** kwargs)
            return rv
        return wrapper
    return inner

def add (x,y=10):
    before =time()
    rv= x+y
    after =time()
    print ('time for run ', after- before)
    return x + y

@timer2
def sub (x,y=10):
    return x - y
#sub = timer2(sub)
@ntimes(5)
def multi(x,y):
    return x*y
print ('add (10)',add(10))
print('add(20,30)',timer1(add,20,30))
print('add("a","b")',add("a","b"))
print('sub("a","b")',sub(30,40))
print('multi("a","b")',multi(30,40))
