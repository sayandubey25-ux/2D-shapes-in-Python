import math 
num1=int(input("Choose a number "))
for i in range(1, num1+1):
    num2=num1/i
    if num2==i:
        print("The number is a square number.")
        break
print(math.sqrt(num1))