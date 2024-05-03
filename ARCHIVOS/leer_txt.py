archivo_sin_leer = open('ARCHIVOS\\Mi_Texto.txt')

#leemos el archivo
#print(archivo_sin_leer.read())

#leer lineas
#lineas = archivo_sin_leer.readlines()

#leer una sola linea
linea = archivo_sin_leer.readline()#lee la primera linea entera o los caractere que querramos, todavia no descubri como seleccionar que linea quiero leer

#cerrar archivo
archivo_sin_leer.close()

print(linea)
