choice = int(input("Enter choice\n1.Car\n2.Truck\n3.Bus\n"))

if choice == 1:
    time = int(input("Enter time parked : "))
    if time <= 3:
        cost = time * 2
    else:
        cost = 3*2 + (time-3) * 4
    print("Total charge will be : ",cost)
    

elif choice == 2:
    time = int(input("Enter the time parked : "))
    if time <= 3:
        cost = time * 4
    else:
        cost = 3*4 + (time-3) *6
    print("Total charge will be : ",cost)
    
elif choice == 3:
    time = int(input("Enter the time parked : "))
    if time <= 3:
        cost = time * 5
    else:
        cost = 3*5 + (time-3) *7
    print("Total charge will be : ",cost)
    
