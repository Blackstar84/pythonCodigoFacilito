variable = 'Cody' or 'CodigoFacilito'

# Esto almacenará Cody ya que el primer string no está vacío,
#  en caso que esté vacío el primero se asignará CodigoFacilito

# Imprimirá Cody
print(variable)


variable = '' or 'CodigoFacilito'

# Imprimirá CodigoFacilito
print(variable)

variable = '' or 0 or [] or True

# Imprimirá True ya que como habíamos visto anteriormente cadenas vacías
# el número cero 0; tuplas, diccionarios y listas vacías son Falsos
print(variable)



listado = []
nombre = 'Cody'


"""
if listado:
    variable = listado
else:
    variable = nombre

"""

variable = listado or nombre

# Asignará el String Cody a la variable ya que listado es una lista vacía
print(variable)        




listado = [1]
nombre = 'Cody'

variable = listado or nombre

# Asignará el listado a la variable ya que listado contiene datos
print(variable)        


# En python todos estos valores representan y equivalen a False (falso), los que no se encuentran aquí son verdaderos
"""
    False
    None 
    0
    0.0
    ""/''
    []
    ()
    {}
"""