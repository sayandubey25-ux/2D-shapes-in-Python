import math
#write code to calculate the square root of a given numver 
num1=int(input("Choose a number "))
#make loop that tests numbers. stop when divisbile is equal to ansewre
for i in range(1, num1+1):
    num2=num1/i
    if num2==i:
        print("The number is a square number.")
        break
print(math.sqrt(num1))