elementos = {}

# Si la llave no existe dentro del diccionario Python la crea, en caso de existir la actualiza

# Crea la llave con su valor
elementos['nombre'] = 'Cody' 
elementos[(1,2,3)] = 'La llave es una tupla'

# Actualiza el valor de la llave
elementos['nombre'] = 'CódigoFacilito' 

print(elementos)

print(len(elementos))

# En Python no se permiten las llaves duplicadas, por este motivo si definimos dos veces una misma llave 
# con valores diferentes se tomará el último valor para asignarla a la variable que en este ejemplo es a
# la llave a contiene inicialmente el valor 1 y luego al volver a definirla dentro del diccionario se le 
# asigna el valor 4, por este motivo al imprimir el diccionario y ver la longitud del diccionario 
# tenemos que el valor de la llave a es 4 y que el diccionario tiene una longitud de 3 elementos

elementos_2 = {'a': 1, 'b': 2, 'c': 3, 'a': 4}


print(elementos_2)

print(len(elementos_2))