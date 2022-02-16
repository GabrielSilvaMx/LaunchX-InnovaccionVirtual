# -*- coding: ISO-8859-15 -*-

# Creamos la variable que almacena el texto
ingreso_planeta = ''
# Creamos la lista que almacena cada uno de los textos que el usuario ingresa
planetas = []

# Ciclo while
while ingreso_planeta != '0':
    if ingreso_planeta:
        # Almacenamos ese valor en la lista        
        planetas.append(ingreso_planeta.capitalize())
    # Capturamos un nuevo valor   
    ingreso_planeta = input('\nIngresa un nuevo planeta (en minúsculas), escribe 0 para terminar: ')

print("Los planetas que ingresaste fueron: ")
for planeta in planetas:
    print(planeta)
