diccionario = {
    'nombre' : 'lucas',
    'apellido' : 'dalto',
    'subs' : 1000000
}

print(diccionario)

#recorriendo diccionario para obtener las claves
for key in diccionario:
    key #chequear si esto es o no necesario
    print(f'la clave es: {key}')

#recorriendo diccionarios con items() para obtener la clave y el valor 
for datos in diccionario.items():
    key = datos [0]
    value = datos [1]
    print(f'la clave es: {key} y el valor es: {value}')