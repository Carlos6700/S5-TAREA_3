#video 8
cadena="si, profe, es cierto... yo me comi la torta"
cadena[10]
" "
cadena[-1]
"a"
cadena[0:9]
"si, profe"
cadena[::3]
"si o,sit.ymciaaa"
cadena[::-1]
"aerat al imoc em oy ...otreic se ,eforp ,is"
cadena[4:9]
"profe"

#soluciones
s="   hola, ¿como estás?"
s[::-1]
"?sátse omóc¿  ,aloh   "
s[len(s)]
s[len(s)-1]
"?"
s.count("o")
2
s.count("Hola")
0
s[-4:]
"tás?"
s[15:]
"estás"
s.find("o")
4
s.strip()
"hola, ¿como estás?"
x=s.upper()
x==s
False
x
"    HOLA, ¿COMO ESTAS?"
s
"    hola, ¿cómo estás?"
s[14:].upper()
"  ESTAS?"
s
"    hola, ¿cómo estás?"
len(s)%2 != 0
True
len(s)
21
s.replace(" ","*")
"***hola,*¿cómo*estás*?" 
s.replace("2", "2")
"   hola, ¿cómo estás?"   

#solucion2 
X="programar en python"
X[-1]
"n"
X[len(X)-1]
"n"
cadena="hola"
cadena.find("2")
-1
"a" in "dátiles"
False
"me gusta programar".find(" ")
2
"me gusta programar".count(" ")
2
cadena[0]="H"
nueva="C"+cadena[1:]
nueva
"Cola"
X
"programar en python"
X="hoy en dia miércoles"
X.replace("1","1")
"hoy es dia miércoles"
X
"hoy es dia miércoles"
X.replace("1", "1").replace("é", "e")
"hoy es dia miércoles"
X
"hoy es dia miércoles"
X.count("a")+X.count("e")+X.count("i")+X.count("o"+X.count("u"))
6
                                            




