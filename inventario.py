print("=====BIENVENIDO=====")

# pedir nombre del producto
nombre_del_producto = input("Ingrese el nombre del producto: ")
while True: 
    
 if nombre_del_producto == "":
  print("nombre invalido, ingrese un nombre valido.")
  nombre_del_producto = input("Ingrese el nombre del producto: ")
  
 elif not nombre_del_producto.isalpha():
     print("nombre invalido, ingrese un nombre valido.")
     nombre_del_producto = input("Ingrese el nombre del producto: ")
     
 else: 
     break


# pedir precio del producto 

while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        break
    except ValueError:
        print("Ingrese un valor valido.")    

# pedir cantidad del producto 
while True:
    try:
        cantidad = int (input("Ingrese la cantiad del producto: "))
        break
    except ValueError:
       print("Ingrese un valor valido.")

costo_total = precio * cantidad 


# imprimir recibo 
print("Nombre del producto:", nombre_del_producto )
print("Precio unitario:", precio)
print("Cantidad del producto:", cantidad)
print("Costo total:", costo_total)
 
