#Crear una clase que se llame estudiante y cumpla con los siguientes atributos
#Nombre
#Edad
#Notas


class Estudiante:
    def __init__(self,nombre,edad,notas):
        self.nombre=nombre
        self.edad=nombre
        self.notas=notas

    def agregar_nota(self,nota):
        self.notas.append(nota)

    def promedio(self):
        return sum(self.notas)/len(self.notas)
    
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Notas: {self.notas}, Promedio: {self.promedio()}")
        
Estudiante1=Estudiante("Tatiana",30,[5,9])
Estudiante2=Estudiante("Andres",25,[4,3,5])
Estudiante3=Estudiante("Lila",28,[5,5,4,4])
Estudiante1.mostrar_info()
Estudiante2.mostrar_info()
Estudiante3.mostrar_info()
Estudiante1.agregar_nota(5)
Estudiante1.mostrar_info()
Estudiante2.agregar_nota(5)
Estudiante2.mostrar_info()
Estudiante3.agregar_nota(3)
Estudiante3.mostrar_info()       
Estudiante1.agregar_nota(4)        
Estudiante1.mostrar_info()       



