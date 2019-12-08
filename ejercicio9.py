<<<<<<< HEAD
#Se tienen tres diccionarios, se solicita ordenarlos de forma ascendente o descendentes usando el
# valor de los diccionarios:
=======
# ok
#Se tienen tres diccionarios, se solicita ordenarlos de forma ascendente o descendentes usando el valor de los diccionarios:
>>>>>>> 2220a3c35f79e125cc378576d5693713f609f757
#Entrada:
#Número a={‘Jose’:18}
#Numero b={‘Maria’:15}
#Número c={‘Pedro’: 24}
#ascendente=True
#Salida:
#(a={‘Maria’:15}, b= {‘Jose’:18}, c={‘Pedro’: 24})    #ascendente=True
#(a={‘Pedro’: 24}, b= {‘Jose’:18}, c={‘Maria’:15})    #ascendente=False
<<<<<<< HEAD
import operator
=======

>>>>>>> 2220a3c35f79e125cc378576d5693713f609f757
a={'Jose':18}
b={'Maria':15}
c={'Pedro':24}
a.update(a)
a.update(b)
a.update(c)

w = sorted(a, key=lambda x:a[x],reverse=False)
print(w)
<<<<<<< HEAD
=======

>>>>>>> 2220a3c35f79e125cc378576d5693713f609f757
for i in w:
   print("%s:%i "%(i,a[i]))


<<<<<<< HEAD










=======
>>>>>>> 2220a3c35f79e125cc378576d5693713f609f757
