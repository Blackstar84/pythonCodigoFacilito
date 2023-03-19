# Attrs de clase -> no serán más que atributos que le pertenecen a una clase
# y para poder utilizarlos obligatoriamente debemos utilizar dicha clase
# Attrs de instancia -> no serán más que atributos que le pertenezcan a un objeto
# y para poder utilzarlo trabajaremos con el objeto


class Usuario:
    # Para que esta función sea un método debe recibir al menos un parámetro
    # Por convensión el nombre de este parámetro debe ser self
   
    def inicializar(self):
        # Estos atributos se van a añadir siempre que llamemos a la función inicializada
        # username y password van a ser añadidos al objeto
        # Añadimos atributos al objeto
        self.username = ''
        self.password = ''


user1 = Usuario()
user2 = Usuario()

# Esto devolvera un diccionario vacío

print(user1.__dict__)
# {}

print(user2.__dict__)
# {}


# Si a estos objetos ejecutamos el método inicializar a los dos
# Se van a agregar de forma dinámica estos atributos al objeto
# tanto para user1 como para user2

user1.inicializar()
user2.inicializar()

print(user1.__dict__)
# {'username': '', 'password': ''}

print(user2.__dict__)
# {'username': '', 'password': ''}

# Estos atributos se añaden al objeto al momento de llamar al método inicializar




class UsuarioNuevo:
    
   # Al agregar más parámetros a self estos deben ser pasados a la hora de inicializar el
   # objeto
    def inicializar(self, username, password):
        # Estos atributos se van a añadir siempre que llamemos a la función inicializada
        # username y password van a ser añadidos al objeto
        # Añadimos atributos al objeto
        self.username = username
        self.password = password


usuario1 = UsuarioNuevo()
usuario1.inicializar('Carlos', '12345')

usuario2 = UsuarioNuevo()
usuario2.inicializar('Lujan', '456')

usuario3 = UsuarioNuevo()
usuario3.inicializar('Cody', '678')

print(usuario1.__dict__)
print(usuario2.__dict__)
print(usuario3.__dict__)

# con __init__ seremos capaces de inicializar los atributos de un objeto al momento de
# instanciarlo, por lo tanto ya no habrá necesidad de utilizar métodos que nos permitan
# inicializar atributos, ya que estaríamos realizando una tarea doble