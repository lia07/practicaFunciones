#Invertir un número ( Ejm: entrada = 123, salida=321).

numero_ingresado = (input("Ingrese un número: "))
revertir = 0
try:
    valor = int(numero_ingresado)
    while valor > 0:
        residuo = valor % 10
        revertir = (revertir * 10) + residuo
        valor //= 10
    print('El inverso del número ingresado es: ', revertir)
except ValueError:
    print("Numero no valido. Ingresar de nuevo!")
