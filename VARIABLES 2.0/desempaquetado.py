#creando los datos
datos_en_tupla= ('Lucas','Dalto',1000000)
datos_en_lista = ['Lucas','Dalto',1000000]
datos_en_set = {'Lucas','Dalto','1000000'}


#desempaquetando
nombre,apellido,suscriptores = datos_en_tupla

#mostrando resultado
print(suscriptores)

#en los conjuntos da error, dalto dice que no deja desempaquetar numeros

#prueba de desempaquetado con for

for data in enumerate(datos_en_tupla):
    indice = data[0]
    valor = data[1]
    print(f'el indice es: {indice} y el valor es: {valor}')