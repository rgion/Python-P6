#P6 E5 - rgion
#Escribe un programa que te pida números cada vez más grandes
#y que se guarden en una lista. Para acabar de escribir los
#números, escribe un número que no sea mayor que el anterior.
#El programa termina escribiendo la lista de números:
numero1=int(input("Escribe un número: "))
lista=[]
lista.append(numero1)
numero2=int(input("Escribe un número mayor que %d: " %(numero1)))
while (numero1<numero2):
    lista.append(numero2)
    numero1=numero2
    numero2=int(input("Escribe un número mayor que %d: " %(numero1)))
string=str(lista[0])
for i in range(1,len(lista)):
    string=string+", "+str(lista[i])
print(string)

