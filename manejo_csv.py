import csv

# Leer el archivo 'datos.csv' con reader()
# Mostar todos los registros, uno a uno:
with open('datos.csv') as csvarchivo:
    output = csv.reader(csvarchivo)
    for reg in output:
        print(reg) # Cada línea se muestra como una lista de campos

# Leer el archivo 'datos.csv' con reader()
# Realizar algunas operaciones básicas:
csvarchivo = open('datos.csv') # Abrir archivo csv
output = csv.reader(csvarchivo) # Leer todos los registros
reg = next(output) # Leer registro (lista)
print(reg) # Mostar registro
nombre, provincia, consumo = next(output) # Leer campos
print(nombre, provincia, consumo) # Mostar campos
del nombre, provincia, consumo, output # Borrar objetos
csvarchivo.close() # Cerrar archivo
del csvarchivo # Borrar objeto
