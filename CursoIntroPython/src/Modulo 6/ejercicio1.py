# -*- coding: ISO-8859-15 -*-

# Creamos la lista planets y la mostramos
planetas = [ "Mercurio", "Venus", "Tierra", "Marte", "J�piter", "Saturno", "Urano", "Neptuno"]

print(f"Los {len(planetas)} planetas del sistema solar son: ",planetas)

# Agregamos a plut�n y mostramos el �ltimo elemento
planetas.append("Plut�n")

print(f"Antes se mencionaba el �ltimo planeta que era: ",planetas[-1])