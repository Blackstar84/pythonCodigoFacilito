# Una función lambda conocida como función anónima, no es más que una función
# la cual es expresada en una sola línea de código además de no poseer un nombre
# ya que comunmente este tipo de funciones realizan tareas muy pequeñas

# nombreFuncion = lambda <parámetros> : <Cuerpo de la función>
# Por default la función lamdba va a retornar la expresión que hayamos colocado dentro
# del cuerpo de la función, no hace falta poner la palabra return
# Obligatoriamente la función lambda debe poseer un cuerpo. por lo menos debe haber
# una expresión que se deba ejecutar sin importar si la misma retorna o no algún valor  

funcion_grados = lambda grados : grados * 1.8 + 32

print(funcion_grados(5))


sin_parametros = lambda : True

parametros_default = lambda p1=40, p2=20, p3=60 : p1 + p2 +p3

asterisco = lambda *args, **kwargs : len(args) + len(kwargs)

print(sin_parametros())
print(parametros_default())
print(asterisco(10,20,30,hola=2, saludo='buen día'))