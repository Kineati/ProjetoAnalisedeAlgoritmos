from audioop import reverse
from random import random
from turtle import done, st
import numpy as np
import random
import time
import math
import sys

sys.setrecursionlimit(100000)
st = time.process_time() #Momento que a CPU Iniciou o Programa

#Programa Principal
soma_x = 0
for i in range (1000000):
    soma_x = soma_x + i

time.sleep(3)
#print("Soma dos Primeiros Milhoes de Numeros",soma_x)

#Algoritmos para os Vetores
def Vetor1000_1():
    Vetor1_1 = []
    i = 0
    for i in range(1000):
        Vetor1_1.append(i)
    return Vetor1_1

def Vetor1000_2():
    Vetor1_2 = []
    i = 0
    for i in range(1000):
        Vetor1_2.append(random.randint(0,1000))
    return Vetor1_2

def Vetor1000_3():
    Vetor1_3 = []
    i = 0
    for i in reversed(range(1000)):
        Vetor1_3.append(i)
    return Vetor1_3


def Vetor10000_1():
    Vetor2_1 = []
    i = 0
    for i in range(10000):
        Vetor2_1.append(i)
    return Vetor2_1

def Vetor10000_2():
    Vetor2_2 = []
    i = 0
    for i in range(10000):
        Vetor2_2.append(random.randint(0,10000))
    return Vetor2_2

def Vetor10000_3():
    Vetor2_3 = []
    i = 0
    for i in reversed(range(10000)):
        Vetor2_3.append(i)
    return Vetor2_3

def Vetor100000_1():
    Vetor3_1 = []
    i = 0
    for i in range(100000):
        Vetor3_1.append(i)
    return Vetor3_1

def Vetor100000_2():
    Vetor3_2 = []
    i = 0
    for i in range(100000):
        Vetor3_2.append(random.randint(0,100000))
    return Vetor3_2

def Vetor100000_3():
    Vetor3_3 = []
    i = 0
    for i in reversed(range(100000)):
        Vetor3_3.append(i)
    return Vetor3_3

#Algoritmos de Ordenacao
def BubbleSort(Vetor,Tamanho):
    i = 0
    j = 0 
    aux = 0
    global Comparacoes
    global Trocas

    for i in range(Tamanho-1):
        for j in range(0,Tamanho-i-1):
            Comparacoes = Comparacoes + 1
            if(Vetor[j] >= Vetor[j+1]):
                aux = Vetor[j]
                Trocas = Trocas + 1
                Vetor[j] = Vetor[j+1]
                Trocas = Trocas + 1
                Vetor[j+1] = aux
                Trocas = Trocas + 1

    print("Total de Trocas Ocorridas:",Trocas)
    print("Total de Comparacoes Ocorridas:",Comparacoes)

def ImprovedBubbleSort(Vetor,Tamanho):
    i = 0
    j = 0 
    aux = 0
    global Comparacoes
    global Trocas
    global Trocou
    global Dif

    for i in range(Tamanho-1):
        for j in range(0,Tamanho-i-1):
            Comparacoes = Comparacoes + 1
            if(Vetor[j] >= Vetor[j+1]):
                Trocou = True
                aux = Vetor[j]
                Trocas = Trocas + 1
                Vetor[j] = Vetor[j+1]
                Trocas = Trocas + 1
                Vetor[j+1] = aux
                Trocas = Trocas + 1

        if not Trocou:
            Dif = 1
            return

    print("Total de Trocas Ocorridas:",Trocas)
    print("Total de Comparacoes Ocorridas:",Comparacoes)

def InsertionSort(Vetor,tamanho):
    nins = 1
    pins = 0 
    aux = 0
    global Trocas
    global Comparacoes

    for nins in range(tamanho):
        aux = Vetor[nins]
        Trocas = Trocas + 1
        pins = nins - 1
        Comparacoes = Comparacoes + 1
        while((pins >= 0) & (aux < Vetor[pins])):
            Comparacoes = Comparacoes + 1
            Vetor[pins+1] = Vetor[pins]
            Trocas = Trocas + 1
            pins = pins - 1
        Vetor[pins+1] = aux
        Trocas = Trocas + 1
    
    print("Total de Trocas Ocorridas:",Trocas)
    print("Total de Comparacoes Ocorridas:",Comparacoes)

