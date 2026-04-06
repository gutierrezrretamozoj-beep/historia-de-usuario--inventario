from servicios import *

from archivos import crear_registro_csv , leer_registros_csv

inventario = []
while True:

    print("\n===== BIENVENIDO, SELECIONE UNA OPCION ======")
    print("1. Agregar producto. ")
    print("2. Mostrar inventrio. ")
    print("3. Buscar producto. ")
    print("4. Actualizar producto. ")
    print("5. Eliminar producto. ")
    print("6. Estadisticas. ")
    print("7. Guardar csv. ")
    print("8. Cargar csv. ")
    print("9. Salir. ")

    opcion = input("Seleccione una opcion (1-9): ").strip() 
    
    while not opcion.isdigit() or opcion == "" or int(opcion) <1 <9:
        print("Error: ingrese una opcion valida. ")
        opcion = input("Seleccione una opcion (1-9): ").strip()
        continue
    avanzar = "si"

    if opcion == "1":
        while avanzar == "si":

            nombre = input("Nombre: ").strip()
            while nombre == "" or not nombre.isalpha():
                print("Error: ingrese un nombre válido.")
                nombre = input("Nombre: ").strip()

            precio = input("Precio: ").strip()
            while precio == "" or not precio.replace(".", "", 1).isdigit() or float(precio) <= 0:
                print("Error: ingrese un precio válido.")
                precio = input("Precio: ").strip()
            precio = float(precio)

            cantidad = input("Cantidad: ").strip()
            while cantidad == "" or not cantidad.isdigit() or int(cantidad) <= 0:
                print("Error: ingrese una cantidad válida.")
                cantidad = input("Cantidad: ").strip()
            cantidad = int(cantidad)

            agregar_producto(inventario, nombre, precio, cantidad)
            print("✅ Producto agregado correctamente.")

            avanzar = input("¿Desea agregar otro producto? (si/no): ").strip().lower()

            while avanzar != "si" and avanzar != "no":
                print("Error: responda solo 'si' o 'no'")
                avanzar = input("¿Desea agregar otro producto? (si/no): ").strip().lower()

    elif opcion == "2":
        mostrar_inventario(inventario)

    elif opcion == "3":
        nombre = input("Ingrese el nombre del producto: ")
        producto_encontrado = buscar_productos(inventario, nombre)

        if producto_encontrado:
            print("Producto encontrado:")
            print(producto_encontrado)
        else:
            print("Producto no encontrado.")

    elif opcion == "4":
        nombre = input("Ingrese el nombre del producto a actualizar: ")

        nuevo_precio = float(input("Ingrese el nuevo precio: "))
        nueva_cantidad = int(input("Ingrese la nueva cantidad: "))

        if actualizar_productos(inventario, nombre, nuevo_precio, nueva_cantidad):
            print(" Producto actualizado.")
        else:
            print(" Producto no encontrado.")

    elif opcion == "5":
        nombre = input("Ingrese el nombre del producto a eliminar: ")
        eliminar_producto(inventario, nombre)

    elif opcion == "6": 
        estadisticas = calcular_estadisticas(inventario)
        print(estadisticas)

    elif opcion == "7":
        for producto in inventario:
            crear_registro_csv(producto, "data.csv")

        print(" Inventario guardado en CSV.")

    elif opcion == "8":
        inventario_csv = leer_registros_csv()

        if inventario_csv:
            print("\n Productos guardados en CSV:\n")
            for producto in inventario_csv:
                print(producto)
        else:
            print(" No hay registros en el archivo.")
   
    elif opcion == "9":
        salir()
        break
    else:
        print("Opcion no valida, intente nuevamente.")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    