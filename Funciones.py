def saludar(nombre="amigo"): #Con esto estamos dejando un valor por defecto siempre que será amigo, hasta cuando el valor de nombre no sea especificado
    mensaje=f"Hola queride {nombre}"# En este caso se crea la variable mensaje que incluye una fstring. La necesidad de usarla como variable, es para darle la oprtunidad de hacer algo más adelante con ella.
    return mensaje # Por eso se invoca con return y no con print.

print (saludar("Andrés Iván"))
print (saludar()) #Aquí no se especifica el nombre, por lo que toma el valor por defecto "amigo"

### En el siguiente ejemplo podemos hacer una validación de condiciones, que si se cumple, sea un True, y podamos usarlo para continuar con el flujo del programa
#1.
def credenciales(usuario, contrasena):
    if usuario=="admin" and contrasena=="1234":
        return True
    else:
        return False
    
print (credenciales("admin", "1234"))
print (credenciales("user", "abcd"))
