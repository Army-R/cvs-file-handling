# Ordenar datos con sort(), sorted(), e itemgetter()

# La funcion sort() se utiliza para ordenar una lista en orden numerico, alfabetico, etc

list = ["d", "a", "e", "b", "c"]
list.sort()
print(list)

# sorted() permite utilizar otros criterios de ordenación, ampliando las posibilidades de sort()
# Sintaxis: sorted(objeto_a_ordenar, key=función, reverse=True/False)
# Si se utiliza key se aplicará a cada elemento la función indicada.
# reverse con el valor True, obtines los elementos ordenados con orden inverso

# Crear listas para ordenarlas con la función sorted()
list1 = ["ABCDEF", "ABCEFGHIJ", "ABC", "ABCD"]
list2 = ["10", "30", "20", "4"]

# Ordenar list1 por la longitud de sus elementos
list1 = sorted(list1, key=len)
print("List1 ordenada por longitud de cadenas: ", list1)

# ordenar list1 por la longitud de sus elementos en orden inverso
list1 = sorted(list1, key=len, reverse=True)
print("List1 ordenada por la longitud de cadenas inverso: ", list1)

# Ordenar list2 por el valor numérico de sus elementos
list2 = sorted(list2, key=int, reverse=False)
print("List2 ordenada por valor numérico: ", list2)

# Utilizar la función itemgetter() del módulo operator con la función sorted()
# permite ordenar una lista de tuplas (o de registros) por el índice de uno de sus campos
# (el índice del primer campo es el 0, del segundo el 1, etc.):
import operator

# Declarar una lista con 4 truplas de dos campos cada una
list3 = [("cccc", 4444), ("d", 1), ("aa", 22), ("bbb", 333)]

# Ordenar list3 por el segundo campo de cada tupla (índice 1)
list3_order = sorted(list3, key=operator.itemgetter(1), reverse=False)
print("List3 ordenada por campo2: ", list3_order)

# Ordenar list3 por el primer campo de cada tupla (índice 0)
# orden inverso

list3_order_reverse = sorted(list3, key=operator.itemgetter(0), reverse=True)
print("List3 ordenada inversa por campo1: ", list3_order_reverse)

# Ordenar alfabéticamente por el primer campo:
list3_order_reverse = sorted(list3)
print("List3 ordenada alfabéticamente: ", list3_order_reverse)
