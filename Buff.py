import pygame
from random import randint
import os
# pygame.init()

caminho_som = os.path.join("assets","som","buff.wav")

start_buff_time = pygame.time.get_ticks()
buff_som = pygame.mixer.Sound(caminho_som)

buffs = []

def colisaoRetangulo(el1,el2):
    if el1[0] < el2[0] + el2[2] and el1[0] + el1[2] > el2[0] and el1[1] < el2[1] + el2[3] and el1[3] + el1[1] > el2[1] :
        return True
    else :
        return False

def adicionaBuff(xpos,ypos,largura,altura,vel,sprite,direcao,indice_sprite):
    tipo = randint(0,1)
    buff = [xpos,ypos,largura,altura,vel,sprite[tipo],direcao,indice_sprite,tipo]
    buffs.append(buff)

def MovimentoBuff(buff):
   
    buff[0] += buff[6][0] * buff[4]
    buff[1] += buff[6][1] * buff[4] 

def SpawnBuff(tamanho_tela,sprite):
    tempo_atual = pygame.time.get_ticks()
    global start_buff_time
    segundos = (tempo_atual - start_buff_time)//1000

    xpos = tamanho_tela[0]
    ypos = randint(50,tamanho_tela[1]-50)
    
    if segundos > 5:
        adicionaBuff(xpos,ypos,10,10,3,sprite,[-1,0],0)
        start_buff_time = pygame.time.get_ticks()


def buffColisao(lista,elemento):
    for el in lista:
        d = ( (el[0] - elemento[0])**2 + (el[1] - elemento[1])**2 )**0.5
        if d <= el[2]/2 + elemento[2]/2:
            buff_som.play()
            if el[8] == 0:
                if elemento[6] <= 10:
                    elemento[6] += 1
                lista.remove(el)
            elif el[8] == 1:
                if elemento[7] >= 450:
                    elemento[7] = 500
                elif elemento[7] < 450:
                    elemento[7] += 50
                lista.remove(el)
            