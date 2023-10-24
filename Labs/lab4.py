#Lab4 Nazli Zamanian Gustavsson

#4.1 Experiment
def myTest():
    yield 1
    yield 5
    yield 6
    yield 99
a = myTest()
b = myTest()

print( a.__next__() )#1
print( a.__next__() )#5
print( b.__next__() )#1
print( b.__next__() )
print( a.__next__() )

#4.2 Task Fibbonacci
def fibbonacci(limit):
    a=0 
    b=1 
    while a<=limit:
        yield a 
        old_a=b
        old_b=a+b
        a=old_a
        b=old_b   
for i in fibbonacci(1000000):
    print(i)