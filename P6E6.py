#P6 E6 - rgion
#Escribe un programa que pida primero dos números (máximo y mínimo)
#y que después te pida números intermedios. Para terminar de escribir
#números, escribe un número que no esté comprendido entre los dos
#valores iniciales. El programa termina escribiendo la lista de números
minimo=int(input("Escribe un número: "))
maximo=int(input("Escribe un número mayor que %d: " %(minimo)))
lista=[]
while (maximo<minimo):
    maximo=int(input("%d no es mayor que %d. Vuelve a probar: " %(minimo,maximo)))
numero=int(input("Escribe un número entre %d y %d: " %(minimo,maximo)))
while (numero<maximo)and(numero>minimo):
    lista.append(numero)
    numero=int(input("Escribe otro número entre %d y %d: "%(minimo,maximo)))
string=str(lista[0])
for i in range(1,len(lista)):
    string+=", "+str(lista[i])
print("Los números situados entre ",minimo," y ",maximo," son: ",string)
