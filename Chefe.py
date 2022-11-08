import pygame

import math
from random import randint
import pygame
from Tiro import *

chefes = []

startTime = pygame.time.get_ticks()

THETA_BOSS = 0

def AdicionaBoss(xpos,ypos,largura,altura,velocidade,cor,direcao,cooldown_max,cooldown_start,tiros,qtd_poder,metade,fogo):
    global chefes
    chefes.append([xpos,ypos,largura,altura,velocidade,cor,direcao,cooldown_max,cooldown_start,tiros,qtd_poder,metade,fogo])

def SpawnChefe(tamanho_tela,velocidade):

    tempo_atual = pygame.time.get_ticks()
    global startTime

    segundos = (tempo_atual - startTime)//1000

    xpos = tamanho_tela[0]
    ypos = (tamanho_tela[1]//2)-100
    
    if segundos > 30:
        AdicionaBoss(xpos,ypos,100,100,velocidade,(255,255,255),[-1,0],5,0,[],10,False,False)
        startTime = pygame.time.get_ticks()


def MovimentoBoss(chefe,tamanho_tela,vel):

    global THETA_BOSS

    seno = math.sin(THETA_BOSS)
    coseno = math.cos(THETA_BOSS)

    if chefe[0] > 700 and not chefe[11]:
        coseno = math.cos(THETA_BOSS)
        coseno -= chefe[4]
        seno = math.sin(THETA_BOSS)

        # chefe[0] += coseno
        # chefe[1] += chefe[6][1] * chefe[4] 

        chefe[1] += seno * 5
        chefe[0] += coseno

    if chefe[0] <= 700 or chefe[11]:
        chefe[11] = True
        coseno = math.cos(THETA_BOSS/2)
        seno = math.sin(THETA_BOSS/2)
        # self.rect.centerx = 600
        chefe[1] += seno * 5
        chefe[0] += coseno * 5

def setTheta_BOSS():
    global THETA_BOSS 
    THETA_BOSS += 0.1

def FogoBoss(chefes,sprite):
    for n in range(len(chefes)): 
        chefe = chefes[n]

        cooldown_maximo_chefe = chefe[7]

        if chefe[8] > cooldown_maximo_chefe:
            anguloStep = 360//(chefe[10]+1)
            anguloAtual = 45 - anguloStep
            if chefe[12]:
                for bullet in range(chefe[10]):
                    sen = math.sin((anguloAtual * math.pi)/180)*1
                    cos = math.cos((anguloAtual * math.pi)/180)*1

                    tiroX = chefe[0] + (chefe[2]/2)
                    tiroY = chefe[1] + (chefe[3]/2)
                
                    tiro_largura = 5
                    tiro_altura = 5
                    tiro_cor = (255,0,0)
                    tiro_direcao = [cos,sen]

                    # tiros_list.append([tiroX,tiroY,tiro_largura,tiro_altura,tiro_cor,tiro_direcao])

                    AdicionaTiroInimigo(tiroX,tiroY,tiro_largura,tiro_altura,tiro_cor,tiro_direcao,chefe[7],chefe[8],chefe[9],sprite,0)
                    anguloAtual -= math.ceil(anguloStep)
                chefe[12] = False
            else :
                chefe[8] = 0
                chefe[12] = True
            chefe[8] = 0
        else :
            chefe[8] += 1
        