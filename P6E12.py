#P6 E12 - rgion
#Escribir un programa para jugar a adivinar un número
#el usuario piensa un número y el programa lo ha de adivinar).
#El programa empieza pidiendo entre qué números está el número
#a adivinar y luego intenta adivinar de qué número se trata. El
#usuario va diciendo si el número que ha dicho el programa es menor,
#mayor o igual al que se ha buscado.
import random
minimo=int(input("Valor mínimo:"))
maximo=int(input("Valor máximo:"))
while (maximo<=minimo):
    maximo=int(input("%d es menor o igual que %d. Vuelve a probar: "%(maximo,minimo)))
secreto=random.randint(minimo,maximo)
print("Piensa un número entero entre",minimo,"y",maximo,"a ver si lo puedo adivinar.")
respuesta=input("Es %d ?: "% (secreto))
while (respuesta!="igual"):
    while(respuesta=="mayor"):
        minimo=secreto
        secreto=random.randint(minimo,maximo)
        respuesta=input("Es %d ?: "% (secreto))
    while(respuesta=="menor"):
        maximo=secreto
        secreto=random.randint(minimo,maximo)
        respuesta=input("Es %d ?: "% (secreto))
    while(respuesta!="mayor")and(respuesta!="menor")and(respuesta!="igual"):
        respuesta=input("Disculpa, no te he entendido. Vuelve a intentar: ")
    if(maximo-minimo==1)or(maximo==minimo):
        print("Te he pillado haciendo trampa. Se terminó el juego")
        respuesta="igual"
print("¡Gracias por jugar!")
