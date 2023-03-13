diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# keys
# values
# items

# El método keys devuelve un objeto donde se encuentran almacenados todas las llaves del diccionario
# Devolverá un objeto de tipo dict_keys, esto podemos convertirlo a una tupla utilizando tuple 
llaves = diccionario.keys()


print(llaves)


llaves_tupla = tuple(diccionario.keys())
print(llaves_tupla)


# Para obtener los valores utilizamos el método values devolverá un objeto donde se encuentren almacenados todos 
# valores, devolverá un objeto de tipo dict_keys, esto podemos convertirlo a una tupla utilizando tuple

valores = diccionario.values()

print(valores)


valores_tupla = tuple(diccionario.values())

print(valores_tupla)

# Para obtener los items utilizamos el método items que devolverá un objeto de tipo dict_items, donde encontraremos 
# un listado que almacena tuplas, estas tuplas tendrán dos valores, el pimer valor hace referencia al key y 
# el segundo al valor del mismo

items = diccionario.items()

print(items)



items_tupla = tuple(diccionario.items())

print(items_tupla)