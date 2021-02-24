#Este código predeterminado es necesario para que se entienda el * (Importar todo) 
import os, glob
__all__ = [os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")]