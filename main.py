#imports
from funciones import *
from datos import *
from menu import *
from errores import *



RUTA_JSON = "usuarios.json"
datos = bajar_datos(RUTA_JSON)  

ejecutable(datos)