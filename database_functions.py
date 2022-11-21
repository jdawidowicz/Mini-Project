import pymysql
import os
import string
from dotenv import load_dotenv

#make functions take/return dictionaries




def connect():
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")


    connection = pymysql.connect(
        host,
        user,
        password,
        database,
        cursorclass = pymysql.cursors.DictCursor
    )
    return connection

def disconnect(cursor,connection):
    cursor.close()
    connection.close()

def load_table(table): #returns list of dictionaries (lod)
    connection = connect()
    cursor = connection.cursor()
    
    cursor.execute(f'SELECT * FROM {table}')

    rows = cursor.fetchall()
    lod = []
    for row in rows:
        lod.append(row)
    
    disconnect(cursor,connection)
    return lod

def add_new_record(table, newdict):
    connection = connect()
    cursor = connection.cursor()

    keys = newdict.keys()
    keys = list(keys)
    sqlstr=''
    keystr = ''
    valuestr = ''
    
    for key in keys:
        try:
            value = float(newdict[key])
            valuestr += f',{value}'
        except:
            value = newdict[key]
            valuestr+= f",'{value}'"
        keystr += f',{key}'
    valuestr = valuestr.lstrip(',')
    keystr = keystr.lstrip(',')
    sqlstr = (f'INSERT INTO {table} ({keystr}) VALUES ({valuestr})')

    cursor.execute(sqlstr)
    connection.commit()
    
    disconnect(cursor,connection)

def delete_record(table, dictionary):
    connection = connect()
    cursor = connection.cursor()
    tablestr = table.rstrip('s')
    id_number = dictionary[f'{tablestr}_id']


    cursor.execute(f'DELETE FROM {table} WHERE {tablestr}_id = {id_number}')
    connection.commit()
    
    disconnect(cursor,connection)

def update_record(table, newdict):
    connection = connect()
    cursor = connection.cursor()
    tablestr = table.rstrip('s')
    keys = list(newdict.keys())
    id_number = newdict[f'{tablestr}_id']

    del keys[0]

    update_str=''
    for key in keys:
        try:
            value = float(newdict[key])
            update_str += f'{key} = {value},'
        except:
            value = newdict[key]
            update_str+= f"{key} = '{value}',"
    id_str = table.rstrip('s')
    update_str = update_str.rstrip(',')
    cursor.execute(f'UPDATE {table} SET {update_str} WHERE {id_str}_id = {id_number};')
    connection.commit()
    print('Record updated')
    disconnect(cursor,connection)
    

