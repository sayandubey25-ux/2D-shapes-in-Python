import math
num1=int(input("Enter a number "))
pow=int(input("Enter the power you would like to times your number by "))
num2=num1
for i in range(1, pow):
    num2=num2*num1
print(num1, "to the power of", pow, "is", num2)
num3=math.pow(num1, pow)
print(num3)