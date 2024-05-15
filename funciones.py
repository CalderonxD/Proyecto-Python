from menu import *
from errores import *
from compras import *

#MAIN
def ejecutable(datos): 
    opc = 0
    while True:  
        menu_principal(datos) 
        try:
            opc = int(input("-"))
            if opc not in [1,2,3]:
                raise ValueError("Opcion invalida")
        except Exception as e:
            lugar = "Menu Inicial"
            almacenar_error(e,nombre_archivo,lugar)
            print("Opción no valida")
        else:
            if opc == 1:
                datos = bajar_datos(RUTA_JSON)
                datos = opcion_sesion(datos) 
                break  
            elif opc == 2:
                datos = bajar_datos(RUTA_JSON)
                datos = registrarUsuario(datos)
                subir_datos(datos,RUTA_JSON)
            elif opc == 3:
                print("--------------------SALIENDO---------------------")
                break

    subir_datos(datos,RUTA_JSON)
    
    
#OPCION SESION EN INICIAR SESION
def opcion_sesion(datos):
    while True:
        try:
            usuario = int(input("Ingrese su id o cedula: "))
        except ValueError as e:
            lugar = "Iniciar Sesion"
            almacenar_error(e, nombre_archivo, lugar)
            print("Por favor ingrese un número")
        else:
            usuario_encontrado = False
            for usuario_info in datos["usuarios"]:
                if usuario_info["id"] == str(usuario):
                    usuario_encontrado = True
                    if usuario_info["rol"] == "Admin":
                        menu_admin(datos)
                        return datos
                    elif usuario_info["rol"] == "Cliente":
                        menu_usuario(datos)
                        return datos
                    break
                
            if not usuario_encontrado:
                print("Usuario equivocado o no registrado.")
        return datos
    
    
    
#VER RECOMENDACIONES
def recomendaciones(datos):
    ""
    

#CRUD USUARIOS

#REGISTRAR USUARIO
def registrarUsuario(datos):
    print("-------------------------------------------------")
    print("\n-----------BIENVENIDO AL REGISTRO--------------\n")
    print("-------------------------------------------------")
    usuario = {}
    usuario["nombre"] = input("Ingrese el nombre: ")
    print("-------------------------------------------------")
    usuario["numero"] = input("Ingrese su numero: ")
    print("-------------------------------------------------")
    usuario["id"] = input("Ingrese su cedula: ")
    print("-------------------------------------------------")
    usuario["direccion"] = input("Ingrese su direccion de residencia: ")
    print("-------------------------------------------------")
    usuario["ciudad"] = input("Ingrese su ciudad de residencia: ")
    print("-------------------------------------------------")
    usuario["categoria"] = ""
    usuario["rol"] = "Cliente"
    
    for usuario_existente in datos["usuarios"]:  #VERIFICAR SI EL USUARIO EXISTE
        if "id" in usuario_existente and usuario["id"] == usuario_existente["id"]:  #verificar si cedula ya fue registrada
            print("Esta cedula ya ha sido registrada")  
            return datos  
    datos["usuarios"].append(usuario)
    print("Usuario registrado con éxito")
    ("-------------------------------------------------")
    return datos

#CREAR USUARIO DESDE ADMIN
def crearUsuarioDesdeAdmin(datos):
    print("-------------------------------------------------")
    print("\n---------------CREANDO USUARIO------------------\n")
    print("-------------------------------------------------")
    usuario = {}
    usuario["nombre"] = input("Ingrese el nombre: ")
    print("-------------------------------------------------")
    usuario["numero"] = input("Ingrese el numero: ")
    print("-------------------------------------------------")
    usuario["id"] = input("Ingrese la cedula: ")
    print("-------------------------------------------------")
    usuario["direccion"] = input("Ingrese la direccion de residencia: ")
    print("-------------------------------------------------")
    usuario["ciudad"] = input("Ingrese la ciudad de residencia: ")
    print("-------------------------------------------------")
    usuario["categoria"] = ""
    rol = input("ingrese el rol del usuario(Cliente o Admin)")
    usuario["rol"] = rol.capitalize()
    for usuario_existente in datos["usuarios"]:  #VERIFICAR SI EL USUARIO EXISTE
        if "id" in usuario_existente and usuario["id"] == usuario_existente["id"]:  #verificar si cedula ya fue registrada
            print("Esta cedula ya ha sido registrada")  
            return datos  
    datos["usuarios"].append(usuario)
    print("Usuario registrado con éxito")
    
    return datos

