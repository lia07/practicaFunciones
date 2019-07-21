# ok
#Escriba el teorema de pitágoras que reciba como entrada las longitudes de los dos catetos a y b , que #entregue como salida el largo de la hipotenusa c del triángulo (Ejm a = 7, b = 5, salida=8.60).

import math

print("\t Teorema de Pitagoras\n")
a=float(input("Ingrese cateto a: "))
b=float(input("Ingrese cateto b: "))
c=math.sqrt((a**2)+(b**2 ))
print('La hipotenusa es: {0:.2f}'.format(c))
