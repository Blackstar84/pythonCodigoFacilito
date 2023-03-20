
def pares(): # Generador -> Lazy Iterator
    for numero in range(0, 12, 2):
        yield numero # La función suspende su ejecución

        print('Se reanuda la ejecución')

generador = pares()

# De esta manera vamos obteniendo los datos que necesitemos de a uno y no utilizamos memoria que no necesitemos

# Cada vez que se llama a la función next() se ejecuta el programa y retorna un valor y el mismo vuelve a quedar
# pausado hasta su siguiente llamada

# Esto imprimirá los números pares del 0 al 12 ya que lo llamamos 7 veces

print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print('Ejecutamos código entre un llamado y otro.')
print(next(generador))

# Si intentamos llamar a un valor que no existe dentro de nuestro rango nos dará un error de StopIteration
# Esto lo podemos resolver con una sentencia Try Catch 
generador = pares()

# Lo que hacemos aquí es ejecutar mientras sea True el try except es lo mismo que try catch el catch en pthon correponde
# a la palabra reservada except
while True:
    try:
        par = next(generador)
        print(par)
    except StopIteration:
        print('El generador finalizo.')
        break # Con el break finalizamos la iteración y salimos del bloque


