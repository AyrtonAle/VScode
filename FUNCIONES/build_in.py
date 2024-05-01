numeros = [4,7,1,42,15]

#encontrando el numero mayor de una lista
numero_mas_alto = max(numeros)
print(numero_mas_alto)

#encontrando el numero menor de una lista
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

#redondeando de forma ineficiente
numero = round(12.345678 * 100)#queda 1.234,5678 y por el redondeo queda 1235, cambiando el 4 por el 5 por aplicacion matematica
print(numero/100)#correjimos la multiplicacion y le corrmos la coma para que nos queden dos decimales quedando asi 12,35

#La funcion round permite elegir cuantos decimales queres que queden, colocando una coma despues del numero
numero = round(12.345678,2)
print(numero)

#retorna Falsae -> 0, vacìo, False, None / True -> distinto de 0, True, cadena, datos no vacìos
resultado_booleano = bool('ahre loco')
print(resultado_booleano)

#retorna True, si todos los valores son verdaderos
resultado_all = all([None,'true',[334,24],True])
print(resultado_all)

#suma todos los valores de un iterable
suma_total = sum(numeros)
print(suma_total)