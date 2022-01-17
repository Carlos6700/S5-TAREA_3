#video numero 18

total=0
nro=int(input("Numero: "))
while nro != 0:
    total+=nro
    nro=int(input("N{umero: "))
print("Total:", total)

#segundo ejercicio
positivos=0
n=int(input("Número (0 para terminar): "))
while n!=0:
    if n>0:
        positivos+=1
    n=int(input("Número (0 para terminar : "))
print("Cantidad de positivos", positivos)

#tercer ejercicio
suma=0
n=int(input("Número positivo:"))
while n!=0:
    digito=n%10
    suma+=digito
    n=n//10
print("suma de los digitos:", suma)

#cuarto ejercicio
pares=0
n=int(input("Número (-1 para terminar el programa): "))
while n!=-1:
    if n%2 == 0:
        pares+=1
    suma=0
    while n!=0:
        digito=n%10
        suma+=digito
        n=n//10
    print("suma de sus digitos:", suma)
    n=int(input("Número (-1 para terminar el programa): "))
print("Se ingresaron", pares, "números pares")
