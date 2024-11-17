cost_price = int(input("Enter the cost prize : "))
colour = input("Enter the colour(red,green,yellow,white) : ")

if colour == "red":
    discount = (cost_price/100) * 10
    selling_price = cost_price - discount
    print("Selling Price : ",selling_price)
    
elif colour == "green":
    discount = (cost_price/100) * 8
    selling_price = cost_price - discount
    print("Selling Price : ",selling_price)
    
elif colour == "yellow":
    discount = (cost_price/100) * 15
    selling_price = cost_price - discount
    print("Selling Price : ",selling_price)
    
elif colour == "white":
    discount = (cost_price/100) * 20
    selling_price = cost_price - discount
    print("Selling Price : ",selling_price)
