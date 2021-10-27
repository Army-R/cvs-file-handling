#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 14:06:12 2021

@author: Army-R
"""
# Leer archivo CSV con reader(), skipinitialspace y strict

# Leer archivo ignorando o no los espacios que existan después
# de los delimitadores de campos

# Si la propiedad skipinitialspace es True se ignorarán
# los espacios
# Si la propiedad strict es True se producirá un error si el 
# archivo csv no es válido 

# Leer archivos sin ignorar espacios
import csv

with open('datos.csv') as csv_file:
    input_ = csv.reader(csv_file,
                       skipinitialspace=False,
                       strict=True)
    for reg in input_:
        print(reg)
        
# Leer archivos ignorando espacios

with open('datos.csv') as csv_file:
    input_ = csv.reader(csv_file, 
                        skipinitialspace=True,
                        strict=True)
    for reg in input_:
        print(reg)