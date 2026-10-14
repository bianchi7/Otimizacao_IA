import random
import numpy as np
import math

def f(x):  # função dos ouvintes das 17h as 00h
    return (-2 *x**3 + 27 * x**2 - 108 * x + 240) * 1/8

def g(x):    #função de interferencia 
    return f(x) + 2 * math.sin(4*x)

def fitness_max(posicao):
    return g(posicao)
    
def PSO(particula, iteracao, w, c1, c2, f):
    Xmin = 0
    Xmax = 7

    # AVALIE A QUALIDADE DO HORARIO EM RELAÇÃO A ELE MESMO
    for i in particula:
        x = random.uniform(Xmin, Xmax)  #Inicializar posição x[i] aleatória entre 0 e 7
        v = random.uniform()      #Inicializar velocidade v[i]
        qualidade = fitness_max(x)
        pBest = x

    # AVALIE A QUALIDADE DO HORARIO EM RELAÇÃO AOS OUTROS
    #gbest = posição com melhor fitness (QUALIDADE) entre todas as partículas
    gBest = 

    #Enquanto não atingir o critério de parada:

        for i in particula:
            r1 = random.uniform()
            r2 = random.uniform()

            v = w * v + c1 * r1 * (pBest - x) + c2 * r2 * (gBest - x)  #Atualizar velocidade:
            x = x + v       #Atualizar posição:
        
            x = random.uniform(Xmin, Xmax)    #Manter x[i] dentro do intervalo [0, 7]
            #Calcular o novo fitness g(x[i])

            #Se a posição atual for melhor que pbest[i]:
                #pbest[i] = x[i]

        #Atualizar gbest com o melhor pbest encontrado

    #Retornar gbest e g(gbest)

#Definir numero particulas
#Definir o número máximo de iterações

#Definir os parâmetros w, c1 e c2