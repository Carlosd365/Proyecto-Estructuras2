import os
from ArbolB import NodoB, ArbolB
from Proveedor import Proveedor

x = 1  
orden = 5
arbol = ArbolB(orden)
raiz = NodoB(orden)  

proveedores_iniciales = [
    ("Ana", "Plomero", 5),
    ("Luis", "Electricista", 4),
    ("Sofía", "Plomero", 3),
    ("Carlos", "Carpintero", 5),
    ("Marta", "Programador", 4),
    ("José", "Albañil", 2),
    ("Lucía", "Diseñador", 5),
    ("Pedro", "Plomero", 1),
    ("Elena", "Electricista", 3),
    ("Diego", "Carpintero", 4),
    ("Diego", "Plomero", 4),
]

for nombre, servicio, calificacion in proveedores_iniciales:
    trabajador = Proveedor(x, nombre, servicio, calificacion)
    raiz = arbol.insertar_en_arbol(raiz, trabajador)
    x += 1

while True:
    os.system('cls')
    print("""   BIENVENIDO  
        Ingrese una de las Opciónes Segun lo que Desea Hacer:
        1. Ingresar a un Nuevo Proveedor
        2. Buscar a un Proveedor por Servico Ofrecido
        3. Ver a los proveedores en orden (Nombre/Calificación)
        4. Mostrar Arbol B
        5. Salir del programa""")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        try:
            nombre = input("Ingrese el nombre del Proveedor: \n")
            servicio = input("Ingrese El Servicio del Proveedor:  \n")
            calificacion = float(input("Ingrese la Calificación del Proveedor: \n"))
            trabajador = Proveedor(x, nombre, servicio, calificacion)
            raiz = arbol.insertar_en_arbol(raiz, trabajador)

            print(f"El proveedor fue insertado")
            x += 1
            input()

        except ValueError:
            print("No ingreso la calificacion con numeros")
            input()

    elif opcion == "2":
        servicio = input("Ingrese el servicio que desea buscar: \n")
        resultados = arbol.buscar_por_servicio(raiz, servicio)

        if resultados:
            print(f"Se encontraron {len(resultados)} proveedores para '{servicio}':")
            for r in resultados:
                r.ImprimirporServicio()
        else:
            print("No se encontraron proveedores con ese servicio.")
        input()

    elif opcion == "3":
        print("Opciones de lista")
        print("1. Listar por nombre")
        print("2. Listar por calificación")
        listar = input("Seleccione una opción: ")
        if (listar == "1"):
            arbol.listar_nombre(raiz)
        elif (listar == "2"):
            arbol.listar_calificacion(raiz)
        else :
            print("Opcion invalida")
        input("Impreciones cualquier tecla para continuar")

    elif opcion == "4":
        arbol.mostrar_arbol(raiz)
        input()
        
    elif opcion == "5":
        print("Saliendo del programa ...")
        break

    else:
        print("Opción no válida. Intente nuevamente.")
        




