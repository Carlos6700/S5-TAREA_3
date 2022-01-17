#video numero 15

#for x in tange(10):
#    print(x)


##for x in range(100,200):
##    print(x)




for x in range(5,20,3):
    print(x)

#segundo ejercicio
n=int(input("Número: "))
for x in range(n, n*2):
    print(x)
    
#tercer ejercicio
C=int(input("Cantidad de números: "))
total=0
for variable in range(C):
    numero=int(input("Número a sumar: "))
    total=total+numero
print("Total de la suma: ", total)

#cuarto ejercicio
frase=input("Frase: ")
print("Vocales en la frase:")
for x in "aeiou":
    if x in frase:
        print(x)
        
#quinto ejercicico
frase=input("Frase: ")
cantidad=0
for x in frase:
    if x in "aeiou":
        cantidad+=1
print("Cantidad de vocales:", cantidad)