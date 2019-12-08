<<<<<<< HEAD
#Calcule el promedio de un curso (Ejm entrada [70,80,90,100], salida=85).
listaN = [80,90,90,100]
#listaN = [70,80,90,100]
tamañoLista = len (listaN)
lista2 = 0
for i in range(tamañoLista):
    lista2 =lista2+listaN[i]
lista2 = lista2/tamañoLista
print('El promedio de un curso es :', lista2)
=======
# ok
#Calcule el promedio de un curso (Ejm entrada [70,80,90,100], salida=85).

def get_promedio_notas(lista):
    tamLista = len(lista)
    lista2 = 0
    for i in range(tamLista):
        lista2 = lista2+lista[i]
    lista2 = lista2/tamLista
    return lista2

lista_notas = [70,80,90,100]
promedio = get_promedio_notas(lista_notas)
print(promedio)
>>>>>>> 2220a3c35f79e125cc378576d5693713f609f757
