''' contador = 1

while contador <= 10:
    print(contador)

    contador = contador + 1 '''


numero = 123456789
contador_digitos = 0

while numero >=1:
    # Esto es lo mismo que el código de contador_digitos += 1
    # contador_digitos = contador_digitos + 1
    contador_digitos += 1

    numero = numero / 10
# cuando numero se menor a 1 ingresará en el else y se ejecutará el print de contador_digitos    
else:
    # Devolverá la cantidad de dígitos que tiene el número que le pasamos
    print(contador_digitos)


