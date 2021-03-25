numero = 1
cadena = '1'

'''
si numero es igual a cadena se imprimira en consola el primer print, si no es verdad esa condicion 
entonces pasamos al elif y si numero y cadena son diferentes se imprimira en consola el segundo print y si no se
cumple ninguna de las dos condiciones se ejecutara else y se imprimira en consola el tercer print.
'''
if numero == cadena:
  print('numero y cadena son iguales')
elif numero != cadena:
  print('numero y cadena son diferentes')
else:
  print('ninguna de las condiciones es verdadera')