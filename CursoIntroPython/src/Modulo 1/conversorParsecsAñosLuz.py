# %% [markdown]
# # Construir un convertidor de unidades.
# Programa de conversión entre parsecs y años luz.

# %%
# 1 parsec es 3.26156 años luz
parsec = 3.26156
lightyears = 0

# %%
parsecs = input("Ingresa los parsec a convertir en años luz: ")
lightyears = int(parsecs) * parsec;
print(str(parsecs) + " parsec son "+str(lightyears)+ " en años luz.")


