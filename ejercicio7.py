#Se le solicita crear un filtro para buscar palabras en  en una lista de cadenas.
#Entrada
#lista = ["vengadores infinity war 2", "VENGADORES: ENDGAME", "X-MEN: FÉNIX OSCURA","ALADDIN",
#"ALADDIN Y LA LAMPARA", "vengadores infinity war"]
#palabra= aladd
#Salida
#res=["ALADDIN","ALADDIN Y LA LAMPARA"]
numeroPal = int(input("Buscar palabras en una lista de cadenas:"))
if numeroPal < 1:
    print("¡NUL!")
else:
    lista = []
    for i in range(numeroPal):
        print("La palabra es aladd", str(i+1)+":", end = "")
        palabra = input()
        lista+= [palabra]
    print("La lista creada es:", lista)