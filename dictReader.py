#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 13:14:42 2021

@author: Army-R
"""
# Leer archivo CSV con DictReader() y filtrar salida

# Leer un archivo csv como lista de diccionarios con DictReader()
# Mostar sólo datos de algunas columnas
import csv, operator

with open('datos.csv') as csv_file:
    input_ = csv.DictReader(csv_file)
    for reg in input_:
        print(reg['provincia'], reg['consumo'])

# Leer archivo CSV con DictReader() y consultar propiedades

# Mostar lista de diccionarios a partir CSV
# Consultar número de lineas (registros), dialecto y campos

csv_file = open('datos.csv')
input_ = csv.DictReader(csv_file)
list_dic = list(input_) # Obtener lista de diccionarios
print('Lista:', list_dic) # Mostar lista de diccionarios
print('Líneas:', input_.line_num) # Obtener número de registros
print('Dialecto:', input_.dialect) # Obtener dialecto
print('Campos:', input_.fieldnames) # Obtener nombre de campos
del input_, list_dic
csv_file.close()
del csv_file

# Leer archivos CSV con DictReader() y ordenar salida por nombre de campo

# Obtener lista ordenada descendente por el campo 'consumo'
# Usar la función itemgetter() del modulo operator

csv_file = open('datos.csv')
input_ = csv.DictReader(csv_file)
dic_list = list(input_)
order_diclist = sorted(dic_list, 
                       key=operator.itemgetter('consumo'), 
                       reverse=True)
for register in order_diclist:
    print(register)

del input_, dic_list, order_diclist
csv_file.close()
del csv_file
    

