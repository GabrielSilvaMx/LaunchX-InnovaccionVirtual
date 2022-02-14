text="""Interesting facts about the Moon. The Moon is Earth's only satellite. 
There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. 
This yearly drift is not significant enough to cause immediate effects on Earth. 
The highest daylight temperature of the Moon is 127 C.""".replace("\n", "")
#divide el texto en cada oracion para trabajar con su contenido
sentencias = text.split('. ')

print(sentencias)

#define algunas palabras clave para busqueda que te ayudaran a determinar si una oracion contiene un hecho.
palabras_clave = ['average','temperature','distance']

#Crea un bucle para imprimir solo datos sobre la Luna que esten relacionados con las palabras clave definidas anteriormente:
print("\nPalabras clave sobre la Luna: ")
for item in sentencias:
    for palabra_clave in palabras_clave:
        if palabra_clave in item:
            print("La palabra clave es: '"+palabra_clave+"' Texto: '"+item+"'")

#actualiza el bucle(ciclo) para cambiar C a Celsius
print("\nCambiar C a Celsius: ")
for item in sentencias:
    print("Texto: '"+item+"'")
    if item.count(' C')>0:
        print("\tNuevo texto: "+item.replace(' C', ' Celsius'))
        break
    else:
        print("\tSin cambios")