import math
num1=float(input("Enter a number "))
num2=int(num1)
if num1>=num2+0.5 and num1<num2+1:
    print(num1, "should be rounded to be", num2+1)
elif num2+0.4>=num1 and num1!=num2:
    print(num1, "should be rounded to be", num2)
else:
    print(num1, "does not need rounding.")
print("The ceiling is", math.ceil(num1))
print("The floor is", math.floor(num1))