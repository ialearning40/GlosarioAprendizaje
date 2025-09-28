
NotaTemp=0
def DatoValido():
        if NotaTemp<"1":
            print("No es valida la nota, mula")
        elif NotaTemp>"5":
            print("No es valida la nota, mula")
        else:
            NotaTemp=="a"
def PromedioNotas():
      return (float(Nota1)+float(Nota2)+float(Nota3))/3    
      
print ("Ingrese las notas:")
while True:
        Nota1= input("Matematicas: ")
        NotaTemp=Nota1
        DatoValido()
        NotaTemp==0
        Nota2= input("Sociales: ")
        NotaTemp=Nota2
        DatoValido()
        NotaTemp==0
        Nota3= input("Fisica: ")
        NotaTemp=Nota3
        DatoValido()
        print (Nota1)
        print (Nota2)
        print (Nota3)
        print (f"Elpromedio es: {PromedioNotas()}")

        
