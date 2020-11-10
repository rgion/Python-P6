#P6 E11 - rgion
#Escribir un programa para jugar a adivinar un número
#(el ordenador "piensa" el número y el usuario lo ha de adivinar).
#El programa empieza pidiendo entre qué números está el número
#a adivinar, se "inventa" un número al azar y luego el usuario
#va probando valores. El programa va decidiendo si son demasiado
#grandes o pequeños. pista:
import random
minimo=int(input("Valor mínimo:"))
maximo=int(input("Valor máximo:"))
intentos=0
secreto=random.randint(minimo,maximo)
print("A ver si adivinas un número entero entre",minimo,"y",maximo)
numero=int(input("Escribe un número: "))
while (numero!=secreto):
    while (numero<secreto):
        numero=int(input("¡Demasiado pequeño! Vuelve a probar: "))
        intentos+=1
    while (numero>secreto):
        numero=int(input("¡Demasiado grande! Vuelve a probar: "))
        intentos+=1
print("¡Correcto! Lo has intentado",intentos,"veces.")
