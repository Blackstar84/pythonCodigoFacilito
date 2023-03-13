diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# De esta manera podemos obtener los valores que deseemos del diccionario
# En este ejemplo queremos obtener el valor que se encuentra en la llave d
valor = diccionario['d']

print(valor)

# Si ponemos una llave que no existe devolverá un error de tipo keyError: 'nombreLlave'

# Ejemplo: valor = ['z']
# Esto devolverá keyError: 'z'

# Para verificar si una llave existe dentro de un diccionario podemos hacer uso de in
# Esto devolverá True o False, en caso de existir ese valor dentro del diccionario devolverá True
# caso contrario devolverá False
print('z' in diccionario)

# por medio de get podemos obtener el valor de una llave de forma segura

# con get obtenemos el valor de una llave en caso exista
# esto devolverá 4
valor = diccionario.get('d')
print(valor)

# en caso que no exista la llave nos devolverá None, pero el programa ya no terminará de forma abrupta 
# como lo hacía cuando poniamos directamente valor = diccionario['z'] y luego imprimíamos el mismo
valor = diccionario.get('z')
print(valor)

# El método get recibe un segundo argumento este valor se recibirá en caso que no exista la llave

valor = diccionario.get('z', 'La llave no existe en el diccionario')
print(valor)

# En caso que exista se devolverá el valor y no se mostrará el mensaje
valor = diccionario.get('b', 'La llave no existe en el diccionario')
print(valor)


# Básicamente podemos poner el valor que deseemos retorne en caso que no exista
# por default es None

valor = diccionario.get('z', False)
print(valor)

valor = diccionario.get('z', 1)
print(valor)

valor = diccionario.get('z', 1.9)
print(valor)


# setDefault nos permitirá agregar un valor por defecto en caso no exista una llave
# recibe 2 argumentos, el primero el nombre de la llave y el segundo será el valor a asignar en caso no exista la llave
# en este ejemplo no existe la llave 'e' en el diccionario por tal motivo se creará la llave e con valor 5 dentro del diccionario
valor = diccionario.setdefault('e', 5)

print(valor)
# al imprimir el diccionario vemos que se creó la llave e con valor 5
print(diccionario)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}