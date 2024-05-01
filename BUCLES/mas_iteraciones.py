frutas = ['banana','manzana','ciruela','pera','naranja','granada','durazno']
cadena = 'Hola Dalto'
numeros = [2,5,8,10]

#evitando que se coma una granada con la sentencia (continue)
for fruta in frutas:
    if fruta == 'granada':
        continue
    print(f'me voy a comer una:{fruta}')

#evitar que el bucle siga ejecutandose con la sentencia (break)
#el else tampoco se ejecuta
for fruta in frutas:
    if fruta == 'pera':
        break
    print(f'me voy a comer una:{fruta}')
else:
    print('Bucle terminado')
    
#recorrer un a cadena de texto
for letra in cadena: 
    print(letra)   

#no es la forma mas eficiente    
numeros_duplicados = list()
for numero in numeros:
    numeros_duplicados.append(numero*2)

print(numeros_duplicados)    

#for en una sola linea de codigo(eficiente)

numeros_duplicados =[x*2 for x in numeros]

print(numeros_duplicados)
        