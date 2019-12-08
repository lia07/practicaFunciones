#Escriba un programa que pida al usuario dos palabras, y que indique
# cuál de ellas es la más larga y por cuántas letras lo es:

palabra1 = input('Ingresar palabra1:')
palabra2 = input('Ingresar palabra2')

cadena1 = len(palabra1)
cadena2 = len(palabra2)

dif=abs(cadena1-cadena2)

if cadena1 > cadena2:
    print('La palabra mayor es:', palabra1)
if cadena1 < cadena2:
    print('La palabra mayor es:', palabra2)
if cadena1 == palabra2:
    print('Las palabras tienen el mismo tamaño')
    print('La diferencia es de %d letras(s)'% (dif))
