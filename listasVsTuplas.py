# Cuando no sepamos la cantidad de elementos a almacenar y/o sepamos que estos 
# elementos pueden variar ya sea que modifiquen su valor incrementen o decrezcan en cantidad
# Haremos uso de Lista

# Si los elementos a almacenar no cambiarán y queremos que se conserven así por el resto
# del programa Haremos uso de tuplas


cursos = ['Python', 'Django', 'Flask']

niveles = ('Básico', 'Intermedio', 'Avanzado')

# Generar Listas a partir de Tuplas o Tuplas a partir de Listas

# Gerenrar Tupla a partir de Lista

cursos_tupla = tuple(cursos)

print(cursos_tupla)

print(type(cursos_tupla))


# Generar Lista a partir de Tupla

niveles_lista = list(niveles)

print(niveles_lista)
print(type(niveles_lista))
