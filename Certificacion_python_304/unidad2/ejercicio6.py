tabla = [
    ["nombre","edad","calificacion"],
    ["danna",16,9.0],
    ["alma",16,9.0],
    ["angel",16,9.0],
    ["joshua",16,8.0],
    ["jorge",16,6.0],
    ["santiago",16,7.8],
    ["angela",16,9.0],
    ["michel",16,9.0],
    ["aaron",17,7.9],
    ["keilani",16,8.0]
]
nombre=input("introduce tu nombre")

filas=len(tabla)
columnas=len(tabla[0])

for i in range(filas):
    for i in range(columnas):
        if tabla[i][j] == numero:
            print("posicion:", f"[{i}][{j}]")
