#Las lista se declara mediante los []
nombres=['Daniel','Dariel']

numeros=[1,2,3,4]

#Mostrar la lista en un intervalo
print(numeros[1:3])

#Mostrar la lista completa
print(numeros[:])

#Para añadir elemento a la lista
numeros.append(5)

numeros.insert(1,'Dariel')

numeros.extend([7,8,9,10])
print(numeros)

#Para concatenar 
listaN=numeros+[12,34]

#Para repetir los elementos de la lista se utiliza *
listaRepetida=[1,2,3,4]*3

#Saber el index de un elemento
numeros.index('Dariel')

#Saber si existe el elemento en la lista
existe='Dariel' in numeros 

#Para eliminar elemento 
numeros.remove(10)

#Elimina el ultimo elemento de una lista
numeros.pop()


#Esto es un caso particular que se conoce como matrices por las {}
matrices=[{0,3},{3,9}]

persona=['Dariel',33,True]

#Para acceder algún elemento de la lista
print(nombres[0])

#Para concatenar se utiliza +
nombre_numero=nombres + numeros

#Metodo para crear una lista de 9 posiciones y de numeros del 1 al 9
rango= list(range(1,10))

print(type(nombres))

#Para setear una poción de la lista 
numeros[0]=100
print(numeros)

#Para devolver los elmentos de alguna posición 
numeros[0:2]