#LEER USUARIO
def leer_usuario(datos):
    repetir = True
    while repetir:
        for usuario in datos["usuarios"]:
            print(f"usuario: {usuario["nombre"]} - id:{usuario["id"]}")
        
        usuario_id = input("Ingrese el id o cedula del usuario: ")
        print(f"Informacion del Usuario {usuario_id}:")
        
        usuario_encontrado = False
        
        for usuario in datos["usuarios"]:
            if usuario_id == usuario["id"]:
                print(f"{usuario}")
                usuario_encontrado = True
                break
            
        if usuario_encontrado == False:
            print("No existe este usuario")
                
        repetir = int(input("Desea leer otro usuario? (1.si, 0.no)"))
        if repetir  == False:
                    return datos    
        

#ACTUALIZAR USUARIO

def actualizar_usuario(datos):
    # Muestra la lista de usuarios
    for usuario in datos["usuarios"]:
        print(f"usuario: {usuario['nombre']} - id: {usuario['id']}")
    
    while True:
        try:
            # Pide el ID del usuario a actualizar
            usuario_id = input("Ingrese el id o cedula del usuario que desea actualizar: ")
        except Exception as e:
            lugar = "Menu Admin,Actualizar usuario,id"
            almacenar_error(e, nombre_archivo, lugar)
            print("Ingrese un valor válido.")
        else:
            # Busca el usuario con el ID proporcionado
            for i in range(len(datos["usuarios"])):
                if usuario_id == datos["usuarios"][i]["id"]:
                    usuario = datos["usuarios"][i]
                    while True:
                        opc = input("Ingrese el campo que desea actualizar (nombre, numero, direccion, ciudad) o 'x' para salir: ").lower()
                        if opc == "nombre":
                            usuario["nombre"] = input("Ingrese el nombre: ")
                            print("¡El nombre del usuario ha sido actualizado!")
                        elif opc == "numero":
                            usuario["numero"] = input("Ingrese el número: ")
                            print("¡El número del usuario ha sido actualizado!")
                        elif opc == "direccion":
                            usuario["direccion"] = input("Ingrese su dirección de residencia: ")
                            print("¡La dirección del usuario ha sido actualizada!")
                        elif opc == "ciudad":
                            usuario["ciudad"] = input("Ingrese su ciudad de residencia: ")
                            print("¡La ciudad del usuario ha sido actualizada!")
                        elif opc == "x":
                            print("Datos guardados. Saliendo.")
                            return datos  # Salir después de guardar los cambios
                        else:
                            print("Opción no válida. Intente de nuevo.")
                    break
            else:
                print("Usuario no encontrado. Intente de nuevo.")

            return datos


#ELIMINAR USUARIO
def eliminar_usuario(datos):
    for usuario in datos["usuarios"]:
        print(f"usuario: {usuario["nombre"]} - id:{usuario["id"]}")
   
    while True:
        numero = input("Escriba el id del usuario que desea eliminar: ")
        for usuario in datos["usuarios"]:
            if usuario["id"] == numero:
                datos["usuarios"].remove(usuario)
                print(f"El usuario {usuario.get("nombre")} ha sido eliminado!")
                return datos
        
            

