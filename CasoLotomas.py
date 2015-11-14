import random

saldo = 50
respuesta='s'

# Saldo inicial

print "----------------------------------------------------------------------------------"
print "CURSO: TALLER DE SOFTWARE I"
print "CASO: LOTOMAS"
print "----------------------------------------------------------------------------------"
print "Ud. cuenta con un saldo de S/. " + str(saldo)

while (respuesta=='S' or respuesta=='s'):
    aciertos=0
    apuesta=0
    coincidencia=0
    numeros=[]
    azar=[]
    
    # Monto para las apuesta
    
    while(apuesta<20 or apuesta>saldo):
        print "----------------------------------------------------------------------------------"
        apuesta=int(input("Ingrese el monto de su apuesta: "))
        if apuesta<20:
            print "Ud. no puede apostar este monto, el monto de su apuesta debe ser mayor de S/. 20"
        else:
            if apuesta>saldo:
                print "Ud. no puede apostar este monto, ya que no cuenta con saldo suficiente"

    if apuesta<=saldo:
        print "Ud. aposto S/. " + str(apuesta)
        saldo=saldo-apuesta
        
        # Numeros Ingresados por el Usuario

        busqueda=0
        while(busqueda==0):
            count=0
            print "----------------------------------------------------------------------------------"
            while (count<6):
                if count==0:
                    numero=int(input("Ingrese numero [" + str(count + 1) + "] : "))
                else:
                    numero=int(input("Ingrese numero [" + str(count + 1) + "] : "))
                    busqueda=numeros.count(numero)
                    if busqueda>0:
                        busqueda=0
                        print "Error de ingreso, Ingrese los numeros nuevamente por favor :P"
                        numeros=[]
                        break
                if numero >30:
                    busqueda=0
                    print "Numero ingresado fuera de rango... :( , Ingreser los numeros nuevamente"
                    break
                numeros.append(numero)
                print "Numero [" + str(count + 1) + "] : " + str(numero)
                count=count+1
                if count==6:
                    busqueda=1

        # Numeros seleccionados al azar

        busqueda=0
        while(busqueda==0):
            count=0
            while (count<6):
                if count==0:
                    aleatorio=random.randint(1,30)
                else:
                    aleatorio=random.randint(1,30)
                    busqueda=azar.count(aleatorio)
                    if busqueda>0:
                        busqueda=0
                        azar=[]
                        break
                azar.append(aleatorio)
                count=count+1
                if count==6:
                    busqueda=1
            
        # Calculando numero de coincidencias
        
        for x in numeros:
            for y in azar:
                if x==y:
                    aciertos=aciertos+1
                    
        # Calculando monto ganado coincidencias
        
        if aciertos==6:
            premio=apuesta*20
            saldo=saldo+premio
        elif aciertos==5:
            premio=apuesta*10
            saldo=saldo+premio
        elif aciertos==4:
            premio=apuesta*5
            saldo=saldo+premio
        elif aciertos==3:
            premio=apuesta
            saldo=saldo+premio
        elif aciertos==2 or aciertos==1 or aciertos==0:
            premio=0
            saldo=saldo+premio
        
        # Reglas adicionales
        
        #1 -  Numeros Pares
        
        adicional1=0
        adicional2=0
        adicional3=0
        adicional4=0
        
        for x in numeros:
            for y in azar:
                if x==y and x%2==0 and aciertos>=1:
                    adicional1=adicional1+(apuesta*0.05)
                    
        #2 -  Numeros Impares
        
        for x in numeros:
            for y in azar:
                if x==y and x%2==1 and aciertos>=1:
                    adicional2=adicional2+(apuesta*0.01)
         
        #3 -  Misma posicion
        
        for x in numeros:
            for y in azar:
                if x==y and numeros.index(x)==numeros.index(y):
                    adicional3=adicional3+(apuesta*0.10)
                    
        #4 -  Mismo numero del monto de apuesta
        
        for x in numeros:
            for y in azar:
                if x==y and x==apuesta:
                    adicional4=adicional4+(apuesta*0.25)
        
        saldo=saldo+adicional1+ adicional2+adicional3+adicional4
        
        print "----------------------------------------------------------------------------------"
        print "Los numeros ganadores son: " + str(azar[0]) + ", " + str(azar[1]) + ", " + str(azar[2]) + ", " + str(azar[3]) + ", " + str(azar[4]) + ", " + str(azar[5])
        print "----------------------------------------------------------------------------------"
        print "Ud. obtuvo " + str(aciertos) + " acierto(s)"
        print "Premio Apuesta: S/. " + str(premio)
        print "Premio Adicional 1(x0.05): S/. " + str(adicional1)
        print "Premio Adicional 2(x0.01): S/. " + str(adicional2)
        print "Premio Adicional 3(x0.10): S/. " + str(adicional3)
        print "Premio Adicional 4(x0.25): S/. " + str(adicional4)
        print "Nuevo saldo: S/. " + str(saldo)
        print "----------------------------------------------------------------------------------"
        
        if saldo<20:
            print "Ud. no cuenta con un saldo suficiente para seguir jugando.. Gracias"
            break
            
        # Sentencias para seguir jugando
        
        respuesta = str(input("Desea seguir apostando?.......[S],[N]?"))
        if respuesta<>'S' and respuesta<>'s':
            print "Muchas Gracias por jugar :)"
            break