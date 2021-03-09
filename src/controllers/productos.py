#Para hace uso de la plantilla de rutas necesitamos importar la app creada en flask
from flask import render_template, request, redirect, url_for
from src import app
from src.models.productos import ProductosModel

@app.route('/productos')
def productos():
    #Se crea una instancia de la clase importada, notar que esta está en minusculas
    productosModel = ProductosModel()
    #Se puede utilizar las funciones definidas y se guarda en una var 
    productos = productosModel.traerTodos()
    return render_template('productos/index.html',productos=productos)

@app.route('/productos/crear', methods=['GET','POST'])
#Estas funciones deben ser unicas en todo el sistema
def crear_producto():
    if request.method == 'GET':
        return render_template('productos/crear.html')

    nombre = request.form.get('nombre')   
    descripcion = request.form.get('descripcion')   
    val_compra = request.form.get('val_compra')  
    val_venta = request.form.get('val_venta')   
    val_ganancia = request.form.get('ganancia') 
    estado = request.form.get('estado')   

    productosModel = ProductosModel()
    productosModel.crear(nombre,descripcion,val_venta,val_compra,val_ganancia,estado)
    return redirect(url_for('productos'))

@app.route('/productos/editar/<int:id>', methods=['GET','POST'])
def editar_producto(id):
    productosModel = ProductosModel()
    if request.method == 'GET':
        productos = productosModel.consulta(id)  
        return render_template('productos/editar.html', productos = productos)
    nombre = request.form.get('nombre')   
    descripcion = request.form.get('descripcion')   
    val_compra = request.form.get('val_compra')  
    val_venta = request.form.get('val_venta')   
    val_ganancia = request.form.get('ganancia') 
    estado = request.form.get('estado')
    productosModel.editar(id,nombre,descripcion,val_compra,val_venta,val_ganancia,estado)
    return redirect(url_for('productos'))
    

@app.route('/productos/eliminar/<int:id>')
def eliminar_producto(id):
    productosModel = ProductosModel()
    productosModel.eliminar(id)
    return redirect(url_for('productos'))
        