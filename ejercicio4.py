<<<<<<< HEAD
#Escriba un programa que pida al usuario dos palabras, y que indique
# cuál de ellas es la más larga y por cuántas letras lo es:

palabra1 = input('Ingresar palabra1:')
palabra2 = input('Ingresar palabra2')
=======
# ok
#Escriba un programa que pida al usuario dos palabras, y que indique cuál de ellas es la más larga y por #cuántas letras lo es.
#Palabra 1: edificio
#Palabra 2: tren
#La palabra edificio tiene 4 letras mas que tren.

palabra1 = input('Ingresar una palabra:')
palabra2 = input('Ingresar otra palabra:')
>>>>>>> 2220a3c35f79e125cc378576d5693713f609f757

cadena1 = len(palabra1)
cadena2 = len(palabra2)

<<<<<<< HEAD
dif=abs(cadena1-cadena2)

if cadena1 > cadena2:
    print('La palabra mayor es:', palabra1)
if cadena1 < cadena2:
    print('La palabra mayor es:', palabra2)
if cadena1 == palabra2:
    print('Las palabras tienen el mismo tamaño')
    print('La diferencia es de %d letras(s)'% (dif))
=======
if cadena1 > cadena2:
	print('La palabra:', palabra1, 'tiene',cadena1-cadena2,'caracter es mayor que la palabra:',palabra2)

else:
	print('La palabra:', palabra2, 'tiene',cadena2-cadena1,'caracter es mayor que la palabra:', palabra1)

***///
#Encuentre el n�mero mayor en una lista(Ejm entrada=[5,1,33,4,4,33,12], salida=33).

lista = [5,1,33,4,4,33,12]
#imprimir lista ordenada ascendente
lista.sort()
print(lista)
#imprimir el ultimo elemento de la lista ordenada
print(lista[-1])
>>>>>>> 2220a3c35f79e125cc378576d5693713f609f757
