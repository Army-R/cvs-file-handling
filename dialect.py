#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 14:26:07 2021

@author: Army-R
"""

# Crear dialecto y leer archivo CSV

# Crear nuevo dialecto 'personal' y abrir archivo usándolo.
import csv

csv.register_dialect('personal',
                     delimiter='|',
                     quotechar='"',
                     quoting=csv.QUOTE_ALL)

with open('salida.csv') as csv_file:
    input_ = csv.reader(csv_file, dialect='personal')
    for reg in input_:
        print(reg)
        
# Listar dialectos disponibles
print(csv.list_dialects())

# Obtener información de un dialecto
# Obtener información del dialecto "personal"

dialect = csv.get_dialect('personal')
print('delimiter', dialect.delimiter)
print('skipinitialspace', dialect.skipinitialspace)
print('doublequote', dialect.doublequote)
print('quoting', dialect.quoting)
print('quotechar', dialect.quotechar)
print('lineterminator', dialect.lineterminator)

# Suprimir dialecto
# suprimir dialecto "personal"

csv.unregister_dialect('personal')
print(csv.list_dialects()) # Listar dialectos después

# Deducir con Sniffer() el dialecto de un archivo csv

with open('salida.csv') as csv_file:
    dialect = csv.Sniffer().sniff(csv_file.read(48))
    csv_file.seek(0)
    print("Dialecto:", dialect)
    csv_file.seek(0)
    input_ = csv.reader(csv_file, dialect)
    for reg in input_:
        print(reg)
        
# Deducir con Sniffer() si un archivo tiene encabezado

# El archivo salida.csv no tiene encabezado

csv_file1 = open('salida.csv')
header1 = csv.Sniffer().has_header(csv_file1.read(48))
print("\ncsv_file1 (salida.csv) encabezado:", header1)
csv_file1.seek(0)
input_ = csv.reader(csv_file1, "unix")
for reg in input_:
    print(reg)
    
csv_file1.close()

# El archivo salidat.csv sí tiene encabezado

csv_file2 = open('salidat.csv')
header2 = csv.Sniffer().has_header(csv_file2.read(76))
print("\ncsv_file2 (salidat.csv) encabezado", header2)
csv_file2.seek(0)
input_ = csv.reader(csv_file2, "excel")
for reg in input_:
    print(reg)
    
csv_file2.close()

# Mostrar/Establecer límite de tamaño de campo a analizar

# Para establecer un nuevo límite: field_size_limit(NuevoLímite)
print(csv.field_size_limit())  