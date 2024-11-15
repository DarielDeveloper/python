#Los diccionarios:
# Estructuras de datos que nos permite almacenar valores de diferente tipo e incluso listas y otros diccionarios.

#La principal característica es que los datos se almacena asociados a una clave de tal forma que se crea una asociación de tipo clave:valor para cada elementos almacenado.

#Los elementos almacenados no están ordenados.

midiccionario={'Alemania':'Berlin','Francia':'Paris','España':'Madrid'}

#Para acceder al valor de una key del diccionario
print(midiccionario['España'] )

#Insertar key y valor o modifica valor en caso de existir el key en el diccionario
midiccionario['Italia']='Lisboa'

#Para eliminar key y valor 
del midiccionario['Italia']

#Para obtener todas las keys
midiccionario.keys()

#Para obtener todas las values
midiccionario.values()

#Para saber longitud 
len( midiccionario)