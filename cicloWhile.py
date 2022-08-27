centinela=100

#comentarios: ciclo while
print ("***MENU***")
print ("1.saludar")
print ("2.despedir")
print ("0.salir")

while(centinela!=0):
    
    centinela=int(input("Digita una opcion")) #casteo o parseo
    if(centinela==1):
        print("Hola")
    elif(centinela==2):
        print("Adios")    
    elif(centinela==0):
        break
    else:
        print("Digite una opcion valida")
else:
        print("termine")