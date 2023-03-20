
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


# Para Heredar de varias clases separamos por coma dentro de los paréntesis
# Python permite la herencia múltiple
class Gato(Mascota, Felino): # Clase Hija
    pass


shadow = Gato()

shadow.comer()
shadow.dormir()
shadow.cazar()