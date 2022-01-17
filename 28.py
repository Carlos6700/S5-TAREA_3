#video numero 28

def titulo(cadena):
    nueva=""
    inicioPalabra=True
    for caracter in cadena:
        nueva=nueva+caracter
        inicioPalabra=True
    else:
        if inicioPalabra:
            nueva=nueva+caracter.upper()
            inicioPalabra=False
        else:
            nueva=nueva+caracter.lower()
    return nueva

##
def titulo(cadena):
    nueva=""
    inicioPalabra=True              #indica el inicio de una palabra
    for caracter in cadena:
        if not caracter.isalpha():
            nueva=nueva+caracter
            inicioPalabra=True
        else:
            if inicioPalabra:
                nueva=nueva+caracter.upper()
                inicioPalabra=False  #ya no es el inicio de una palabra 
            else:
                nueva=nueva+caracter.lower()
    return nueva
