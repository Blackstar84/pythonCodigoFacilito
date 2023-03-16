# Al poner asterisco frente al argumento listado le estamos diciendo que todos argumentos utilizados al momento de 
# llamar a la función van a servir para generar una tupla, tupla a la cuál se va a asignar al parámetro que tenga asterisco
# De esta forma podemos crear funciones que reciban N cantidad de argumentos
# Por convención todos los argumentos que tengan * deben nombrarse como args, siempre deben estar pegados el * y args
# No agregar espacios entre ellos, siempre debe ir así *args

def combinacion(p1,p2,*args):
    print(p1)
    print(p2)
    print(args)


# Aquí los primeros dos argumentos pertenecen a p1 y p2, apartir del tercero hasta el final corresponden a args
# que es lo que será una tupla con dichos valores 
combinacion(10,20, 1, 2, 3, 4, 5, 6, 7, 8)    

"""
    Esto devolverá los siguientes valores
   p1 = 10
   p2 = 20
   args = (1, 2, 3, 4, 5, 6, 7, 8)

"""

def combinacion(p1,p2,*args, p4=500):
    print(p1)
    print(p2)
    print(args)
    print(p4)


# Al llamar a la función nos devolverá lo mismo que la función de arriba más p4 = 500
combinacion(10,20, 1, 2, 3, 4, 5, 6, 7, 8)   

"""
    Esto devolverá los siguientes valores
   p1 = 10
   p2 = 20
   args = (1, 2, 3, 4, 5, 6, 7, 8)
   p4 = 500
"""
# Si queremos pasarle el 4 parámetro y reemplazar el valor por defecto de p4 podemos apoyarnos 
# de los nombres de los argumentos

combinacion(10,20, 1, 2, 3, 4, 5, 6, 7, 8, p4=1000)

# Por Convención cuando tenemos dos o más funciones separar las mismas por dos saltos de línea
# Ejemplo:

"""
def suma():
    return 3 + 2


def suma_valores(a1,b1):
    return a1 + b1
    
"""

# Como podemos observar hay dos saltos de líneas entre cada definición de las funciones suma y suma_valores
# Los saltos deben encontrarse entre funciones