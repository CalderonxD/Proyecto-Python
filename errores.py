import datetime

def almacenar_error(error,archivo,lugar):
    tiempo = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(archivo,"a") as file:
        file.write(f"{tiempo} Error en {lugar}: {error} \n")

nombre_archivo = "errores.txt"