#diccionarios en python estan compuestos por clave y valor. 

mi_diccionario = {
  'nombre':'Leonel',
  'apellidos':'Marquez',
  'edad':22,
  'genero':'M'
}

print(mi_diccionario)

rs = mi_diccionario.get('nombre') #aqui obtenemos el nombre ingresando la clave
print(rs)


lista_dic = [
  {
  'nombre':'Ale',
  'apellidos':'turcios',
  'edad':22,
  'genero':'M'
},
{
  'nombre':'ricky',
  'apellidos':'malo',
  'edad':21,
  'genero':'F'
},
{
  'nombre':'tu',
  'apellidos':'yo',
  'edad':1,
  'genero':'F'
}
]

print()
for dic in lista_dic:
  print(dic.get('nombre'), "\n")







