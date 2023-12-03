#Lab4 Nazli Zamanian
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
print('\n')

def number_generator():
    yield 2
    yield 3
    yield 4
    yield 5
numbers= number_generator()
print(next(numbers))
print(next(numbers))
print(next(numbers))
print('\n')

#4.2 Task Fibbonacci
print("4.2 Fibbonacci using yield")
def fibbonacci(limit):
    a=0 
    b=1 #default values for fibbonaci 0+1=1, 1+1=2, 1+2=3...
    while a<=limit: 
        yield a 
        a,b= b, a+b
for i in fibbonacci(1000000):
    print(i)