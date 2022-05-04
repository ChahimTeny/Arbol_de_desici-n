import os

print("¿Conviene más demandar o aceptar el proyecto?")
print ("--------------------------------------------\n")

print("1. Analizar el proyecto")
print("2. Demandarlos por estafa")
respuesta=input("Selecciona una opción  ")

if respuesta == "1":
    print ("__________________________________\n")
    print("1. Aceptar el proyecto")
    print("2. Rechazar el proyecto")
    desicion=input("Seleccione una opción ")
    print ("----------------------------------\n")
    
    if desicion == "1":
        print("Matematicamente no es la mejor opción")
        print ("----------------------------------\n")
    else:
        print("Matematicamente es la mejor desición")
        print("__________________________________\n")
    os.system("pause") 
    
elif respuesta == "2":
    print("La probabilidad de que pierdas el caso es del 30%")
    print("__________________________________\n")
    print("Si gana el caso, puede pasar una de las siguientes probabilidades\n")
    print("1. Gana y se le da un pago menor")
    print("2. Gana y se le da un pago medio")
    print("3  Gana y se le da un pago algo")
    probabilidad=input("Seleccione una opción ")
    global valor
    
    if probabilidad == "1":
        valor=0.50*0.1
        print ("Existe un 50% de que le den un pago de Q185,000")
    elif probabilidad == "2":
        valor=0.30*0.3
        print ("Existe un 30% de que le den un pago de Q415,000")
    else:
        valor=0.20*0.6
        print ("Existe un 20% de que le den un pago de Q580,000")
else:
    print("Realiza una acción")