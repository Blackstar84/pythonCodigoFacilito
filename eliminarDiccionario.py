diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(len(diccionario))

# Para eliminar utilizamos la palabra reservada del seguido del diccionario y la llave de la cual deseamos eliminar
# 1era Forma
del diccionario['d']

print(diccionario)
print(len(diccionario))

# 2da Forma
# Utilizando pop y pasandole el nombre de la llave que deseemos eliminar del diccionario, en caso de no existir 
# la llave dará un error de KeyError: 'nombreLlave'
valor = diccionario.pop('b')
print(valor)

print(diccionario)
print(len(diccionario))

# 3era Forma
# Para vaciar el diccionario utilizamos la función clear()

diccionario.clear()
print(diccionario)
print(len(diccionario))