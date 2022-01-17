#video numero 21

while True:
    print("Opcion 1 - comenzar programa")
    print("Opcion 2 - comenzar listado")
    print("Opcion 1 - comenzar programa")
    opcion=int(input("Opcion elegida: "))
    if opcion==1:
        print("!comenzamos!")
    elif opcion==2:
        print("!Comenzamos!")
        print("Nadia, Esteban, Mariela, Fernanda")
    elif opcion==3:
        print("Hasta la proxima")
        break
    else:
        print("Opcion incorrecta. Debe ingresar 1, 2 o 3")

#segundo ejercicio 
frase=input("Frase: ")
l=input("Letra para buscar su posición: ")
i=0
while i!=len(frase):
    if l!=frase[i]:
        print("No se encontró en la posición", i)
        i+=1
        continue
    print("Se encontró en la posición", i)
    break