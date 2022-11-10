import csv

wrongoption = ('Please try again and select a valid menu option')
products = []
couriers = []

orders = [{"Name": "John", "Address" : "20 LS29AJ", "Phone":"0798989899", "Status":"Preparing" }
,{"Name": "Paul", "Address" : "19 LS41AY", "Phone":"0780000000", "Status":"Delivered" }]
statuslist = ["Preparing", "Delivered", "Out for Delivery"]

with open(r'Mini Project\products.txt', 'r') as p: #currently reads file into a list, could read the file, keep file as a list straight into a variable, close it on menu
    for product in p.readlines():
        product = product.strip()
        products.append(product)

with open(r'Mini Project\couriers.txt', 'r') as c: 
    for courier in c.readlines():
        courier = courier.strip()
        couriers.append(courier)

def IsInt(num, listrange): #Function to check menu inputs are integers, and within the available options (i.e. only 01234)
        try:
            integernum = int(num)
            if integernum in range(listrange):
                return integernum
            else:
                return "notInt"
        except:
            return "notInt"


def ProductsList(): #These 4 list functions print the contents of the respective objects
    print('-------------------')
    print('Index\t\tProduct')
    for product in products:
        print(f'{products.index(product)}.\t\t{product}')

def CouriersList():
    print('-------------------')
    print('Index\t\tCourier')
    for courier in couriers:
        print(f'{couriers.index(courier)}.\t\t{courier}')


def OrdersList():
    print('-------------------')
    print('Index\t\tName\t\tAddress\t\t\tPhone\t\tStatus')
    for order in orders:
        print(f'{orders.index(order)}.\t\t{order["Name"]}\t\t{order["Address"]}\t\t{order["Phone"]}\t{order["Status"]}')

def StatusList():
    for status in statuslist:
        print(f'{statuslist.index(status)}. {status}')



def MainMenu():
    mainmenuinput = IsInt(input("-------------------\n\
Main Menu:\n\
    0. Exit\n\
    1. Products\n\
    2. Couriers\n\
    3. Orders\n\
    "), 4)
    if mainmenuinput == 0:
        print('Goodbye!')
        with open(r'Mini Project\products.txt', 'w') as p:
            for product in products:
                p.write(f'{product}\n')
        with open(r'Mini Project\couriers.txt', 'w') as c:
            for courier in couriers:
                c.write(f'{courier}\n')
        return
    elif mainmenuinput == 1:
        ProductsMenu()
    elif mainmenuinput == 2:
        CouriersMenu()
    elif mainmenuinput == 3:
        OrdersMenu()
    else:
        print(wrongoption)
        MainMenu()

def ProductsMenu():
    productsmenuinput = IsInt(input("-------------------\n\
Product Menu:\n\
    0. Return to Main Menu\n\
    1. Products List\n\
    2. Add a product\n\
    3. Update existing product\n\
    4. Delete existing product\n\
    "), 5)

    if productsmenuinput == 0:
        MainMenu()

    elif productsmenuinput == 1:
        ProductsList()
        ProductsMenu()

    elif productsmenuinput == 2:
        newproduct=input("Please enter the name of the product you would like to add: \n")
        products.append(newproduct)
        print(newproduct, ' has been added to the products list.')
        ProductsMenu()
    
    elif productsmenuinput == 3:
        ProductsList()
        while True:
            selection = IsInt(input('Please select the number of the product you would like to update. \n'), len(products))
            if selection == "notInt":
                print(wrongoption)
                continue
            oldproduct = products[selection]
            break
        updatedproduct = input('Please input the new name: \n')
        print(oldproduct, ' has been updated to:', updatedproduct)
        products[selection] = updatedproduct
        ProductsMenu()

    elif productsmenuinput == 4:
        ProductsList()
        while True:
            selection = IsInt(input('Please select the number of the product you would like to delete. \n'), len(products))
            if selection == "notInt":
                print(wrongoption)
                continue
            selproduct = products[selection]
            break
        print(selproduct, ' has been removed from the list.')
        del selproduct
        ProductsMenu()
    
    else:
        print(wrongoption)
        ProductsMenu()





