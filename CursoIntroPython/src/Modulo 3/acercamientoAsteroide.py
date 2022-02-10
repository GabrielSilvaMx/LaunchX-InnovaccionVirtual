# %% [markdown]
# # Rayo de luz del asteroide desde la tierra
#     Escribe la lógica condicional para alertar a las personas de todo el mundo que deben buscar un asteroide en el cielo.
# Si un asteroide entra en la atmósfera de la Tierra a una velocidad mayor o igual a 20 km/s, a veces produce un rayo de luz que se puede ver desde la Tierra.

# %%
rayoluz_asteroide=20

#  ¡Hay uno que se dirige a la tierra ahora a una velocidad de 19 km/s!
velocidad_asteroide = 19

# Determinar si puedes ver el rayo de luz desde la tierra
if velocidad_asteroide<=0:
    print("Nada que ver por el momento en el cielo.")
elif velocidad_asteroide < rayoluz_asteroide:
    print("Atento próximamente.")
    print("¡Hay un asteroide que se dirige a la tierra a una velocidad de "+str(velocidad_asteroide)+" km/s!")
elif velocidad_asteroide == rayoluz_asteroide:
    print("Observa el cielo y busca en este momento esa luz brillante... ¡Es el asteroide!")
else:
    print("¡No te lo pierdas! Observa el cielo y mira esa luz brillante... ¡Es un asteroide!")



