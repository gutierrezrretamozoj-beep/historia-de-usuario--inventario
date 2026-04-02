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
    
    if opcion == "1":
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        
        
        agregar_producto(inventario, nombre, precio, cantidad)
        print("Producto agregado correctamente.")
        
    elif opcion == "2":
        mostrar_inventario(inventario)
        
    elif opcion  == "3":
        buscar_productos(inventario,nombre)
        
    elif opcion == "4":
        actualizar_productos(inventario, nombre, nuevo_precio=None, nueva_cantidad=None)
        
    elif opcion == "5":
        eliminar_producto(inventario, nombre)
    
    elif opcion == "6": 
        calcular_estadisticas()
        
    elif opcion == "7":
     crear_registro_csv()   
     
    elif opcion == "8":
        leer_registros_csv()
        
    else: 
        salir()
        break
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    