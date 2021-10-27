# Leer archivo CSV con reader() y ordenar salida por un campo

# Mostrar ordern por tercer campo con la función itemgetter() del modulo operator
import operator, csv

csv_file = csv.reader(open('datos.csv'))
order_list = sorted(csv_file, key=operator.itemgetter(2), reverse=False)
print(order_list)

# Leer archivo CSV con reader() de un dialecto determinado

# Leer archivo csv con dialecto 'unix'

with open('salida.csv') as csv_file:
    input_ = csv.reader(csv_file,
                        dialect='unix',
                        delimiter='|')
    for reg in input_:
        print(reg)
        