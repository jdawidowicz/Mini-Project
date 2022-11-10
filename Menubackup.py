wrongoption = ('Please try again and select a valid menu option')
products = ['Fanta', 'Pepsi', 'Pepsi Max']
orders = [{"Name": "John", "Address" : "20 LS29AJ", "Phone":"0798989899", "Status":"Preparing" }
,{"Name": "Paul", "Address" : "19 LS41AY", "Phone":"0780000000", "Status":"Delivered" }]
statuslist = ["Preparing", "Delivered"]

def IsInt(num):
    try:
        integernum = int(num)
        return integernum
    except:
        return "notInt"


def ProductsList():
    print('-------------------')
    print('Index\t\tProduct')
    for product in products:
        print(f'{products.index(product)}.\t\t{product}')


def OrdersList():
    print('-------------------')
    print('Index\t\tName\t\tAddress\t\t\tPhone\t\tStatus')
    for order in orders:
        print(f'{orders.index(order)}.\t\t{order["Name"]}\t\t{order["Address"]}\t\t{order["Phone"]}\t{order["Status"]}')

def liststatus(statuses):
    for status in statuses:
        print(f'{statuses.index(status)}. {status}')



def MainMenu():
    mainmenuinput = IsInt(input("-------------------\n\
Main Menu:\n\
    0. Exit\n\
    1. Products\n\
    2. Orders\n\
    "))
    if mainmenuinput == 0:
        print('Goodbye!')
        return
    elif mainmenuinput == 1:
        ProductsMenu()
    elif mainmenuinput == 2:
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
    "))

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
            selection = IsInt(input('Please select the number of the product you would like to update. \n'))
            if selection == "notInt":
                print(wrongoption)
                continue
            try:
                oldproduct = products[selection]
            except:
                print(wrongoption)
                continue
            break
        updatedproduct = input('Please input the new name: \n')
        print(oldproduct, ' has been updated to:', updatedproduct)
        products[selection] = updatedproduct

    elif productsmenuinput == 4:
        ProductsList()
        while True:
            selection = IsInt(input('Please select the number of the product you would like to delete. \n'))
            if selection == "notInt":
                print(wrongoption)
                continue
            try:
                selproduct = products[selection]
            except:
                print(wrongoption)
                continue
            break
        print(products[selection], ' has been removed from the list.')
        del products[selection]
    
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

    if ordersmenuinput == 1:
        OrdersList()
        OrdersMenu()

    if ordersmenuinput == 2:
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

    if ordersmenuinput == 3:
        OrdersList()
        selection = IsInt(input("-------------------\nPlease type the order number you would like to update.\n"))
        liststatus(statuslist)
        newstatus = IsInt(input("-------------------\nWhat is the new status?(select index)\n"))
        order = orders[selection]
        print(f'Order number {selection} has been updated from {order["Status"]} to {statuslist[newstatus]}')
        order["Status"] = statuslist[newstatus]
        OrdersMenu()

    if ordersmenuinput == 4:
        OrdersList()
        selection = IsInt(input("-------------------\nPlease type the order number you would like to update.\n"))
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

    if ordersmenuinput ==5:
        OrdersList()
        selection = IsInt(input("-------------------\nPlease type the order number you would like to delete.\n"))
        print(f'Order No.{selection} has been deleted from the list')
        del orders[selection]
        OrdersMenu()
      

MainMenu()



    