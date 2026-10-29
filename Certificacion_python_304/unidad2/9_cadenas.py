#cadenas y concatacion con (+) 
cadena1='hola'
cadena2='mundo'
multilinia="""esto es un cadena
de varias lineas"""
print(cadena1 + cadena2 + multilinia)#print(f"{cadena1}"")
#cadena y repeticion
eco="ja"*3
print(eco)
#cambiar una cadena de minuscula a mayuscula
tu_nombre='Danna'
print(tu_nombre.upper())
#cambiar una cadena de mayuscula a minuscula
print(tu_nombre.lower())
#remplazar texto en una cadena
frase="Me gusta programacion"
print(frase.replace("programacion","matematicas"))
#formato de cadenas (F-string)
edad=16
nombre='danna'
mensaje=f"hola,me llamo\n{nombre}\ny tengo\n{edad}años"
print(mensaje)
#contar los caracteres de una cadena
texto= "¡felicidades por aun continuar en el CECY!!!"
cantidad_caracteres=len(texto)
print(cantidad_caracteres)
#comprobar si un texto contiene una palabra
oracion="aprender python es divertido"
if "jova" in oracion:
    print("encontrado")
else:
    print("no esta")
#validar contenido de una cadena
nlista="16"
print(nlista.isalpha())
print(nlista.isdigit())
