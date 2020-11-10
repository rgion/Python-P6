#P6 E7 - rgion
#Escribe un programa que pida un número (límite) y luego
#te pida números hasta que la suma de los números introducidos
#supere el límite inicial. El programa termina escribiendo
#la lista de números.
limite=int(input("Escribe límite: "))
valor=int(input("Escribe un valor: "))
lista=[]
lista.append(valor)
suma=valor
while (suma<limite):
    valor=int(input("Escribe otro valor: "))
    lista.append(valor)
    suma=suma+valor
string=str(lista[0])
for i in range(1,len(lista)):
    string+=", "+str(lista[i])
print("El límite a superar es ",limite,". La lista creada es: ",string," \n\
ya que la suma de estos números es: ",suma,".")
