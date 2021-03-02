from src.config.db import DB

class ProductosModel():
    def traerTodos(self):
        #Instancia de conexion a la DB
        cursor = DB.cursor()
        #Entiendo que cursor es un objeto que ayuda a encontrar un resultado escecificado, 
        # primero empiezas por las bases disponibles, 
        """ Despues la tabla, condicion where y por ultimo un fetchall:Devuelve todo el array de resultados"""
        cursor.execute('select * from productos')
        productos = cursor.fetchall()
        cursor.close()

        return productos
    
    def crear(self, nombre,descripcion,val_venta,val_compra,estado):
        cursor = DB.cursor()
        cursor.execute('insert into productos(nombre,descripcion,precio_venta,precio_compra,estado) values(?,?,?,?,?)',(nombre,descripcion,val_venta,val_compra,estado,))
        cursor.close()