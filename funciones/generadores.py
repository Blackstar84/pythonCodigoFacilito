
def pares():
    for numero in range(0, 100, 2):
        #print(numero)
        # Al ejecutar return finalizaremos automáticamente la ejecución de la función
        # Por ese motivo sólo imprimirá cero 0
        return numero
        # Esto no se mostrará porque la operación finaliza en el return numero que se encuentra en la línea anterior
        print('Mensaje luego de return no se ejecutará')




print(pares())




def pares2(): # Generador -> Lazy iterator
    for numero in range(0, 100, 2):
        # La palabra reservada yield nos permite retornar valores sin que la función finalice
        # únicamente pausando su ejecución para que posteriormente pueda reanudarse desde el punto
        # donde se quedo
        # La función retorna y pausa su ejecución
        yield numero
        
        print('Se reanuda la ejecución')
       

# En cada iteración retorna y pausa su ejecución
for par in pares2():
    print(par)