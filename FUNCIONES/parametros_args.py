#forma no optima de sumar valores
#def suma(lista):
    #numeros_sumado = 0
    #for numero in lista:
        #numeros_sumado =numeros_sumado + numero
    #return numeros_sumado 

#resultado = suma([5,3,9])

#forma optica de sumar valores
def suma_total(numeros):
    return sum([5,3,9,10,20,3])

#lo mismo que arriba pero utilizando el operador * como parametro (*args)
def suma(nombre,*numeros):
    return f'{nombre}, la suma de tus numeros es: {sum(numeros)}'
    
resultado = suma('lucas',4,5,6,7,9)
print(resultado)


    


