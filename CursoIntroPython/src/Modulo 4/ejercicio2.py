#Datos con los que vas a trabajar
nombre = "Luna"
gravedad = 0.00162 # in kms
planeta = "Planeta Tierra"

#crea un titulo para el texto.
titulo = f'Datos de gravedad acerca de {nombre}'

#crea una plantilla de cadena multilinea para contener el resto de la informacion.
#En lugar de usar kilometros, debes convertir la distancia a metros multiplicando por 1,000.
plantilla=f"""Nombre : "{nombre}"
Planeta : "{planeta}"
Gravedad : {round(gravedad*1000,2)} m/s
"""

#Usa ambas variables para unir el titulo y los hechos.
hechos = [titulo, plantilla]
print('\n'.join(hechos))

#Nuevos datos muestra
planeta = 'Marte'
gravedad  = 0.00143
nombre = 'Ganimedes'


titulo = f'Datos de gravedad acerca de {nombre}'

plantilla=f"""Nombre : "{nombre}"
Planeta : "{planeta}"
Gravedad : {round(gravedad*1000,2)} m/s
"""

hechos = [titulo, plantilla]
print('\n'.join(hechos))