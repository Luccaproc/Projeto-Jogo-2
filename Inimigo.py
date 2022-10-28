import math
from random import randint
import pygame
from Tiro import *

inimigos = []

startTime = pygame.time.get_ticks()

THETA = 0

def AdicionaInimigo(xpos,ypos,largura,altura,velocidade,cor,direcao,cooldown_max,cooldown_start,tiros):
    global inimigos
    inimigos.append([xpos,ypos,largura,altura,velocidade,cor,direcao,cooldown_max,cooldown_start,tiros])

def SpawnInimigo(tamanho_tela):
    tempo_atual = pygame.time.get_ticks()
    global startTime
    segundos = (tempo_atual - startTime)//1000

    xpos = tamanho_tela[0]
    ypos = randint(50,tamanho_tela[1]-50)
    
    if segundos > 1:
        AdicionaInimigo(xpos,ypos,50,25,2,(255,255,255),[-1,0],70,0,[])
        startTime = pygame.time.get_ticks()

def MovimentoInimigo(inimigo):
    global THETA
    seno = math.sin(THETA)
    inimigo[0] += inimigo[6][0] * inimigo[4]
    inimigo[1] += inimigo[6][1] * inimigo[4] 
    inimigo[1] += seno * 5

def setTheta():
    global THETA 
    THETA += 0.1

def FogoInimigo(inimigos):
    for n in range(len(inimigos)): 
        inimigo = inimigos[n]

        cooldown_maximo_inimigo = inimigo[7]

        if inimigo[8] > cooldown_maximo_inimigo:
            AdicionaTiroInimigo(inimigo[0],inimigo[1],5,5,(255,0,0),[-1,0],inimigo[7],inimigo[8],inimigo[9])
            inimigo[8] = 0
        else :
            inimigo[8] += 1
        