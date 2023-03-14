# Para definir una función agregar def seguido del nombre que deseemos
# Si es una palabra compuesta usar suma_valores snake case

# PARA RECORDAR
# AL UTILIZAR INPUT ESTE DEVUELVE UN VALOR DE TIPO STRING, DEBEMOS CONVERTIRLO A TIPO INT
# PARA PODER REALIZAR OPERACIONES MATEMÁTICAS CON LOS MISMOS

def suma():

    # Convertimos a int los valores introducidos por el usuario
    numero_uno = int(input('Ingresa el primer número entero: '))
    numero_dos = int(input('Ingresa el segundo número entero: '))

    # En la variable resultado guardamos el valor de la suma de los dos números
    # y luego los imprimimos

    resultado = numero_uno + numero_dos
    print(resultado)

# Llamamos a la función  
suma()    

# Podemos llamar las N cantidad veces que deseemos a la función y pasarle varios parámetros

suma()
suma()