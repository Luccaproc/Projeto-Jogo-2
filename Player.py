import pygame
from Tiro import *

naves = []

def AdicionaNave(xpos,ypos,largura,altura,cor,tiros,power):
    naveX = xpos + 3
    naveY = ypos + 3
    nave_largura = largura
    nave_altura = altura
    nave_cor = cor
    naves.append([naveX,naveY,nave_largura,nave_altura,nave_cor,tiros,power])

def MovimentoNave(nave, tamanho_tela):
    velocidade = 5
    
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT]: # We can check if a key is pressed like this
        if(nave[0] >= 0 + nave[2]):
            nave[0] = nave[0] - velocidade
        else:
            nave[0] = nave[0]
    if keys[pygame.K_RIGHT]:
        if nave[0] <= tamanho_tela[0] - nave[2]:
            nave[0] = nave[0] + velocidade
        else: 
            nave[0] = tamanho_tela[0] - nave[2]
    if keys[pygame.K_UP]:
        if nave[1] >= 0 + nave[3]:
            nave[1] = nave[1] - velocidade
        else:
            nave[1] = nave[1]
    if keys[pygame.K_DOWN]:
        if nave[1] <= tamanho_tela[1] - nave[3]:
            nave[1] = nave[1] + velocidade
        else:
            nave[1] = tamanho_tela[1] - nave[3]

def TiroNave(nave,tempo):
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_SPACE]:
        AdicionaTiroNave(nave[0],nave[1] + (nave[3]/2),5,5,(255,255,255),[1,0],5,nave[5],nave[6])

