soyVerdadero=True
# Estructuras condicionales
if soyVerdadero:
    print('soy un valor:'+str(soyVerdadero))


test = int(input('inserte un valor a testear\n'))

# Condicion con if-else
if test>10:
    print('soy un valor mayor que 10: '+str(test))
else:
    print('soy un valor menor que 10: '+str(test))


val1 = int(input('inserte el valor 1\n'))
val2 = int(input('inserte un valor 2\n'))


# Condicion con if-elif
if val1>10 and val2<100:
    print('val1>10 and val2<100')
elif val2>200:
    print('val2>200')
elif val1<10:
    print('val1<10')

val1 = int(input('inserte el valor 1\n'))
val2 = int(input('inserte un valor 2\n'))


# Condicion con if-else
if val1>10 and val2<100:
    print('val1>10 and val2<100')
elif val2>200:
    print('val2>200')
else:
    print('No tengo condicion :S')

nombre = input('inserte un nombre\n')
apellido = input('inserte apellido\n')

soyUnNombreCompleto = val1+val2
soyUnNombreCompletoconUnEspacio = val1+' '+val2

print(soyUnNombreCompleto)
print(soyUnNombreCompletoconUnEspacio)


# Inception de if - nombre len mayor a 20
if len(nombre) >= 10:
    if apellido <= 10:
        print('apellido con menos de 10 caracteres')
    print('nombre con 10 caraceteres o mas')
else:
    print('nombre con mas de 10 caracteres')


# Dentro de un if podemos evaluar mas de una condicion
a=10
b=20
c=30
print(a,b,c)

#O Podemos ser mas fancy y hacer esto

a, b, c = 11, 22, 30
print(a,b,c)

if a < b and a < c:
    print('a es el numero menor')
elif b < c:
    print('b es el numero menor')
else:
    print('c es el numero menor')


# Hagamos una busqueda en una lista
# Recordemos que una lista es un tipo de dato que permite
# guardar/contener un conjunto de elementos
# ordenados, con un indice y que permite elementos duplicados

laLista = [1,2,3,4,5]
x = 13
if x not in laLista:
    print('x la lista')

# Estructuras iterativas - loops

# Ejercicios:
# 1. Ahora que ya conoce los condicionales resuelva el siguiente problema (representado en el diagrama de flujo) usando python


