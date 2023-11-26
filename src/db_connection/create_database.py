# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 13:40:32 2023

@author: Heitor Nunes Rosa
@gmail: heitornunes12@gmail.com
@github: @hnrosa
"""

import mysql.connector 
from mysql.connector import Error
import csv
from creds import PASSWORD


def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")
        
def create_db(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name,
            autocommit = True
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def execute_query(connection, query, values = None):
    cursor = connection.cursor()
    try:
        cursor.execute(query, values)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")
        
# %%

server_connection = create_server_connection('localhost', 'root', PASSWORD)

# %%

create_database(server_connection, 'CREATE DATABASE icao')

# %%

db = create_db('localhost', 'root', PASSWORD, 'icao')


# %%

with db.cursor() as cur:
    
    cur.execute("""
            CREATE TABLE icao_specifications (
                NOME_FABRICANTE varchar(50),
                MODELO varchar(50),
                TIPO_ICAO varchar(20),
                ATERRISSAGEM varchar(50),
                TIPO_MOTORES varchar(50),
                NUM_MOTORES int,
                WTC varchar(5)
                );
            """)
            
    cur.execute("SHOW TABLES")
    
    print(cur.fetchall())
            


# %%

file_path = '../../data/raw/icao_categories.csv'

with open(file_path) as f:
    
    data = csv.reader(f, delimiter = ',')
    
    for i, row in enumerate(data):
        
        with db.cursor() as cur:
        
            if i == 0:
                continue
        
            if row[-2] == 'C':
                row[-2] = '1'
        
            row[-2] = int(row[-2])
        
            try:
                cur.execute("""
                            INSERT INTO icao_specifications(NOME_FABRICANTE,
                                                            MODELO,
                                                            TIPO_ICAO,
                                                            ATERRISSAGEM,
                                                            TIPO_MOTORES,
                                                            NUM_MOTORES,
                                                            WTC)
                            VALUES (%s, %s, %s, %s, %s, %s, %s);
                            """, row)
                            
                cur.execute("""SELECT * FROM icao_specifications NOME_FABRICANTE""")
                
                print(f'{len(cur.fetchall())} rows added.')
             
            except Error as err:  
                print(f'Insertion not occured due to {err}')
                
    db.commit()
# %%


    


            
