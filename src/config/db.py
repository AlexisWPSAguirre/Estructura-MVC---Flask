import mariadb

config = {
    'host': 'localhost',
    'port': 3308,
    'user': 'root',
    'password': '',
    'database': 'flask_mvc'
}
#**config envia los atributos de un diccionario como parametros de una función
DB = mariadb.connect(**config)
#Para poder comitar las consultas, para que no queden en cache los cambios en DB
DB.autocommit = True