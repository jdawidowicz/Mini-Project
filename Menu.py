import csv
import os

wrongoption = ('Please try again and select a valid menu option')
products = []#Empty lists to read csv's into
couriers = []
orders = []
statuslist = ["Preparing", "Delivered", "Out for Delivery"]


def load_csv(filename, list): #loads csv file as dictionaries into given list
    path = os.path.realpath(f'{filename}.csv')
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            list.append(row)

def write_csv(filename, list):#Writes all data from list to a csv file in the same format as it reads
    path = os.path.realpath(f'{filename}.csv')
    keys=[]
    for key in list[0].keys():
        keys.append(key)
    with open(path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(list)


load_csv("products", products)
load_csv("orders", orders)
load_csv("couriers", couriers)

def view_list(list): #Function to display lists in a readable manner
    keystr = 'Index\t\t'
    for key in list[0].keys():
        keystr += key
        keystr += '\t\t'
        if key == "Address":
            keystr += '\t\t\t\t'
        if key == 'Status':
            keystr += '\t'
    print('---------------------------------------------------------\n'+keystr)
    for dict in list:
        valuestr = f'{list.index(dict)}\t\t'
        for value in dict.values():
            valuestr += value
            valuestr += '\t\t'
        print(valuestr)

def add_new(list, input=input): #Function to add new items to list
    newdict={}
    for key in list[0].keys():
        if key == "Status" :
            newdict["Status"] = "Preparing"
        if key == "Products":
            view_list(products)
            print('Input index values')
        elif key == "Courier":
            view_list(couriers)
            print('Please select index value')
        value = input(f'Please enter the {key}: ')
        newdict[key] = value
    list.append(newdict)
    print('New entry successfully added')    


def update(list, status = False, input1 = input, input2 = input): #Function to update existing item in a list, for just order status update, status is set to True
        view_list(list)
        try:
            index = int(input1('---------------------------------------------------------\n\
    Please select the index of the data you would like to update: '))
            sdict = list[index]
        except:
            print('That is not a valid choice.\nReturning to menu...')
            return
        if status == True:
            print(f'You have selected no. {index}, with status: {sdict["Status"]}. Please select the new status.\n')
            print('Index\t\tStatus')
            for status in statuslist:
                print(f'{statuslist.index(status)}\t\t{status}')
            while True:
                statusinput = input2('\n')
                try:
                    sdict["Status"] = statuslist[statusinput]
                    print(f'Status successfully changed to {statuslist[statusinput]}')
                    return
                except:
                    print(wrongoption)
                    continue

        print(f'You have selected no. {index}.\nFor each of the following columns, please input a new value or leave blank to keep the same.')
        for key in sdict.keys():
            newvalue = input2(f'Current {key}: {sdict[key]}. New {key}?\n')
            if newvalue != '':
                sdict[key] = newvalue


def delete_from(list, input = input): #Function to delete item from a list
    view_list(list)
    try:
        index = int(input('---------------------------------------------------------\n\
            Please select the index of the entry you would like to delete'))
        del list[index]
        print(f'Entry no.{index} successfully deleted')
    except:
        print('That is not a valid choice.\nReturning to menu...')    
    
    


def main_menu():
    while True:
        mainmenuinput = input("---------------------------------------------------------\n\
Main Menu:\n\
    0. Exit\n\
    1. Products\n\
    2. Couriers\n\
    3. Orders\n\
    ")
    
        match mainmenuinput:
            case "0":
                print('Goodbye!')
                write_csv("products", products)
                write_csv("orders", orders)
                write_csv("couriers", couriers)
                return
            
            case '1':
                products_menu()
            case '2':
                couriers_menu()
            case '3':
                orders_menu()
            case _:
                print(wrongoption)

def products_menu():
    while True:
        productsmenuinput = input("---------------------------------------------------------\n\
    Products Menu:\n\
        0. Return to Main Menu\n\
        1. Products List\n\
        2. Add a product\n\
        3. Update existing product\n\
        4. Delete existing product\n\
        ")
        match productsmenuinput:
            case '0':
                return
            case '1':
                view_list(products)
            case '2':
                add_new(products)
            case '3':
                update(products)
            case '4':
                delete_from(products)
            case _:
                print(wrongoption)

def couriers_menu():
    while True:
        couriersmenuinput = input("""-------------------
Couriers Menu:
    0. Return to Main Menu
    1. View Couriers
    2. Add New Courier
    3. Update Existing Courier
    4. Delete Existing Courier
    """)
        match couriersmenuinput:
            case '0':
                return
            case '1':
                view_list(couriers)
            case '2':
                add_new(couriers)
            case '3':
                update(couriers)
            case '4':
                delete_from(couriers)
            case _:
                print(wrongoption)

def orders_menu():
    while True:
        ordersmenuinput = input("""-------------------
Orders Menu:
    0. Return to Main Menu
    1. View Orders
    2. Add New Order
    3. Update Order Status
    4. Update Existing Order
    5. Delete Existing Order
    """)
        match ordersmenuinput:
                case '0':
                    return
                case '1':
                    view_list(orders)
                case '2':
                    add_new(orders)
                case '3':
                    update(orders, status = True)
                case '4':
                    update(orders)
                case '5':
                    delete_from(orders)
                case _:
                    print(wrongoption)


if __name__ == '__main__':
    main_menu()