# -*- coding: ISO-8859-15 -*-

#Contruir un informe de combustible que requiere información de varias ubicaciones de combustible en todo el cohete.

# Extrae el cálculo promedio de la función en una nueva función para que el promedio se pueda hacer de forma independiente
def promedio(*args):
    total = sum(args)
    num_tanques = len(args)
    return total / num_tanques


# Función para leer 3 tanques de combustible y muestre el promedio
def informe_tanques(tanque1,tanque2, tanque3):
    print("Combustible del primer tanque: ",tanque1)
    print("Combustible del segundo tanque: ",tanque2)
    print("Combustible del tercer tanque: ",tanque3)
    
    print("El promedio de los tres tanques es de: ",round(promedio(tanque1,tanque2,tanque3),2),"% " )

informe_tanques(10,40,50)

