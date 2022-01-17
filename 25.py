#video numero 25

def coordenadaZ(x,y):
    x=x+10
    y=y+15
    return x+y

#programa principal
x=int(input("coordenada eje x: "))
y=int(input("Coordenada eje y: "))
for i in range(3):
    z=coordenadaZ(x,y)
    x=x+1
    y=y+1
print(x," . ",y)
####
from Funciones import *
#programa principal
x=int(input("un número: "))
y=int(input("Otro número: "))
print(maximo(x-3, minimo (x+2, y-5)))