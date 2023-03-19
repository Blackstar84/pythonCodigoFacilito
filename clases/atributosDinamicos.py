# Attrs de clase -> no serán más que atributos que le pertenecen a una clase
# y para poder utilizarlos obligatoriamente debemos utilizar dicha clase
# Attrs de instancia -> no serán más que atributos que le pertenezcan a un objeto
# y para poder utilzarlo trabajaremos con el objeto


class Usuario:
    # Atributos de clase
    username = 'Username por Default'
    email = ''

# Añadiremos atributos dinámicos a nuestro objeto

user1 = Usuario()

# Este atributo le pertenece al objeto y no a la clase y lo añade en tiempo de ejecución
user1.username = 'Carlos' # De esta manera añadimos el atributo al objeto
# Van a tener ids diferentes porque uno es un atributo de instancia y el otro de clase

print(id(user1.username)) # Atributo de instancia
print(id(Usuario.username)) # Atributo de clase

print(user1.__dict__)
# Nos devolverá un diccionario con una llave y un valor
# {'username': 'Carlos'}

# De esta manera podemos añadir atributos dinámicos a nuestro objeto

user1.password = '123BVF'

print(user1.__dict__)



user1.password = 'password'

print(user1.__dict__)


user2 = Usuario()


# Esto dará un  error porque el atributo password sólo fue añadido al user1 y 
# el atributo password no existe en la clase

# Los objetos pueden tener atributos completamente diferentes
print(user2.password)

# Cuando los objetos son de la misma clase, lo recomendable es estandarizar los atributos
# que pueden llegar a tener 
# Esto para que user1 y user2 tengan la misma cantidad y tipos de atributos