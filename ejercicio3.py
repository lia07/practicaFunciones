#Escriba el teorema de pitágoras que reciba como entrada las longitudes de los dos catetos a y b , que #entregue como salida el largo de la hipotenusa c del triángulo (Ejm a = 7, b = 5, salida=8.60).

import math
#import math.sqrt()
print("\t Teorema de Pitagoras\n")
a=input("Ingrese cateto a: ")
b=input("Ingrese cateto b: ")
c=math.sqrt((a*a)+(b*b ))
print("La hipotenusa es:", c)
