import math
shape=int(input("Please enter a shape. 2 for circle, 3 for triangle, 4 for rectangle/square."))
if shape==2:
    radius=int(input("What is the radius of your circle? "))
    area=math.pi*(radius**2)
    print("The area of your circle is", area)
elif shape==3:
    base=int(input("What is the base of your triangle? "))
    height=int(input("What is the height of your triangle? "))
    area=(base*height)/2
    print("The area of your triangle is", area)
elif shape==4:
    length=int(input("What is the length of your shape? "))
    width=int(input("What is the width of your shape? "))
    area=width*length
    if width==length:
        print("The area of your square is", area)
    else:
        print("The area of your rectangle is", area)
else:
    print("Not a valid choice")