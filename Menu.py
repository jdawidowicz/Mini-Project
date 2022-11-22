# Need to add more tests, SQL, Terminal output handling i.e clears, sleeps, art
import os
import pyfiglet
from csv_read_write import write_csv
import time
from database_functions import load_table, add_new_record, update_record, delete_record
from dictionary_functions import view_table, add_new, update, dictionary_select

clear = lambda: os.system('cls')
wrongoption ='Please select a valid option to continue.'

#Main loop
def main_menu():
    while True:
        clear()
        print(pyfiglet.figlet_format('MAIN', font = 'starwars' ))
        time.sleep(2)
        mainmenuinput = input("---------------------------------------------------------\n\
Main Menu:\n\
    [0]...Exit\n\
    [1]...Products\n\
    [2]...Couriers\n\
    [3]...Orders\n\
\nPlease type the number you would like to select: ")
        match mainmenuinput:
            case "0":
                csv_input = input('Would you like to export a backup in csv format?\n\
[1].....Yes\n\
[Any]...No\n')
                if csv_input == '1':
                    products = load_table('products')
                    couriers = load_table('couriers')
                    orders = load_table('orders')
                    write_csv('products', products)
                    write_csv('couriers', couriers)
                    write_csv('orders', orders)

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
    clear()
    print(pyfiglet.figlet_format('PRODUCT', font = 'starwars' ))
    time.sleep(1)
    while True:
        productsmenuinput = input("---------------------------------------------------------\n\
Products Menu:\n\
    [0]...Return to Main Menu\n\
    [1]...Products List\n\
    [2]...Add a product\n\
    [3]...Update existing product\n\
    [4]...Delete existing product\n\
\nPlease type the number you would like to select: ")
        match productsmenuinput:
            case '0':
                return
            case '1':
                view_table('products')
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
                if dict_2_delete == None:
                    continue
                delete_record('products',dict_2_delete)
            case _:
                print(wrongoption)


def couriers_menu():
    clear()
    print(pyfiglet.figlet_format('COURIER', font = 'starwars' ))
    time.sleep(1)
    while True:
        couriersmenuinput = input("---------------------------------------------------------\n\
Couriers Menu:\n\
    [0]...Return to Main Menu\n\
    [1]...View Couriers\n\
    [2]...Add New Courier\n\
    [3]...Update Existing Courier\n\
    [4]...Delete Existing Courier\n\
\nPlease type the number you would like to select: ")
        match couriersmenuinput:
            case '0':
                return
            case '1':
                view_table('couriers')
            case '2':
                new_courier = add_new('couriers')
                add_new_record('couriers', new_courier)
            case '3':
                updated_dictionary = update('couriers')
                if updated_dictionary == None:
                    continue
                update_record('couriers', updated_dictionary)
            case '4':
                dict_2_delete = dictionary_select('couriers')
                if dict_2_delete == None:
                    continue
                delete_record('couriers',dict_2_delete)
            case _:
                print(wrongoption)


def orders_menu():
    clear()
    print(pyfiglet.figlet_format('ORDER', font = 'starwars' ))
    time.sleep(1)
    while True:
        ordersmenuinput = input("------------------------------------\n\
Orders Menu:\n\
    [0]...Return to Main Menu\n\
    [1]...View Orders\n\
    [2]...Add New Order\n\
    [3]...Update Order Status\n\
    [4]...Update Existing Order\n\
    [5]...Delete Existing Order\n\
\nPlease type the number you would like to select: ")
        match ordersmenuinput:
                case '0':
                    return
                case '1':
                    view_table('orders')
                case '2':
                    new_order = add_new('orders')
                    add_new_record('orders', new_order)
                case '3':
                    updated_dictionary = update('orders', status = True)
                    if updated_dictionary == None:
                        continue
                    update_record('orders', updated_dictionary)
                case '4':
                    updated_dictionary = update('orders')
                    if updated_dictionary == None:
                        continue
                    update_record('orders', updated_dictionary)
                case '5':
                    dict_2_delete = dictionary_select('orders')
                    if dict_2_delete == None:
                        continue
                    delete_record('orders',dict_2_delete)
                case _:
                    print(wrongoption)


if __name__ == '__main__':
    main_menu()