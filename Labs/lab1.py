#print("Hello, world!")

#1.3.1 Test questions on number
#1 

result= 15*" spam " #prints out 15 spams
a = [10,90,32,43,54,5,6,7]
r = a
s = a[0:3]
t = a[:]
a[0] = 99

print(r) #r will be 99 both a and r point to [0] of the array.
print(s) #s will be from index[0] to index[3].
print(t)#creates a new cooy of the list. 
# (a) What is then r ?
# (b) What is then s ?
# (c) What is then t ? 

# 1.3.4 Test questions on First steps...
# 1. Assume that a och b are two variables. What does the following statement do?
# a,b = b,a a on the left side is given the value b from the rightside of the =. 
# 2. Write a while-loop that prints all integers between 1 and 9 on the
def while_loop():
    a=1 
    while a<=9:
        print(a)
        a+=1
while_loop()
    

# 1.4.2 for-statement
# 1. Assume that animal = ["dog, "cat", "elefant"]. Write a
# for-statement that prints all elements of animal!

def animal():
    animals = ["dog", "cat", "elefant"]
    for animal in animals:
        print(animal)
animal()
