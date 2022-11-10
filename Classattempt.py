import csv
statuslist = ["Preparing", "Delivered", "Out for Delivery"]
orders = []

class Order:

    def __init__(self, name, address, phone, status = "Preparing") -> None:
        self.name = name
        self.address = address
        self.phone = phone
        self.status = status

        self.info ={
            "Name" : self.name,
            "Address" : self.address,
            "Phone" : self.phone,
            "Status" : self.status
        }


    def delete(self):
        del self


    def update(self):
        print('For each of these values, type the new value or leave blank to keep the same')
        for key in self.info.keys:
            newvalue = input(f'{key}: {self.info[key]}. New {key}?\n')
            if newvalue == '':
                continue
            self.info[key] = newvalue
    

    def change_status(self, statusindex):
        self.status = statuslist[statusindex]
    
    def view(self):
        print(f'{self.info["Name"]}\t\t{self.info["Address"]}\t\t{self.info["Phone"]}\t{self.info["Status"]}')

order1 = Order("John", )


def orders_menu():
    orders_menu_input = input(("""-------------------
Orders Menu:
    0. Return to Main Menu
    1. View Orders
    2. Add New Order
    3. Update Order Status
    4. Update Existing Order
    5. Delete Existing Order
    """))
    match orders_menu_input:
        case "0":
            return
        case "1":
            print('-------------------')
            print('Index\t\tName\t\tAddress\t\t\tPhone\t\tStatus')
            for order in orders:
                print(order)
        case "2":
            print('hi')
        