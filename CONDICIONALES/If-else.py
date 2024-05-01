contraseña_almacenada = 'Barbarita22'

contraseña_escrita = 'Barbarita22'

if contraseña_almacenada == contraseña_escrita:
    print('INICIANDO SESIÒN...')
else:
    print('CONTRASEÑA INVALIDA!!!')

ingreso_mensual = 500
gasto_mensual = 75000


if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print('Estas en Deficit')
    elif ingreso_mensual - gasto_mensual > 3000:
        print('Bien Crack, estas bien')
    else:
        print('Y pa, estas gastando una banda') 
    
    
elif ingreso_mensual > 1000:
    print('Estas bien economicamente en Latinoamerica')
    
elif ingreso_mensual > 500:
    print('Estas bien en Argentina')
    
elif ingreso_mensual > 200:
    print('Estas bien en Venezuela')
else:
    print('Sos Pobre')    