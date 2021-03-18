import mariadb
from os import path
import json
import src.config.g as g

CONEXION_PATH = path.abspath('src/config/conexion.json')
SQL_PATH = path.abspath('DB.sql')

def installDB():
    fileSQL = open(SQL_PATH, 'r')
    sql = fileSQL.read()
    sqlCommands = sql.split(';')
    cursor = g.DB.cursor()
    for command in sqlCommands:
        try:
            if command.strip != '':
                cursor.execute(command)
        except:
            print('skip command')

def createDB():
    if path.exists(CONEXION_PATH):
        file_conexion = open(CONEXION_PATH, 'r')
        config = json.loads(file_conexion.read())
        g.DB = mariadb.connect(**config)
        g.DB.autocommit = True
    else:
        g.DB = False

createDB()