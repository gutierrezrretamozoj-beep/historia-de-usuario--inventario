def agregar_producto(inventario, nombre, precio, cantidad): 

    producto = {
        "nombre" : nombre,
        "precio" : precio,
        "cantidad" : cantidad
    }
    
    inventario.append(producto)
        
def mostrar_inventario(inventario):
    if not inventario: 
        print("\n Inventario vacio. ")
        return 
    print("\n ===== INVENTARIO ====== ")
    for productos in inventario:
        print(f"nombre: {productos["nombre"]}  precio: {productos["precio"]}  cantidad: {productos["cantidad"]}")
        
        
def buscar_productos(inventario,nombre):
    for productos in inventario:
        if productos["nombre"].lower() == nombre.lower():
            return productos
        return None
    

def actualizar_productos(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    producto = buscar_productos(inventario, nombre)
    if producto is None:
        return False
    elif nuevo_precio is not None:
        producto["precio"] = nuevo_precio
    elif nueva_cantidad is not None: 
        producto["cantidad"] = nueva_cantidad
    return True


def eliminar_producto(inventario, nombre):
    productos = buscar_productos(inventario, nombre)
    if productos is None:
        return False
    inventario.remove(productos)
    return True


def calcular_estadisticas(inventario):
    if not inventario:
        return {
            "unidades_totales":0,
            "valor_total":0,
            "producto_mas_caro":None,
            "producto_mayor_stock":None
        }
    subtotal = (lambda productos: productos["precio"] * productos["cantidad"])
    unidades_totales = sum(productos["cantidad"] for productos in inventario)
    valor_total = sum (subtotal(productos) for productos in inventario)
    producto_mas_caro = max(inventario, key=lambda productos: productos["precio"])
    producto_mayor_stock = max(inventario, key=lambda productos: productos["cantidad"])
    return{
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock
    }
    
    
def salir():
    print("SALIENDO DEL PROGRAMA. ")
    