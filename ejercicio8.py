<<<<<<< HEAD
#Escriba una función que dibuje el hexágono del tamaño indicado por el usuario de acuerdo al ejemplo:
#Lado 4:
=======
# ok
#Escriba una función que dibuje el hexágono del tamaño indicado por el usuario de acuerdo al ejemplo:
#Lado: 4

>>>>>>> 2220a3c35f79e125cc378576d5693713f609f757
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
<<<<<<< HEAD



=======
>>>>>>> 2220a3c35f79e125cc378576d5693713f609f757
