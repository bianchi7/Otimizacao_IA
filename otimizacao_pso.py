import random
import numpy as np
import math
import copy

def f(x):  # função dos ouvintes das 17h as 00h
    return (-2 * x**3 + 27 * x**2 - 108 * x + 240) * 1/8

def g(x):    #função de interferencia 
    return f(x) + 2 * math.sin(4*x)

def fitness(posicao):
    return g(posicao)
    
def PSO(particula, iteracao, w, c1, c2, fitness, m): #m = max(1) ou min(0)
    Xmin = 0
    Xmax = 7

    if m not in (0, 1):
        raise ValueError("M precisa ser 0 (min) ou 1 (max)")

    # AVALIE A QUALIDADE DO HORARIO EM RELAÇÃO A ELE MESMO
    x = [random.uniform(Xmin, Xmax) for _ in range(particula)]  #Inicializar posição x[i] aleatória entre 0 e 7
    v = [random.uniform(-1, 1) for _ in range(particula)]  #Inicializar velocidade v[i]
    pBest = x.copy()
    pBestFitness = [fitness(pos) for pos in x] 

    # AVALIE A QUALIDADE DO HORARIO EM RELAÇÃO AOS OUTROS
    if m == 1:
        indice = pBestFitness.index(max(pBestFitness))
    else:
        indice = pBestFitness.index(min(pBestFitness))
    gBest = pBest[indice]
    gBestFitness = pBestFitness[indice]

    #Enquanto não atingir o critério de parada:
    for _ in range(iteracao):
        for i in range(particula):
            r1 = random.random()
            r2 = random.random()

            v[i] = w * v[i] + c1 * r1 * (pBest[i] - x[i]) + c2 * r2 * (gBest - x[i])  #Atualizar velocidade:
            x[i] = x[i] + v[i]       #Atualizar posição:

            # Manter posição no intervalo [0, 7]
            x[i] = max(Xmin, min(Xmax, x[i]))

            # Calcular fitness
            qualidade = fitness(x[i])

            if m == 1:
                melhorou = qualidade > pBestFitness[i]
            else:
                melhorou = qualidade < pBestFitness[i]

            if melhorou:
                pBest[i] = x[i]
                pBestFitness[i] = qualidade

            # Verificar melhora global
            if m == 1:
                melhor_global = pBestFitness[i] > gBestFitness
            else:
                melhor_global = pBestFitness[i] < gBestFitness

            if melhor_global:
                gBest = pBest[i]
                gBestFitness = pBestFitness[i]

    return gBest, gBestFitness

        