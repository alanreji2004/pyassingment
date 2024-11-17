import math

a = int(input("Enter the first side : "))
b = int(input("Enter the second side : "))
c = int(input("Enter the third side : "))

if a == b == c:
    area = (math.sqrt(3) / 4) * (a ** 2)
    print("The area of the equilateral triangle is : ",area)

elif a == b or b == c or a == c:
    if a == b:
        base = c
        height = math.sqrt((a**2)-(base/2)**2)
    elif b == c:
        base = a
        height = math.sqrt((b**2)-(base/2)**2)
    else:
        base = b
        height = math.sqrt((c**2)-(base/2)**2)
        
    area = (1/2) * base * height
    print("The area of the isosceles triangle is : ",area)

else:
    s = (a + b + c) / 2
    if a + b > c and a + c > b and b + c > a:
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        print(f"The area of the scalene triangle is: {area:.2f}")
    else:
        print("The entered sides do not form a valid triangle.")
