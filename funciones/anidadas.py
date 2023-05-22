# En Python podemos tener funciones anidadas dentro de otra función
# Lo recomendable es tener funciones anidadas de no más de 2 niveles
# Así como vemos en este ejemplo tenemos una función que tiene 2 funciones dentro 
# a esto es a lo que se le conoce como funciones de dos niveles
"""
    En este ejemplo lo que hacemos es definir una función de nombre operación que va a 
    recibir 2-3 parámetros siendo el 3er parámetro opcional, que en caso de no pasarle el
    3er parámetro este será por defecto de tipo depósito.
    Dentro de la misma tenemos una validación, que verifica si el parámetro es deposito
    o retiro, en base a eso dentro del if llamará a una de las dos funciones definidas 
    dentro de operación. 
    Si el tipo es deposito llamará a la función deposito y retornará una operación de 
    suma de cantidad + balance.
    En caso que el tipo sea retiro llamará a la función retiro y retornará una 
    operación de tipo resta de balance - cantidad
    luego fuera de la función Operación llamamos a la misma y guardamos su valor
    en una variable de nombre resultado el cual imprimiremos por consola.
"""
def operacion(cantidad, balance, tipo='deposito'):
    def deposito(cantidad, balance):
        return cantidad + balance
    
    def retiro(cantidad, balance):
        if cantidad <= balance:
            return balance - cantidad
        else:
            return None
    if tipo == 'deposito':
        return deposito(cantidad, balance)
    elif tipo == 'retiro':
        return retiro(cantidad, balance)
resultado = operacion(10, 30)        
print(resultado)
resultado = operacion(10, 20, 'retiro')    
print(resultado)