def OrdersMenu():
    ordersmenuinput = IsInt(input("""-------------------
Orders Menu:
    0. Return to Main Menu
    1. View Orders
    2. Add New Order
    3. Update Order Status
    4. Update Existing Order
    5. Delete Existing Order
    """))   
    if ordersmenuinput == 0:
        MainMenu()

    elif ordersmenuinput == 1:
        OrdersList()
        OrdersMenu()

    elif ordersmenuinput == 2:
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

    elif ordersmenuinput == 3:
        OrdersList()
        while True:
            selection = IsInt(input("-------------------\nPlease type the order number you would like to update.\n"), len(orders))
            if selection == "notInt":
                print(wrongoption)
                continue
            break
        StatusList()
        while True:
            newstatus = IsInt(input("-------------------\nWhat is the new status?(select index)\n"), len(statuslist))
            if newstatus == "notInt":
                print(wrongoption)
                continue
            break
        order = orders[selection]
        print(f'Order number {selection} has been updated from {order["Status"]} to {statuslist[newstatus]}')
        order["Status"] = statuslist[newstatus]
        OrdersMenu()

    elif ordersmenuinput == 4:
        OrdersList()
        while True:
            selection = IsInt(input("-------------------\nPlease type the order number you would like to update.\n"), len(orders))
            if selection == "notInt":
                print(wrongoption)
                continue
            break
        order = orders[selection]
        print('For each of these values, type the new value or leave blank to keep the same')
        for key in order.keys():
            newvalue = input(f'{key}: {order[key]}. New {key}?\n')
            if newvalue == '':
                continue
            order[key] = newvalue
        print(f'Order No.{orders.index(order)} updated to:\nIndex\t\tName\t\tAddress\t\t\tPhone\t\tStatus')
        print(f'{orders.index(order)}.\t\t{order["Name"]}\t\t{order["Address"]}\t\t{order["Phone"]}\t{order["Status"]}')
        OrdersMenu()

    elif ordersmenuinput == 5:
        OrdersList()
        while True:
            selection = IsInt(input("-------------------\nPlease type the order number you would like to delete.\n"), len(orders))
            if selection == "notInt":
                print(wrongoption)
                continue
            break
        print(f'Order No.{selection} has been deleted from the list')
        del orders[selection]
        OrdersMenu()
    
    else:
        print(wrongoption)
        OrdersMenu()



def CouriersMenu():
    couriersmenuinput = IsInt(input("""-------------------
Couriers Menu:
    0. Return to Main Menu
    1. View Couriers
    2. Add New Courier
    3. Update Existing Courier
    4. Delete Existing Courier
    """), 5)
    
    if couriersmenuinput == 0:
        MainMenu()
    
    elif couriersmenuinput == 1:
        CouriersList()
        CouriersMenu()

    elif couriersmenuinput == 2:
        newcourier=input("Please enter the name of the courier you would like to add: \n")
        couriers.append(newcourier)
        print(newcourier, ' has been added to the couriers list.')
        CouriersMenu()
    
    elif couriersmenuinput == 3:
        CouriersList()
        while True:
            selection = IsInt(input('Please select the number of the courier you would like to update. \n'), len(couriers))
            if selection == "notInt":
                print(wrongoption)
                continue
            oldcourier = couriers[selection]
            break
        updatedcourier = input('Please input the new name: \n')
        print(oldcourier, ' has been updated to:', updatedcourier)
        courier[selection] = updatedcourier
        CouriersMenu()

    elif couriersmenuinput == 4:
        CouriersList()
        while True:
            selection = IsInt(input('Please select the number of the courier you would like to update. \n'), len(couriers))
            if selection == "notInt":
                print(wrongoption)
                continue
            selcourier = couriers[selection]
            break
        print(selcourier, ' has been removed from the list.')
        del selcourier
        CouriersMenu()
    
    else:
        print(wrongoption)
        ProductsMenu()



MainMenu()



    
