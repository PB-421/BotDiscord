import json

lista = [
    #lista de fechas, {'fecha':yyyy-mm-dd, 'mensaje':'contenido del mensaje'}
]

# Especifica el nombre del archivo donde se guardará
nombre_archivo = 'recordatorios.json'

# Abre el archivo en modo de escritura
with open(nombre_archivo, 'w') as archivo:
    # Convierte el array de recordatorios a formato JSON y lo escribe en el archivo
    json.dump(lista, archivo, indent=4)  # indent=4 es para formatear el JSON de forma legible

print(f'Los recordatorios se han guardado en {nombre_archivo}.')

frases_random = [
    #frases random, array de strings
]

nombre_archivo2 = 'frases.json'

# Abre el archivo en modo de escritura
with open(nombre_archivo2, 'w') as archivo2:
    # Convierte el array de frases_random a formato JSON y lo escribe en el archivo
    json.dump(frases_random, archivo2, indent=4)  

print(f'Las frases se han guardado en {nombre_archivo2}.')