#ASIGNAR CATEGORIA
def asignar_categoria(datos):
    for usuario in datos["usuarios"]:
        print(f"usuario: {usuario['nombre']} - id: {usuario['id']}")

    while True:
        try:
            # Pide el ID del usuario a actualizar
            usuario_id = input("Ingrese el id o cedula del usuario que desea actualizar: ")
        except Exception as e:
            lugar = "Menu Admin,Actualizar usuario,id"
            almacenar_error(e, nombre_archivo, lugar)
            print("Ingrese un valor válido.")
        else:
            # Busca el usuario con el ID proporcionado
            for i in range(len(datos["usuarios"])):
                if usuario_id == datos["usuarios"][i]["id"]:
                    usuario = datos["usuarios"][i]
                    categoria = input("Ingrese la categoría del usuario (cliente nuevo, cliente regular, cliente leal): ")
                    usuario["categoria"] = categoria.capitalize()
                    print(f"Categoría del usuario {usuario['nombre']} actualizada a {usuario['categoria']}.")
                    return datos  # Asegúrate de retornar datos actualizados
                
            print("Usuario no encontrado. Intente de nuevo.")
          

       
#--------------------------------------------------------------------------
       
       
#CRUD SERVICIOS

#AGREGAR SERIVICIO
def agregar_servicio(datos):

    print("-------------------------------------------------")
    print("\n---------------Agregar servicio------------------\n")
    print("-------------------------------------------------")
    servicio = {}
    servicio["nombre"] = input("Ingrese el nombre del servicio: ")
    print("-------------------------------------------------")
    servicio["precio"] = input("Ingrese el precio: ")
    print("-------------------------------------------------")
    servicio["tamano"] = input("Ingrese tamaño del paquete # + (MB o GB): ")
    print("-------------------------------------------------")
    servicio["dias"] = input("Ingrese la cantidad de dias: ")
    print("-------------------------------------------------")
    servicio["tipo"] = input("Ingrese el tipo de servicio (Minutos, Datos, Todo incluido, Fibra Optica): ")
    print("-------------------------------------------------")
    servicio["filtro"] = input("ingrese el tipo de plan(Prepago o Postpago): ")
    
    for servicio_existente in datos["usuarios"]:  #VERIFICAR SI EL SERVICIO EXISTE
        if "nombre" in servicio_existente and servicio["nombre"] == servicio_existente["nombre"]:  #verificar si el servicio ya fue registrada
            print("Este servicio ya existe")  
            return datos  
    if servicio["filtro"] == "prepago":
        datos["servicios_prepago"].append(servicio)
        print("Servicio registrado con éxito")
        return datos
    elif servicio["filtro"] == "postpago":
        datos["servicios_postpago"].append(servicio)
        print("Servicio registrado con éxito")
        return datos
    else:
        print("El tipo de plan no es valido")
        return datos
    


#LEER SERVICIO
def leer_servicio(datos):
    repetir = True
    while repetir:
        print("Filtrar por Prepago o Postpago")
        opc = input("Ingrese la opción: ")
        if opc == "prepago":
            print("------------------PREPAGO---------------------")
            
            for servicio in datos["servicios_prepago"]:
                print(f"Servicio: {servicio["nombre"]} - tipo:{servicio["filtro"]}")
                
                nombre_servicio = input("Ingrese el nombre del servicio: ")
                print(f"Informacion del Servicio {nombre_servicio}:")
                servicio_encontrado = False
        
            for servicio in datos["servicios_prepago"]:
                if nombre_servicio == servicio["nombre"]:
                    print(f"{servicio}")
                    servicio_encontrado = True
                    break
            
            if servicio_encontrado == False:
                print("No existe este usuario")

            repetir = int(input("Desea leer otro servicio? (1.si, 0.no)"))
            if repetir  == False:
                return datos 
                     
        elif opc == "postpago":
            print("------------------POSTPAGO---------------------")
            for servicio in datos["servicios_postpago"]:
                print(f"Servicio: {servicio["nombre"]} - tipo:{servicio["filtro"]}")

            nombre_servicio = input("Ingrese el nombre del servicio: ")
            print(f"Informacion del Servicio {nombre_servicio}:")
            
            servicio_encontrado = False

            for servicio in datos["servicios_postpago"]:
                if nombre_servicio == servicio["nombre"]:
                    print(f"{servicio}")
                    servicio_encontrado = True
                    break
                
            if servicio_encontrado == False:
                print("No existe este servicio")

            repetir = int(input("Desea leer otro servicio? (1.si, 0.no)"))
            if repetir  == False:
                return datos   
  
  
