try:
    edad=int(input("Ingrese la edad en números, por favor: "))
    while edad <= 0 or edad>100:
        
         print("Edad incorrecta. ")
         edad=int(input("Ingrese la edad en números, por favor: "))
except ValueError:
    print("Valor incorrecto. Vuelva a cargar el formulario para comenzar de nuevo")

    
   

grupoRiesgo= input("Posee una patologia de base que lo convierta en una persona de grupo de riesgo? (Si/No): ")
if grupoRiesgo=="si" or grupoRiesgo=="Si" or grupoRiesgo=="SI":
    patologia=input("Ingrese cual es la patologìa por favor: ")
 
numeroTelefonico=int(input("Ingrese su numero de contacto, por favor: "))

print("Muchas Gracias por completar el formulario de vacunación contra COVID19. Lo contactaremos a la brevedad para otorgarle un turno.")
  
