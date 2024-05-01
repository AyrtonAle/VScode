#creando una funcion de 3 parametros
def frase(nombre,apellido,adjetivo):
    return f'Hola {nombre} {apellido}, sos muy {adjetivo}'

frase_resultante = frase('ayrton','alejandro','kpo')
print(frase_resultante)

#creando la misma funcion con un parametro opcional y un valor por defecto
def frase(nombre,apellido,adjetivo='alto'):#valor por defecto
    return f'Hola {nombre} {apellido}, sos muy {adjetivo}'

frase_resultante = frase('ayrton','alejandro','facha')#parametro variable
print(frase_resultante)