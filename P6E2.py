#P6 E2 - rgion
#Escribe un programa que te pida números y los guarde en
#una lista. Para terminar de introducir número, simplemente
#escribe “Salir”. El programa termina escribiendo la lista de números.
numero=int(input("Escribe un número: "))
lista=[]
while (numero!="salir"):
    numero=int(numero)
    lista.append(numero)
    numero=input("Escribe más números: ")
print("Los números que has escrito son: ",lista)

