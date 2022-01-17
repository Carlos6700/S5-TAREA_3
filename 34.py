#video numero 34

lista=[1,2,3,4]
lista=lista+[5]
print(lista)
otra=[9,8,7]
lista=lista+otra
print(lista)
a=lista+[otra]
print(a) 
###
lista=[1,2,3,4]
for elemento in lista:
    print(elemento)
    
#2
articulos={154:["jabón en polvo","limpieza",True],
           248:["talco","cosmética",False],
           199:["cera para pisos","limpieza",True]}
for clave, valor in articulos.items():
    print("Código:",clave)
    print("Descripción: ",valor[0])
    print("Rubro: ",valor[1])
    if valor[2]:
        print("Hay stock")
    else:
        print("Agotado")
    print("---------")

###
lista=[1,2,3,4,5,6,7,8,0,9,9,9]

for i in range(len(lista)-1):
    if lista[i]==lista[i+1]:
        print(lista[i])

##
def empleadoExiste(empleados,nombre):
    for datos in empleados.Values():
        if datos[0]==nombre:
            return True
    return False

empleados={100: ["Jorge Millán","Administración"],
           200: ["Oriana López","Gerencia"],
           300: ["Guadalupe Ríos","RR.HH. "],
           400: ["Lionel Campos","Ventas"]}

nombre=input("Nombre de empleado: ")
if not empleadoExiste(empleados, nombre):
    print("El empleado no se encuentra en la nómina")