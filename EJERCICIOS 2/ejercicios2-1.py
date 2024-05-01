#falto el profe y los pibes van a armar la clase.

#pedir el nombre y la edad de lso compañeros que vinieron hoy a clase.

#funcion para obtener el asistente y al profesor segun la edad
def obtener_compañeros(cantidad_de_compañeros):
    
    #creando la lista con los compañeros 
    compañeros = []
    
    #ejecutando un for para pedir informacion de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre = input('ingrese  el nombre de un compañero: ')
        edad = int(input('ingrese la edad del compañero: '))
        compañero = (nombre,edad)
        
        #agregando la informacion a la lista
        compañeros.append(compañero)
    
    #ordenandolos de menor a mayor segun su edad
    compañeros.sort(key = lambda x:x[1])#repasar ejemplos de esto
    
    #compañeros[x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre
    #para definir el asistente y al profesor
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    
    #retornamos una tupla
    return asistente,profesor

#desempaquetamos lo que nos retorna la funciòn        
asistente,profesor = obtener_compañeros(5)

#mostrando el resultado
print(f'el asistente es:  {asistente}')
print(f'el profesor es:  {profesor}')   