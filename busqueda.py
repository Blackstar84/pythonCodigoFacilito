titulo_curso = 'Curso profesional de Python, donde aprenderemos Python'

# Devolverá la cantidad de veces que existe una palabra o un caracter dentro de un String
contador = titulo_curso.count('Python')

print(contador)

# Esto devolverá la cantidad de veces que existe la letra "O" dentro del String
# devolverá 7 que es la cantidad de O que existe en el String
cantidad_o = titulo_curso.count('o')

print(cantidad_o)

# En caso de no existir devolverá cero 0
cantidad_x = titulo_curso.count('x')

print(cantidad_x)


# Otra forma es utilizar in esto devolverá True o False
# En este caso devolverá True ya que Python existe dentro del String titulo_curso
print('Python' in titulo_curso)

# Esto devolverá False porque es diferente Python a python
print('python' in titulo_curso)

# Para estandarizar podemos estandarizar las letras pasando todo a minúsculas

# En este caso devolverá True ya que pasamos todo el string a minúsculas antes de 
# buscar la palabra deseada
print('python' in titulo_curso.lower())


# También podemos pasarlo a Mayúsculas con upper()
print('PYTHON' in titulo_curso.upper())

# También podemos negar
# En este caso devolverá True ya que codigofacilito no existe en el string titulo_curso
print('codigofacilito' not in titulo_curso.lower())

# Pdemos buscar si un string existe al inicio de otro String
# Devolverá True ya que Curso se encuentra al inicio del String
print(titulo_curso.startswith('Curso'))

# Verificará si Pyton se encuentra al final del String titulo_curso
print(titulo_curso.endswith('Python'))
