# La variable animal que esta declarada fuera de la función y la variable animal declarada 
# dentro de la función son objetos diferentes ya que fueron creadas en scopes diferentes por lo cual 
# tienen alcances diferentes

# Variables Globales son las declaradas fuera de bloques
# Las variables Globales pueden ser utilizadas dentro de cualquier bloque,
# dentro de una función, condición o ciclo

# Variables Locales son las declaradas dentro de bloques

animal = 'León' # Variable Global

# En python para poder distinguir un objeto de otro podemos hacer uso de su identificador único
# utilizando la función id

# Las variables locales sólo pueden ser utilizadas dentro del bloque donde fueron creadas
def imprimir_animal():
    # animal = 'Ballena' # Variable Local
    # si queremos modificar una variable global hacemos lo siguiente
    # ponemos global nombreVariableGlobal que deseemos modificar
    # y debajo de esta línea asignamos el valor a la variableGlobal
    # con esto modificaremos el valor anterior que fue definido a nivel Global
    # En este ejemplo animal = 'León' va a ser modificado por animal = 'Ciervo'
    # Si no utilizamos la palabra global nombreVariableGlobal esto sería una variable LOCAL
    # Si simplemente ponemos animal = 'Ciervo' esto será una variable LOCAL
    #global animal

    animal = 'Ciervo'
    tipo = 'Mamifero' # Variable Local


    print(animal)
    print(id(animal))
    print(tipo)

imprimir_animal()

print(animal)
print(id(animal))

# Al imprimir los ids nos devolverá valores diferentes para cada objeto, 
# ya que para python los objetos son diferentes

# Al intentar hacer este print nos dará un error ya que tipo es una variable local 
# y existe únicamente dentro de la función imprimir_animal()
# Esto ya dará un error antes de ejecutar especificando que tipo no está definido
# print(tipo)