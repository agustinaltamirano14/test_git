# TP Evaluativo - N2
# Altamirano Agustín 

# 1) - Crear una clase abstracta Persona
from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, DNI, edad):
    
        if not isinstance(nombre, str) or not nombre:
            raise ValueError("Nombre invalido.")
        if not isinstance(DNI, str) or not DNI.isdigit():
            raise ValueError("DNI inválido.")
        if not isinstance(edad, int) or edad <= 0 or edad >= 130:
            raise ValueError("Edad inválida.")

        self.__nombre = nombre
        self.__DNI = DNI
        self.__edad = edad

    def get_nombre (self):
        return self.__nombre
    def get_DNI(self):
        return self.__DNI
    def get_edad (self):
        return self.__edad        
    
    def set_nombre(self, nombre):
        if not isinstance(nombre, str) or not nombre:
            raise ValueError("Nombre inválido.")
        self.__nombre = nombre
        
    def set_DNI(self, DNI):
        if not isinstance(DNI, str) or not DNI.isdigit():
            raise ValueError("DNI inválido.")
        self.__DNI = DNI
        
    def set_edad(self, edad):
        if edad <= 0 or edad >= 130:
            raise ValueError("Edad inválida.")
        self.__edad = edad
    
    @abstractmethod
    def mostrar_datos(self):
        pass
    
#2) - Crear clases derivadas
    
class Estudiante(Persona):
    def __init__(self, nombre, dni, edad, carrera):
        super().__init__(nombre, dni, edad)
        self.__carrera = carrera

    def get_carrera(self):
        return self.__carrera

    def set_carrera(self, carrera):
        if isinstance(carrera, str) and carrera.strip() != "":
            self.__carrera = carrera
        else:
            raise ValueError("La carrera debe ser un texto válido.")

    def aprobar_materia(self, materia):
        print(f"{self.get_nombre()} ha aprobado la materia {materia}.")

    def mostrar_datos(self):
        return f"- Estudiante: Nombre: {self.get_nombre()}, DNI: {self.get_DNI()}, Edad: {self.get_edad()}, Carrera: {self.get_carrera()}"


class Docente(Persona):
    def __init__(self, nombre, dni, edad, materia_asignada):
        super().__init__(nombre, dni, edad)
        self.__materia_asignada = materia_asignada

    def get_materia_asignada(self):
        return self.__materia_asignada
    
    def set_materia_asignada(self, materia_asignada):
        if isinstance(materia_asignada, str) and materia_asignada.strip() != "":
            self.__materia_asignada = materia_asignada
        else:
            raise ValueError("La materia es inválida")
    
    def dictar_clase(self):
        return f"El docente {self.get_nombre()} está dictando la clase de {self.__materia_asignada}."

    def mostrar_datos(self):
        return f"- Docente: Nombre: {self.get_nombre()}, DNI: {self.get_DNI()}, Edad: {self.get_edad()}, Materia asignada: {self.__materia_asignada}"


class Administrativo(Persona):
    def __init__(self, nombre, dni, edad, sector):
        super().__init__(nombre, dni, edad)
        self.__sector = sector

    def get_sector(self):
        return self.__sector

    def set_sector(self, sector):
        if isinstance(sector, str) and sector.strip() != "":
            self.__sector = sector
        else:
            raise ValueError("El sector debe ser un texto válido.")

    def registrar_asistencia(self):
        print(f"{self.get_nombre()} ha registrado asistencia en el sector {self.get_sector()}.")

    def mostrar_datos(self):
        return f"- Administrativo: Nombre: {self.get_nombre()}, DNI: {self.get_DNI()}, Edad: {self.get_edad()}, Sector: {self.get_sector()}"

if __name__ == "__main__":
    lista_personas = [
        Estudiante("Agustín", "42502831", 25, "TAS"),
        Docente("Brenda", "41654321", 26, "Ciencias Sociales"),
        Administrativo("Leo", "40223344", 27, "Ingeniería")
    ]

    for persona in lista_personas:
        print(persona.mostrar_datos())

    print ("_________________________________________________")
    lista_personas[0].aprobar_materia("Programación")
    print(lista_personas[1].dictar_clase())
    lista_personas[2].registrar_asistencia()
    print ("_________________________________________________")        
    #--------------------------------------------  