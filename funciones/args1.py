"""
    La función print puede recibir N cantidad de argumentos
"""

print('String', 10, 14.5, True)
# La función sum nos devuelve la suma de todos los elementos de una colección
# ya sea dentro de un listado o dentro de una tupla
def promedio(listado):
    return sum(listado)/len(listado)


#print(promedio([10, 10, 5, 7, 10]))


# Al poner asterisco frente al argumento listado le estamos diciendo que todos argumentos utilizados al momento de 
# llamar a la función van a servir para generar una tupla, tupla a la cuál se va a asignar al parámetro que tenga asterisco
# De esta forma podemos crear funciones que reciban N cantidad de argumentos
# Por convención todos los argumentos que tengan * deben nombrarse como args, siempre deben estar pegados el * y args
# No agregar espacios entre ellos, siempre debe ir así *args
def promedio(*args):
    print(args)
    # Imprimirá una tupla con los valores (10, 10, 5, 7, 10)

    print(type(args))
    # Devolverá el tipo tupla <class 'tuple'>

    return sum(args)/len(args)

# Como podemos observar le estamos pasando parámetros separados por comas a la función promedio
print(promedio(10, 10, 5, 7, 10, 20, 30))