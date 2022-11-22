from csv_read_write import load_csv

wrongoption = ('Please try again and select a valid menu option')
statuslist = ["Preparing", "Delivered", "Out for Delivery"] 
products = load_csv("products") #read csv's into lists
orders = load_csv("orders")
couriers = load_csv("couriers")


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
            print('Status set to Preparing')
            continue
        elif key == "Products":
            view_list(products)
            print('Input index values separated by commas')
        elif key == "Courier":
            view_list(couriers)
            print('Please select index value')
        while True:
            value = input(f'Please enter the {key}: ')
            if input == '':
                print('Empty field not allowed')
                continue
            break
        newdict[key] = value
    list.append(newdict)
    print('New entry successfully added')    


def update(list, status = False, input1 = input, input2 = input): #Function to update existing item in a list, for just order status update, status is set to True
        view_list(list)
        try: #try except clause to handle index errors
            index = int(input1('---------------------------------------------------------\n\
    Please select the index of the data you would like to update: '))
            sdict = list[index]
        except:
            print('That is not a valid choice.\nReturning to menu...')
            return #returns to menu if incorrect input

        if status == True: #if status is set to true in args, just status of an order is changed
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
        for key in sdict.keys(): #Takes input to update each column, blank leaves it the same
            newvalue = input2(f'Current {key}: {sdict[key]}. New {key}?\n')
            if newvalue != '':
                sdict[key] = newvalue


def delete_from(list, input = input): #Function to delete item from a list
    view_list(list)
    try: # try except to handle index errors
        index = int(input('---------------------------------------------------------\n\
Please select the index of the entry you would like to delete: '))
        del list[index]
        print(f'Entry no.{index} successfully deleted')
    except:
        print('That is not a valid choice.\nReturning to menu...')    
    