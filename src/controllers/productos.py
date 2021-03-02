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
    print(productos) 
    return render_template('productos/index.html',productos=productos)

@app.route('/productos/crear', methods=['GET','POST'])
#Estas funciones deben ser unicas en todo el sistema
def crear_producto():
    if request.method == 'GET':
        return render_template('productos/crear.html')

    nombre = request.form.get('nombre')   
    descripcion = request.form.get('descripcion')   
    val_venta = request.form.get('val_venta')   
    val_compra = request.form.get('val_compra')   
    estado = request.form.get('estado')   

    productosModel = ProductosModel()
    productosModel.crear(nombre,descripcion,val_venta,val_compra,estado)
    return redirect(url_for('productos'))
        