def SelectionSort(Vetor,Tamanho):
    i = 0
    j = 0
    aux = 0
    global Comparacoes
    global Trocas

    for i in range(Tamanho-1):
        for j in range(i+1,Tamanho):
            Comparacoes = Comparacoes + 1
            if(Vetor[i] > Vetor[j]):
                aux = Vetor[i]
                Trocas = Trocas + 1
                Vetor[i] = Vetor[j]
                Trocas = Trocas + 1
                Vetor[j] = aux
                Trocas = Trocas + 1
    
    print("Total de Trocas Ocorridas:",Trocas)
    print("Total de Comparacoes Ocorridas:",Comparacoes)

def MergeSort(Vetor):
    #print("Splitting ",alist)
    global Comparacoes
    global Trocas
    global Dif

    if len(Vetor)>1:

        mid = len(Vetor)//2
        MetadeEsquerda = Vetor[:mid]
        MetadeDireita = Vetor[mid:]

        MergeSort(MetadeEsquerda)
        MergeSort(MetadeDireita)

        i=0
        j=0
        k=0
        while i < len(MetadeEsquerda) and j < len(MetadeDireita):
            Comparacoes = Comparacoes + 1
            if MetadeEsquerda[i] < MetadeDireita[j]:
                Trocas = Trocas + 1
                Vetor[k]=MetadeEsquerda[i]
                i=i+1
            else:
                Trocas = Trocas + 1
                Vetor[k]=MetadeDireita[j]
                j=j+1
            k=k+1

        while i < len(MetadeEsquerda):
            Trocas = Trocas + 1
            Vetor[k]=MetadeEsquerda[i]
            i=i+1
            k=k+1

        while j < len(MetadeDireita):
            Trocas = Trocas + 1
            Vetor[k]=MetadeDireita[j]
            j=j+1
            k=k+1
    Dif = 1
    return Vetor

def QuickSort(Vetor):
    QuickSortHelper(Vetor,0,len(Vetor)-1)

def QuickSortHelper(Vetor,Primeiro,Ultimo):
    if Primeiro<Ultimo:
        PontoParticao = Particao(Vetor,Primeiro,Ultimo)

        QuickSortHelper(Vetor,Primeiro,PontoParticao-1)
        QuickSortHelper(Vetor,PontoParticao+1,Ultimo)

def Particao(Vetor,Primeiro,Ultimo):
    global Comparacoes
    global Trocas
    global Dif

    ValorPivo = Vetor[Primeiro]

    Esquerda = Primeiro+1
    Direita = Ultimo

    Pronto = False
    while not Pronto:

        while Esquerda <= Direita and Vetor[Esquerda] <= ValorPivo:
            Esquerda = Esquerda + 1
            Comparacoes = Comparacoes + 1

        while Vetor[Direita] >= ValorPivo and Direita >= Esquerda:
            Direita = Direita -1
            Comparacoes = Comparacoes + 1

        if Direita < Esquerda: 
            Pronto = True
        else:
            Trocas = Trocas + 1
            Aux = Vetor[Esquerda]
            Trocas = Trocas + 1
            Vetor[Esquerda] = Vetor[Direita]
            Trocas = Trocas + 1
            Vetor[Direita] = Aux

    Trocas = Trocas + 1
    Aux = Vetor[Primeiro]
    Trocas = Trocas + 1
    Vetor[Primeiro] = Vetor[Direita]
    Trocas = Trocas + 1
    Vetor[Direita] = Aux
    Dif = 1
    return Direita

#Programa Final
Comparacoes = 0
Trocas = 0
Trocou = False
Dif = 0

#Teste
V = Vetor1000_1()
SelectionSort(V,len(V))
#Teste

et = time.process_time() #Momento que a CPU Finalizou o Programa
resultado = et-st

if(Trocou == False and Dif == 1):
    print("Total de Trocas Ocorridas:",Trocas)
    print("Total de Comparacoes Ocorridas:",Comparacoes)
elif(Dif == 1):
    print("Total de Trocas Ocorridas:",Trocas)
    print("Total de Comparacoes Ocorridas:",Comparacoes)
print("Tempo de Execucao: ",resultado, "Segundos")


