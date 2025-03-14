# def addTwoNumbers(a,b): #this function takes two arguments and returns their sum
#     c=a+b
#     return c

# d=addTwoNumbers(1,2)
# print(d)

# ################## multiplies three numbers
# def multiplyThreeNumbers(a,b,c):
#     d=a*b*c
#     return d
# print(multiplyThreeNumbers(1,2,3))

# ################## calclates the greatest divisor of two numbers
# def greatestDivisor(a,b):
#     if a<0:
#         a=-a
#     if b<0:
#         b=-b
#     if a<b:
#         temp=a
#         a=b
#         b=temp
#     if b==0:
#         return 0
#     while b!=0:
#         temp=b
#         b=a%b
#         a=temp
#     return a
# print(greatestDivisor(12,18))

# ############# calculating quadratic equation

# import math
# def quadraticEquation(a,b,c):
#   discriminant = b**2 - 4*a*c
#   if discriminant < 0:
#     return "No real roots"
#   elif discriminant == 0:
#     root= -b/(2*a)
#     return root
#   else:
#     return (-b + math.sqrt(discriminant))/(2*a), (-b - math.sqrt(discriminant))/(2*a)  
# print(quadraticEquation(1,5,6))
# print(quadraticEquation(1,2,1))
# print(quadraticEquation(1,2,3)) 

# ########### compute power without *** operator
# def computePower(a,b):
#     if a==0:
#         if b==0:
#             return "Undefined"
#         else:
#             return 0
#     else:
#        if b>0:
#           result=1
#           for i in range(1,b+1):
#               result=result*a
#     return result
# print(computePower(2,3))
# print(computePower(2,0))

################# provides date and time

# import datetime

# from datetime import date
# def currentDateAndTime():
#     return datetime.datetime.now()
# print(currentDateAndTime())    

########## fuction that return welcome message when called
# def welcomeMessage():
#     return "Welcome to Python"
# print(welcomeMessage())

# ######### fuction to create a random motivation message
# import random
# def motivationMessage():
#     messages=["You are doing great","Keep going","You are the best","You are awesome"]
#     return random.choice(messages)
# print(motivationMessage())    

######## fuction that generates a random univesal unique identifier
# import uuid
# def generateUUID():
#     return uuid.uuid1()
# print(generateUUID())

###### fuction for random password generator
# import random
# import string
# length=8
# characters=string.ascii_letters+string.digits+string.punctuation
# password=""
# for i in range(1,length+1):
#     password=''.join(random.choice(characters))
#     return password
# print(generatePassword())

# ####### procedure funtion
# def greetuser(name):
#     print(f"Hello {name}")
# greetuser("Jose")

# ######## fucntion that counts down from a given number
# def countDown(n):
#     if n<0:
#         n=-n
#     while n+1>0:
#         print(n)
#         n=n-1
# countDown(5)

################ fuction that does not return anything

def do_nothing():
    pass  # The function does absolutely nothing

# Example usage
do_nothing()  # Calling this does nothing

########## function that prints hello

def printHello():
    print("Hello")  # This function prints "Hello"


####### funtion to screer screem
def cleanScreen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    return
cleanScreen()

#######
def enjoyMarchBreak():
    print("Enjoy your March Break")