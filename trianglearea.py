import math
choice = int(input("Enter choice\n1.Equilateral\n2.Isosceles\n3.Scalene\n"))

if choice == 1:
    side = int(input("Enter length of side: "))
    area = (math.sqrt(3)/4) * (side ** 2)
    print("The area of scalene Equilateral is: ",area)
    
elif choice == 2:
    base = int(input("Enter the base of the triangle: "))
    height = int(input("Enter the height of the triangle: "))
    area = (1/2) * base * height
    print("The area of scalene Isosceles is ",area)
    
elif choice == 3:
    a = int(input("Enter the first side: "))
    b = int(input("Enter the second side: "))
    c = int(input("Enter the third side: "))    
    
    s =(a+b+c)/2 
    
    area = math.sqrt(s* (s-a)* (s-b)*(s-c))
    if a + b > c and a + c > b and b + c > a:
        print("The area of the scalene triangle is:", area)
    else:
        print("The entered sides do not form a valid triangle.")    

else:
    print("invalid choice")
