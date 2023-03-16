
def saludar():

    def mostrar_mensaje():
        print('Hola nos encontramos en el curso de Python.')

    return mostrar_mensaje


respuesta = saludar()

# Imprimirá la función saludar que llama a la función mostrar_mensaje, no mostrará el mensaje de impresión que 
# se encuentra dentro de mostrar_mensaje
# <function saludar.<locals>.mostrar_mensaje at 0x0000024CF640EE60>
print(respuesta)

# Imprimirá el tipo de valor de 
print(type(respuesta))
# <class 'function'>

# Al llamar a la función de esta manera imprimirá lo que se encuentre dentro de la llamada a la 
# función mostrar_mensaje
respuesta()
# Hola nos encontramos en el curso de Python.
