# -*- coding: ISO-8859-15 -*-

# Planets and moons

lunas_planetas = {
    'mercurio': 0,
    'venus': 0,
    'tierra': 1,
    'marte': 2,
    'jupiter': 79,
    'saturno': 82,
    'urano': 27,
    'neptuno': 14,
    'plutón': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

# Añade el código para determinar el número de lunas.
total_de_lunas = 0

for clave in lunas_planetas.keys():
    print(f" Planeta: {clave.capitalize()} - No. de Lunas: {lunas_planetas[clave]} ")
    total_de_lunas += lunas_planetas[clave]

print("Suma total de lunas: ",total_de_lunas)
promedio = (total_de_lunas / len(lunas_planetas.keys()) )

# Muestra el promedio
print(f"Promedio de lunas en el sistema solar: ",round(promedio,2))