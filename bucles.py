from time import sleep #aqui importamos la funcion sleep del modulo time para programar retardos de tiempo.
# bucle for
n = [1,2,3,4,5]

for i in n:
  print(i, end=' ') #end='' nos permite que los datos se impriman uno a la par de otro con un espacio.

print() #este metodo esta siendo usado como un salto de linea

for i in range(0,10): #aqui generamos numeros  entre el rango de 0 y con una longitud de 10 numeros, debido a esto se imprimiran numero del 0 al 9
  print(i, end=' ') 

print() #espaciado

valor = True

# bucle while tiene que programarsele un contador en caso de recorrer datos y asi con en el siguiente caso se debe definir un fin en el cual 
# la variabe debera pasar a falso para no seguir siendo ejecutada
while (valor):
  sleep(0.9)
  print('Estoy funcionando ...')
  sleep(0.5)
  valor = False
  print('variable valor pasada a False y eso hace que nuestro bucle for se detenga.\n\n')


'''
una manera de simular el ciclo do-while de otros lenguajes es declarando una variable en true y si se cumplen las condiciones 
dentro del bucle esta seguira siendo true o se cambiara a false para tener el bucle o tambien se puede una la palabra reservada (break).

'''

while True:
  print('inicio mi primer iteracion')
  sleep(1)
  print('A pasado un segundo de que inicio la ejecucion programada por defecto en mi bucle')
  sleep(1)
  print('if 5 > 10: continue')
  if 5 > 10:
    continue
  else:
    sleep(0.5)
    print('aqui termina la ejecucion de mi bucle, se ejecuto una vez y luego con una condicion dentro de esta se decidio detener su flujo')
    break










