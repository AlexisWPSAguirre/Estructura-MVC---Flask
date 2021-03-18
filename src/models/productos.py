import src.config.g as g

class ProductosModel():
    def traerTodos(self):
        #Instancia de conexion a la DB
        cursor = g.DB.cursor()
        #Entiendo que cursor es un objeto que ayuda a encontrar un resultado escecificado, 
        # primero empiezas por las bases disponibles, 
        """ Despues la tabla, condicion where y por ultimo un fetchall:Devuelve todo el array de resultados"""
        cursor.execute('select * from productos')
        productos = cursor.fetchall()
        cursor.close()

        return productos
    
    def crear(self, nombre,descripcion,val_venta,val_compra,ganancia,estado):
        cursor = g.DB.cursor()
        cursor.execute('insert into productos(nombre,descripcion,precio_venta,precio_compra,ganancia,estado) values(?,?,?,?,?,?)',(nombre,descripcion,val_venta,val_compra,ganancia,estado,))
        cursor.close()
    
    def consulta(self,id):
        cursor = g.DB.cursor()
        cursor.execute("""select * from productos where id = ?""",(id,))
        productos = cursor.fetchone()
        cursor.close()
        return productos

    def eliminar(self,id):
        cursor = g.DB.cursor()
        cursor.execute(""" DELETE FROM productos WHERE id = ? """,(id,))
        cursor.close()

    def editar(self,id,nombre,descripcion,val_compra,val_venta,val_ganancia,estado):
        cursor = g.DB.cursor()
        cursor.execute(""" UPDATE productos SET nombre=?, descripcion=?, precio_compra=?,
        precio_venta=?, ganancia=?, estado=? WHERE id=? """,(nombre,descripcion,val_compra,val_venta,val_ganancia,estado,id,))
        cursor.close()