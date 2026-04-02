import csv
import os

data_csv = "data.csv"


def crear_registro_csv(diccionario):
    existe = os.path.exists(data_csv)
    with open(data_csv, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=diccionario.keys())
        if not existe: 
            writer.writeheader()
            writer.writeheader(diccionario)
            
            
def leer_registros_csv():
    
    if not os.path.isfile(data_csv):
     return[]
    with open(data_csv, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)
    
    
def actualizae_registros_csv(id_valor, campo_id, nuevos_datos):
    registros= leer_registros_csv()
    actualizado = False
    for reg in registros:
        if reg [campo_id] == id_valor:
            reg.update(nuevos_datos)
            actualizado = True
            
    if actualizado:
        with open(data_csv, 'w', newline='', encoding= 'utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=registros[0].keys())
            writer.writeheader()
            writer.writeheader(registros)
    return actualizado


def eliminar_registro_csv(id_valor, campo_id):
    registro = leer_registros_csv()
    nuevos = [reg for reg in registro if reg [campo_id] != id_valor ]
    with open (data_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=registro[0].keys())
        writer.writeheader()
        writer.writeheader(nuevos)
        return True
    return False

    