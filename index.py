lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]

# Ordenar Lista
 
# Con el método sort ordenamos la lista de manera ascendente o descendente
# con reverse True ordenamos de manera descendente

# De esta manera ordenará de menor a mayor (Ascendente)
lista.sort()
print(lista)
# De esta manera ordenará de mayor a menor (Descendente)
lista.sort(reverse=True)

print(lista)

# Encontrar el número menor y el mayor de una lista podemos hacerlo de la siguiente manera
# Ordenamos la lista de menor a mayor luego obtenemos el primer valor en el índice 0 esto 
# corresponderá al menor seguido del índice -1 esto corresponderá al último elemento de la lista
# lista[0] = menor
# lista[-1] = mayor

lista.sort()
print(lista[0])
print(lista[-1])

# La función recomendada es utilizar las funciones min y max

print(min(lista))

print(max(lista))

# Para conocer si un elemento existe dentro de una lista utilizamos in
# Devolverá verdadero si existe el elemento y falso si no se encuentra en la lista

# Esto devolverá verdadero ya que 8 existe en la lista
print(10 in lista)

# Esto devolverá verdadero ya que 8 existe en la lista
print(8 in lista)

# Preguntamos si 8 no está en la lista, esto devolverá falso ya que si existe en la lista
print(8 not in lista)