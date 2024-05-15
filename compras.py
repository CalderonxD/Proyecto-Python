from datetime import datetime

def guardar_servicio(usuario, servicio):
    with open("compras.txt", "a") as archivo:
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        registro = (
            f"Fecha y Hora: {fecha_hora}, Usuario ID: {usuario['id']}, "
            f" COMPRA DE SERVICIO:"
            f"Servicio: {servicio['nombre']}, Precio: {servicio['precio']}, "
            f"Tipo: {servicio['tipo']}, Vigencia: {servicio['dias']} dias\n"
        )
        archivo.write(registro)
        
def guardar_producto(usuario,producto):
    with open("compras.txt", "a") as archivo:
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        registro = (
            f"Fecha y Hora: {fecha_hora}, Usuario ID: {usuario['id']},"
            f" COMPRA DE PRODUCTO:"
            f"Producto: {producto["nombre"]}, Precio: {producto["precio"]}"
        )
        archivo.write(registro)