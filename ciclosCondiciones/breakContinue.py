titulo_curso = 'Curso profesional de Python'


# Esto imprimirá cada caracter uno bajo a otro del String que se encuentra en la variable titulo_curso

''' for caracter in titulo_curso:
    print(caracter)
 '''

# Con break rompemos (Finalizamos el ciclo for) la ejecución del ciclo
for caracter in titulo_curso:
    if caracter == 'P':
        break

    print(caracter)


# Con continue simplemente saltamos la impresión del caracter si el caracter es igual a P, luego seguirá imprimiendo
#  el resto de caracteres
for caracter in titulo_curso:
    if caracter == 'P':
        continue

    print(caracter)


# Aquí sólo evitaremos imprimir los espacios
for caracter in titulo_curso:
    if caracter == ' ':
        continue

    print(caracter)