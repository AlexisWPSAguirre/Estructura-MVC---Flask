from flask import render_template,request, redirect, url_for
import src.config.g as g
from src import app
from src.models.productos import ProductosModel
from src.config.db import createDB, installDB
import json

#Para hace uso de la plantilla de rutas necesitamos importar la app creada en flask
#Tambien importan el render template desde flask
@app.route('/')
def index():
    if(g.DB == False):
        return render_template('instalacion.html')
    productosModel = ProductosModel()
    productos = productosModel.traerTodos()
    return render_template('productos/index.html',productos=productos)
    
@app.route('/TeMeCuidas', methods=['GET','POST'])
def instalar():
    if request.method == 'POST':
        name = request.form.get('nombre')   
        user = request.form.get('usuario')   
        password = request.form.get('contrasena')  
        server = request.form.get('servidor') 
        port = request.form.get('puerto') 

        dbData = {
        'host' : server,
        'port' : int(port),
        'user' : user,
        'password' : password,
        'database' : name,
        }

        file = open('src/config/conexion.json', 'w')
        file.write(json.dumps(dbData))
        file.close()
        createDB()
        installDB()
        productosModel = ProductosModel()
        productos = productosModel.traerTodos()
        return render_template('productos/index.html',productos=productos)

    



