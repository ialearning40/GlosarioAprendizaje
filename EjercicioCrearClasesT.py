class Notas:
    def __init__(self, nota1, nota2, nota3):
     self.nota1 = nota1
     self.nota2 = nota2
     self.nota3 = nota3

    def promedio(self):
       return (self.nota1 + self.nota2 + self.nota3) / 3


class Estudiante:
    def __init__(self, nombre, edad, notas: Notas):
        self.nombre = nombre
        self.edad = edad
        self.notas = notas

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, "
         f"Promedio: {self.notas.promedio():.2f}")


# Crear un objeto de Notas
notas1 = Notas(4.0, 3.5, 5.0)

# Asociar esas notas a un estudiante
estudiante1 = Estudiante("Jeimmy", 30, notas1)

# Mostrar información completa
estudiante1.mostrar_info()