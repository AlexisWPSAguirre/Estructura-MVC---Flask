# Ojo al dato xD, creo que como la función create_app está dentro del init no es necesario especificar src._init_.py 
from src import create_app

#Este main.py está encargado solo de arrancar la aplicación. 

#Se ejecuta solo cuando este modulo sea el principal es decir, cuando hayamos hecho click sobre este o inicializado
""" desde consola con su nombre, en este caso, "main.py """
if __name__ == '__main__':
    create_app()