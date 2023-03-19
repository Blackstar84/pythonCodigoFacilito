# Attrs de clase -> no serán más que atributos que le pertenecen a una clase
# y para poder utilizarlos obligatoriamente debemos utilizar dicha clase
# Attrs de instancia -> no serán más que atributos que le pertenezcan a un objeto
# y para poder utilzarlo trabajaremos con el objeto


class Usuario:
    # Atributos de clase
    username = 'Username por Default'
    email = ''

# De esta forma podemos utilizar los atributos de clase
# clase.atributo

print(Usuario.username)

# Para modificar un atributo de clase

Usuario.username = 'User1'
Usuario.email = 'carlosalmada84@gmail.com'
print(Usuario.username)
print(Usuario.email)