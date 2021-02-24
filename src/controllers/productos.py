#Para hace uso de la plantilla de rutas necesitamos importar la app creada en flask
from src import app
from src.models.productos import ProductosModel

@app.route('/productos')
def productos():
    productosModel = ProductosModel()

    productos = productosModel.traerTodos()

    print(productos)

    return 'En productos'