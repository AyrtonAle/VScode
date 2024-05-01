#creando una funcion simple
#def saludar():
#    print('hola lucas, mi maestro, ¿Como estas?')
    
#saludar()
#saludar()
#saludar()

#creando una funcion que tenga parametros
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == 'mujer'):
        adjetivo = 'doña'
    elif(sexo =='hombre'):
        adjetivo = 'amigo'
    else:
        adjetivo = 'amigue'
        
    print(f'Hola {nombre}, mi {adjetivo} ¿Como estas?')

saludar('Rosalia','trans')

#crear una funcion que me devuleva multiples valores
def crear_contraseña_random(num):
    chars = 'abcdefghij'
    num_entero = str(num)
    num = int(num_entero[0])#darle una repasada a esto que no quedo muy claro
    c1 = num - 2 
    c2 = num
    c3 = num - 5
    contraseña = f'{chars[c1]}{chars[c2]}{chars[c3]}{num_entero*2}'
    return (contraseña,num)

#desmpaquetando la funcion
passsword,primer_numero = crear_contraseña_random(3)

#mostrando los datos obtenidos y los datos utilizados para crearlo
print(f'Tu contraseña nueva es: {passsword}')
print(f'el dato utilizado para crearla fue: {primer_numero}')
