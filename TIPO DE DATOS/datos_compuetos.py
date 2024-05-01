#CREANDO UNA LISTA (SE PUEDE MODIFICAR LOS DATOS GUARDADOS DENTRO)
lista = ["Lucas Dalto","Soy Dalto",True,1.85]

#CREANDO UNA TUPLA (NO SE PUEDE MODIFICAR LOS DATOS GUARDADOS DENTRO)
tupla = ("Lucas Dalto","Soy Dalto",True,1.85)

#ESTO ES VALIDO
lista[3] = "Maquinola"
print(lista[3])

#ESTO NO
#tupla[3] = "Maquinola"

#creando un conjunto (set)
#No se accede a elementos por su indice, No almacena datos duplicados

conjunto = {"Lucas Dalto","Soy Dalto",True,1.85}

# print(conjunto[1]) no puede acceder al elemento

#Creando un diccionario (dict)
diccionario = {
    'nombre' : 'Lucas Dalto',
    'canal' : 'Soy Dalto',
    'esta_emocionado' : True,
    'altura' : 1.84,
    'dato duplicado': "Soy dalto "}
print(diccionario['nombre'])



