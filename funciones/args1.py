"""
    La función print puede recibir N cantidad de argumentos
"""

print('String', 10, 14.5, True)
# La función sum nos devuelve la suma de todos los elementos de una colección
# ya sea dentro de un listado o dentro de una tupla
def promedio(listado):
    return sum(listado)/len(listado)


print(promedio([10, 10, 5, 7, 10]))