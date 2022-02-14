# Almacenar las entradas del usuario

nombre_planeta1 = input("Escribe el nombre del primer planeta: ")
distancia_planeta1 = input("Distancia al sol en km: ")
nombre_planeta2 = input("Escribe el nombre del segundo planeta: ")
distancia_planeta2 = input("Distancia al sol en km: ")

# Convierte las cadenas de ambos planetas a numeros enteros
distancia_planeta1 = abs(int(distancia_planeta1))
distancia_planeta2 = abs(int(distancia_planeta2))

print("Planeta   | Distancia al sol")
print(f"{nombre_planeta1} | {distancia_planeta1:,} km")
print(f"{nombre_planeta2} | {distancia_planeta2:,} km" )

# Calcular la distancia entre planetas
diferencia_distancia =  abs(distancia_planeta2 - distancia_planeta1) * 0.621
# En millas
print(f"La distancia entre {nombre_planeta1} y {nombre_planeta2} es de {diferencia_distancia:,} millas")