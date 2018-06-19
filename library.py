##metaclases
class BaseMeta(type):
    def __new__(cls,name,bases,body):
        if not 'bar' in body:
            raise TypeError("bad users class")
        print('basemetta.__new__',cls,name,bases,body)
        return super().__new__(cls,name,bases,body)

class Base(metaclass=BaseMeta):
    def foo(self):
        def foo(self):
            return self.bar()
        def __init_subclass__(self,*a ,**kw):
            print ('init_subclas_',a,kw)
            return super().__init_subclass__(cls,*a,**kw)
#old_bc = __build_class__
#def my_bc(fun,name,bases=None, ** kw):
#    if bases is Base:
#        print ('check if bar method defined')
#    if base is not None:
#        return old_bc(fun,name,base,**kw)
#    return old_bc(fun,name,**kw)
#import builtins
#builtins.__build_class__= my_bc
