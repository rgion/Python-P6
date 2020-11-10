#P6 E9 - rgion
#Escribe un programa que te pida nombres de personas y sus
#números de teléfono. Para terminar debe pulsar “S” cuando
#te pida el nombre. El programa termina escribiendo nombres
#y números de teléfono. Nota: La lista en la que se
#guardan los nombres y números de teléfono tiene esta
#estructura[[nombre1, telef1], [nombre2, telef2], [nom3, telef3]
#, etc], es decir, lista de listas.
lista=[]
nombre="A"
while(nombre!="S"):
    nombre=input("Dame un nombre: ")
    if(nombre!="S"):
        telefono=input("Dame un teléfono: ")
        lista.append([nombre,telefono])
print("Los nombres y teléfonos de la agenda son: ")
for i in range(len(lista)):
    print("nombre: ",lista[i][0]," telefono: ",lista[i][1])

