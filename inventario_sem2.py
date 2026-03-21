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
            
         nombre = input("Ingrese el nombre del producto: ").strip()
        
         while nombre.strip() == "" or nombre.isdigit():
            print("Error: nombre invalido. ")
            nombre = input("Ingrese el nombre del producto: ").strip()
        
        
        
        precio = input("Ingrese el precio del producto: ")
        while not precio.replace('.', '', 1).isdigit() or float(precio) <= 0:
           print("Error: precio invalido. ")
           precio = input("Ingrese el precio del producto: ")
        precio = float(precio)
        
        cantidad = input("Ingrese la cantidAd del priducto:  ")
        while not cantidad.isdigit() or int(cantidad) <= 0: 
            print("Error: cantidad invalida. ")
            cantidad = input("Ingrese la cantidAd del priducto:  ")
        cantidad = int(cantidad)
            
        producto = {
                "nombre": nombre,
                    
                "precio": precio,  
                    
                "cantidad": cantidad
                    
                }
            
        inventario.append(producto)
        continuar = input("desea agregar otro producto? (si/no): ")
        if continuar.lower() != "si":
                
         print("Producto/s agregados. ")
            
    # Opcion 2, mostrar inventario. 
            
    
    elif opcion == "2":
        for productos in inventario:
            print("\n==== SUS PRODUCTOS AGREGADOS SON: ")
            print("Producto:", [nombre])
            print("Precio:", [precio])
            print("Cantidad:", [cantidad])
            
        else:
            if not inventario:
                print("Inventario vacio. ")
                
                
    
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
            
            
  
  

        
         
                    
            
                
            
    