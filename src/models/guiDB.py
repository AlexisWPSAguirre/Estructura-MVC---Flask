import mariadb
import src.config.g as g
from src.config.db import createDB

class guiDBModel():
    consBase = 'darVolverAtras:3'
    def listarBases(self):
        bases = []
        cursor = g.DB.cursor()
        cursor.execute('show databases')
        for base in cursor:
            bases.append(base)
        g.DB.close()
        return bases

    def listarTablas(self,base): 
        self.consBase = base
        tables = []
        createDB()
        cursor = g.DB.cursor()
        query = "USE " + base
        cursor.execute(query)
        cursor.execute("SHOW TABLES")
        for table in cursor:
            tables.append(table)
        g.DB.close()
        return tables

    def describirTablas(self,tablas):
        describe = []
        createDB()
        cursor = g.DB.cursor()
        query = "USE "+ self.consBase
        cursor.execute(query)
        for tabla in tablas: 
            query = "DESCRIBE "+ tabla[0]
            cursor.execute(query)
            desc = cursor.fetchall()
            describe.append(desc)
        g.DB.close() 
        return describe

    def registrosTablas(self,tabla):
        registros = []
        createDB()
        cursor = g.DB.cursor()
        query = "USE "+ self.consBase
        cursor.execute(query)
        query = "SELECT * FROM "+ tabla
        cursor.execute(query)
        registros = cursor.fetchall()
        g.DB.close()
        return registros
