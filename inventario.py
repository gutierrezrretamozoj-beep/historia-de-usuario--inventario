print("=====BIENVENIDO=====")

# En esta parte del codigo se pide al usuario ingresar el nombre del producto,utlizando nombre_del_producto = input("Ingrese el nombre del producto: "),
# tambien implemente un bucle (while) para validar que ingrese una opcion valida.
nombre_del_producto = input("Ingrese el nombre del producto: ")
while nombre_del_producto == "":
  print("nonbre invalido, ingrese un nombre valido.")
  nombre_del_producto = input("Ingrese el nombre del producto: ")

#En esta parte del codigo se le pide al usuario ingresar el precio de su producto,utlizando precio = float (input("Ingrese el precio del producto: ")),
# tambien implemente un bucle (while) para validar que ingrese una opcion valida.
precio = float (input("Ingrese el precio del producto: "))
while precio <= 0:
  print("valor invalido, ingrese en precio correcto.")
  precio = float (input("Ingrese el precio del producto: "))
 
#En esta parte del codigo se le pide al usuario ingresar la cantidad del producto, utilizando cantidad = int (input("Ingrese la cantiad del producto: ")),
# tambien implemente un bucle (while) para validar que ingrese una opcion valida.
cantidad = int (input("Ingrese la cantiad del producto: "))
while cantidad <= 0:
    print("cantidad invalida, ingrese una cantidad correcat.")
    cantidad = int (input("Ingrese la cantiad del producto: "))

# Esta parte del codigo se encarga de hacer el debido proceso matematico para, se utilizo una variable
# en la que se encerra los datos dados por el cliente para luego multiplicar usando costo_total = precio * cantidad 
# y luego arrojar el precio final al cliente.
costo_total = precio * cantidad 
 
#En esta parte del codigo se muestra el recibo final de la copra realizada por el cliente, usando print se muestra al cliente 
#toda la informacion sobre su compra 
print("Nombre del producto:", nombre_del_producto )
print("Precio unitario:", precio)
print("Cantidad del producto:", cantidad)
print("Costo total:", costo_total)
    
# Este programa en si trata sobre un sistema que registra productos con su nombre,cantidad y precio, para luego mostrarle al cliente que esta comprando, 
#cuanto cuesta y cual es su total a pagar, automatizando asi las compras de los clientes.   