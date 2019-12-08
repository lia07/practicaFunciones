#Escriba una función que dibuje el hexágono del tamaño indicado por el usuario de acuerdo al ejemplo:
#Lado 4:
n= int(input('num'))
espacio = n-1
asterisco = n

for i in range(n):
    cadena = " "*espacio+"*"*asterisco +" "*espacio
    espacio-=1
    asterisco+= 2
    print(cadena)

espacio = espacio+2
asterisco = asterisco-4

for i in range(n-1):
    cadena = " "*espacio+"*"*asterisco +" "*espacio
    espacio+=1
    asterisco-=2
    print(cadena)



