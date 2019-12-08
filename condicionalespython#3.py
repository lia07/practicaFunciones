# operadores
# < menor que                5<10
# >mayor que                 10>2
# <= menor o igual           10<=10
# >=mayor o igual             5>=1
# == comparacion             5==5
# !diferenete                10!=8

numero = 7
if numero>5:
    print("El numero es mayor que 5")
    if numero < 10:
        print("El numero tambien es mayor a 10")
    else:
        print("El numero sobrepasa al 10")

edad = int(input("Introduce tu edad:"))
if edad>=18:
    print("Eres mayor de edad")
elif 10 <= edad < 18:
    print("Te falta poco para ser mayor de edad")
else:
    print("Aun eres menor")

