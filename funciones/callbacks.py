# No son más que funciones las cuáles son utilizadas como argumentos para otras 
# funciones y serán las funciones que reciban estos argumentos las cuales las llamen

promedio = lambda *args : sum(args) / len(args)

aprobatorio = lambda calificacion : calificacion >= 7

def es_aprobatorio(calificacion):
    return calificacion >= 90

""" print(promedio(10, 10, 9, 8, 7))


print(aprobatorio(7))
print(aprobatorio(5)) """

# Lo que hacemos aquí es pasarle funciones como argumentos
def mostrar_mensaje(func_promedio, func_aprobatorio, *args):
    # con *args dentro de func_promedio le estamos pasando la N cantidad de argumentos
    # a nuestra función 

    promedio = func_promedio(*args)
    # En la función promedio guardamos el resultado de la operación promedio
    #  de los puntajes que pasamos como parámetros

    # Aquí verificamos si el valor es true o false llamando a la función aprobatorio
    # o a la función es aprobatorio, en base a qué función pasemos como segundo 
    # parámetro al llamar a la función mostrar_promedio()
    # a esto es a lo que se le conoce como programación modular 
    if func_aprobatorio(promedio):
        print(f'Felicidades, aprobaste la materia con {promedio}')
    else:
        print(f'No aprobaste la materia, tu promedio fue: {promedio}')    


mostrar_mensaje(promedio, aprobatorio, 10, 1, 1, 7, 7)  
mostrar_mensaje(promedio, aprobatorio, 10, 10, 1, 7, 7)      
mostrar_mensaje(promedio, es_aprobatorio, 10, 10, 1, 7, 7)  