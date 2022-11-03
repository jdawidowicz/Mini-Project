#Start of the Program
def orderindex(orderslist):
    for order in orderslist:
        print(f'-------------------\n{orderslist.index(order)}. Name: {order["Name"]}\nAddress: {order["Address"]}\n\
Phone Number: {order["Phone"]}\nStatus: {order["Status"]}')
    return

def liststatus(statuses):
    for status in statuses:
        print(f'{statuses.index(status)}. {status}')


wrongoption = ('Please try again and select a valid menu option')

products = ['Fanta', 'Pepsi', 'Pepsi Max']
orders = [{"Name": "John", "Address" : "20 Bigston Avenue", "Phone":"0798989899", "Status":"Preparing" }
,{"Name": "Paul", "Address" : "19 Bigston Road", "Phone":"0780000000", "Status":"Delivered" }]

statuslist = ["Preparing", "Delivered"]

print('------------------- \nWelcome to the stock manager!')
print('To select an option please type its number.')

while True: #Main Menu will loop until a correct option is selected, either 0 or 1
    mainmenuinput = input("""-------------------
Main Menu:
    0. Exit
    1. Products
    2. Orders
    """)
    mainmenuinput = int(mainmenuinput)
    
    if mainmenuinput == 0: #If option 0 is selected, loop breaks and program finishes
        print('Thank you for using the stock manager. Goodbye!')
        break

    elif mainmenuinput == 1: #Option 1 will go into the product menu, which is another nested while loop
        while True:
            selection = input("""-------------------
Product Menu:
    0. Return to Main Menu
    1. Products List
    2. Add a product
    3. Update existing product
    4. Delete existing product
    """)
            productsmenu = int(selection)
            
            if productsmenu == 0: #Breaks loop to return to main menu 
                break

            elif productsmenu == 1:
                print('-------------------')
                for product in products:
                    print(product)

            elif productsmenu == 2:
                newproduct=input("Please enter the name of the product you would like to add: \n")
                products.append(newproduct)
                print(newproduct, ' has been added to the products list.')

            elif productsmenu == 3:
                for product in products:
                    print(products.index(product), '. ', product)
                selection = int(input('Please select the number of the product you would like to update. \n'))
                updatedproduct = input('Please input the new name: \n')
                print(products[selection], ' has been updated to:', updatedproduct)
                products[selection] = updatedproduct

            elif productsmenu == 4:
                for product in products:    
                    print(products.index(product), '. ', product)
                selection = int(input('Please select the number of the product you would like to delete. \n'))
                print(products[selection], ' has been removed from the list.')
                del products[selection]
            
            elif productsmenu != (0 and 1 and 2 and 3 and 4):
                print(wrongoption)
                continue
    if mainmenuinput == 2:
        while True:
            ordersinput = input("""-------------------
Orders Menu:
    0. Return to Main Menu
    1. View Orders
    2. Add New Order
    3. Update Order Status
    4. Update Existing Order
    5. Delete Existing Order
    """)        
            ordersmenu = int(ordersinput)
            if ordersmenu == 0:
                break
                
            elif ordersmenu == 1:
                orderindex(orders)
                continue

            elif ordersmenu == 2:
                neworder = {}
                keys = orders[0].keys()
                for key in keys:
                    if key == "Status":
                        neworder[key] == "Preparing"
                        continue
                    value=input(f'What is the {key}?\n')
                    neworder[key] = value
                orders.append(neworder)
                print(f'{neworder["Name"]}\'s order has been added to the list as Preparing')
            

            elif ordersmenu == 3:
                orderindex(orders)
                selection = int(input("-------------------\nPlease type the order number you would like to update.\n"))
                liststatus(statuslist)
                newstatus = int(input("What is the new status?(select index)\n"))
                order = orders[selection]
                print(f'Order number {selection} has been updated from {order["Status"]} to {statuslist[newstatus]}')
                order["Status"] = statuslist[newstatus]
            
            
                
             
   
   
    elif mainmenuinput != (0 and 1 and 2):
                print(wrongoption)
                continue
