Background.

The client for this mini project was a business in the food industry, looking for a system to store data about their orders and customers.
The system I designed operates from the terminal to meet these specifications.

'''
Requirements
As a business:
•I want to maintain a collection of products and couriers.
•When a customer makes a new order, I need to create this on the
system.
•I need to be able to update the status of an order i.e: preparing,
out-for-delivery, delivered.
•When I exit my app, I need all data to be persisted and not lost.
•When I start my app, I need to load all persisted data.
•I need to be sure my app has been tested and proven to work well.
•I need to receive regular software updates.
'''

The design consists of 2 main objects; firstly a database to store all data, and secondly a menu system in the terminal to provide an easy to use interface for the database.

These 2 objects are divided further for ease of use, the database has 3 tables to store and edit data about orders, products, and couriers.
There is a 4th table which stores an order status list however remains static.

The menu system is divided into 3 sub menus, corresponding to the relevant tables i.e orders menu, products menu, and couriers menu.
In the sub menu, various operations can be used as need, 
for example to view the records stored, add a new record and update or delete existing records.
The orders menu also has an additional option to change just the status of any order.

All data is persisted with the database, and is updated 'in real-time' as any command is executed.
There is also an option to export a back up of the data onto csv files.

I have kept the program as simple as possible. Since every record is read as a dictionary with different keys,
all functions have been made to either process dictionaries or output dictionaries, and the same core functions are applied throughout the menus. 
These are individually tested to gurantee functionality, and the simplicity ensures that any future improvements or fixes are quick and easy to implement.


If I had more time, the main thing I would do is more unit testing on the database related functions, as I found myself struggling to write these; and also add an option to import csv data as I found myself scratching my head on how I could factor that feature in regarding the clash with the database.

The most fun I had was certainly refactoring. I started with a very janky program with lots of copy-paste, and to get it down to just a dozen general functions retaining full functionality was very satisfying. I was particularly happy with getting sql statements working for any desired table with f strings. 

