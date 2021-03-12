# Ojo al dato xD, creo que como la función create_app está dentro del init no es necesario especificar src._init_.py 
from src import create_app, instalar
import os.path as path

if __name__ == '__main__':
    create_app()
#Se hace el funcionamiento normal del sistema
