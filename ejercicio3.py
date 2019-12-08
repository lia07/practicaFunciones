#Escriba el teorema de pitágoras que reciba como entrada las longitudes de los dos catetos a y b,
# que entregue como salida el largo de la hipotenusa c del triángulo (Ejm a = 7, b = 5, salida=8.60)
import math
numero_ingresado = (input("Ingrese a: "))
numero_ingresado = (input("Ingrese b: "))

for a in range(1,15):
  for b in range(a,15):
    c=math.sqrt(a**2+b**2)
    if c == int(c):
      print('a,b:', c)
