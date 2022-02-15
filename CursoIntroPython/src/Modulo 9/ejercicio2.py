# -*- coding: ISO-8859-15 -*-

# Informe de cohete que requiere varias piezas de información, como el tiempo hasta el destino, el combustible a la izquierda y el nombre del destino

# Función con un informe preciso de la misión. Considera hora de prelanzamiento, tiempo de vuelo, destino, tanque externo y tanque interno

def infome_mision(**kargs):
    # print(kargs)
    # revisa primero que los parámetros son correctos
    if 'destino' not in kargs:
        return "Faltan parámetros del destino."
    if 'combustible' not in kargs:
        return "Faltan parámetros del combustible."
    if 'minutos' not in kargs:
        return "Faltan parámetros de los minutos."
    desglose_tiempo=""
    for clave in kargs['minutos'].keys():
        desglose_tiempo+="\t + "+clave.capitalize()+" : "+str(kargs['minutos'][clave])+" minutos \n"
    desglose_combustible=""
    for clave in kargs['combustible'].keys():
        desglose_combustible+=f"""\t + {clave.capitalize()}: {kargs['combustible'][clave]:,} litros faltantes\n"""

    reporte = f"""
    Nombre del destino: {kargs['destino']}
    Tiempo total del viaje: {sum(kargs['minutos'].values())} minutos
    {desglose_tiempo}
    Total de combustible:  {sum(kargs['combustible'].values()):,} litros
    {desglose_combustible}
    """
    
    return reporte

print(infome_mision(destino="Luna",
        combustible={'tanque interno':300000, 'tanque externo':200000, 'tanque de reserva': 100000},
        minutos={'hora de prelanzamiento':8, 'tiempo de vuelo':11, 'destino':55 }
        ))