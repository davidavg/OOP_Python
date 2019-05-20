'''
Created on Aug 9, 2018

@author: david avalos
'''
boolean = True
while boolean:
    operacion = input("Qué operación desea realizar?\n1.Suma\n2.Resta\n3.Multiplicación\n4.División\n5.Salir\n\n->")
    
    if operacion == "5":
        break
    try:  
        if int(operacion) > 5:
            print("La opción seleccionada no es válida. Intente de nuevo.\n")
            continue
    except:
        print("ups! La opción que eleigió no es un número entero! Intente de nuevo!\n")
        continue
    
    a = input("Escriba un número entero 'a' -> ")
    b = input("Escriba un número entero 'b' -> ")
    
    
    if operacion == "1":
        suma = int(a) + int(b)
        print("\nLa suma de " + a + " + " + b + " es: ", str(suma),"\n")
    
    elif operacion == "2":
        resta = int(a) - int(b)
        print("\nLa resta de " + a + " - " + b + " es: ", str(resta),"\n")
        
    elif operacion == "3":
        multiplicacion = int(a) * int(b)
        print("\nLa multiplicación de " + a + " * " + b + " es: ", str(multiplicacion),"\n")
    
    elif operacion == "4":
        division = int(a) / int(b)
        print("\nLa multiplicación de " + a + " * " + b + " es: ", str(division),"\n")
        
        
print("\nFin")
    