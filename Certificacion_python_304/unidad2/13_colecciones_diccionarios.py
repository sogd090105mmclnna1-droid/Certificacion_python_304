#creando un diccionario
persona={
    "nombre":"danna",
    "edad":16,
    "profecion":"programador",
    "estidiante":True
}
print(persona)
#accediendo a un valor especifico 
print(persona["nombre"])
#se puede usasr el metodo get()
#es util porque no marca error si el valor existe
print(persona.get("profecion"))
#modificar un valor existente
persona["edad"]=19
print(persona["edad"])