import math
import random
#import pandas as pd

print('Hello World')
# operators
print(1 + 1)
a = 10
b = 10
print(a + b)
print(a - b)
print(a * b)
print(a / b)
a = 8.98
print(round(a))
a = -5
print(abs(a))

print(pow(a, 3))
print(a ** 2)  # for power

print(max(a, b))
print(min(a, b))

print(math.ceil(a))  # rounds to next integer
print(math.floor(a))  # rounds to integer

print(math.factorial(9))
a = 2
print(a % 2)  # modulus operator

# ifelse
pwd_correct = True

if pwd_correct:
    print("Logged In")

else:
    print("wrong password")

num = 10
if num > 1:
    print("true")
    # relational operators  >, <, <=, >=, ==, !=

if num % 10 == 0:
    print(str(num) + "is multiple of 10")

else:
    print(str(num) + "is not multiple of 10")

    # ifelse ladder
ind_score = 360

if ind_score >= 350:  # note if statement should be given  at the starting of line otherwise it will show u error
    print("India will win")
elif ind_score >= 250:
    print("India might win")
elif ind_score >= 150:
    print("Aus might win")
else:
    print("Aus will win")

# nested if
num = int(input("enter a num:"))

if num > 99 and num < 1000:  # or else if num>99 and num<1000 and num % 2 == 0:
    if num % 2 == 0:
        print(str(num) + "is a three digit even number")
    else:
        print(str(num) + "is a three digit even number")

# bitwise operators

# & and
# | OR
# ~ NOT, << LEFT SHIFT(value doubled), >> RIGHT SHIFT(half reduced)
a = 12
b = 14
print(12 << 1)

print(12 >> 1)

print(a & b)

#  a  b      and   or  exor
#  0  0       0    0     0
#  0  1       0    1     1
#  1  0       0    1     1
#  1  1       1    1     0

# string slicing

name = "Logic First"

#  L   O   G   I   C    F  I  R  S  T
#  0   1   2   3  4  5  6  7  8  9  10
# -11 -10 -9 -8 -7 -6 -5 -4 -3 -2  -1

print(name[3])

print(name[0:4])

print(name[:4])

print(name[2:4])

print(name[2:])

print(name[2:10:2])  # skips 2 character str[start:stop:step]

print(name[-5:-2])

print(name[-2:-5:-1])

print(name[::-1])  # prints reverse

print(name[:-3:-1])

print(name[2:-2])

# using slice classmethod

x = slice(2, -2)
print(name[x])

# lists
cities = ["Chennai", "Madurai", "Trichy", "coimbatore", "salem"]
val = [3, 5, 6, 3, 2, 9]
list1 = ["Chennai", 3, "Salem"]

# Accessing list with indexing
print(cities[0])
print(val[2])
print(cities[:3])

# negative indexing

print(cities[-2])

print(cities[::2])
print(val)
print(cities[::])
print(cities[::1])
print(cities[::-1])

# modify
cities[2] = "Tiruchy"
print(cities)

# append - adding at the end
cities.append("karur")  # should be declared within double quotes in list for strings
# takes exactly one argument
print(cities)

# insert
cities.insert(3, "tanjore")  # does not return any value
print(cities)

# delete
del cities[3]
print(cities)

# Remove using pop() to identify which element has been deleted. It returns some value
deleted = cities.pop(2)  # delete 2nd value in list which returns value
print(deleted + "has been deleted")
print(cities)

# Remove by value
cities.remove("coimbatore")
print(cities)

# remove by using storing in variable that the fn remove returns
city_del = "salem"
cities.remove(city_del)
print(cities)

# temporary sorted

print(sorted(cities))
print(cities)

print(sorted(val))

# permanent sorted
cities.sort()
print(cities)

# reverse
cities.reverse()  # permanently reverse the element
print(cities)

# length of a list
print(len(cities))

# loop - repeats a set of code for a specified condition whie, for
letter = ' '
while not letter.isalpha():
    letter = input("enter an alphabet:")

print("u have entered" + letter)

# print 1 to 10

num = 1
while num <= 10:
    print(num)
    num += 1  # num = num+1

# for loop

for i in range(1, 10 + 1):  # 1 is included 10 is excluded so 10+1
    print(i)
'''
else:
    print("over")
'''

print(list(range(1, 10)))

print(list(range(21, 31, 2)))

print(list(range(10, 0, -2)))

list = [6, 7, 4, 1, 9]

for i in list:
    print(i * i)
# guess the number
'''num = random.randint(1,20)

guess = int(input("can you guess the number iam thinking? it's less than 20"))

while num!=guess:
    if guess > num:
        print("ur guess is higher")
    else:
        print("ur guess is lower")
    guess = int(input("Guess again: "))

print("You won!")
'''

'''
for i in range(1,4):
    for j in range(1,6):
      print(j, end='' ) #stops execution at this point and shows the value of variables, from this we able to know 
             #how value changes. we can fix error by using debugging
    print(' ')#next line
'''
# break, continue, pass

# get a list of numbers from the user and add to a list
print("enter list of numbers: enter z to exit")
list = []
while True:  # execute the loop until the condition specified within the loop

    inp = input()
    if inp == 'z':
        break
    list.append(int(inp))
print(list)

# remove , from a string using continue

str = "A,B,C,D,E,F"
str2 = ''

for i in str:
    if i == ',':
        continue
    str2 = str2 + i

print(str2)

# remove , from a string using pass

str = "A,B,C,D,E,F"
str2 = ''

'''
for i in str:
    if i == ',':
        pass
    else:
    str2 = str2 + i

print(str2)   
'''
# split and join in strings
str_in = "abc, def,ghi,jkl"
split_list = str_in.split(',')  # what to delimits
print(split_list)

split_joined = '-'.join(split_list)
print(split_joined)

