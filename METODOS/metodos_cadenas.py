cadena1 = 'Hola Broder'
cadena2 = 'Bienvenido'

resultado = dir(cadena1)

#convierte a mayuscula 
mayusc = cadena1.upper()

#convierte a minuscula

minusc = cadena1.lower()

#primera letra en mayuscula

primer_letra_mayusc = cadena1.capitalize()

#Buscar una cadena dentro de otra cadena, si no hay coincidencias nos devuleve -1

busqueda_find = cadena1.find("D")

#Buscamos una cadena dentro de otra cadena, si no hay coincidencias lanza una exepcion

#busqueda_index = cadena1.index() 

#Si es numerico devuelve True, sino devuelve False

es_numerico = cadena1.isnumeric()

#Si es alfanumerico devuelve True sino devuelve False(los espacios generan errores)

es_alfanumerico = cadena1.isalpha()

#Buscamos coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de veces que coincida 

contar_coincidencias = cadena1.count('z')

#Contamos cuantos caracteres tiene una cadena

contar_caracteres = len(cadena1)

#Vereificamos si una cadena empieza con otra cadena dada, si es asi devuelve  True

empieza_con = cadena1.startswith("Al")

#Verificamos si una cadena terminas con otra cadena dada, si es asi devuelve True

termina_con = cadena1.endswith('')

#Reemplaza un pedazo de la cadena dada por otra dada

cadena_nueva = cadena1.replace('la','lu')
cadena_nueva_2 = cadena_nueva.capitalize()

#Separa cadenas con la cadena que le pasemos

cadena_separada = cadena1.split(',')

print(contar_caracteres)