from flask import render_template

#Para hace uso de la plantilla de rutas necesitamos importar la app creada en flask
#Tambien importan el render template desde flask
from src import app

@app.route('/')
def index():
    return render_template('index.html')
