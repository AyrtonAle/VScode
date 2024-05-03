#importando un modulo y asignando el nombre "ms"
#import modulo_saludar as ms

#Llamo a modulo_saludar desde otra carpeta usando lo siguiente
#from funciones_buenas.modulo_saludar import saludar as saludar_normal,saludar_raro as saludar_como_coscu

from modulo_afuera.saludo import saludar as saludar_normal,saludar_raro as saludar_como_coscu


import modulo_afuera.saludo as ms
#creamos las variables con los saludos
saludo = saludar_normal('Lucas')
saludo_raro = saludar_como_coscu('Fran')

#mostramos los resultados
print(saludo_raro)
print(saludo)

#para ver las propiedades y metodos del namespace (dir)
#print(dir(namespace) )

print(ms.__name__)
