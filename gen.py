#top level syntax
#top level syntax , function
from time import sleep
def add(x,y):
    return x+y
class Adder:
    def __init__(self):
        self.z=0
    def __call__ (self,x,y):
        return x+y+self.z
ad2=Adder()

def compute():
    rv=[]
    for i in range(10):
        sleep(.5)
        rv.append(i)
    return rv
class compute_class:
    def __call__ (self):
        rv=[]
        for i in range (99999):
            sleep(5)
            rv.append(i)
        return rv
    def __iter__(self):
        self.last=0
        return self
    def __next__(self):
        rv=self.last
        self.last+=1
        if self.last > 10 :
            raise StopIteration()
        sleep(.5)
        return rv
#for val in compute_class():
#    print(val)

def computet2():
    for i in range(10):
        sleep(.5)
        yield i
computet2()

def api:
    def run_this_first(self):
        first()
    def run_this_second(self):
        second()
    def run_this_last(self):
        last()
#generator
def api():
    first()
    yield
    second()
    yield
    last()
