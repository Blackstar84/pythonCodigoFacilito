lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java', 'Rust']
#                  0          1        2       3        4       5

print(lista_cursos)
print(len(lista_cursos))

# Añadir nuevos elementos a la lista

# Con append agregamos elementos al final de la lista
lista_cursos.append('MongoDB')
lista_cursos.append('C#')
lista_cursos.append('JavaScript')

# Con insert(índice,valorAInsertar) este recibe 2 parámetros el primero es el índice donde deseamos insertar el mismo 
# y el segundo es el valor que deseamos insertar  
# En este ejemplo insertamos el valor PyGame en la posición 0 de la lista
lista_cursos.insert(1, 'Rails')
lista_cursos.insert(0, 'PyGame')

print(lista_cursos)

print(len(lista_cursos))

# con len(nombreLista) obtenemos la longitud de la lista


# Extender lista
# con extend añadimos los elementos de una lista a otra

lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java', 'Rust']
#                  0          1        2       3        4       5

lista_cursos_2 = ['C', 'C++', 'Docker']
#                  0     1       2        

lista_cursos.extend(lista_cursos_2)

# Como podemos observar lista_cursos fue modificado mientras que lista_cursos_2 sigue igual
print(lista_cursos)

print(lista_cursos_2)


# Eliminar Elementos de una lista

lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java', 'Rust']
#                  0          1        2       3        4       5

lista_cursos.append('MongoDB')
lista_cursos.append('C#')
lista_cursos.append('JavaScript')

lista_cursos.insert(1, 'Rails')
lista_cursos.insert(0, 'PyGame')

print(lista_cursos)

# Con remove(valorAEliminar) pasamos el nombre del elemento que deseemos eliminar 
lista_cursos.remove('MongoDB')

print(lista_cursos)

# Otra forma de eliminar es pasando el índice
#Por Ejemplo: queremos eliminar el elemento en el índice 0
# se utiliza la palabra reservada del nombreLista[índice] 

del lista_cursos[0]
print(lista_cursos)

# Para dejar vacía una lista utilizamos el método clear
# nombreLista.clear()


lista_cursos.clear()
print(lista_cursos)
print(len(lista_cursos))