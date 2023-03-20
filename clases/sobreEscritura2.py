class Animal: # Clase Padre
    def comer(self):
        print('El animal come.')

    def dormir(self):
        print('El animal duerme.')

class Mascota(Animal): # Clase Padre
    pass


class Felino:

    def cazar(self):
        print('El felino caza.')


class Gato(Mascota, Felino): # Clase Hija
    
    def __init__(self, nombre):
        self.nombre = nombre

        

"""
    Python funciona de la siguiente manera para la herencia, en este ejemplo quiere acceder
    a los métodos comer y dormir, los mismos no se encuentran definidos dentro de la clase Gato.
    Clase con la cuál creamos el objeto patricio, entonces lo que hace Python es cuando no encuentra, busca
    en las clases que Hereda, de izquierda a derecha, en este caso irá a buscar en la clase Mascota,
    como ahí tampoco existe va a la clase Animal, ya que como vemos la clase Mascota hereda de la clase Animal,
    como ahí existe va a ejecutarse ese método
"""
patricio = Gato('Patricio')
# patricio.comer()
# patricio.dormir()



# APARTIR DE AQUÍ TRABAJAREMOS CON SOBRE ESCRITURA DE MÉTODOS

"""
    Es cuando las clases hijas pueden modificar los comportamiento de los métodos de la clase Padre, 
    esto para que se adecuen a los comportamientos deseados en la clase hija.

Para sobreescribir un método de la clase Padre, basta con definir el método en la clase hija y dentro
 definimos el nuevo comportamiento que deseamos tenga el mismo.
"""

class SerVivo:
    
    def dormir(self):
        print('El ser duerme.')


class Animal(SerVivo): # Clase Padre
    def comer(self):
        print('El animal come.')


class Mascota(Animal): # Clase Padre
    def comer(self):
        super().comer()
        print('La mascota come')


class Felino:

    def cazar(self):
        print('El felino caza.')


class Gato(Mascota, Felino): # Clase Hija
    
    def __init__(self, nombre):
        self.nombre = nombre

    # Si queremos que se ejecute el método de la clase padre podemos hacerlo utilizando la palabra
    # reservada super().nombreMetodo()
    # En este ejemplo estamos ejecutando el método comer de la clase Padre inmediata que sería
    # la clase Mascota que es la primera de la cuál hereda, recordemos que se recorre de izquierda a derecha
    # class Gato(Mascota, Felino):
    # primero buscará en la clase Mascota y si no existe buscará en la clase Felino

    def comer(self):
        super().comer()
        print(f'{self.nombre} come')

# si comentamos este método se ejecutará el método declarado en la clase SerVivo
    ''' def dormir(self):
        print(f'{self.nombre} duerme')     '''

    

patricio = Gato('Patricio')
patricio.comer()
patricio.dormir()    