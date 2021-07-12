
# a shop gives the discount if quantity is greater then 10
# 100 rs per quantity
Quantity=int(input("enter the quantity"))
if Quantity>10:
    print("your total price is ",Quantity*100-(.1*Quantity*100))
else:
    print("your total price is",Quantity*100)
