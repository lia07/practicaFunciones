<<<<<<< HEAD
# Invertir un número ( Ejm: entrada = 123, salida=321)
numero_ingresado = (input("Ingrese un número: "))
invertir = 0
=======
# ok
#Invertir un número ( Ejm: entrada = 123, salida=321).

numero_ingresado = (input("Ingrese un número: "))
revertir = 0
>>>>>>> 2220a3c35f79e125cc378576d5693713f609f757
try:
    valor = int(numero_ingresado)
    while valor > 0:
        residuo = valor % 10
<<<<<<< HEAD
        invertir = (invertir * 10) + residuo
        valor //= 10
    print('El inverso del número ingresado es: ', invertir)
except ValueError:
  print("Ese número no es valido. Inténtalo de nevo !")
=======
        revertir = (revertir * 10) + residuo
        valor //= 10
    print('El inverso del número ingresado es: ', revertir)
except ValueError:
    print("Numero no valido. Ingresar de nuevo:!")
>>>>>>> 2220a3c35f79e125cc378576d5693713f609f757
