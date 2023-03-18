# Docstring

# Para documentar utilizaremos Docstring
# Se coloca dentro de triple comillas dobles en la primera línea de nuestra
# función
# En la primera línea vamos a colocar una breve descripción de la tarea que realiza 
# la función 
# posteriormente detallamos cada una de las partes de la función, los argumentos y los 
# valores que retorna

# __doc__ (Módulos, Clases, Métodos y Funciones)

def suma(numero_1, numero_2):
    """
    La función suma dos números enteros.

    Argumentos:
    numero_1 (int)
    numero_2 (int)

    Se retorna la suma de los parámetros.

    >>> suma(10, 20)
    30

    >>> suma(100, 200)
    300

    """
    return numero_1 + numero_2


# Podemos testear nuestra función con el Docstring
# Para esto dentro de la documentación de nuestra función agregamos los 
# >>> nombreFunción(parametro1, parámetro2)
#     valor que debería retornar
# Luego por consola escribimos lo siguiente:

# python -m doctest testear.py 

# si no da ningún error es porque paso las pruebas
# en nuestro ejemplo le pasamos dos pruebas
# >>> suma(10, 20)
# 30
# que debe retornar el valor 30
# y luego
# >>> suma(100, 200)
# 300
# que debe retornar el valor 300

# si ponemos por ejemplo que realice una prueba y de un valor incorrecto
# >>> suma(100, 200)
# 500
# dará un error, que dirá se esperaba 500 y se obtiene 300

# El módulo doctest se encargará de probar todos los objetos documentables dentro 
# del archivo y para ello probará utilizando el Docstring

def resta(numero_1, numero_2):
    """
    >>> resta(100, 200)
    -100
    """
    return None

# Devolverá un error porque en la prueba le estamos diciendo que debería retornar -100
# Y está retornando nada

"""
**********************************************************************
File "/Users/Blackstar/Documents/pythonCodigoFacilito/funciones/testear.py", line 59, in testear.resta
Failed example:
    resta(100, 200)
Expected:
    -100
Got nothing
**********************************************************************
1 items had failures:
   1 of   1 in testear.resta
***Test Failed*** 1 failures.
"""