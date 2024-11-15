tiempo=input('¿Como amaneció? ')

if tiempo=='lluvia':
  print('Busca una sombrilla')
elif tiempo=='sol':
  print('Busca una gorra')
else:
  print('No se comprende el estado del tiempo')


edad = int( input('¿Que edad tienes? '))
if edad>=18:
  print('Eres mayor de edad')
elif edad>0:
  print('Eres menor de edad')
else:
  print('No se reconoce la edad '+str(edad))