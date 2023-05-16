# Pasar parámetros a una función
# dentro de la definición de la función le pasamos los parámetros
# a los valores de entrada los conoceremos como argumentos
def suma(n1, n2):
    # Como podemos observar podemos almacenar el valor en una variable y retornar 
    # el valor de la misma o directamente retornar la suma de los argumentos que le pasamos
    #resultado = n1 + n2
    #return resultado
    #return n1 + n2
    # Podemos retornar N cantidad de valores pero es recomendable no superar una cantidad
    # mayor a 3 valores
    return n1 + n2, 'La función retorna 2 valores'

numero_uno = int(input('Ingresa el primer número entero: '))
numero_dos = int(input('Ingresa el segundo número entero: '))    

result = suma(numero_uno, numero_dos)
# Al imprimir result esto retornará una tupla con los valores que retornamos
# Esto devolverá una tupla con los siguientes valores
# El resultado es: (5, 'La función retorna 2 valores')
# Como podemos observar retorna una tupla con la suma de los valores y el String que 
# definimos en el return
print(f'El resultado es: {result}')

# Esto devolverá lo siguiente:
# El resultado es: 5 La función retorna 2 valores
print(f'El resultado es: {result[0]} {result[1]}')

# Otra forma es declarando dos variables a la hora de llamar a la función suma
# en la variable de nombre resultado se almacenará el valor de la suma de los valores
# n1 + n2
# en la variable mensaje se almacenará el valor del String 'La función retorna 2 valores'

resultado, mensaje = suma(numero_uno, numero_dos)
print(f'El resultado es: {resultado}')
print(mensaje)



