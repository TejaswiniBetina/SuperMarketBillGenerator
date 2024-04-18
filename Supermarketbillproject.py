from datetime import datetime 
# Enter the useranme and print statement
username = input("Enter your name: ")
print(f"Welcome to online shopping:",username)

# List of items
list_items = {
    "sugar": 20,
    "rice": 30,
    "flour": 25,
    "bread": 15,
    "Dal": 35
}

#Variable Declaration and Assignments of values
Finalamount = 0
Totalamount = 0
Products = []
plist = []
qlist = []
ilist = []
Taxrate = 0.13

# Main part of code
while True:
    press = int(input("Press 1 to continue and 2 to exit: "))
    if press == 1:
        print("Avaliable items")
        for i,j in list_items.items():
            print(f" {i}:{j}Rs/kg")
        while True:
            press = int(input("Press 1 to Buy and 2 to exit: "))
            if press ==1 :
                items =input("Enter the items: ")
                if items in list_items:
                    quantity =int(input("Enter the Quantity: "))
                    price = list_items[items]* quantity
                    Products.append((items, quantity, price))
                    Totalamount += price
                    # Adding the variables to list for indexing
                    plist.append(price)
                    qlist.append(quantity)
                    ilist.append(items)
                else:
                    print("Invalid item")
            elif press ==2: 
                for items, quantity, price in Products:
                    print(f" {items}: {quantity} x {price} Rs = {quantity * price} Rs")
                print( Totalamount)
                break 
    elif press ==2:
        print("Thanks for shopping")
        break
    else:
        print("Invalid inputs enter 1 or 2")

# Assignment of Final price
if Totalamount > 0:
    Tax = (Totalamount * Taxrate)
    Finalprice = Totalamount + Tax

    # Visulaization of code 
    print(25 * "=", "Homely Supermarket", 25 * "=")
    print(28 * " ", "Vijaywada")
    print("Name:", username, 30 * " ", "Date:", datetime.now())
    print(75 * "-")
    print("S.No", 10 * " ", 'items', 8 * " ", 'quantity', 8 * " ", 'price')
    for i in range(len(Products)):

        print(i, 13 * " ", ilist [i], 8 * " ", qlist[i], 8 * " ", plist[i])
    print(75 * "-")
    print(50 * " ", 'Total amount:', 'Rs', Totalamount)
    print("Tax amount", 50 * " ", 'Rs', Tax)
    print(75 * "-")
    print(50 * " ", 'Final amount:', 'Rs', Finalprice)
    print(75 * "-")
    print(20 * " ", "Thank you & Please visit again")
    print(75 * "-")

else :
    print("Please valid Items into cart")







        





