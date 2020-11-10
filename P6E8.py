#P6 E8 - rgion
#Escribe un programa que te pida primero un número y luego
#te pida números hasta que la suma de los números introducidos
#coincida con el número inicial. El programa termina
#escribiendo la lista de números.
limite=int(input("Escribe límite: "))
valor=int(input("Escribe un valor: "))
lista=[]
lista.append(valor)
suma=valor
while (suma!=limite):
    if(suma<limite):
        valor=int(input("Escribe otro valor: "))
        suma=suma+valor
        lista.append(valor)
    elif(suma>limite):
        lista.remove(valor)
        suma=suma-valor
        valor=int(input("%d es demasiado grande. Escribe otro valor: "%(valor)))
        suma=suma+valor
        lista.append(valor)
string=str(lista[0])
for i in range(1,len(lista)):
    string+=", "+str(lista[i])
print("El límite a alcanzar es ",limite,". La lista creada es: ",string)

