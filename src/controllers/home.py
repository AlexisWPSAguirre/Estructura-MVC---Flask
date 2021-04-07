from flask import render_template,request, redirect, url_for
import src.config.g as g
from src import app
from src.config.db import createDB, installDB
from src.models.guiDB import guiDBModel
import json
#Para hace uso de la plantilla de rutas necesitamos importar la app creada en flask
#Tambien importan el render template desde flask
bases = []
describes = []
GUIDBMODEL = guiDBModel()
@app.route('/')
def index():
    if(g.DB == False):
        return render_template('instalacion.html')
    GUIDBMODEL = guiDBModel()
    global bases
    bases = GUIDBMODEL.listarBases()
    return render_template('mariadb/index.html',bases = bases)
    
@app.route('/Gui', methods=['GET','POST'])
def instalar():
    if request.method == 'GET':
        return redirect(url_for('instalar'))

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
    global bases
    bases = GUIDBMODEL.listarBases()
    return render_template('mariadb/index.html',bases = bases)

    
    
@app.route('/Gui/MariaDB/<id>', methods=['GET','POST'])
def listarDB(id):
    tablas = GUIDBMODEL.listarTablas(id)
    global describes
    describes = GUIDBMODEL.describirTablas(tablas)
    return render_template('mariadb/tablas.html', tablas = tablas, bases = bases, describes = describes)

@app.route('/Gui/MariaDB/Registros/<id>/<int:cont>')
def registrosTB(id,cont):
    registros = GUIDBMODEL.registrosTablas(id)
    return render_template('mariadb/registros.html', registros = registros, bases = bases, describe = describes[cont])
    






