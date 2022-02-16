# -*- coding: ISO-8859-15 -*-

# Creamos la lista planets y la mostramos
planetas = [ "Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]

print(f"Los {len(planetas)} planetas del sistema solar son: ",planetas)

# Agregamos a plutón y mostramos el último elemento
planetas.append("Plutón")

print(f"Antes se mencionaba el último planeta que era: ",planetas[-1])