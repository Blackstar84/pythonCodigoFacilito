# Reducir líneas de código duplicadas, más legible, fácil de testear, fácil de mantener.

"""
    a -> la Función principal (Decorador)
    b -> La Función a decorar
    c -> La Función decorada

    a(b) -> c
    la función a va a recibir como argumento la función b y dará como resultado 
    la función c
"""

def funcion_a(funcion_b):

    def funcion_c():
        pass

    return funcion_c

# Con esta línea de código le estamos diciendo a Python que función a
# va a recibir como argumento la función saludar
@funcion_a
def saludar():
    print('Hola nos encontramos en una función')

# No estaremos ejecutando directamente la función decorada sino que estaremos ejecutando la función que se
# nos retorne
# Al ejecutar esto no nos traerá nada ya que lo que retornará en este caso es la 
# función c la cual no hace nada
saludar()    


# Al agregarle que realice algo la función c2 esta se ejecutará al llamar la función decorada
def funcion_a2(funcion_b2):
    
    def funcion_c2():
        print('>>> Antes del llamado.')
        # PAra que se ejecuta la función b (saludar2) simplemente agregamos aquí la llamada a
        # la misma 
        funcion_b2()
        print('>>> Después del llamado.')

    return funcion_c2


# Con esta línea de código le estamos diciendo a Python que función a
# va a recibir como argumento la función saludar
@funcion_a2
def saludar2():
    print('Hola nos encontramos en una función')


saludar2()    

"""
    Los decoradores se utilizan para agregar/extender funcionalidades sin tener que modificar la función
    principal.

"""

@funcion_a2
def suma():
    print(10 + 30)

suma()    