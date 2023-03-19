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
        self.username = ''
        self.password = ''


user1 = Usuario()
user2 = Usuario()


print(user1.__dict__)
print(user2.__dict__)