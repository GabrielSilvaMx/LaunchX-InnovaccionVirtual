# -*- coding: ISO-8859-15 -*-

# Lista de planetas
planetas = [ "Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]
print(f"Los {len(planetas)} planetas del sistema solar son: ",planetas)

nombre_planeta = input("Indica que planeta deseas consultar: ")

indice_planeta= planetas.index(nombre_planeta)
print(f"{nombre_planeta} es el planeta # {indice_planeta + 1} del Sistema Solar")

# Muestra los planetas más cercanos al sol
planetas_cercanos = planetas[:indice_planeta]
planetas_lejanos = planetas[indice_planeta+1:]
print(f"Los planetas mas cercanos al Sol antes que {nombre_planeta} son: ",planetas_cercanos)
print(f"Los planetas mas lejanos al Sol despues que {nombre_planeta} son: ",planetas_lejanos)
