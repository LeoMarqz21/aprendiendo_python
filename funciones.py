#FUNCIONES SIN PARAMETROS, CON PARAMETROS Y PARAMETROS CON VALORES POR DEFECTO.
def funcion_sin_parametros():
  print('funcion 1')
  print('hola mundo\n')

def funcion_con_parametros(nombre):
  print('funcion 2')
  print("Hola ", nombre, "\n")

def funcion_con_parametros_y_datos_por_defecto(nombre = "Anonimus"):
  print('funcion 3')
  print("Hola ", nombre, "\n")


#llamado a las funciones para ser ejecutadas.

funcion_sin_parametros()
funcion_con_parametros('personita')
funcion_con_parametros_y_datos_por_defecto()


