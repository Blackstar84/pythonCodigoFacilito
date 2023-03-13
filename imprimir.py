nombre = 'Carlos Antonio'
apellido = 'Almada'

# Por Default al usar la funció print nos imprimirá por consola los strings separados 
# por espacio
print(nombre, apellido, 'Aguilar')

print(nombre, apellido, 'Aguilar', (12, 34, 55))

# Si queremos separar por otro caracter lo especificamos utilizando 
# el parámetro sep='character'
# En este ejemplo utilizamos sep='*' va a imprimir los valores separados por espacios
# Esto imprimirá lo siguiente: Carlos Antonio*Almada*Aguilar*(12, 34, 55)
print(nombre, apellido, 'Aguilar', (12, 34, 55), sep='*')

# ASí también podemos utilizar el Fstring dentro del print para no declarar una variable 
# que va a imprimir lo mismo
print(f'Mr. {nombre} {apellido} {"Aguilar"} {38 * 2}.')


