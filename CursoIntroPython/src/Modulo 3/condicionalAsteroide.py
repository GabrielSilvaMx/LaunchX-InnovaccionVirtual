# %% [markdown]
# # Condicional Asteroide
#     Imprime una advertencia si un asteroide se acerca a la Tierra demasiado rápido.
# La velocidad del asteroide varía dependiendo de lo cerca que esté del sol, y cualquier velocidad superior a 25 kilómetros por segundo (km/s) merece una advertencia.

# %%
advertencia = 25

# Un asteroide se acerca y viaja a una velocidad de 49 km/s.
velocidad_asteroide = 49

# Expresión para calcular si necesita una advertencia.
if velocidad_asteroide > advertencia:
    print("***** ¡ADVERTENCIA! ****")
    print("El asteroide se acerca con una velocidad peligrosa de "+str(velocidad_asteroide)+" km/s")
else:
    print("*TODO EN ORDEN *")
    print("El asteroide lleva una velocidad de "+str(velocidad_asteroide)+" km/s")


