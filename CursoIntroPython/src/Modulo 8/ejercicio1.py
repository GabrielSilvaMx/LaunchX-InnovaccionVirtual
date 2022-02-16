# -*- coding: ISO-8859-15 -*-

# Crea un diccionario llamado planet con los datos propuestos
planeta = {
    'nombre': 'Marte',
    'lunas': 2
    }
print(f"Planeta: {planeta['nombre']} ")
print(f"Número de lunas: {planeta['lunas']} ")

planeta.update( {'circunferencia (km)': {'polar': 6752, 'ecuatorial':6792 } })

# Imprime el nombre del planeta con su circunferencia polar.
print(f"{planeta['nombre']} tiene su circunferencia polar de {planeta['circunferencia (km)']['polar']} km")