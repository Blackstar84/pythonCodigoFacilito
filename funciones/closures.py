# No es más que una función la cual puede generar de forma dinámica a otra función y esta nueva función 
# puede acceder a las variables locales aún cuando la primera haya finalizado

def saludar(username):
    mensaje = f'Hola {username}' # Variable Local

    def mostrar_mensaje(): # Función Anidada
        print(mensaje)

    return mostrar_mensaje # Retorna la función Anidada


username = 'Cody'
 
respuesta = saludar(username)

respuesta()

username = 'Carlos'
 
#respuesta = saludar(username)
respuesta()

"""
    Aquí vemos que definimos de vuelta la variable con el valor Carlos
    luego llamamos de vuelta a la función respuesta y esta devolverá Cody 
    no Carlos, esto porque mantiene en memoria la variable declarada la primera vez
    y que luego es seteada dentro de respuesta, que es donde pasamos esa variable de username
    si volvemos a definir respuesta = saludar(username) esto si tomara la nueva variable definida
    
"""