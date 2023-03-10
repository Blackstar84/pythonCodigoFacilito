lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java', 'Rust']
#                  0          1        2       3        4       5

# [start:end]

'''
[START:END]
 RECORDAR QUE EL ÍNDICE DEL FINAL ES SIEMPRE UNO ANTERIOR, ES DECIR SI PONEMOS 
 POR EJEMPLO [1:4] VA A TRAER DATOS DESDE EL 1 HASTA EL ÍNDICE 3, EL ELEMENTO EN 
 LA POSICIÓN 4 NO SE VA A INCLUIR
'''
# Esto tomará elementos desde el ídice 0 al 2
sub_lista = lista_cursos[0:3]

print(sub_lista)

# sublista del índice 1 al 4
# Esto tomará elementos desde el ídice 1 al 3

sub_lista = lista_cursos[1:4]

print(sub_lista)


# Esto devolverá los elementos desde el 1 hasta el final, no devolverá ningún error por más que el índice final sea menor al número especificado
sub_lista = lista_cursos[1:100]

print(sub_lista)

# Si queremos traer desde cierto índice hasta el último elemento de la lista le damos [start:]
#[start:] -> Obtenemos los últimos elementos de la lista a partir del índice especificado
# por ejemplo queremos traer desde el índice 1 hasta el 5 [1:]

sub_lista = lista_cursos[1:]

print(sub_lista)


# Para tomar todos los elementos desde el inicio hasta un índice específico lo hacemos de la siguiente manera [:end]

# [:end] -> Obtenemos los primeros elementos desde el inicio hasta el índice especificado
# por ejemplo queremos traer todos los elementos desde el inicio hasta el índice 4 [:4]
sub_lista = lista_cursos[:4]

print(sub_lista)


# [start:end:skip] skip sería para saltarse elementos
# ejemplo [1:5:2] traería Django, Ruby ya que recordemos que el índice 5 no es incluído
# aquí traería Django ya que es el primer índice y de ahí iría de 2 en 2

sub_lista = lista_cursos[1:5:2]

print(sub_lista)

# Si ponemos de [0:5:2] traería los elementos de Python, Flask, Java

sub_lista = lista_cursos[0:5:2]

print(sub_lista)

# si ponemos [::-1] nos devolvería la lista completa pero invertida
sub_lista = lista_cursos[::-1]

print(sub_lista)
