#Variables
 #Python es de tipado débil

my_variable_string='Buenas practica de declarar variable'
my_variable_int=5
my_variable_bool=True

#Variables en una sola linea
name, apellido, alias, edad='Dariel','Nuñez Acosta', 'darieldev',33 
 
# Concatenación de variables en un print
print(my_variable_string,my_variable_bool)

print('Me llamo  {} {} y mi edad es {}'.format(name,apellido,edad))

#Este es el mas indicado
print('Me llamo  %s %s y mi edad es %d' %(name,apellido,edad))

print('Me llamo'+name+apellido+' y mi edad es'+edad+' ')

#######Algunas funciones del sistema
#len() función para retornar el tamaño de la variable
print(len(my_variable_string))
