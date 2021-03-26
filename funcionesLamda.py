# FUNCIONES lambda  O ANONIMAS

hola = lambda s: print('hola que tal como estas ', s)
# hola("Leo")

sumar = lambda x,y: print(x + y)
# sumar(5,5)

numeros = [1,2,3,4,5,6,7,8,9]

def recorrer(arreglo, fun):
  for i in arreglo:
    fun(i)

# recorrer(numeros, lambda n: print(n))

def sum(arreglo, respuesta):
  rs = 0
  for i in arreglo:
    rs += i
  respuesta(rs)
  
def filter(arreglo, fun):
  rs = []
  for i in arreglo:
    if fun(i):
      rs.append(i)
  return rs


sum(numeros, lambda x: print("Resultado de la suma del arreglo numeros: ", x))
print("resultado de la funcion (filter): ", filter(numeros, lambda x: x > 2))

