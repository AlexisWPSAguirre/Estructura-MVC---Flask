from flask import render_template,request, redirect, url_for
import src.config.g as glo
from src import app
from src.models.productos import ProductosModel


from src.config.db import Bases
#Para hace uso de la plantilla de rutas necesitamos importar la app creada en flask
#Tambien importan el render template desde flask
@app.route('/')
def index():
    if(glo.DB == False):
        return render_template('instalacion.html')
    productosModel = ProductosModel()
    productos = productosModel.traerTodos()
    return render_template('productos/index.html',productos=productos)
    
@app.route('/productosss', methods=['GET','POST'])
def instalar():
    if request.method == 'POST':
        nombre = request.form.get('nombre')   
        usuario = request.form.get('usuario')   
        contrasena = request.form.get('contrasena')  
        servidor = request.form.get('servidor') 
        puerto = request.form.get('puerto') 
        puerto = int(puerto)

        Bases.conexion(nombre,usuario,contrasena,servidor,puerto)    
        Bases.instalarDB()
        productosModel = ProductosModel()
        productos = productosModel.traerTodos()
        return render_template('productos/index.html',productos=productos)

    



