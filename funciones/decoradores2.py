
def funcion_a(funcion_b):

    def funcion_c(*args, **kwargs):
       print('>>> Antes del llamado.')
       resultado = funcion_b(*args,**kwargs)
       #print(resultado)
       print('>>> Después del llamado.')
       return resultado 

    return funcion_c


@funcion_a
def suma(numero_1, numero_2):
    return numero_1 + numero_2

#resultado = suma(10, 20)

#print(resultado)

# Tenemos dos formas de mostrar el resultado de la operación de la función suma, como vemos 
# al llamar a la misma se ejecuta el decorador funcion_a que recibe una función y dentro tiene otra
# función anidada que hace uso de esa función, lo que podemos hacer es imprimir directamente el 
# valor de la función_b que recibimos como parámetro y es utilizada dentro de la función_c que 
# a  su vez recibe una cantidad no conocida de argumentos por ello pasamos *args y **kwargs, con esto podemos
# crear otras funciones que pueden recibir N cantidad de elementos, ya sean tuplas o diccionarios 
# luego dentro de la función guardamos dentro de la variable resultado de ejecutar la función suma
# e imprimir directamente esa variable o retornando ese valor e imprimirlo fuera en la llamada de suma

# Método 1
def funcion_a(funcion_b):
    
    def funcion_c(*args, **kwargs):
       print('>>> Antes del llamado.')
       # Guardamos el resultado de la función en la variable resultado
       resultado = funcion_b(*args,**kwargs)
       
       print('>>> Después del llamado.')
       # Retornamos el valor resultado
       return resultado 

    return funcion_c


@funcion_a
def suma(numero_1, numero_2):
    return numero_1 + numero_2

# Guardamos el valor de la llamada a la función resultado dentro de una variable de nombre resultado
#resultado = suma(10, 20)

# Imprimimos la variable resultado que contiene lo que se ejecuta en la función anidada funcion_c que
# esta dentro de la función_a
#print(resultado)





# Método 2
def funcion_a(funcion_b):
    
    def funcion_c(*args, **kwargs):
       print('>>> Antes del llamado.')
       # Guardamos el resultado de la función en la variable resultado
       resultado = funcion_b(*args,**kwargs)
       # Imprimimos su valor una vez se ejecute la función_b
       print(resultado)
       print('>>> Después del llamado.')
       

    return funcion_c


@funcion_a
def suma(numero_1, numero_2):
    return numero_1 + numero_2

# Con la simple llamada a la función se imprimirá por consola lo siguiente_:
"""
    >>> Antes del llamado.
    30
    >>> Después del llamado.
"""
# Que es lo que se encuentra definido dentro de la funcion_c anidada dentro de la función_a
suma(10, 20)



# Con esto lo que hacemos es crear la suma de los valores de la tupla y diccionario
@funcion_a
def suma2(*args, **kwargs):
    total = 0
    
    # Sumar los valores de *args
    for arg in args:
        total += arg
    
    # Sumar los valores de **kwargs
    for key, value in kwargs.items():
        total += value

    return total


suma2(1,2,3,4,5,hola=5, chau=2)