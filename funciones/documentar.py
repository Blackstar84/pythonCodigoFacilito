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

    TODO: 
        *
    """
    return numero_1 + numero_2

# De estas dos maneras podemos mostrar la documentación que tiene nuestra función

print(suma.__doc__)

print(help(suma))
