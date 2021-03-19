from flask import render_template,request, redirect, url_for
import src.config.g as g
from src import app
from src.config.db import createDB, installDB,listarBases,listarTablas
import json
#Para hace uso de la plantilla de rutas necesitamos importar la app creada en flask
#Tambien importan el render template desde flask
bases = []
@app.route('/')
def index():
    if(g.DB == False):
        return render_template('instalacion.html')
    return render_template('mariadb/index.html')
    
@app.route('/Gui', methods=['GET','POST'])
def instalar():
    if request.method == 'GET':
        return render_template('mariadb/index.html',bases = bases)

    user = request.form.get('usuario')   
    password = request.form.get('contrasena')  
    server = request.form.get('servidor') 
    port = request.form.get('puerto') 
    dbData = {
    'host' : server,
    'port' : int(port),
    'user' : user,
    'password' : password
    }
    file = open('src/config/conexion.json', 'w')
    file.write(json.dumps(dbData))
    file.close()
    createDB()
    bases = listarBases()
    return render_template('mariadb/index.html',bases = bases)

    
    
@app.route('/Gui/MariaDB/<id>', methods=['GET','POST'])
def listarDB(id):
    print(id)
    tables = listarTablas(id)
    print(tables)
    return render_template('mariadb/tablas.html', tables = tables)




