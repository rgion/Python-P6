#P6 E10 -rgion
#Escribe un programa que te pida los nombres y notas de
#alumnos. Si escribes una nota fuera del intervalo de 0 a 10,
#el programa entenderá que no quieres introducir más notas
#de este alumno. Si no escribes el nombre, el programa entenderá
#que no quieres introducir más alumnos. Nota: La lista en la
#que se guardan los nombres y notas tiene esta estructura
#[[nombre1, nota1, nota2, etc], [nombre2, nota1, nota2, etc],
#[nom3, nota1, nota2, etc], etc]
lista=[]
laux=[]
nombre=input("Dame un nombre: ")
while(nombre!=""):
    laux.append(nombre)
    nota=float(input("Escriba una nota: "))
    while (nota>=0)and(nota<=10):
        laux.append(nota)
        nota=float(input("Escriba otra nota: "))
    lista.append(laux)
    laux=[]
    nombre=input("Dame un nombre: ")
print("Las notas de los alumnos son: ")
for i in range(len(lista)):
    print(lista[i][0],":",end=" ")
    print(lista[i][1],end=" ")
    for j in range(1,len(lista[i])):
        print(" - ",lista[i][j],end=" ")
    print("")
