# Pasar parámetros a una función
# dentro de la definición de la función le pasamos los parámetros
# a los valores de entrada los conoceremos como argumentos
def suma(n1, n2):
    resultado = n1 + n2
    print(resultado)


numero_uno = int(input('Ingresa el primer número entero: '))
numero_dos = int(input('Ingresa el segundo número entero: '))    

suma(numero_uno, numero_dos)

suma(10,5)

