''' 
Las tuplas a dieferencia de las listas no pueden modificarse o agregar elemento de usando metodos como append,
las tuplas son listas inmutables osea que no pueden modificarse de la misma manera que las listas normales 
'''
mi_tupla = (1,2,3,4,5)

# mi_tupla.append(8) --> si esto se ejecuta lanzara un error.
# print(mi_tupla)

rs = mi_tupla.index(2)
print('indice correspondiente al numero 2 de mi tupla: ',rs)

print('cantidad de elemento de mi tupla: ',len(mi_tupla))

del mi_tupla
# print(mi_tupla) esto daria error ya que mi tupla fue eliminada en la linea anterior.