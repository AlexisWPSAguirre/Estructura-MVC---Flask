import mariadb
from flask import render_template
import src.config.g as glo
from os import path

config = {
    'host': 'localhost',
    'port': 3308,
    'user': 'root',
    'password': '',
    'database': 'flask_mvc'
}

try: 
    glo.DB = mariadb.connect(**config)
    glo.DB.autocommit = True    
except: 
    glo.DB = False
    

class Bases():
    def conexion(nombre,usuario,contrasena,servidor,puerto):
        config = {
            'host': servidor,
            'port': puerto,
            'user': usuario,
            'password': contrasena,
            'database': nombre
        }
        try: 
            glo.DB = mariadb.connect(**config)
            glo.DB.autocommit = True    
        except: 
            glo.DB = False

    def instalarDB():
        SQL_PATH = path.abspath('DB.sql')
        file_sql = open(SQL_PATH, 'r')
        sql = file_sql.read()
        cursor = glo.DB.cursor()
        sqlCommands = sql.split(';')    
        for command in sqlCommands:
            try:
                if command.strip() != '':
                    cursor.execute(command)
            except:
                print ("Saltando comando")
        cursor.close()