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

################## calclates the greatest divisor of two numbers
def greatestDivisor(a,b):
    if a<b:
        temp=a
        a=b
        b=temp
    if b==0:
        return 0
    while b!=0:
        temp=b
        b=a%b
        a=temp
    return a
print(greatestDivisor(12,18))