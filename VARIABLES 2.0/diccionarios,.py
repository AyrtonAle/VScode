#creando un diccionario con dict()

diccionario = dict(nombre='lucas',apellido = 'dalto')

#las listas no pueden ser claves y usamos frozenset para meter conjutos

diccionario = {frozenset(['dalto','rancio']):'jajaja'}

#creando diccionarios con fromkeys() valor por defecto: None

diccionario = dict.fromkeys(["nombre","apellido"])

#creando diccionarios con fromkeys() cambiando el valor por: No se
diccionario = dict.fromkeys(["nombre","apellido"],'No se')


print(diccionario) 