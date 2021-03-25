# OPERADORES ARITMETICOS
print('Operador de suma (+): ', 5 + 2)
print('Operador de resta (-): ', 5 - 2)
print('Operador de multiplicacion (*): ', 5 * 2)
print('Operador de division (/): ', 5 / 2)
print('Operador de modulo (%): ', 5 % 2) 
#con modulo podemos ver cuantas veces cabe un numero en otro por ejemplo el 2 cabe 2 veces en 5 pero modulo retorna el residuo que seria 1

print('\n\n')#dos saltos de linea

# OPERADORES DE COMPARACION

dato1 = 5
dato2 = 10

print('dato1 es igual a dato2: ', dato1 == dato2)
print('dato1 es diferente a dato2: ', dato1 != dato2)
print('dato1 es mayor a dato2: ', dato1 > dato2)
print('dato1 es menor a dato2: ', dato1 < dato2)
print('dato1 es mayor o igual a dato2: ', dato1 >= dato2)
print('dato1 es menor o igual a dato2: ', dato1 <= dato2)

print('\n\n')

d = True
f = False

print('d es igual a verdader y f es igual a verdadeo: ', d and f) #las dos varaible deben ser para que la condicion retorne como true
print('d es igual a verdader y f es igual a verdadeo: ', d or f) #si una de las dos variables es verdadera regresara true y si no retornara falso
print('f es verdadera: ', not f) #retornara verdadero debido a que la palabra reservada not invierte los valores reales u originales respecto al tipo de dato booleano
print('d es verdadera: ', not d) #d es verdadera pero cambiara a falso