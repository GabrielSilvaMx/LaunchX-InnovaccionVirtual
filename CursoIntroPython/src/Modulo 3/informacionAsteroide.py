# %% [markdown]
# # Operadores OR y AND 
#     Programa que emita la advertencia o información correcta a la gente de la Tierra, según la velocidad y el tamaño de un asteroide.
# 
# *Los asteroides de menos de 25 metros en su dimensión más grande probablemente se quemarán a medida que entren en la atmósfera de la Tierra.
# 
# Si una pieza de un asteroide que es más grande que 25 metros pero más pequeña que 1000 metros golpeara la Tierra, causaría mucho daño.
# También discutimos en el ejercicio anterior que:
# 
# La velocidad del asteroide varía en función de lo cerca que esté del sol, y cualquier velocidad superior a 25 kilómetros por segundo (km/s) merece una advertencia.
# Si un asteroide entra en la atmósfera de la Tierra a una velocidad mayor o igual a 20 km/s, a veces produce un rayo de luz que se puede ver desde la Tierra.

# %%


# %%
dimension_25m = 25 # metros
dimension_1000m = 1000  # metros
advertencia = 25 # km/s
rayoluz_asteroide = 20 # km/s

asteroide_distancia = 20
asteroide_velocidad = 25

# %%
# Un asteroide se acerca y viaja a una velocidad de 25 km/s.
velocidad_asteroide = 25
# su tamo es pequeño de 5 metros
tamaño_asteroide = 5

# no hay ningún peligro
if tamaño_asteroide < dimension_25m:
    if velocidad_asteroide > advertencia:
        print("***** ¡ADVERTENCIA! ****")
        print("El asteroide de "+str(tamaño_asteroide)+" metros se acerca a una velocidad de "+str(velocidad_asteroide)+" km/s")
    # produce un rayo de luz
    elif velocidad_asteroide >= rayoluz_asteroide:
        print("¡Observa el cielo!")
        print("¡El asteroide de "+str(tamaño_asteroide)+" metros está produciendo un rayo de luz!")
    else:
        print("Sin ningún peligro. Hay un asteroide de "+str(tamaño_asteroide)+" metros en el cielo.")
elif (tamaño_asteroide >= dimension_25m and tamaño_asteroide < dimension_1000m):
    print("***** ¡ADVERTENCIA! ****")
    print("El asteroide de "+str(tamaño_asteroide)+" metros puede causar daño a la Tierra.")
    print("Su velocidad es de "+str(velocidad_asteroide)+" m/s.")
    if velocidad_asteroide >= advertencia:
        print("No queda mucho tiempo.")        
    else:
        print("¡Vamos a desviarlo!")
# es mayor a 1000 m 
else:
    print("***** ¡PELIGRO! ****")
    print("¡El asteroide de "+str(tamaño_asteroide)+" metros es demasiado grande!")


