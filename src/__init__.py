from flask import Flask
""" Al ser el archivo que se inicia cuando se importa un modulo, se le encarga la FUNCIÓN de crear la aplicación
más no de arrancar el programa """
#Cambia la carpeta de templates raíz, a views para seguir con el MVC
app = Flask(__name__, template_folder='views')

# Importando Controllers
# Se crea un archivo init para que lo reconozca como paquete
from src.controllers import *

def create_app():
    app.run(debug=True)