from database_functions import load_table

wrongoption = ('Please try again and select a valid menu option')

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


#Function to list data from a table, and take user input to select an item. Returns a dictionary
def dictionary_select(table_name):
    lod = load_table(table_name)
    id_str = table_name.rstrip('s')
    view_list(lod)
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
        if key == f'{id_str}_id':
            continue
        elif key == "status" : 
            newdict["status"] = "Preparing" 
            print('Status set to Preparing')
            continue
        elif key == "products":
            products = load_table('products')
            view_list(products)
            print('Input ID values separated by commas')
        elif key == "courier":
            couriers = load_table('couriers')
            view_list(couriers)
            print('Please select courier ID')
        while True:
            value = input(f'Please enter the {key}: ')
            if value == '':
                print('Empty field not allowed')
                continue
            break
        newdict[key] = value
    print('New entry successfully added')    
    return newdict


#Function to update existing dictionary from a table, returns updated dictionary
#If status is set to true, only updates order status
def update(table_name, status = False, input2 = input):
        sdict = dictionary_select(table_name)
        id_str = table_name.rstrip('s')
        id_no = sdict[f'{id_str}_id']
        
        if sdict == None:
            print('Valid record not selected, returning to menu...')
            return

        if status == True:
            statuslist = load_table('order_status')
            print(f'You have selected order no. {id_no}, with status: {sdict["status"]}.\
            Please select the new status.\n')
            view_list(statuslist)
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
        for key in sdict.keys(): 
            if key == f'{id_str}_id':
                continue
            newvalue = input2(f'Current {key}: {sdict[key]}. New {key}?\n')
            if newvalue != '':
                sdict[key] = newvalue
        return sdict
