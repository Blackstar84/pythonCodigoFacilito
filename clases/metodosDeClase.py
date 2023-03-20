
class Circulo:

    pi = 3.141592

# Por convención un método de clase debe tener entre parámetros la palabra cls que hace referencia a la clase

    # Para que sea un método de clase debemos utilizar @classmethod
    @classmethod
    def area(cls, radio):
        return cls.pi * (radio ** 2)
    
# El método de clase area lo estamos ejecutando sin necesidad de crear un objeto
resultado = Circulo().area(14)
print(resultado)