# ok
#Escriba un programa que pida al usuario dos palabras, y que indique cuál de ellas es la más larga y por #cuántas letras lo es.
#Palabra 1: edificio
#Palabra 2: tren
#La palabra edificio tiene 4 letras mas que tren.

palabra1 = input('Ingresar una palabra:')
palabra2 = input('Ingresar otra palabra:')

cadena1 = len(palabra1)
cadena2 = len(palabra2)

if cadena1 > cadena2:
	print('La palabra:', palabra1, 'tiene',cadena1-cadena2,'caracter es mayor que la palabra:',palabra2)

else:
	print('La palabra:', palabra2, 'tiene',cadena2-cadena1,'caracter es mayor que la palabra:', palabra1)
