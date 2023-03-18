def pares(): # Generador -> Lazy iterator
    for numero in range(0, 12, 2):
        # La palabra reservada yield nos permite retornar valores sin que la función finalice
        # únicamente pausando su ejecución para que posteriormente pueda reanudarse desde el punto
        # donde se quedo
        # La función retorna y pausa su ejecución
        yield numero
        
        print('Se reanuda la ejecución')
       

# Utilizaremos la palabra next

generador = pares()

# Con este Lazy iterator ahorramos uso de memoria ya que se ejecutará siempre
# que lo necesitemos no estaremos reservando espacio en memoria que muy probablemente
# no vayamos a utilizar


# Con next vamos recorriendo de a una ejecución nuestra función pares
# Esto imprimirá un valor a la vez
# Imprimirá los valores : 
# 0
print(next(generador))

# 2
print(next(generador))

# 4 
print(next(generador))

print('Ejecutamos código entre un llamado y otro')

# 6
print(next(generador))

# 8
print(next(generador))

# 10
print(next(generador))

# Si intentamos obtener el siguiente elemento del generador cuando este ya haya 
# finalizado utilizando next obtendremos un error de tipo StopIteration
# Esto dara error de Tipo StopIteration ya que tenemos sólo valores hasta el 12
# ya que nuestro for va del 0 al 11 y recorre de 2 en 2
# print(next(generador))

# Para evitar este tipo de errores utilizaremos try except para manejar los errores

generadores = pares()

while True:
    try:
        par = next(generadores)
        print(par)
    except StopIteration:    
        print('El generador finalizo.')
        break

# El try except es lo mismo que el try catch de PHP

# Lo que hacemos aquí es mientras existan elementos disponibles dentro del next
# Lo vamos imprimiendo, caso lleguemos a iterar sobre todos los elementos ingresará 
# al except StopIteration e imprimirá el mensaje de El generador finalizo y 
# luego con el break salimos del ciclo while

