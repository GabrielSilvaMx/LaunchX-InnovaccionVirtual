# %% [markdown]
# # Mi primer programa
# Mostrar la fecha de hoy en el formato dd/mm/yyyy

# %%
from datetime import date

# %%
fecha = date.today() # Retorna la fecha local actual.

print("La fecha de hoy es: " + str(fecha.day) + "/" + str(fecha.month) + "/" + str(fecha.year) )


