# Para que un parámetro sea opcional ponemos = luego del parámetro seguido del valor 
# default
# Por convención poner el nombreParámetro=valor sin espacios, esto debe estar junto
# cuando declaramos un valor por default pi=3.14
def area_circulo(radio, pi=3.14):
    # area de un círculo es pi x radio al cuadrado
    # para elevar a una potencia en python utilizamos doble asterisco y la cantidad 
    # a la cuál deseemos elevar
    return pi * (radio ** 2)

# En este caso pasamos dos valores y el segundo parámetro reemplazar al que 
# está por default
resultado = area_circulo(10, 3.141592)

print(resultado)

# En este caso tomará el primer valor y el segundo tomará el valor por default definido 
# en la función 
resultado = area_circulo(32)

print(resultado)

# En python podemos utilizar el nombre de los parámetros que recibe la función
# con esto podemos alterar el orden de los parámetros que le pasamos a la función 
# ya que python va a identificar los parámetros en el orden que definamos

resultado_sin_orden = area_circulo(pi=3.2,radio=32)
# Aquí python sabe que el primer parámetro que definimos corresponde 
# al segundo argumento que recibe la función area_circulo y que el segundo parámetro
# radio corresponde al primero
# Esto porque pusimos pi=valor y el identifica que el mismo nombre corresponde al segundo
# valor que recibe y radio=valor corresponde al primer valor que recibe

print(resultado_sin_orden)

