class Alumno:
    __nombre = None
    __matricula = None
    __carrera = None
    def __init__(self):
        print("Alumno")
    def setNombre(self,nombre): #funcion para modificar el valor de la variable 
        self.__nombre = nombre #modifica el valor de la variable  privada __nombre y nombre
    def getNombre(self):
        return self.__nombre
    def setMatricula(self,matricula):
        self.__matricula = matricula
    def getMatricula(self):
        return self.__matricula
    def setCarrera(self,carrera):
        self.__carrera = carrera
    def getCarrera(self):
        return self.__carrera

jair = Alumno()

jair.setNombre("jair") 
print (jair.getNombre())

jair.setMatricula("1722110433") 
print (jair.getMatricula())


jair.setCarrera("Desarrollo de Software") 
print (jair.getCarrera())