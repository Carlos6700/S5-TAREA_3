#Video numero 13

numero=int(input("Número: "))
if numero<0:
    numero=numero*-1
print("El valor absoluto es", numero)

#segundo ejercicio
nombre1=input("Un nombre: ")
nombre2=input("Otro nombre: ")
indice_final_nombre1=len(nombre1)-1
indice_final_nombre2=len(nombre2)-1
if nombre1[0]==nombre2[0] or nombre1[indice_final_nombre1]==nombre2[indice_final_nombre2]:
    print("Coinidencia")
else:
    print("No hay coincidencia")
    
#tercer ejercicio
candidato=input("Candidato elegido: ")
if candidato.upper()=="A":
    print("Usted ha votado por el partido rojo")
elif candidato.upper()=="B":
    print("Usted ha votado por el partido azul")
elif candidato.upper()=="C":
    print("Usted ha votado por el partido verde")
else:
    print("Opción errónia")
    
#cuarto ejercicio
letra=input("Letra: ")
if len(letra)!=1:
    print("Debe ser solo una letra")
else:
    if letra.lower() in "aeiou":
        print("Es vocal")
        
#quinto ejercicio
anio=int(input("Año: "))
if anio%4 != 0:
    print("No es bisiesti.")
else:
    if anio%100 != 0 or anio%400 ==0:
        print("es bisiesto")
    else:
        print("No es bisiesto")