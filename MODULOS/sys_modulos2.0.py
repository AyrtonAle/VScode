#import modulo_afuera.saludo as m_saludar 

#print(m_saludar.saludar('lucas'))

#So no renombrabamos a m_saludar, deberiamos haber colocado toda la ruta del modulo en el print
#osea             print(funciuones_buenas.saludo.saluar('lucas'))

#-----------------------------------------------------------------------------------------------

import sys

#print(sys.builtin_module_names) #modulos integrados en python

sys.path.append('c:\\Users\\usuario\\Desktop\\Curso de Python\\modulo_afuera')

import saludo as saludin

print(saludin.saludar('lucas'))
