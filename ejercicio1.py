#Calcule el promedio de un curso (Ejm entrada [70,80,90,100], salida=85).
listaN = [80,90,90,100]
#listaN = [70,80,90,100]
tamañoLista = len (listaN)
lista2 = 0
for i in range(tamañoLista):
    lista2 =lista2+listaN[i]
lista2 = lista2/tamañoLista
print('El promedio de un curso es :', lista2)
