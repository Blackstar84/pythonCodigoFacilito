
class Usuario:

    # Object
    def __init__(self):
        print('Estamos creando un usuario')


user1 = Usuario()
user2 = Usuario()
user3 = Usuario()

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)

# Al ejecutar este programa se imprimirá 3 veces el mensaje que se encuentra dentro del
# método init, ya que el mismo se ejecuta cuando creamos instancias de un objeto




class Usuario:

    # Object
    def __init__(self):
        self.username = ''
        self.password = ''


user1 = Usuario()
user2 = Usuario()
user3 = Usuario()

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)

# Cuando creemos un objeto de tipo Usuario este objeto obligatoriamente va a poseer dos
# atributos, tanto username y passsword, por defaul estos atributos almacenarán un string
# vacío

# Con esto estaremos creando 3 instancias de objeto de tipo Usuario que tendrán 
# dentro de su diccionario un username= '' y password = '', esto fue definido dentro
# del init de la clase Usuario
# como tenemos 3 objetos imprimirá tres veces esto
# {'username': '', 'password': ''}

# El método init se ejecutará siempre que creemos un objeto de la clase



# PAsar parámetros de inicialización
class Usuario:

    # Object
    # El objeto Usuario permite inicializar estos parámetros de username y password
    # al no poner valores por defecto para username y password, estos van a ser requeridos
    # a la hora de inicializar el objeto de tipo Usuario
    def __init__(self, username, password):
        self.username = username
        self.password = password

# Si creamos instancias del Objeto Usuario y este tiene que recibir parámetros, estos
# deben ser pasados a la hora de la creación del mismo ya que los mismos van a ser
# obligatorios
user1 = Usuario('Carlos', '234')
user2 = Usuario('Cody', '109')
user3 = Usuario('Claudia', '879')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)


# Esto dará un error ya que existen parámetros obligatorios que deben ser pasados
# a la clase usuario a la hora de crear el mismo
# user11 = Usuario()
# user22 = Usuario()
# user33 = Usuario()
# TypeError: Usuario.__init__() missing 2 required positional arguments:
#  'username' and 'password'
# indica que necesita los argumentos de username y password a la hora de crear la instacia
# del objeto Usuario
# print(user11.__dict__)
# print(user22.__dict__)
# print(user33.__dict__)



class Usuario:

    # Object
    # El objeto Usuario permite inicializar estos parámetros de username y password
    # En este caso es opcional agregar el usuario y contraseña, en caso de no poner
    # un valor inicial, hemos definido que usuario y password tendrán un string vacío
    def __init__(self, username='', password=''):
        self.username = username
        self.password = password


user1 = Usuario('Carlos', '234')
user2 = Usuario('Cody', '109')
user3 = Usuario()


print(user1.__dict__)
# {'username': 'Carlos', 'password': '234'}

print(user2.__dict__)
# {'username': 'Cody', 'password': '109'}

print(user3.__dict__)
# {'username': '', 'password': ''}



