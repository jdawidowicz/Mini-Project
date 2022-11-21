# Need to add more tests, SQL, Terminal output handling i.e clears, sleeps, art
import os
import pyfiglet
import pymysql
from csv_read_write import load_csv, write_csv
from database_functions import load_table, add_new_record, update_record,delete_record

wrongoption = ('Please try again and select a valid menu option')
statuslist = ["Preparing", "Delivered", "Out for Delivery"]
clear = lambda: os.system('cls')
# products = load_csv("products") #read csv's into lists
# orders = load_csv("orders")
# couriers = load_csv("couriers")

def view_list(list): #Function to display lists in a readable manner
    keystr = ''
    for key in list[0].keys():
        keystr += key
        keystr += '\t\t'
        if key == "Address":
            keystr += '\t\t\t\t'
        if key == 'Status':
            keystr += '\t'
    print('---------------------------------------------------------\n'+keystr)
    for dict in list:
        valuestr =''
        for value in dict.values():
            valuestr += str(value)
            valuestr += '\t\t'
        print(valuestr)

def dictionary_select(table_name):
    lod = load_table(table_name)
    id_str = table_name.rstrip('s')
    view_list(lod)
    try: #try except clause to handle input errors
        id_no = int(input('---------------------------------------------------------\n\
Please type the ID of the data you would like to select: '))
        for dictionary in lod:
            if dictionary[f'{id_str}_id'] == id_no:
                index = lod.index(dictionary)
                sdict = lod[index]
    except:
        print('That is not a valid choice.\nReturning to menu...') 
        return
    return sdict

def add_new(table_name, input=input): #Function to add new items to list, returns a dictionary
    newdict={}
    table = load_table(table_name)
    id_str = table_name.rstrip('s')
    for key in table[0].keys():
        if key == f'{id_str}_id':
            continue
        elif key == "status" : #If statements for edge cases, i.e to display courier list when selecting courier,
            newdict["status"] = "Preparing" #or automatically set status to "Preparing" for new order
            print('Status set to Preparing')
            continue
        elif key == "products":
            products = load_table('products')
            view_list(products)
            print('Input index values separated by commas')
        elif key == "courier":
            couriers = load_table('couriers')
            view_list(couriers)
            print('Please select ID value')
        while True:
            value = input(f'Please enter the {key}: ')
            if value == '':
                print('Empty field not allowed')
                continue
            break
        newdict[key] = value
    print('New entry successfully added')    
    return newdict


def update(table_name, status = False, input2 = input): #Function to update existing item in a list, status update, status is set to True returns dict
        sdict = dictionary_select(table_name)
        id_str = table_name.rstrip('s')
        id_no = sdict[f'{id_str}_id']
        if sdict == None:
            return

        if status == True: #if status is set to true in args, just status of an order is changed
            print(f'You have selected no. {id_no}, with status: {sdict["Status"]}. Please select the new status.\n')
            print('Index\t\tStatus')
            for status in statuslist:
                print(f'{statuslist.index(status)}\t\t{status}')
            while True:
                statusinput = input2('\n')
                try:
                    sdict["status"] = statuslist[statusinput]
                    print(f'Status successfully changed to {statuslist[statusinput]}')
                    return
                except:
                    print(wrongoption)
                    continue

        print(f'You have selected no. {id_no}.\nFor each of the following columns, please input a new value or leave blank to keep the same.')
        for key in sdict.keys(): #Takes input to update each column, blank leaves it the same
            if key == f'{id_str}_id':
                continue
            newvalue = input2(f'Current {key}: {sdict[key]}. New {key}?\n')
            if newvalue != '':
                sdict[key] = newvalue
        return sdict

        


# def delete_from(table_name, input = input):#Function to delete item from a list
#     lod = load_table(table_name)
#     id_str = table_name.rstrip('s') 
#     view_list(lod)
#     try: # try except to handle index errors
#         id = int(input('---------------------------------------------------------\n\
# Please select the ID of the entry you would like to delete: '))
#         del list[index]
#         print(f'Entry no.{index} successfully deleted')
#     except:
#         print('That is not a valid choice.\nReturning to menu...')    


def main_menu():
    print(pyfiglet.figlet_format('MAIN', font = 'starwars' ))
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
                products = load_table('products')
                view_list(products)
            case '2':
                new_product = add_new('products')
                add_new_record('products', new_product)
            case '3':
                updated_dictionary = update('products')
                if updated_dictionary == None:
                    continue
                update_record('products', updated_dictionary)
            case '4':
                dict_2_delete = dictionary_select('products')
                delete_record('products',dict_2_delete)
            case _:
                print(wrongoption)


def couriers_menu():
    while True:
        couriers = load_table('couriers')
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
        ordersmenuinput = input("""------------------------------------\n\
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