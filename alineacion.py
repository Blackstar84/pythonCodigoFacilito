mensaje = 'Hola Mundo!'

# ljust -> Justifica a la Izquierda
# rjust -> Justifica a la Derecha
# center -> Centrar el texto
# Estos métodos no modifican al String original sino que apartir de él se genera uno nuevo

# Agregará 20 espacios a la izquierda del String
mensaje = mensaje.ljust(20)
print(mensaje, '.')

mensaje2 = 'Hola Mundo!'

# Agregará 20 espacios a la derecha del String
mensaje2 = mensaje2.rjust(20)
print(mensaje2) 

mensaje3 = 'Hola Mundo!'

# Agregará 20 espacios en total, 
# 10 espacios a la izquierda y 10 espacios derecha del String
mensaje3 = mensaje3.center(20)
print(mensaje3)

