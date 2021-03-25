#CLASES EN PYTHON
class Saludar:
  def __init__(self,nombre): #constructor de la clase, aqui es donde inicializamos las variables u objetos que querramos.
    self.__nombre = nombre #el doble guion hace privado este atributo y debido a eso es invisible al querer modificarlo desde otra clase u objeto creado de esta.
  
  def getNombre(self): #metodo denominado getter debido a que con este obetenemos el valor de nombre
    return self.__nombre
  
  def setNombre(self,nombre): #metodo setter, con este podremos cambiar el nombre que pasamos en el metodo contructor de la clase.
    self.__nombre = nombre
  
  def saludar(self):
    print("Hola " , self.__nombre)

#self es el equivalente a this en otros lenguajes y hace referencia a la misma clase.

saludame = Saludar('Leo') #este es un objeto o instancia de la clase Saludar.

rs = saludame.getNombre()
print(rs)

saludame.saludar()
saludame.setNombre('marqz') #modificamos el nombre que habiamos dado anteriormente
saludame.saludar()# aqui ya no dira hola leo, dira hola marqz.