from ast import Continue
from operator import contains


nombre= input('\nIngrese su Nombre completo por favor: ') #pido nombre
nombre= nombre.capitalize()

def comprobacion (em):  #función que pide el mail y evalúa si está bien escrito en función de poseer una arroba y uno o más puntos
    global email        #de lo contrario lo pide nuevamente
    check = False
    puntos = 0
    arroba = 0
    
    
    for i in em:
        if i == '.':
            puntos+=1
        elif i == '@':
            arroba+=1
    
    if puntos >= 1 and arroba == 1:
        check=True
    
    return check



email = input('\nIngresá tu email: ')
         
while comprobacion(email) == False:
     print('La dirección de correo introducida es incorrecta')
     email = input('\nIngresá tu email: ')
    
    
else:
    Continue
    #print('La dirección de correo introducida es correcta, proseguimos con los datos')
   
    




def comprueba_edad (ed): 
    global edad       
    comprueba = False
    puntos = 0
    
    for i in ed:
        if i.isnumeric() == True:
            puntos+=1
        
    
    if puntos >= 1:
        comprueba = True
    
    return comprueba



edad = input('\nIngresá tu edad: ')
         
while comprueba_edad(edad) == False:
     print('La edad debe introducirse en números')
     edad = input('\nIngresá tu edad: ')

else:
    Continue
   

salida = False
if int(edad) < 18:
    print('Debes ser mayo a 18 para registrarte')
    Salida = True
    
    

while salida == False:   
    grupoRiesgo= input("\nPosee una patologia de base que lo convierta en una persona de grupo de riesgo? (Si/No): ")
    grupoRiesgo=grupoRiesgo.lower() # con esta función pasás todo a minúscula, no importa como lo haya ingresado
    if grupoRiesgo=="si" :#or grupoRiesgo=="Si" or grupoRiesgo=="SI": <---- entonces esto ya no es necesario
        patologia=input("Ingrese cual es la patologìa por favor: ")
        salida= True
    else:
        patologia = 'No posee'
        break
    
numeroTelefonico=int(input("\nIngrese su numero de contacto, por favor: "))


#.......AGREGUÉ ESTO ............

print('\nDATOS DEL PACIENTE: \n')
print('Nombre: ', nombre, '\nemail: ', email, '\nedad: ', edad, '\nPatología: ', patologia, '\nNum de contacto: ', numeroTelefonico )
print("\nMuchas Gracias por completar el formulario de vacunación contra COVID19. Lo contactaremos a la brevedad para otorgarle un turno.\n")
  

