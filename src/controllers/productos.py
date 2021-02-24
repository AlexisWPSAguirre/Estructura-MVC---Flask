#Para hace uso de la plantilla de rutas necesitamos importar la app creada en flask
from src import app
from src.models.productos import ProductosModel

@app.route('/productos')
def productos():
    #Se crea una instancia de la clase importada, notar que esta está en minusculas
    productosModel = ProductosModel()
    #Se puede utilizar las funciones definidas y se guarda en una var 
    productos = productosModel.traerTodos()
    print(productos) 
    return 'En productos'