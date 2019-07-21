# ok
#Escriba una función que pida al usuario dos números enteros, y luego entregue la suma de todos los números que están #entre ellos. Por ejemplo, si los números son 1 y 7, debe entregar como resultado 2 + 3 + 4 + 5 + 6 = 20.
#Ingrese num: 1
#Ingrese num: 7
#La suma es 20

n1 = int(input("Ingrese n1: "))
n2 = int(input("Ingrese n2: "))
n3 = n2 + 1
if n1 > n2:
      n1,n2=n2,n1
i = sum(range(n1+1,n2))
print("La suma es", end=' ')
print(i)
