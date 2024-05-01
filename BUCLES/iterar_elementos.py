animales = ['gato','perro','loro','cocodrilo','pez']

numeros = [12,34,46,78,90]

#recorriendo la lista animales
for animal in animales:
    print(f'ahora la variable animal es igual a: {animal}')

#recorreindo la lista numeros y multiplicando cada valor por 10    
for numero in numeros:
    resultado = numero * 10
    print(resultado)
    
    
for numero,animal in zip(numeros,animales):
    print(f'recorriendo lista 1: {numero}')
    print(f'recorriendo lista 2: {animal}')
    
#recorre la cantidad de numeros del elemento 0 hasta el ultimo que le pasemos sin contarlo
for num in range(10,20):
    print(num)

#forma no optima de recorrer una lista (NO FUNCIONA EN CONJUNTOS)     
for num in range(len(numeros)):
    print(numeros[num])

#forma correcta de recorrer una lista por su indice
for num in enumerate(numeros):
    indice = num [0]
    valor = num [1]
    print(f'el indice es: {indice} y el valor es: {valor}')
    #print(num)
    
#usando el for/else
for numero in numeros:
    print(f'ejecutando el ultimo bucle, valor actual: {numero}')
else:
    print('el bucle termino')    

#todo lo anterior sirve tambien para TUPLAS y CONJUNTOS   