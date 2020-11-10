#P6 E3 - rgion
#Escribe un programa que pida notas y los guarde en una lista.
#Para terminar de introducir notas, escribe una nota que no esté
#entre 0 y 10. El programa termina escribiendo la lista de notas.
nota=float(input("Escribe una nota: "))
lista=[]
while (nota<=10)and(nota>=0):
    lista.append(nota)
    nota=float(input("Escribe más notas: "))
print("Las notas que has escrito son: ",lista)
