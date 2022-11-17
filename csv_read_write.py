import os
import csv

def load_csv(filename): #loads csv file, returns a list of dictionaries
    newlist =[]
    path = os.path.realpath(f'{filename}.csv')
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            newlist.append(row)
    return newlist

def write_csv(filename, list):#Writes all data from list to a csv file in the same format as it reads
    path = os.path.realpath(f'{filename}.csv')
    keys=[]
    for key in list[0].keys():
        keys.append(key)
    with open(path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(list)