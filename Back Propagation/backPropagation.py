__author__ = 'AndrewJ'
import math

#Entradas
entradas =[[0,0],[0,1],[1,0],[1,1]]
#Valores esperados:
deseada = [0,1,1,0]

#Pesos ocultos
w1 = [[0.1, -0.7], [0.5, 0.3]]
w2 = [0.2, 0.4]

#Net
net=[0,0]
net2=[0]
#Salida
salida=[0,0]
salida2=[0]

#Tasa de aprendizaje
tasaDeAprendizaje = 0.25

def backPropagation():

    #contador para llevar la cantidad de corridas
    cont = 0
    iteracion = 0

    parar=True
    while(True):
        #Neurona 1
        #entrada neta:
        net[0] = w1[0][0] * entradas[iteracion][0] + w1[0][1] * entradas[iteracion][1]
        #salida:
        salida[0] = 1 / (1 + math.e**-net[0])

        #Neurona 2
        #entrada neta:
        net[1] = w1[1][0] * entradas[iteracion][0] + w1[1][1] * entradas[iteracion][1]
        #salida:
        salida[1] = 1 / (1 + math.e**-net[1])

        #Neurona salida
        #entrada neta:
        net2[0] = w2[0] * salida[0] + w2[1] * salida[1]
        #salida:
        salida2[0] = 1 / (1 + math.e**-net2[0])

        #Error de la capa de salida
        error = deseada[iteracion] - salida2[0]

        if (error!=0):
            #Ajuste de peso de la neurona salida:
            #ToDo: delta might be wrong in (deseada[iteracion]-salida2[0]) * error = (error * error)?
            w2Temp = [w2[0],w2[1]]
            delta = salida2[0] * (1-salida2[0]) * error
            w2[0] = w2[0] + tasaDeAprendizaje * salida[0] * delta
            w2[1] = w2[1] + tasaDeAprendizaje * salida[1] * delta

            #Ajuste de pesos de la capa oculta:
            #Neurona 1
            deltaN1 = salida[0] * (1-salida[0]) * (w2Temp[0] * delta)
            w1[0][0] = w1[0][0] + tasaDeAprendizaje * entradas[iteracion][0] * deltaN1
            w1[0][1] = w1[0][1] + tasaDeAprendizaje * entradas[iteracion][1] * deltaN1

            #Neurona 2
            deltaN2 = salida[1] * (1-salida[1]) * (w2Temp[1]* delta)
            w1[1][0] = w1[1][0] + tasaDeAprendizaje * entradas[iteracion][0] * deltaN2
            w1[1][1] = w1[1][1] + tasaDeAprendizaje * entradas[iteracion][1] * deltaN2
            parar = False

        print("\n"+str(cont) + " ---------------------------------------------------------"+str(iteracion))
        print("Entradas: "+ str(entradas[iteracion][0]) + ", " + str(entradas[iteracion][1]))
        print("Pesos: " + str(w1[0][0]) +", "+ str(w1[0][1]) + ", " + str(w1[1][0]) + ", " + str(w1[1][1]) )
        print("Net: " +str(net[0])+", "+str(net[1])+", "+str(net2[0]))
        print("Salida: " +str(salida[0])+", "+str(salida[1])+", "+str(salida2[0]))
        print("Deseado: " +str(deseada[iteracion]))
        print("Error: " +str(error))

        cont=cont+1
        #Condiciones de parada:
        if(iteracion==3):
            if(parar==True):
                break
            iteracion = 0
            parar=True
        else:
            iteracion = iteracion + 1


backPropagation()




