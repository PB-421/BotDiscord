import json

lista = [
    #lista de fechas, array
]

# Especifica el nombre del archivo donde se guardará
nombre_archivo = 'recordatorios.json'

# Abre el archivo en modo de escritura
with open(nombre_archivo, 'w') as archivo:
    # Convierte el array de recordatorios a formato JSON y lo escribe en el archivo
    json.dump(lista, archivo, indent=4)  # indent=4 es para formatear el JSON de forma legible

print(f'Los recordatorios se han guardado en {nombre_archivo}.')