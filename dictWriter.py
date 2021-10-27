#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 14:13:45 2021

@author: Army-R
"""
# Escribir archivo CSV con DictWriter() capturando excepciones
import csv

try:
    csv_output = open('campos.csv', 'w')
    fields = ['Campo1', 'Campo2']
    output = csv.DictWriter(csv_output, fieldnames=fields)
    output.writeheader()
    for index in range(6):
        output.writerow({'Campo1':index+1,
                         'Campo2':chr(ord('a') + index)})
        
    print('Se ha creado el archivo "campos.csv"')
    
finally:
    csv_output.close()
    
