# Tipos de datos enteros, strings y booleanos
# Definiendo variables

# Soy un comentario
numero=1
numeroConDecimal=1.2
texto='hola'
otrotexto="hola otra vez"
soyVerdadero=True
soyFalso=False
soyNulo=None
_soyRaroPeroFunciono='Intro Tel'

# !otraVariableIncorrect=1.2
# 1variableIncorrect=1.2
# -variableIncorrect=1.2

# imprimiendo en consola
print(soyNulo)
print(1)
print('un texto')
print('un texto con variables, numero con decimal es:'+str(numeroConDecimal))
print(f'un texto con variables, numero con decimal es:{numeroConDecimal}')
print('texto: {0}\notrotexto:{1}'.format(texto, otrotexto))
str1='Hola estudiantes'
str1=str1*3
print("Prueba despues de multiplicar un str:",str1)

# pidiendo informacion por consola
variablePaGuardar = input('Soy el texto que se ve en consola\n')
numeroInsertado = input('Inserte un numero\n')
print(type(variablePaGuardar))
print(type(numeroInsertado))
print(type(int(numeroInsertado)))

numeroInsertado = int(input('Inserte un numero\n'))
# operaciones basicas
print(str(numeroConDecimal*numeroInsertado))

# -------------------------------------

# Palabras que no podemos usar por que son reservadas
# if = 'hola'
# print(if)


# for = 'hola'
# print(for)


# Algunas se dejan pero genera problemas :S
# print = 'print como variable'
# print(print)

# print = lambda x: x*2
# print(10)

# funciones y parametros - this can wait

def miprimerafuncion():
    print('hola')


miprimerafuncion()

def misegundafuncion(entero=None):
    print('hola')
    print(entero)

misegundafuncion()
misegundafuncion(2)

def mitercerafuncion(entero, numero2, parametro3):
    print(entero+numero2+parametro3)

mitercerafuncion(2,1,4)


miLista = [22, 53, 20, 55, 62, 65, 91, 79, 33, 38, 24, 45,  2, 13, 56,  5, 98,  4, 70, 39, 18, 43, 54, 71, 27,  8, 97, 77, 90, 14, 66, 75, 58, 41, 40,  1, 37, 96, 31, 44,  6, 10, 60, 52, 74, 84,  7, 47, 80, 82, 61, 81, 49, 19, 30, 12, 42, 95, -25, 94, 92, 50, 17, 83, 57, 25, 93, 69, 99,  3, 32, 78, 36, 28, 87, 85, 34, 64, 73, 59, 16, 51, 67,  9, 86, 63, 26, 11, 23, 3312, 48, 29, 46, 15, 68, 89, 72, 35, 76, 88, 21]

# Solucion al Reto del menor y el mayor usando un for
minVal=miLista[0]
maxVal=miLista[0]
for num in miLista:
    minVal = num if num<minVal else minVal
    maxVal = num if num>maxVal else maxVal

print(minVal)
print(maxVal)

# Otra forma de hacer el reto con funciones arimeticas de Python
print("Soy el numero menor: "+str(min(miLista)))
print("Soy el numero mayor:"+str(max(miLista)))


variable=1
variable2=3
variable = variable2 - 1
print(variable)

# Ejercicio
# Construyamos un formulario sencillo que me permita insertar mi nombre y apellido
# el formulario debe generar un reporte saludando al usuario y diciendole cuanto dias
# ha vivido.