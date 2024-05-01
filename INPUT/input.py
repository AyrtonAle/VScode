#pedirle un dato al usuario
nombre = input('che maestro, dame tu nombre: ')#el dato que va a devolver input siempre es un texto/str

#~mostrando el dato
print(f'el nombre es {nombre}')
print('el nombre es ' +  (nombre))

#le pedimos un numero al usuario
numero = input(f'dame un numero, {nombre} : ')

#convertimos el numero en entero y lo multiplicamos por 2
resultado_entero = int(numero)*2

resultado_flotante = float(numero)*2

print(resultado_flotante)