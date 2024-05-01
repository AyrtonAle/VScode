diccionario ={
    'nombre' : 'lucas',
    'apellido' : 'dalto',
    'subs' : 1000000
}

#nos devuelve un objeto dict_item
claves = diccionario.keys()

#obteniendo un elemento con get(si no lo encuentra, no da error y continua)
valor_de_un_elemento = diccionario.get('nombre') 

#eliminando todo el diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop('nombre')

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()


print(diccionario_iterable)