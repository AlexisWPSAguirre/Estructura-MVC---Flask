import src.config.g as g

class ProyectosModel():
    def traerTodos(self):
        cursor = g.DB.cursor()
        cursor.execute("""
        SELECT 
        a.id,
        a.no_proyecto,
        a.proceso,
        a.fecha_iniciacion,
        a.fecha_terminacion,
        a.fecha_liquidacion,
        a.supervision_interventoria,
        b.nombre,
        a.proceso,
        b.nit
        FROM proyecto a 
        INNER JOIN contratista b ON b.id = a.contratista_fk
        """)
        proyecto = cursor.fetchall()
        cursor.close()
        return proyecto 