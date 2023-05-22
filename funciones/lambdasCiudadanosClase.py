def centigrados_a_farenheit(grados):
    return grados * 1.8 + 32

""" print(centigrados_a_farenheit(10))
print(centigrados_a_farenheit(-1))
print(centigrados_a_farenheit(8)) """

# Las funciones en python son ciudadanos de primera clase, puden ser asignadas a variables
# Las funciones pueden ser utilizadas como argumentos de otras funciones, e incluso
# Las funciones puden retornar otras funciones

# Lo que hacemos aquí es asignar una función a una variable, para esto ponemos el nombre
# de la variable = nombreFunción sin los paréntesis
# Ejemplo calcular_grados = centigrados_a_farenheit
mi_funcion = centigrados_a_farenheit

print(type(mi_funcion))

# Luego escribimos el nombre de la variable y entre paréntesis le pasamos todos los 
# parámetros que necesita la función, en este caso es un sólo parámetro que son los grados
print(mi_funcion(45))

