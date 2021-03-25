''' Las tuplas a dieferencia de las listas no pueden modificarse o agregar elemento de usando metodos como append '''
mi_tupla = (1,2,3,4,5)

# mi_tupla.append(8) --> si esto se ejecuta lanzara un error.
# print(mi_tupla)

print(mi_tupla.index(5,1,3))