#ACTUALIZAR SERVICIO          
def actualizar_serivicio(datos):
     # Muestra la lista de servicios
    print("-------------------------------------------------")
    print("servicios prepago:")
    print("-------------------------------------------------")
    for servicio in datos["servicios_prepago"]:
        print(f"servicio: {servicio['nombre']} - tipo: {servicio['tipo']}")
        print("-------------------------------------------------")
        
    print("servicios postpago")
    print("-------------------------------------------------")
    for servicio in datos["servicios_postpago"]:
        print(f"servicio: {servicio['nombre']} - tipo: {servicio['tipo']}")
        print("-------------------------------------------------")
    while True:
        # Pide el nombre del servicio a actualizar
        print("Filtrar por Prepago o Postpago")
        opc = input("Ingrese la opción: ")
        # Busca el servicio con el nombre proporcionado
        if opc == "prepago":
            nombre_servicio = input("Ingrese el nombre del servicio que desea actualizar: ")
            for i in range(len(datos["servicios_prepago"])):
                if nombre_servicio == datos["servicios_prepago"][i]["nombre"]:
                    servicio = datos["servicios_prepago"][i]
                    while True:
                        opc = input("Ingrese el campo que desea actualizar (nombre, precio, tamaño, dias, tipo, filtro(prepago o postpago)) o 'x' para salir: ").lower()
                        if opc == "nombre":
                            servicio["nombre"] = input("Ingrese el nombre: ")
                            print("¡El nombre del servicio ha sido actualizado!")
                        elif opc == "precio":
                            servicio["precio"] = input("Ingrese el precio: ")
                            print("¡El precio del servicio ha sido actualizado!")
                        elif opc == "tamaño":
                            servicio["tamano"] = input("Ingrese tamaño del paquete # + (MB o GB): ")
                            print("¡El tamaño del servicio ha sido actualizado!")
                        elif opc == "dias":
                            servicio["dias"] = input("Ingrese los dias de vigencia del servicio: ")
                            print("¡Los dias de vigencia del servicio han sido actualizados!")
                        elif opc == "tipo":
                            servicio["tipo"] = input("Ingrese el tipo de servicio (Minutos, Datos, Todo incluido, Fibra Optica): ")
                            print("¡El tipo de servicio ha sido actualizado!")
                        elif opc == "filtro":
                            servicio["filtro"] = input("Ingrese el filtro(prepago o postpago): ")
                            print("¡El tipo de filtro ha sido actualizado!")
                        elif opc == "x":
                            print("Datos guardados. Saliendo.")
                            return datos  # Salir después de guardar los cambios
                        else:
                            print("Opción no válida. Intente de nuevo.")
                            break
            else:
                print("Usuario no encontrado. Intente de nuevo.")
                return datos
        elif opc == "postpago":
            nombre_servicio = input("Ingrese el nombre del servicio que desea actualizar: ")
            for i in range(len(datos["servicios_postpago"])):
                if nombre_servicio == datos["servicios_postpago"][i]["nombre"]:
                    servicio = datos["servicios_postpago"][i]
                    while True:
                        opc = input("Ingrese el campo que desea actualizar (nombre, precio, tamaño, dias, tipo, filtro(prepago o postpago)) o 'x' para salir: ").lower()
                        if opc == "nombre":
                            servicio["nombre"] = input("Ingrese el nombre: ")
                            print("¡El nombre del servicio ha sido actualizado!")
                        elif opc == "precio":
                            servicio["precio"] = input("Ingrese el precio: ")
                            print("¡El precio del servicio ha sido actualizado!")
                        elif opc == "tamaño":
                            servicio["tamano"] = input("Ingrese tamaño del paquete # + (MB o GB): ")
                            print("¡El tamaño del servicio ha sido actualizado!")
                        elif opc == "dias":
                            servicio["dias"] = input("Ingrese los dias de vigencia del servicio: ")
                            print("¡Los dias de vigencia del servicio han sido actualizados!")
                        elif opc == "tipo":
                            servicio["tipo"] = input("Ingrese el tipo de servicio (Minutos, Datos, Todo incluido, Fibra Optica): ")
                            print("¡El tipo de servicio ha sido actualizado!")
                        elif opc == "filtro":
                            servicio["filtro"] = input("Ingrese el filtro(prepago o postpago): ")
                            print("¡El tipo de filtro ha sido actualizado!")
                        elif opc == "x":
                            print("Datos guardados. Saliendo.")
                            return datos  # Salir después de guardar los cambios
                        else:
                            print("Opción no válida. Intente de nuevo.")
                            break
            else:
                print("Usuario no encontrado. Intente de nuevo.")
                return datos


