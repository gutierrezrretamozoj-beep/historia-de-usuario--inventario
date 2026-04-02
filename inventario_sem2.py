inventario = []
while True:

    print("\n===== BIENVENIDO, SELECIONE UNA OPCION ======")
    print("1. Agregar producto. ")
    print("2. Mostrar inventrio. ")
    print("3. Calcular estadisticas. ")
    print("4. Salir. ")

    opcion = input("Seleccione una opcion: ")
    
    # Opcion 1, agregar producto. 
  

    if opcion == "1": 
        
     continuar = "si"
     while continuar.lower() == "si":
        
        #  NOMBRE
        nombre = input("Ingrese el nombre del producto: ").strip()
        while nombre == "" or nombre.isdigit():
            print("Error: nombre invalido.")
            nombre = input("Ingrese el nombre del producto: ").strip()

        # PRECIO
        precio = input("Ingrese el precio del producto: ")
        while not precio.replace('.', '', 1).isdigit() or float(precio) <= 0:
            print("Error: precio invalido.")
            precio = input("Ingrese el precio del producto: ")
        precio = float(precio)

        #  CANTIDAD
        cantidad = input("Ingrese la cantidad del producto: ")
        while not cantidad.isdigit() or int(cantidad) <= 0:
            print("Error: cantidad invalida.")
            cantidad = input("Ingrese la cantidad del producto: ")
        cantidad = int(cantidad)

        #  GUARDAR
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }

        inventario.append(producto)
        print("Producto agregado correctamente.")

        continuar = input("¿Desea agregar otro producto? (si/no): ")
            
    # Opcion 2, mostrar inventario. 
            
    
    elif opcion == "2":
        
        if not inventario:
            print("Inventario vacío.")
        else:
            print("\n==== SUS PRODUCTOS AGREGADOS SON: ")
            for producto in inventario:
                print("Producto:", producto["nombre"])
                print("Precio:", producto["precio"])
                print("Cantidad:", producto["cantidad"])
                print("-" * 20)
                
    
    # Opcion 3, calcular estadisticas. 
     
    elif opcion == "3":
         
        if not inventario: 
            print("invenario vacio. ")
            
        else:
            
            total_inventario = 0
            total_productos = 0
            
            for productos in inventario : 
                total_inventario += productos["precio"] * productos["cantidad"]
                total_productos += productos["cantidad"] 
                
            print("\n======LAS ESTADISTICAS DE SU INVENTARIO SON =======")
            print("Total inventario: ", total_inventario)
            print("Total de productos en su inventario es: ", total_productos)
    # Opcion 4, salir del programa.         
    else: 
        print("\n===== SALIENDO DEL PROGRAMA ======")
        break
            
            
  
  

        
         
                    
            
                
            
    