uno, dos, tres, cuatro = 1, 2, 3, 4

print(uno)
print(dos)
print(tres)
print(cuatro)
print(" ")


# Esto sirve cuando conocemos de antemano el tamaño final de valores
numeros = (1, 2, 3, 4, 5)

# Esto es lo mismo que lo declarado en las cinco líneas siguientes
# Se lee mejor de esta manera 
uno, dos, tres, cuatro, cinco = numeros

# Aquí se hace más larga la asignación de variables
uno = numeros[0]
dos = numeros[1]
tres = numeros[2]
cuatro = numeros[3]
cinco = numeros[4]

print(uno)
print(dos)
print(tres)
print(cuatro)
print(cinco)




numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Si no conocemosla cantidad de valores de la tupla podemos hacer uso de lo siguiente
# Al agregar *nombre estos valores van a ser almacenados en una lista
# Python sabe que estos valores no fueron asignados a variables entonces los agrupa 
# dentro de una lista
# El asterisco denota listas

uno, dos, tres, cuatro, *resto_valores = numeros

print(uno)
print(dos)
print(tres)
print(cuatro)
print(resto_valores)

# Si se declara lo mismo pero después del * agregamos un guión bajo le estamos 
# diciendo a python que no vamos a querer trabajar con estos valores
# Si no vamos a trabajar con esos valores es mejor no agregarlos y no utilizar este tipo
# de declaraciones

# * -> lista
# _ -> Omitir valor

numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# Esto nos creará variables del uno al cuatro y luego los últimos dos y no creará 
# las variables para el 5, 6, 7, 8
uno, dos, tres, cuatro, *_, nueve, diez = numeros

print(uno)
print(dos)
print(tres)
print(cuatro)
print(nueve)
print(diez)

# Ahora si ponemos *resto_valores los valores del 5 al 8 van a ser almacenados en una lista
uno, dos, tres, cuatro, *resto_valores, nueve, diez = numeros

print(uno)
print(dos)
print(tres)
print(cuatro)
print(resto_valores)
print(nueve)
print(diez)


# Con esto omitiremos la creación del elemento en el índice 1 
# entonces se crearán variables para el 1, 3, 4, 9, 10
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
uno, _, tres, cuatro, *resto_valores, nueve, diez = numeros



print(uno)
print(tres)
print(cuatro)
print(nueve)
print(diez)