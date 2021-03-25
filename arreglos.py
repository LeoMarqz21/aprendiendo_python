''' 
Las lista son indexadas por python y el primer indice no es 1, el primer indice siempre sera 0.

'''
#lista
mi_lista = [1,2,3,4,5,6,7,8,9]
print('lista original: --> ', mi_lista , "\n")
#aqui eliminamos el ultimo dato de mi_lista.
mi_lista.pop()

#tamaño de mi lista.
print("cantidad elementos de mi lista (mi_segunda): " ,len(mi_lista))

#recortamos nuestra lista para almacenarla en otra variable.
mi_lista_dos = mi_lista[2:5]
print('Nueva lista resultante del recorte de mi_lista: ', mi_lista_dos)

#aqui reasignamos el indice 0 que tenia el calor de 1 y lo cambiamos a 77.
mi_lista[0] = 77
print("mi lista despues de reasignar el valor del indice 0: ",mi_lista)
'''
insertamos datos en la lista.
primero definimos el indice en que deseamos agregarlo y despues el dato a ser a gregado.
esto no elimina el valor que anteriormente ocupada ese puesto, solo lo transfiere al siguiente puesto.
'''
mi_lista.insert(4, 19)
print("mi lista despues de insertar un dato en un indice seleccionado: ",mi_lista, "\n")

#extendemos el tamaño de la lista fucionandole otra con la funcion extend que sirve para agregar multiples valores a una lista.
otr_lista = ['hola','mundo']
print('mi lista: ', mi_lista)
mi_lista.extend(otr_lista)
print('mi lista extendida: ',mi_lista, "\n")

#--------------------------------------------------------------------
numeros = [5,4,9,7,2,3,1,6]
print('lista numeros original: ', numeros)
numeros.sort()
print('lista numeros ordenada: ',numeros, "\n")

numeros.pop(1)
print('el indice 1 es eliminado: ', numeros)

numeros.reverse()
print('lista numeros invertida: ', numeros, "\n")

print('indice al que pertenece el numero 6: ',numeros.index(6))

print('limpio mi lista con el metodo clear: ',numeros.clear(), "\n")

del numeros
#print('borramos mi lista: ',  numeros) #esto lanzara un error debido a que cuando se ejecute esta linea la lista numeros ya no existira.




