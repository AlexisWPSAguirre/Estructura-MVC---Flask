from flask import render_template, request, redirect, url_for
from src import app
from src.models.proyectos import ProyectosModel

@app.route("/proyectos/editar/<int:id>", methods=['GET','POST'])
def editar_proyecto(id):
    proyectosModel = ProyectosModel()
    if request.method == 'GET':
        print(id)
    print(id)
    return redirect(url_for('index'))
    
