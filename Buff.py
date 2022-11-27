import pygame
from random import randint

start_buff_time = pygame.time.get_ticks()

buffs = []

def adicionaBuff(xpos,ypos,largura,altura,vel,sprite,direcao,indice_sprite):
    rand_tipe = randint(0,2)
    buff = [xpos,ypos,largura,altura,vel,sprite,direcao,rand_tipe,indice_sprite]
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
            if elemento[6] > 5:
                elemento[6] += 0
            else :
                elemento[6] += 1
            lista.remove(el)
            