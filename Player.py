from random import randint
import pygame
from Tiro import *

naves = []
particulas_nave = []

def AdicionaNave(xpos,ypos,largura,altura,sprite,tiros,power,vida_atual,vida_maxima,sprite_indice):
    vivo = True
    naveX = xpos + 3
    naveY = ypos + 3
    nave_largura = largura
    nave_altura = altura
    nave_sprite = sprite
    naves.append([naveX,naveY,nave_largura,nave_altura,nave_sprite,tiros,power,vida_atual,vida_maxima,vivo,sprite_indice])

def MovimentoNave(nave, tamanho_tela):
    if nave[9]:
        velocidade = 5
        # nave[10] = 2
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
                nave[10] -= 0.2
                if nave[10] <= 0:
                    nave[10] = 0
            else:
                nave[1] = nave[1]
        if keys[pygame.K_DOWN]:
            if nave[1] <= tamanho_tela[1] - nave[3]:
                nave[1] = nave[1] + velocidade
                nave[10] += 0.2
                if nave[10] > 3:
                    nave[10] = 4
            else:
                nave[1] = tamanho_tela[1] - nave[3]
                
def estabilizaNave(nave) :
    if nave[10] > 2:
        nave[10] -= 0.1
    if nave[10] < 2:
        nave[10] += 0.1

def TiroNave(nave,tempo):
    if nave[9]:
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_SPACE]:
            AdicionaTiroNave(nave[0]+100,nave[1] + (nave[3]/2),5,5,(255,255,255),[1,0],5,nave[5],nave[6])

def drawParticlesPlayer(nave,vel):
    if nave[9]:
        particulas_nave.append([[nave[0],nave[1]+(nave[3]/2)],[randint(0,20)/10-1,-2],randint(4,15)])
        for particle in particulas_nave:
            particle[0][0] += particle[1][1] * vel
            particle[0][1] += particle[1][0]
            particle[2] -= 0.2
            particle[1][1] -= 0.3
            if(int(particle[2]*0.3) > 0):
                        # pygame.draw.circle(game,(255//(int(particle[2]*0.7)),255//(int(particle[2]*2)),255//(int(particle[2]*2))),[int(particle[0][0]),int(particle[0][1])],int(particle[2]))
                pygame.draw.rect(pygame.display.get_surface(),(255//(int(particle[2]*0.3)),255//(int(particle[2]*0.6)),255//(int(particle[2]*2))),(int(particle[0][0]),int(particle[0][1]),int(particle[2]),int(particle[2])))
            if(particle[2] <= 0):
                particulas_nave.remove(particle)

def verificaVida(lista,nave):
    for nave in lista:
        if nave[7] <= 0:
            nave[9] = False
            nave[0] = -100
            nave[1] = -100
            lista.remove(nave)
        