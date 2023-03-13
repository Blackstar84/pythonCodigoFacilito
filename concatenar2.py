nombre = 'Carlos'
apellido = 'Almada'

nombre_completo = 'Mr. {} {} {}.'.format(nombre, apellido, 'Aguilar')

print(nombre_completo)


nombre_completo = 'Mr. {nombre} {primer_apellido} {segundo_apellido}.'.format(
    nombre= nombre,
    primer_apellido= apellido,
    segundo_apellido= 'Aguilar')

print(nombre_completo)