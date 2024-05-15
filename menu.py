import funciones
from datos import *
from informe import *
#import main

RUTA_JSON = "usuarios.json"

#MENU PRINCIPAL
def menu_principal(datos):
    print("-------------------------------------------------")
    print("\n-------------------BIENVENIDO--------------------\n")
    print("-------------------------------------------------")
    opciones = ["1.Iniciar sesion","2.Registrarse","3.Salir...\n\n"]
    longitud_total = 45
    for i in range(len(opciones)):
        print(opciones[i].center(longitud_total))
    return datos



#MENU ADMIN
def menu_admin(datos):
    while True:
        print("                  BIENVENIDO")
        print("------------------->ADMIN<---------------------")
        print("----DESEA ACCEDER A LOS USUARIOS O A LOS SERVICIOS----")
        print("---------------O A LOS PRODUCTOS<----------------")
        print("------->GENERAR INFORME DE OBJETOS A LA VENTA<-------")
        print("                    (informe)")
        print("             GENERAR INFORME DE VENTAS")
        print("                     (ventas)")
        print("---------------->0 Para salir<------------------")
        eleccion = input("Elegir opción: ")
        if eleccion == "usuarios":
            while True:     
                print("----------------->USUARIOS<-------------------")
                opciones_usuario = ["1.Crear usuario","2.leer usuario","3.Actualizar usuario","4.Eliminar Perfil de usuario","5.Asignar categoria de usuario","0.Volver"]
                longitud_total = 45
                for i in range(len(opciones_usuario)):
                    print(opciones_usuario[i].center(longitud_total))

                opc = input("Elegir opción: ")
                if opc == "1":
                    datos = bajar_datos(RUTA_JSON)
                    funciones.crearUsuarioDesdeAdmin(datos)
                    subir_datos(datos,RUTA_JSON)
                    continue
                elif opc == "2":
                    funciones.leer_usuario(datos)
                    continue
                elif opc == "3":
                    datos = bajar_datos(RUTA_JSON)
                    funciones.actualizar_usuario(datos)
                    subir_datos(datos,RUTA_JSON)
                    continue
                elif opc == "4":
                    datos = bajar_datos(RUTA_JSON)
                    funciones.eliminar_usuario(datos)
                    subir_datos(datos,RUTA_JSON)
                    continue
                elif opc == "5":
                    datos = bajar_datos(RUTA_JSON)
                    funciones.asignar_categoria(datos)
                    subir_datos(datos,RUTA_JSON)
                    continue
                elif opc == "0":
                    print("Volviendo a eleccion de menu de admin")
                    break
        elif eleccion == "servicios":
            while True:   
                print("----------------->SERVICIOS<-------------------")
                opciones_servicios = ["1.Añadir un Servicio","2.leer un servicio","3.Actualizar un servicio","4.Eliminar un servicio","0.Volver"]
                longitud_total = 45
                for i in range(len(opciones_servicios)):
                    print(opciones_servicios[i].center(longitud_total))
                    
                opc = input("Elegir opción: ")
                if opc == "1":
                    datos = bajar_datos(RUTA_JSON)
                    funciones.agregar_servicio(datos)
                    subir_datos(datos,RUTA_JSON)
                    continue
                elif opc == "2":
                    funciones.leer_servicio(datos)
                elif opc == "3":
                    datos = bajar_datos(RUTA_JSON)
                    funciones.actualizar_serivicio(datos)
                    subir_datos(datos,RUTA_JSON)
                    continue
                elif opc == "4":
                    datos = bajar_datos(RUTA_JSON)
                    funciones.eliminar_servicio(datos)
                    subir_datos(datos,RUTA_JSON)
                elif opc == "0":
                    print("Volviendo a eleccion de menu de admin")
                    break
                    
        elif eleccion == "productos":
            while True:
                print("----------------->PRODUCTOS<-------------------")
                opciones_servicios = ["1.Añadir producto","2.leer un producto","3.Actualizar un producto","4.Eliminar un producto","0.volver"]
                longitud_total = 45
                for i in range(len(opciones_servicios)):
                    print(opciones_servicios[i].center(longitud_total))
                    
                opc = input("Elegir opción: ")
                if opc == "1":
                    datos = bajar_datos(RUTA_JSON)
                    funciones.agregar_producto(datos)
                    subir_datos(datos,RUTA_JSON)
                    continue
                elif opc == "2":
                    funciones.leer_producto(datos)
                elif opc == "3":
                    datos = bajar_datos(RUTA_JSON)
                    funciones.actualizar_producto(datos)
                    subir_datos(datos,RUTA_JSON)
                    continue
                elif opc == "4":
                    datos = bajar_datos(RUTA_JSON)
                    funciones.eliminar_producto(datos)
                    subir_datos(datos,RUTA_JSON)
                elif opc == "0":
                    print("Volviendo a eleccion de menu de admin")
                    break
        elif eleccion == "informe":
            print("-------------------------------------------------")
            print("            SE HA CREADO EL INFORME")
            print("-------------------------------------------------")
            informe(datos)
            continue
        elif eleccion == "ventas":
            print("-------------------------------------------------")
            print("            SE HA CREADO EL INFORME")
            print("-------------------------------------------------")
            ventas(datos)
            continue
        
        elif eleccion == "0":
            print("Cerrando sesion")
            funciones.ejecutable(datos)
            break



#MENU USUARIO 
def menu_usuario(datos):
     while True:
        print("------------------BIENVENIDO-------------------")
        print("------------------->USUARIO<--------------------")
        opciones = ["1.Ver servicios disponibles","2.Ver productos disponibles","0.Salir"]
        longitud_total = 45
        for i in range(len(opciones)):
            print(opciones[i].center(longitud_total))
        opc = input("Ingrese su opción: ")
        if opc == "1":
            datos = bajar_datos(RUTA_JSON)
            funciones.ver_servicios(datos)
            subir_datos(datos,RUTA_JSON)
        elif opc == "2":
            datos = bajar_datos(RUTA_JSON)
            funciones.ver_productos(datos)
            subir_datos(datos,RUTA_JSON) 
        elif opc == "0":
            print("Cerrando sesion.")
            funciones.ejecutable(datos)
            return datos
    

