''' # range por default comenzará en 0 hasta el 10
range = range(11) # 0 - 10

# Si ponemos range de 20 será del 0 al 19, el 20 no será incluido dentro del rango
# range = range(20) # 0 - 19

# imprimira un objeto de tipo range con valores del 0 al 10 
print(range)
# Esto es lo que imprimirá:  range(0, 11)

# Nos devolverá que la variable range es del tipo range
print(type(range))


# Podemos recorrer ese objeto con un for 
for valor in range:
    print(valor)
 '''

''' for valor in range(21):    
    print(valor) '''



# si queremos especificar desde donde empezar agregamos otro argumento al método range
# El primer parámetro será el inicio y el segundo es hasta donde ir, si agregamos un tercer argumento 
# este sería tipo un salto por ejemplo ir de 2 en 2, si agregamos 3 saltos de 3 en 3
# start=0, end, skips

# esto haría un range del 5 al 20
for valor in range(5,21,2):    
    print(valor)

numeros = [10, 20, 30, 40, 50]


# La función enumerate nos va a retornar un objeto iterables que a su vez tiene tuplas, estas tuplas van a almacenar 
# dos valores, el primer valor hace referencia al índice del elemento dentro de la colección y el segundo valor 
# hace referencia al elemento en sí el cual estamos iterando
for indice, numero in enumerate(numeros):
    print(indice, numero)


# Si queremos modificar el índice agregamos un segundo argumento

# en este caso queremos que el índice inicie en 10

# no es muy común ver este tipo de código

for indice, numero in enumerate(numeros, 10):
    print(indice, numero)