#ELIMINAR SERVICIO
def eliminar_servicio(datos):
    print("-------------------------------------------------")
    print("servicios prepago:")
    print("-------------------------------------------------")
    for servicio in datos["servicios_prepago"]:
        print(f"servicio: {servicio['nombre']} - tipo: {servicio['tipo']}")
        
    print("-------------------------------------------------")
    print("servicios postpago")
    print("-------------------------------------------------")
    for servicio in datos["servicios_postpago"]:
        print(f"servicio: {servicio['nombre']} - tipo: {servicio['tipo']}")
        print("-------------------------------------------------")
    
    
    while True:
        
        try:
            # Pide el nombre del servicio a eliminar
            print("Filtrar por Prepago o Postpago,0 para salir")
            opc = input("Ingrese la opción : ")
            if opc not in ["prepago","postpago","0"]:
                raise ValueError("Opcion invalida")
        except Exception as e:
            lugar = "Eliminar Servicio"
            almacenar_error(e,nombre_archivo,lugar)
            print("Opción no valida")
    
        if opc == "prepago":
            nombre_servicio = input("Escriba el nombre del que desea eliminar: ")
            for servicio in datos["servicios_prepago"]:
                if servicio["nombre"] == nombre_servicio:
                    datos["servicios_prepago"].remove(servicio)
                    print(f"El servicio {nombre_servicio} ha sido eliminado!")
                    return datos
        elif opc == "postpago":
            nombre_servicio = input("Escriba el nombre del que desea eliminar: ")
            for servicio in datos["servicios_postpago"]:
                if servicio["nombre"] == nombre_servicio:
                    datos["servicios_postpago"].remove(servicio)
                    print(f"El servicio {nombre_servicio} ha sido eliminado!")
                    return datos
        elif opc == "0":
            print("Saliendo")
            return datos
        else:
            print("Valor Invalido.")
           

