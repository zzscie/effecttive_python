from sqlite3 import connect
from contextlib import contextmanager
#with open ('gen.py') as f:
#    pass
@contextmanager
def temptable(cur):
    cur.execute('create table points(x int, y int)')
    try:
        yield
    finally:
        cur.execute('drop table points')
'''
class conetextmanager:
    def __init__(self,cur):
        self.cur=cur
    def __enter__(self):
        self.gen=temptable(self.cur)
        next(self.gen)
    def __exit__(self, *args):
        next(self.gen,None)
'''
with connect('test.db') as conn:
     cur= conn.cursor()
     with temptable(cur):
         #cur.execute('create table points(x int, y int)')
         cur.execute('insert into points (x, y) values(1,1)')
         cur.execute('insert into points (x, y) values(1,2)')
         cur.execute('insert into points (x, y) values(2,1)')
     for row in cur.execute('select x,y from points'):
         print(row)
     for row in cur.execute('select sum (x*y) from points'):
         print(row)
     cur.execute('drop table points')
