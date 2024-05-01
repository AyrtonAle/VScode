#creando una lista con list
lista = list([ 34, True])

#Devuelve la cantidad de elementos de la lista
cantidad_de_elementos = len(lista)

#Agregar un elemento a la lista
lista.append(7)

#Agregando un elemento a la lista en un indice especifico
lista.insert(3,'beatiful')

#Agregamos varios elementos a la lista
lista.extend([23,3500,False,False])

#Eliminando un elemento de la lista por su indice
lista.pop(-1) #-1 para eliminar el ultimo, -2 para el anteultimo y asi sucesivamente

#Removiendo un elemento de la lista por su valor
lista.remove('beatiful')

#Ordenamos la lista de forma ascendente (si usamos el parametro reverse = True lo ordenamos a la inversa)
lista.sort(reverse=True)

#Invierte los elementos de una lista 
lista.reverse()




#Eliminando todos los elementos de la lista
#lista.clear()



print(dir(('sadasd')))