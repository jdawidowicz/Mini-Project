from database_functions import load_table
import pandas as pd
from tabulate import tabulate 
wrongoption = ('Please try again and select a valid menu option')

#Function to display records in a nice table
def view_table(table_name):
    lod = load_table(table_name)
    headers = lod[0].keys()
    df = pd.DataFrame(data=lod)
    print(tabulate(df, headers=headers, showindex = False, tablefmt = 'mixed_grid'))



#Function to list data from a table, and take user input to select an item. Returns a dictionary
def dictionary_select(table_name):
    lod = load_table(table_name)
    #id_str is just formatting for ID columns
    id_str = table_name.rstrip('s')
    view_table(table_name)
    #try except clause to handle input errors
    try: 
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


#Function to take user input for table headers, returns a dictionary
def add_new(table_name, input=input):
    newdict={}
    table = load_table(table_name)
    id_str = table_name.rstrip('s')
    for key in table[0].keys():
        #If statements for extra information, i.e to display courier list when selecting courier,
        #or automatically set status to "Preparing" for new order
        keyfmt = key.title().replace('_',' ')
        if key == f'{id_str}_id':
            continue
        elif key == "status" : 
            newdict["status"] = "Preparing" 
            print('Status set to Preparing')
            continue
        elif key == "products":
            view_table('products')
            print('Input ID values separated by commas')
        elif key == "courier":
            view_table('couriers')
            print('Please select courier ID')
        while True:
            value = input(f'\nPlease enter the {keyfmt}: ')
            if value == '':
                print('Empty field not allowed')
                continue
            break
        newdict[key] = value
    print('New entry successfully added')    
    return newdict


#Function to update existing dictionary from a table, returns updated dictionary
#If status is set to true, only updates order status
def update(table_name, updatestatus = False, input2 = input):
        sdict = dictionary_select(table_name)
        id_str = table_name.rstrip('s')
        id_no = sdict[f'{id_str}_id']
        
        if sdict == None:
            print('Valid record not selected, returning to menu...')
            return
        
        if updatestatus == False:

            print(f'You have selected no. {id_no}.\nFor each of the following columns, please input a new value or leave blank to keep the same.')
            for key in sdict.keys(): 
                if key == f'{id_str}_id':
                    continue
                elif key == 'status':
                    updatestatus = True
                    break

                keyfmt = key.title().replace('_',' ')
                newvalue = input2(f'Current {keyfmt}: {sdict[key]}. \nNew {keyfmt}:\n')
                if newvalue != '':
                    sdict[key] = newvalue

        if updatestatus == True:

            statuslist = load_table('order_status')
            print(f'You have selected order no. {id_no}, with status: {sdict["status"]}.')
            view_table('order_status')
            print('Please select the new status ID:')
            while True:
                try:
                    statusinput = int(input2(''))
                    if statusinput == '':
                        break
                    for status in statuslist:
                        if statusinput == status['id']:
                            sdict["status"] = status['order_status']
                    print(f'Status successfully changed to {sdict["status"]}')
                    return sdict
                except:
                    print(wrongoption)
                    continue        
        return sdict
