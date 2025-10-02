def Saludo(Nombre=f"Hermanito"): #Defino una función que va a ser mi saludo siempre
    Mensaje=f"Bienvenido Hermano {Nombre}"# Invoco un mensaje que si no le ingreso un valor tiene uno por defecto
    return Mensaje #Ejecutelo


##Pienso que debo dejar las funciones y clases de manera previa a usarlas, ya que el uso si va a ser secuencial
#class BesoMonjas():
#   def __init__(self,nombremonja,cantidad_besos):
#            self.nombremonja=nombremonja
#            self.besos=cantidad_besos
#    def mostrar_besos(self):
#        print (f"Ud otorgo {self.besos} a {self.nombremonja}") 

class Feligres():
     def __init__(self):
          self.nombrefeligres=str(input(f"Ingrese su nombre Hermano: "))
          print (Saludo(self.nombrefeligres))

class BesoMonjas():

    def __init__(self):
            self.nombremonja=str(input(f"Ingrese El nombre de la monja: "))
            self.besos=int(input(f"Ingrese el número de besos: "))
            def NumeroBesosValidos():
                    if self.besos >10:
                        return False
                    else:
                        return True
            while not NumeroBesosValidos():
                 self.besos=int(input(f"No mienta, ingrese el número REAL de besos: "))
            self.PuntajeBesos=(((self.besos*5)*100)/50) #Son 5 puntos por cada beso, lo que quiere decir que máximo acumulará 50 ptos. Y a esto le sacamos el %     
    def mostrar_besos(self):
        print (f"Ud otorgo {self.besos} Besos a {self.nombremonja}")
        print (f"Su puntuación ha sumado {self.PuntajeBesos}% en puntos por besos!")
        return self.PuntajeBesos
    


class Limosna():
    def __init__ (self):# ¿En qué situación si debería ir así :def __init__ (self,VecesLimosna,CantidadLimosna)? 
          self.VecesLimosna=int(input(f"Ingrese el número de veces que dio Limosna: "))
          self.CantidadLimosna=int(input(f"Ingrese la suma que daba en cada Limosna: "))
          self.PuntajeLimosna=((((self.VecesLimosna*self.CantidadLimosna)//10)*100)/300000) #Por cada 10 pesos suma 1 pto.
    def mostrar_limosna(self):  
        #print (PuntajeLimosna)
        if self.PuntajeLimosna>100:
            self.PuntajeLimosna = 100     
        print (f"Su puntuación ha sumado {int(self.PuntajeLimosna)}% puntos por Limosna!")
        return self.PuntajeLimosna

        


#while True:
for i in range(2): #Le indico que van a ser 5 iteraciones
    print ("                      A continuación vamos a determinar si eres apto para ingresar al Cielo:") 
    #Feligres=input(f"Ingrese su nombre Hermano: ") #Le permito ingresar un dato que queda en la variable feligres
    #print(Saludo(Feligres)) #Imprimo el saludo con el mensaje de bienvenida y el dato ingresado de cada Feligres
    #nombremonja = input("Ingrese el nombre de la monja: ")
    #cantidad_besos = input("Ingrese la cantidad de besos otorgados: ")
    Feligres() #acá podríamos o no manejar la variable Feligres1 si queremos usar los datos más adelante
    #BesoMonjas().mostrar_besos() #Si yo quisiera podría usar solamente el invocar la clase BesoMonjas y me pediría los datos, pero si quiero
                                #visualizarlos, que es lo que hace el método mostrar_besos, pues debo invocarlo
    #Limosna().mostrar_limosna()
    BM=BesoMonjas()
    BM.mostrar_besos()
    LM=Limosna()
    LM.mostrar_limosna()
    PromedioCielo=(BM.mostrar_besos() + LM.mostrar_limosna())/2
    print (f"Su puntaje total para ingresar al cielo es de: {int(PromedioCielo)}%")
    if PromedioCielo<41:
        print ("Lo siento, no va al cielo ni cagando")
    elif 41<=PromedioCielo<80:
        print ("Se queda en el purgatorio")
    else:
        print ("Felicitaciones papá! Entraste al cielo")

    print ("--- Siguiente Parroquiano ---")
#    continuar=str(input("¿Desea ingresar otro Feligres? (s/n):


#if promedio in 20  40 "no va al cielo
#ifelse 41 - 80 "queda en el purgarotrio
#else: va al cielo


#En este caso hicimos un cambio para que los datos de las variables de input de nombremonja y cantidad de besos quedaran dentro
#de la clase, y no dentro de la estructura del ciclo for, lo que debería darle un mejor manejo y menor complejidad en mantenimiento

 

#2 condiciones que valuan si vas al cielo
#Perfectamente podrías hacer un promedio que sea m=(Besos+Limosna)

#(50+1000) 100

#Maximo de besos=10 -> Si son más de 10 es mentira, no se admite el dato
#    50 - 100%
#    10 -  X
#Maximo de Limosna=300 ->
#    300 - 100%
#    10 -  X


