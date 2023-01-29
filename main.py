# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
   # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
for i in range(1, 4):
    for j in range(1, 6):
        print(j, end='')
    print('')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print("hello world")

print("Hello World")
print("hi") # string-set of characters- comment
print("the name python comes from the british comedy troope- monty python")
print("Guido Van Rossum") #ABC

#function - print() - inbuilt funcion - call
#python 3

#name - variables
name = "dhivya"
print(name)
print("name")
print("hi " + name)# concatenation
name = "dhi"
print("hi " + name)
print(1+1)
price = 45
amount = 33.2

child = False

#boolean value
#python is a dynamically typed language as we are not defining the type of the variable"

#executes from the first line of the code

# is a single line comment
''' is multiline comment
valid variable names - start with small letter after $,_, capital letter can be included like "name_01" 
invalid - (should not start with $, _,numbers) keywords
'''

#string handling

message = "hello "
name = "n1"
print(name.upper()) #invoking a classmethod

#functions perform a specified task
#shoud be within () parantheses
print(name.lower())
print(message.title())#first letter will be caps
print(message + name)#concatenate or joining string-set

print("hello \n world")
print("hello \t world")

print(len(message))#fix index to each chaacter h will be at 0th index

print(message.find("h"))#displays index

print(message.find("s"))#if its not then -1 displays or returns. The returned value is printed

print(message.count("l")) #its all inbuilt fn which displays count of l

print(message.replace("e", "r"))

print(message.isalpha())#checks whether all are alphabet

print(message.isdigit())# all are digit???. returns false if even space is there

print(message * 10)
#multiple assignments
name, age, height = "deepa", 30, 178

like = dislike = 100
print(like)

#type casting

#int,str,boolean are data types

otp = 785412

#print("ur otp is" +otp)

print("otp is " + str(otp))

print(type(otp))

otp = str(otp)
print(type(otp))

count = "20"
print(int(count)+1) #+ add bw two int and join bw two string

count = 20.5
print((float(count))+1)

quote='"poem"'
print(quote)

name = "Dhivya"
days = "15"
year = "2023"
print("Dear " + name)
print("you have " +days+ "days of leave for this\nyear " +year )
#assignments1

'''
Dear name,
You have 15 days of leave for this 
year 2023
'''

#user input

name =input("whats ur name")
print("hello " + name)

height = float( input("whats ur height"))
height_inches = "{:.2f}".format(height/2.54) #before format fn there should be a string so " "
print("u r " +str(height)+ "cm")
print("u r " +height_inches+ "inches tall")

#Math operations
a=10
b=20
print(a+b)

print(10+20)





