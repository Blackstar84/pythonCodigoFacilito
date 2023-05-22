# Attrs de clase -> no serán más que atributos que le pertenecen a una clase
# y para poder utilizarlos obligatoriamente debemos utilizar dicha clase
# Attrs de instancia -> no serán más que atributos que le pertenezcan a un objeto
# y para poder utilzarlo trabajaremos con el objeto


class Usuario:
    # Atributos de clase
    username = 'Username por Default'
    email = ''

# meta atributo __dict__
user1 = Usuario()
# 1.- Verifica si el atributo existe dentro del objeto, si existe se utiliza el atributo
# 2.- Verifica si el atributo se existe dentro de la clase -> Lectura
# 3.- Si no existe al atributo dentro de la clase devolverá un error, ya que no existe 
# dentro de la clase ni del objeto

print(user1.username)

print(id(user1.username))
print(id(Usuario.username))

"""
    Mediante __dict__ podemos conocer todos los atributos que posea nuestro
    objeto, esto mediante un diccionario
"""
print(user1.__dict__)

print(Usuario.__dict__)
