import os
from ArbolB import NodoB, ArbolB
from Proveedor import Proveedor

x = 0  
arbol = ArbolB()
raiz = NodoB()  

while True:
    os.system('cls')
    print("""   BIENVENIDO  
          Ingrese una de las Opciónes Segun lo que Desea Hacer:
          1. Ingresar a un Nuevo Proveedor
          2. Buscar a un Proveedor por Servico Ofrecido
          3. Ver a los proveedores en orden (Nombre/Calificación)
          4. Salir del programa""")

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
        print("Carloos")
        arbol.recorrido_inorden(raiz)
        input()

    elif opcion == "3":
        print("Daviiid")
       
        
    elif opcion == "4":
        break

    else:
        print("Opción no válida. Intente nuevamente.")
        




