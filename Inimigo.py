import math
from random import randint
import pygame
from Tiro import *

inimigos = []

startTime = pygame.time.get_ticks()

THETA = 0

def AdicionaInimigo(xpos,ypos,largura,altura,velocidade,sprite,sprite_index,direcao,cooldown_max,cooldown_start,tiros,vida,vivo):
    global inimigos
    theta = 0
    inimigos.append([xpos,ypos,largura,altura,velocidade,sprite,sprite_index,direcao,cooldown_max,cooldown_start,tiros,theta,vida,vivo])

def SpawnInimigo(tamanho_tela,sprites,velocidade):
    rand = randint(1,9)
    tempo_atual = pygame.time.get_ticks()
    global startTime
    segundos = (tempo_atual - startTime)
    rand_sprite = randint(0,1)
    xpos = tamanho_tela[0]
    ypos = randint(100,tamanho_tela[1]-100)
    
    if segundos >  1000 * (10/rand):
        vida_adicional = velocidade * 10
        AdicionaInimigo(xpos,ypos,50,25,velocidade,sprites[rand_sprite],0,[-1,0],100,0,[],50+vida_adicional,True)
        startTime = pygame.time.get_ticks()

def MovimentoInimigo(inimigo,vel):
    global THETA
    if inimigo[13]:
        seno = math.sin(inimigo[11])

        inimigo[0] += inimigo[7][0] * inimigo[4] 
        inimigo[1] += inimigo[7][1] * inimigo[4] 
        inimigo[1] += seno * 5

        inimigo[11] += 0.1

def setTheta():
    global THETA 
    THETA += 0.1

def seno(angulo):
    angulo % 360

def FogoInimigo(inimigos,sprite):
    for n in range(len(inimigos)): 
        inimigo = inimigos[n]
        if inimigo[13]:
            cooldown_maximo_inimigo = inimigo[8]
            
            if inimigo[9] > cooldown_maximo_inimigo:
                AdicionaTiroInimigo(inimigo[0]-(inimigo[2]//2),inimigo[1]+(inimigo[3]//2)+5,5,5,(255,200,30),[-1,0],inimigo[8],inimigo[9],inimigo[10],sprite,0)
                inimigo[9] = 0
            else :
                inimigo[9] += 1
            
