# Herencia

class Mascota: # Clase Padre
    
    def comer(self):
         print('La mascota come.')

    def dormir(self):
         print('La mascota duerme.')


# Para Heredar en Pyhton ponemos entre paréntesis la clase de la cuál deseemos herdar
# En este caso la clase Perro hereda de la clase Mascota

# Al heredar la clase Perro puede acceder fácilmente a los métodos y atributos
# que se encuentren dentro de la clase Mascota

class Perro(Mascota): # Clase Hija
    pass


duke = Perro()

duke.comer()
duke.dormir()


class Gato(Mascota):
     pass

shadow = Gato()

shadow.comer()
shadow.dormir()

"""
    Como podemos observar las clases de Perro y Gato no tienen métodos ni atributos
    pero los mismos pueden acceder a los métodos dormir y comer que se encuentran
    dentro de la Clase Padre Perro por medio de la herencia
"""