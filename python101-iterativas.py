# las estructuras iterativas nos permiten ejecutar
# una o mas acciones de forma repetitiva hasta que
# se cumpla una condicion

# Tienen esta estructura

# inicio de la estructura de control:
#     expresiones

# el inicio de la estructura suele ser una evaluacion de una condicion
# algo similar a los if, sin embargo esta condicion nos permite detener
# la ejecucion del ciclo ~|'u'|~

# Los ciclos son el for y el while, recuerden que son palabras reservadas,
# no las pueden usar

# podemos validar en una lista de elementos
avengers = ['mazamorra', 'changua', 'cholado', 'pandebono', 'pandebono']
for heroe in avengers:
    print('el {} esta en la lista'.format(heroe))


# podemos validar en un rango
# primero usemos la funcion rango

# Genera numeros entre range(inicio, fin~) , note el ~ indica que no se incluye dentro del rango
soyUnRango = range(2001, 2013)
print(soyUnRango)
print(type(soyUnRango))
print(soyUnRango[0])
print(soyUnRango[-1])
print(2013 in soyUnRango)

soyUnRangoAgain = range(1, 2013)
print(soyUnRangoAgain)


for anio in range(2000, 2013):
    print("Informes del Año:", str(anio))

# Ejercicio
# Traduzcamos este diagrama de flujo en un algoritmo en Python
