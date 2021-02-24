# from flask import render_template
from src import app
#Para hace uso de la plantilla de rutas necesitamos importar la app creada en flask

@app.route('/contacto')
def contacto():
    return 'En contacto'