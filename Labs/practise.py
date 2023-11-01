#practise 
age =20
price =19.5
first_name ="nazli"
print(first_name)
#case sensative, dont neeed datatypes, reads from up to do
# 3 types of data: numbers ,strings and booleans 
new_patient ="john smith"
#name =input("What is your name?")
#print("Hello" + name)

#birth_year= input("Enter  birthyear")
#int(birth_year) #translate birth_year to an int
#age= 2023-int(birth_year)
#print(age)

first =input("First: ") #input return a string
sec= input("Seccond: ")
sum=float(first)+float(sec)
print(sum)

file_path="score2.txt"
with open(file_path, 'r') as file:
    contents=file.read()
    print(contents)
    