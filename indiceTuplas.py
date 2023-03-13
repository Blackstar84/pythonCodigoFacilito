cursos = ('Python', 'Flask', 'Django', 'Rails', 'MongoDB')
#            0         1        2         3         4

primer_curso = cursos[0]

print(primer_curso)


primer_curso = cursos[-1]

print(primer_curso)

# Esto devolverá los elementos desde el índice 0 al 2
# Traerá Python, Flask y Django

sub_tupla = cursos[0:3]

print(sub_tupla)

# Esto devolverá los elementos desde el inicio hasta el índice final especificado
# Traerá Python, Flask y Django

sub_tupla = cursos[:3]

print(sub_tupla)

# Si no ponemos ningun valor en entre los índices de start y end generará 
# una nueva tupla con todos los valores de la tupla original
sub_tupla = cursos[:]

print(sub_tupla)