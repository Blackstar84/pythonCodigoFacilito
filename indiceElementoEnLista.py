lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]

# Para encontrar el índice donde se encuentra el elemento utilizamos la función index
# Si en la lista existen más de un elemento, retornará el primer índice del primer elemento que encuentre
# por ejemplo lista = [8, 5, 90, 1, 5, 44, 132, 600, 5, 3, 4] devolverá el índice 1

print(5 in lista)

index = lista.index(5)

print(index)