promedio=float(input("Ingresa tu promedio"))
#El numero ingresado es 9
if promedio>=0:
    print("Tu promedio es muy bajo")
elif promedio<4:
    print("Tu promedio no existe")
elif promedio>4 and promedio<=6:
    print("Tu promedio es bajo")
elif promedio>7 and promedio<=9:
    print("Tu promedio es bueno")
elif promedio>9 and promedio <=10:
    print("Tu promedio es excelente")
else:
    print("Ese promedio no existe")