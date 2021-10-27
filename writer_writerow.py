#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 13:41:06 2021

@author: Army-R
"""
# Escribir archivo CSV con writer() y writerow().

"""
Quoting:
La opción de quoting establece el tipo de entrecomillado que se aplicará a un archivo CSV. 
Existen cuatro posibilidades: 
QUOTE_ALL para entrecomillar todos los campos; 
QUOTE_MINIMAL para entrecomillar sólo los campos que sean necesarios para mantener la integridad de los datos; 
QUOTE_NONE para no entrecomillar nada y 
QUOTE_NONNUMERIC para entrecomillar sólo aquellos campos que no sean numéricos.

"""
# Leer con DictReader y escribir datos en otro csv si se cumple la condición
# En el archivo 'salida.csv' se escribirán todos los datos
# entrecomillados con dobles comillas y separdos entre si
# con el caracter '|'
import csv

with open('datos.csv') as csv_file:
    input_ = csv.DictReader(csv_file)
    csv_output = open('salida.csv', 'w', newline='')
    output = csv.writer(csv_output, delimiter='|',
                        quotechar='"',
                        quoting=csv.QUOTE_ALL)
    print('Escribiendo archivo "salida.csv"...')
    print('Dialecto:', input_.dialect, '...')
    for reg in input_:
        if reg['provincia'] != 'Huelva':
            output.writerow([reg['nombre'],
                             reg['consumo']]) # Escribir registro
    
    print('El proceso de escritura ha terminado')
    
del input_, output, reg
csv_output.close()
del csv_output

# Escribir todas las tuplas de una lista con writerows()

data = [('aaa', 111), ('bbb', 222), ('ccc', 333)]
csv_output = open('salidat.csv', 'w', newline='')
output = csv.writer(csv_output)
output.writerows(['campo1', 'campo2'])
output.writerows(data)
del output 
csv_output.close()

    
     