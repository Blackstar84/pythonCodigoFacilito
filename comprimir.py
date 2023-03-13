lista = [1, 2, 3, 4, 5]

tupla = (10, 20, 30, 40, 50)

# Esto generará un zip con la combinación de la lista y la tupla
# El orden dentro del zip indica el orden en el que van a ser combinados
# En este caso primero tomará el valor de la tupla seguido del valor de la lista
resultado = zip(tupla, lista) # -> zip
# Esto dará como resultado ((10, 1), (20, 2), (30, 3), (40, 4), (50, 5))

resultado = tuple(resultado)
print(resultado)

# Primero el valor de la lista y luego el valor de la tupla
resultado = zip(lista, tupla) # -> zip
# Esto dará como resultado ((1, 10), (2, 20), (3, 30), (4, 40), (5, 50))
resultado = tuple(resultado)
print(resultado)



lista = [1, 2, 3, 4, 5]

tupla = (10, 20, 30, 40, 50)

lista_2 = [100, 200, 300, 400, 500]

tupla_2 = (1000, 2000, 3000, 4000, 5000)


resultado = zip(lista, tupla, lista_2, tupla_2) # -> zip
resultado = tuple(resultado)
print(resultado)

# en caso de no tener la misma cantidad de elementos los mismos no son tomados en cuenta 
# para generar las tuplas ya que la combinación debe ser exacta

lista = [1, 2, 3, 4, 5, 6, 7]

tupla = (10, 20, 30, 40, 50)

lista_2 = [100, 200, 300, 400, 500]

tupla_2 = (1000, 2000, 3000, 4000, 5000)


resultado = zip(lista, tupla, lista_2, tupla_2) # -> zip
resultado = tuple(resultado)
print(resultado)