#VER SERVICIOS
def ver_servicios(datos):
    while True:    
        print("Servicios Prepago:")
        for servicio in datos["servicios_prepago"]:
            print(f"Servicio: {servicio['nombre']} valor: {servicio['precio']}")

        print("---------------------------------")
        print("Servicios Postpago")
        for servicio in datos["servicios_postpago"]:
            print(f"Servicio: {servicio['nombre']} valor: {servicio['precio']}")

        ver_mas = input("Desea contratar? (si/no): ")
        if ver_mas.lower() == "si":
            tipo_servicio = input("Está interesado en prepago o postpago?: ").lower()
            if tipo_servicio == "prepago":
                for servicio in datos["servicios_prepago"]:
                    print(f"Servicio: {servicio['nombre']}, valor: {servicio['precio']}, Tamaño: {servicio['tamano']}, Vigencia: {servicio['dias']} dias, tipo: {servicio['tipo']}")
                    
                contratar = input("Ingrese el nombre del servicio que le gustaría contratar (0 para volver): ")
                if contratar == "0":
                    continue
                
                contratado = None
                for servicio in datos["servicios_prepago"]:
                    if contratar == servicio["nombre"]:
                        contratado = servicio
                        break
                
                if contratado:
                    verificar_usuario = input("Ingrese su ID nuevamente: ")
                    usuario_encontrado = False
                    for usuario in datos["usuarios"]:
                        if usuario["id"] == verificar_usuario:
                            usuario_encontrado = True
                            if "servicios" not in usuario:
                                usuario["servicios"] = []
                            usuario["servicios"].append(contratado)
                            print(f"Servicio {contratado['nombre']} contratado con éxito.")
                            guardar_servicio(usuario, contratado)
                            return datos
                    if not usuario_encontrado:
                        print("ID de usuario no encontrado.")
                else:
                    print("Servicio no encontrado.")
            elif tipo_servicio == "postpago":
                for servicio in datos["servicios_postpago"]:
                    print(f"Servicio: {servicio['nombre']}, valor: {servicio['precio']}, Tamaño: {servicio['tamano']}, Vigencia: {servicio['dias']} dias, tipo: {servicio['tipo']}")

                contratar = input("Ingrese el nombre del servicio que le gustaría contratar (0 para volver): ")
                if contratar == "0":
                    continue
                
                contratado = None
                for servicio in datos["servicios_postpago"]:
                    if contratar == servicio["nombre"]:
                        contratado = servicio
                        break
                
                if contratado:
                    verificar_usuario = input("Ingrese su ID nuevamente: ")
                    usuario_encontrado = False
                    for usuario in datos["usuarios"]:
                        if usuario["id"] == verificar_usuario:
                            usuario_encontrado = True
                            if "servicios" not in usuario:
                                usuario["servicios"] = []
                            usuario["servicios"].append(contratado)
                            print(f"Servicio {contratado['nombre']} contratado con éxito.")
                            guardar_servicio(usuario, contratado)
                            return datos
                    if not usuario_encontrado:
                        print("ID de usuario no encontrado.")
                else:
                    print("Servicio no encontrado.")
        elif ver_mas.lower() == "no":
            print("Gracias por su visita")
            return datos
        else:
            print("Respuesta no válida. Por favor, responda con 'si' o 'no'.")

#----------------------------------------------------------------------------

#CRUD DE PRODUCTOS

#AGREGAR PRODUCTO
def agregar_producto(datos):
    print("-------------------------------------------------")
    print("\n---------------Agregar Producto------------------\n")
    print("-------------------------------------------------")
    producto = {}
    producto["nombre"] = input("Ingrese el nombre del Producto: ")
    print("-------------------------------------------------")
    producto["marca"] = input("Ingrese la marca el Producto: ")
    print("-------------------------------------------------")
    producto["caracteristicas"] = input("Ingrese las caracteristicas del Producto): ")
    print("-------------------------------------------------")
    producto["precio"] = input("Ingrese el precio del producto: ")
    print("-------------------------------------------------")
    for producto_existente in datos["productos"]:  #VERIFICAR SI EL PRODUCTO EXISTE
        if "nombre" in producto_existente and producto["nombre"] == producto_existente["nombre"]:  #verificar si el servicio ya fue registrada
            print("Este Producto ya existe")  
            return datos  
    datos["productos"].append(producto)
    print("Producto Agregado correctamente")
    print("-------------------------------------------------")
    return datos


