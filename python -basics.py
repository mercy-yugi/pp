import math

a=10
print(id(10))
print(type(a))
print('hello mercy', type('hello'))
fruit=[2,'yes',34.2]
print(fruit, 'has type',type(fruit))
print(int(30.5))
print(bool('mercy'))
print(isinstance(3,int))
print(isinstance('mercy',bool))
# name=input('what is your name:')
# print(f'you have entered {name}')
print(math.sin(30))
print(math.sqrt(25))
print(pow(3,2))
print(pow(8,10))
print(abs(-100))
x=10
y=20
print(x==10 and y==20)
print('enter your full names')
names=input()
if names=='mercy':
    print(f'your name is {names}, i love your name')
age=int(input('Enter your current age: '))
if age>=18:
    print(f'your age is {age} you can therefore vote. Yey!!')
else:
    print('sorry, try agin next elections')
year=int(input('Enter your year of birth: '))
if 2022-year>=18:
    print(f'you are {2022-year}years old')
    print('you can attend this beach event')
else:
    print('maybe try again next time')
# using elif for displaying ages.
ages=int(input('Enter your age: '))
if ages<1:
    print('you are an infant')
elif ages<=1 and ages>=6:
    print('you are a todler')
elif ages<=7 and ages>=12:
    print('you are a child')
elif ages<=13 and ages>=19:
    print('you are a teeneger')
elif ages<=20 and ages>=35:
    print('you are a youth')
elif ages<=36 and ages>=55:
    print('you are a adult')
elif ages>56:
    print('you are a getting old')
# checking for divisibility
a=int(input('Enter a number to check for divisibilty: '))
if a%5==0:
    if a>=10:
        print('Your number is divisible by five and greater than 10')
    else:
        print('Your number is not divisible by 5 and is smaller than 10')
else:
    print('your number is not divisible by 5')
    #PYTHON EXECISES ON IF--ELSE--ELIF
# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.
salary=int(input('Enter your total salary: '))
year=int(input('Enter total year of service: '))
if year>5:
    print(f'The net bonus is {salary*0.05}')
else:
    print('no bonus')
# Take values of length and breadth of a rectangle from user and check if it is square or not.
len=int(input('Enter the length: '))
wid=int(input('Enter the width: '))
if len==wid:
    print('it is a square')
else:
    print('it is not a square')
#Take two int values from user and print greatest among them.
num1=int(input('Enter your first number: '))
num2=int(input('Enter your second number: '))
if num1>num2:
    print(f'The greatest is {num1}')
elif num2>num1:
    print(f'The greatest is {num2}')
else:
    print('They are both equal')
# A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.
quantity=int(input('Enter total number of units: '))
cost=quantity*100
if cost>1000:
    print(f'Cost is {cost}-{cost*0.1}')
else:
    print(f'Cost is {cost}')
#A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.
marks=int(input('Enter your total score: '))
if marks>=80 and marks<=100:
    print('A')
elif marks>=60 and marks<=80:
    print('B')
elif marks>=50 and marks<=59:
    print('C')
elif marks>=45 and marks<=49:
    print('D')
elif marks>=25 and marks<=44:
    print('E')
elif marks<24:
    print('F')
else:
    print('Out of range')
# Take input of age of 3 people by user and determine oldest and youngest among them.
name1=int(input('Enter your age: '))
name2=int(input('Enter your age: '))
name3=int(input('Enter your age: '))
if name1>name2 and name1>name3:
    print('The oldest is ',name1)
elif name2>name1 and name2>name3:
    print('The oldest is ',name2)
elif name3>name1 and name3>name2:
    print('The oldest is ',name3)
else:
    print('they are all equal')
#smallest
name4=int(input('Enter your age: '))
name5=int(input('Enter your age: '))
name6=int(input('Enter your age: '))
if name4<name5 and name4<name6:
    print('The smallest is ',name4)
elif name5<name4 and name5<name6:
    print('The smallest is ',name5)
elif name6<name5 and name6<name4:
    print('The smallest is ',name6)
else:
    print('they are all equal')
# Write a program to print absolute vlaue of a number entered by user. E.g.-
# INPUT: 1        OUTPUT: 1
# INPUT: -1        OUTPUT: 1
absolut=int(input('Enter your number: '))
if absolut<0:
    print(absolut*-1)
else:
    print(absolut)
# A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.
classHeld=int(input('Number of classes held: '))
classAttend=int(input('Number of classes attended: '))
percentage=classAttend/classHeld*100
if percentage<75:
    print('You will not attend the exam')
else:
    print('You can attend your exam')
# Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.
medic=int(input('Do you have a medical condition?'))
if medic==Yes|Y|YES:
    print('You can have a sit')
else:
    print('You cannot sit')
#Write a program to check if a year is leap year or not.
# If a year is divisible by 4 then it is leap year but if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.
leap=int(input('Enter the year to check: '))
if leap%4==0:
    print('It is a leap year')
else:
    print('it is not a leap year')


# Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
# if employee is female, then she will work only in urban areas.

# if employee is a male and age is in between 20 to 40 then he may work in anywhere

# if employee is male and age is in between 40 t0 60 then he will work in urban areas only.

# And any other input of age should print "ERROR
agee=int(input('Enter your age: '))
sex=int(input('Enter your gender: '))
marital=int(input('Enter your marital status: '))
if marital=='female':
    print('You can work on urban areas')
elif marital=='male' and agee>=20 and agee<=60:
    print('Yo can work anywhere')
elif marital=='male' and agee>=40 and agee<=60:
    print('You can work in urban areas only')
else:
    print('ERROR')


# A 4 digit number is entered through keyboard. Write a program to print a new number with digits reversed as of orignal one. E.g.-
# INPUT : 1234        OUTPUT : 4321
# INPUT : 5982        OUTPUT : 2895
four=int(input('Enter a four digit number: '))
    # print(four.reverse())