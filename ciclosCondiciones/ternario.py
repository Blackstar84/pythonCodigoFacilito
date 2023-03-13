calificacion = 8
color = None


if calificacion >= 7:
    color = 'Verde'
else:
    color = 'Rojo'

print(calificacion, color)        

# Esto mismo puede hacerse con el ternario, en una sola línea

# En color definimos el valor en base a la condición if 

# Cuando definimos en una sola línea el else es obligatorio

color = 'Verde' if calificacion >= 7 else 'Rojo'

print(calificacion, color)  