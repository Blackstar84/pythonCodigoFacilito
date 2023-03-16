# Siempre ** seguido de la palabra kwargs esto por convención
# Al poner **kwargs eso se convierte en un diccionario
def usuarios(**kwargs):
    print(kwargs)
    print(type(kwargs))

# Para pasar diccionarios hacerlo de la siguiente manera
# primero definimos un nombre seguido del signo = sin espacios y entre corchetes los valores separados por coma
# Ejemplo carlos=[1, 2, 3] esto va a ser interpretado como argumento para el diccionario
usuarios(eduardo=[10, 10, 8], fernando=[10, 9, 9])    


# Como podemos observar podemos combinar tuplas y diccionarios en los parámetros que recibe la función
def combinacion(*args, **kwargs):
    print(args)
    print(kwargs)

# Aquí los valores del 1 al 5 serán parte de la tupla y cody y curso serán parte del diccionario
combinacion(1, 2, 3, 4, 5, cody=True, curso='Python')    