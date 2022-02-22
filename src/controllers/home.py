from flask import render_template,request, redirect, url_for
import src.config.g as g
from src import app
from src.models.proyectos import ProyectosModel
from src.config.db import createDB, installDB
import json

#Para hace uso de la plantilla de rutas necesitamos importar la app creada en flask
#Tambien importan el render template desde flask
@app.route('/')
def index():
    if(g.DB == False):
        return render_template('instalacion.html')
    proyectosModel = ProyectosModel()
    proyectos = proyectosModel.traerTodos()
    return render_template('contratos/index_proyectos.html', proyectos = proyectos)
    
@app.route('/instalacion', methods=['GET','POST'])
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
        return render_template('contratos/index_contratos.html')

    



