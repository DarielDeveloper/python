#Las Tuplas:
# Son listas inmutables, es decir no se puede modificar después de su creación.
#- No permiten añadir, eliminar, mover elementos etc(no append, extend, remove)
#- Si permiten extraer porciones, pero el resultado de la extracción es una tupla nueva.
#- Si permiten comprobar si existe un elemento en la tupla.

################# Ventajas con respecto a las listas ########

#-Mas rápidas
#-Menos espacios(mayor optimización)
#-Formatean string
#-Pueden utilizare como claves en un diccionario. (las listas no)

#Los () es opcional 
nombres=('Daniel','Dariel')
numeros=(1,2,3,4)
miTupla=('Dariel', 6,8,1991)

#Para convertir una tupla a lista
milista=list(nombres)

#Para llevar una lista a tupla
mitupla=tuple(milista)

#Para saber si existe un elemento en la tupla
print('Daniel' in  nombres)

#Para saber cuantas veces existe el elemento en la tupla
print(numeros.count(2))

#Para saber cuantos elementos tiene en la tupla
print(len(nombres)) 

#Para desempaquetar tupla 
nombre, dia, mes, year=miTupla
