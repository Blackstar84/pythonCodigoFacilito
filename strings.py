lenguajes = 'Python Ruby Java Rust C++ C'

listado_lenguajes = lenguajes.split()  
# por defecto toma los espacios para dividir los elementos

print(listado_lenguajes)

# Si queremos dividir por los caracteres por los cuáles deseemos separar 
# ponemos el mismo dentro del split

lenguajes = 'Python-Ruby-Java-Rust-C++-C'

listado_lenguajes = lenguajes.split('-')  

print(listado_lenguajes)

# Si deseamos limitar la cantidad de divisiones hacemos lo siguiente

lenguajes = 'Python-Ruby-Java-Rust-C++-C'
# Como vemos le decimos que divida dos veces y luego el resto lo tome como un 
# solo elemento
listado_lenguajes = lenguajes.split('-', 2)  

# Esto nos devolverá una lista con los siguientes elementos
# ['Python', 'Ruby', 'Java-Rust-C++-C']
# Como podemos observar dividió 2 veces y luego el resto metio como un único elemento

print(listado_lenguajes)


# Método join nos permite generar un string apartir de una lista

lenguajes = ['Python', 'Ruby', 'Java', 'Rust']

# Con join podemos unir cada uno de los elementos del listado en un string separado por 
# espacios 
string_lenguajes = ' '.join(lenguajes)

print(string_lenguajes)

print(type(string_lenguajes))

# Si queremos unir cada uno de los elementos por algún caractér especial se lo ponemos
# por ejemplo: '-'.joint(lenguajes) va a devolver un string con todos los elementos 
# de la lista unidos por -
# Python-Ruby-Java-Rust

string_lenguajes = '-'.join(lenguajes)

print(string_lenguajes)