#LEER PRODUCTO
def leer_producto(datos):
    repetir = True
    while repetir:
        for producto in datos["productos"]:
            print(f"Producto: {producto["nombre"]} - Precio:{producto["precio"]}")
        
        nombre_producto = input("Ingrese el nombre del producto: ")
        print(f"Informacion del Usuario {nombre_producto}:")
        
        produto_encontrado = False
        
        for producto in datos["productos"]:
            if nombre_producto == producto["nombre"]:
                print(f"{producto}")
                usuario_encontrado = True
                break
            
        if usuario_encontrado == False:
            print("No existe este usuario")
                
        repetir = int(input("Desea leer otro producto? (1.si, 0.no)"))
        if repetir  == False:
                    return datos    
                

#ACTUALIZAR PRODUCTOS
def actualizar_producto(datos):
    for producto in datos["productos"]:
        print(f"Producto: {producto['nombre']} - precio: {producto['precio']}")
    
    while True:
        try:
            # Pide el nombre del producto a actualizar
            nombre_producto = input("Ingrese el nombre del producto que desea actualizar: ")
        except Exception as e:
            lugar = "Menu Admin,Actualizar Producto,Nombre"
            almacenar_error(e, nombre_archivo, lugar)
            print("Ingrese un valor válido.")
        else:
            # Busca el prodcuto con el nombre proporcionado
            for i in range(len(datos["productos"])):
                if nombre_producto == datos["productos"][i]["nombre"]:
                    producto = datos["productos"][i]
                    while True:
                        opc = input("Ingrese el campo que desea actualizar (nombre, precio, marca, caracteristicas) o 'x' para salir: ").lower()
                        if opc == "nombre":
                            producto["nombre"] = input("Ingrese el nombre: ")
                            print("¡El nombre del producto ha sido actualizado!")
                        elif opc == "precio":
                            producto["precio"] = input("Ingrese el precio: ")
                            print("¡El precio del producto ha sido actualizado!")
                        elif opc == "marca":
                            producto["marca"] = input("Ingrese la marca del producto: ")
                            print("¡La marca del producto ha sido actualizada!")
                        elif opc == "caracteristicas":
                            producto["caracteristicas"] = input("Ingrese las caracteristicas del producto: ")
                            print("¡Las caracteristicas del producto han sido actualizadas!")
                        elif opc == "x":
                            print("Datos guardados. Saliendo.")
                            return datos  # Salir después de guardar los cambios
                        else:
                            print("Opción no válida. Intente de nuevo.")
                            break
            else:
                print("Usuario no encontrado. Intente de nuevo.")

            return datos


#ELIMINAR PRODUCTO
def eliminar_producto(datos):
    for producto in datos["productos"]:
        print(f"Producto: {producto["nombre"]} - Precio:{producto["precio"]}")
   
    while True:
        nombre = input("Escriba el nombre del producto que desea eliminar: ")
        for producto in datos["productos"]:
            if producto["nombre"] == nombre:
                datos["productos"].remove(producto)
                print(f"El Producto {nombre} ha sido eliminado!")
                return datos
        


#VER PRODUCTOS
def ver_productos(datos):
    while True:
        for producto in datos["productos"]:
            print(f"Producto:{producto["nombre"]}, Precio: {producto["precio"]}")
            
        ver_mas = input("Desea comprar algun Producto (si/no)")
        if ver_mas.lower() == "si":
            for producto in datos["productos"]:
                print(f"Producto:{producto}")

            comprar = input("Escriba el nombre del producto que desea comprar (0 para volver): ")
            if comprar == "0":
                continue
                
            comprado = None
            for producto in datos["productos"]:
                if comprar == producto["nombre"]:
                    comprado = producto
                    break
            
            if comprado:
                verificar_usuario = input("Ingrese su ID nuevamente: ")
                for usuario in datos["usuarios"]:
                    if usuario["id"] == verificar_usuario:
                        if "Productos" not in usuario:
                            usuario["Productos"] = []
                            usuario["Productos"].append(comprado)
                            print(f"Producto {comprado['nombre']} comprado con éxito.")
                            guardar_producto(usuario, comprado)
                            return datos
                else:
                    print("ID de usuario no encontrado.")
            else:
                print("Producto no encontrado.")