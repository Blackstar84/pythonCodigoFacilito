'''
    insert()
    Inserta los elementos en un índice especificado
'''
my_input = [1, 2, 3, 4, 5]
print(f'Current Numbers List {my_input}')
number = int(input("Please enter a number to be added:\n"))
index = int(input(f'Enter the index between 0 and {len(my_input) - 1} to add the given number:\n'))
my_input.insert(index, number)
print(f'Updated List {my_input}')

'''
    append()
    Inserta los elementos al final de la lista
'''

my_input = ['Engineering', 'Medical'] 
my_input.append('Science') 
print(my_input)


'''
    extend()
    Permite la inserción de una lista dentro de otra
'''
my_input = ['Engineering', 'Medical'] 
input1 = [40, 30, 20, 10] 
my_input.extend(input1) 
print(my_input)