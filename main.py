loop1="1"
while loop1=="1":
    num1=int(input("Enter a number "))
    num2=int(input("Enter another number "))
    operation=input("Enter an operation between +, -, /, x ")
    result=None
    if operation=="+":
        result=num1+num2
        print(result)
        loop1=input("Would you like to continue? press 1 for yes.")
    elif operation=="-":
        result=num1-num2
        print(result)
        loop1=input("Would you like to continue? press 1 for yes.")
    elif operation=="x":
        result=num1*num2
        print(result)
        loop1=input("Would you like to continue? press 1 for yes.")
    elif operation=="/":
        result=num1/num2
        print(result)
        loop1=input("Would you like to continue? press 1 for yes.")
    else:
        print("Not a valid choice.")
        loop1=input("Would you like to continue? press 1 for yes.")
