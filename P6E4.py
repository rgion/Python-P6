#P6 E4 - rgion
#Escribe un programa que te pida dos números, de manera
#que el segundo sea mayor que el primero. El programa termina
#escribiendo los dos números tal y como se pide:
numero1=int(input("Escribe un número: "))
numero2=int(input("Escribe un número mayor que %d " %(numero1)))
while (numero1>=numero2):
    numero2=int(input("%d no es mayor que %d. Vuelve a introducir un número: " %(numero2,numero1)))
print("Los números que has escrito son: ",numero1," y ",numero2)
