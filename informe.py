#GENERAR INFORME DE PRODUCTOS A LA VENTA
def informe(datos):
    with open("informe.txt", "w") as archivo:
        archivo.write("Servicios ofrecidos:\n")

        archivo.write("PREPAGO:\n")
        for temp in datos["servicios_prepago"]:
            archivo.write(f"Nombre: {temp['nombre']}, Precio: {temp['precio']}, Tamaño: {temp.get('tamano', 'N/A')}, Vigencia: {temp.get('dias', 'N/A')} dias, Tipo: {temp.get('tipo', 'N/A')}\n")

        archivo.write("\nPOSTPAGO:\n")
        for temp in datos["servicios_postpago"]:
            archivo.write(f"Nombre: {temp['nombre']}, Precio: {temp['precio']}, Tamaño: {temp.get('tamano', 'N/A')}, Vigencia: {temp.get('dias', 'N/A')} dias, Tipo: {temp.get('tipo', 'N/A')}\n")

        archivo.write("\nPRODUCTOS\n")
        for temp in datos["productos"]:
            archivo.write(f"Nombre: {temp['nombre']}, Marca: {temp['marca']}, Caracteristicas: {temp['caracteristicas']}, Precio: {temp['precio']}\n")
            
#GENERAR INFORME DE CANTIDAD DE PRODUCTOS VENDIDOS
def ventas(datos):
    with open("ventas.txt", "w") as archivo:
        archivo.write("Conteo de ventas por usuarios:\n\n")
        
        for usuario in datos["usuarios"]:
            nombre_usuario = usuario["nombre"]
            id_usuario = usuario["id"]
            
            servicios = usuario.get("servicios", [])
            productos = usuario.get("Productos", [])

            # Contar servicios
            conteo_servicios = {}
            for servicio in servicios:
                nombre_servicio = servicio["nombre"]
                if nombre_servicio in conteo_servicios:
                    conteo_servicios[nombre_servicio] += 1
                else:
                    conteo_servicios[nombre_servicio] = 1

            # Contar productos
            conteo_productos = {}
            for producto in productos:
                nombre_producto = producto["nombre"]
                if nombre_producto in conteo_productos:
                    conteo_productos[nombre_producto] += 1
                else:
                    conteo_productos[nombre_producto] = 1

            # Escribir información del usuario
            archivo.write(f"Usuario: {nombre_usuario}\n")
            archivo.write(f"ID: {id_usuario}\n")
            
            # Escribir servicios contratados
            archivo.write("Servicios contratados:\n")
            if conteo_servicios:
                for nombre_servicio, cantidad in conteo_servicios.items():
                    archivo.write(f"  - {nombre_servicio}: {cantidad} vez/veces\n")
            else:
                archivo.write("  No tiene servicios contratados\n")
            
            # Escribir productos comprados
            archivo.write("Productos comprados:\n")
            if conteo_productos:
                for nombre_producto, cantidad in conteo_productos.items():
                    archivo.write(f"  - {nombre_producto}: {cantidad} vez/veces\n")
            else:
                archivo.write("  No tiene productos comprados\n")
            
            archivo.write("\n")
            
