# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 17:54:34 2023

@author: Heitor Nunes Rosa
@gmail: heitornunes12@gmail.com
@github: @hnrosa
"""

import mysql.connector 
from mysql.connector import Error
import pandas as pd
import warnings
from creds import PASSWORD
warnings.filterwarnings('ignore')

def create_db_connection(host_name, user_name, user_password, db_name):
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

db = create_db_connection('localhost', 'root', PASSWORD, 'icao')

# %%

with db.cursor() as c:
    
    c.execute("""SELECT NOME_FABRICANTE FROM icao_specifications""")
    
    print('Number of Rows: ', len(c.fetchall()))

# %%

update_type = """
UPDATE icao_specifications
SET TIPO_MOTORES = CASE
    WHEN TIPO_MOTORES = "Piston" THEN "Pistão"
    WHEN TIPO_MOTORES = "Jet" THEN "Jato"
    WHEN TIPO_MOTORES = "Turboprop/Turboshaft" THEN "Turbo-Hélice"
    WHEN TIPO_MOTORES = "Rocket" THEN "Foguete"
    WHEN TIPO_MOTORES = "Electric" THEN "Elétrico"
    ELSE TIPO_MOTORES
    END;
"""

update_land = """
UPDATE icao_specifications
SET ATERRISSAGEM = CASE
    WHEN ATERRISSAGEM  = "LandPlane" THEN "Terrestre"
    WHEN ATERRISSAGEM  = "Helicopter" THEN "Helicóptero"
    WHEN ATERRISSAGEM  = "Amphibian" THEN "Anfíbio"
    WHEN ATERRISSAGEM  = "Gyrocopter" THEN "Girocóptero"
    WHEN ATERRISSAGEM  = "SeaPlane" THEN "Aquático"
    ELSE ATERRISSAGEM
    END;
"""

with db.cursor() as c:
    c.execute(update_land)
    c.execute(update_type)
    db.commit()

# %%

create_manufactures = """ 
CREATE TABLE icao_manufactures AS (
SELECT
    NOME_FABRICANTE,
    COUNT(TIPO_ICAO) AS NUM_ICAO,
    GROUP_CONCAT(DISTINCT NUM_MOTORES, '') AS NUMS_MOTORES,
    GROUP_CONCAT(DISTINCT TIPO_MOTORES, '') AS TIPOS_MOTORES,
    GROUP_CONCAT(DISTINCT ATERRISSAGEM, '') AS ATERRISSAGENS,
    GROUP_CONCAT(DISTINCT WTC, '') AS WTCS
FROM
    icao_specifications
GROUP BY
    NOME_FABRICANTE
);
"""

with db.cursor() as c:
    c.execute(create_manufactures)
    db.commit()
    
# %%

with db.cursor() as c:
    c.execute("SHOW TABLES")
    print(c.fetchall())

# %%
                  
df = pd.read_sql_query("""SELECT * FROM icao_specifications""", db)

tb = df.loc[:, ['NOME_FABRICANTE', 'TIPO_ICAO']]

tb_dd = tb.drop_duplicates()
