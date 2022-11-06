import pygame
import os

from random import randint

from Player import *
from Tiro import *
from Inimigo import *
from Particulas import *
from Colisoes import *
from Chefe import *
# from Parallax import *

pygame.init()

fps = 60
tamanho_tela = (1024,512)
background = (0,0,0)

tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption('Synth Invaders')
relogio = pygame.time.Clock()
tempo = pygame.time.get_ticks()


backgroundImg = pygame.image.load(os.path.join("assets","imagens","cenario.png")).convert_alpha()
backgroundImg2 = pygame.transform.scale(backgroundImg,(4096,2048))

cenarios = []

qtd_cenarios = 14

for index in range(qtd_cenarios):
    col = index%4
    linha = index//4
    
    corte = (col*1024,linha*512,1024,512)
    img = backgroundImg2.subsurface(corte)
    objImg = [img,0,0]
    cenarios.append(objImg)

cenario_width = cenarios[0][0].get_width()


def draw_bg(img,speed):
    tiles = math.ceil(tamanho_tela[0]/cenario_width)+math.ceil(speed)
    scrollInfinito(img,speed, tiles)
    scrollReset(img,speed)

def scrollInfinito(img,speed,tiles):
    for i in range(0, tiles):
        tela.blit(img[0],((i * cenario_width )+ img[1],0))
            # tela.blit(img[0],((i*cenario_width)-(img[1]*speed),0))

def scrollReset(img,speed):
    img[1] -= 5 * speed 
    if abs(img[1]) > cenario_width :
        img[1] = 0 

def jogo():
    jogando = True
    pontos = 0
    
    AdicionaNave(tamanho_tela[0]/2,tamanho_tela[1]/2,50,25,(255,255,255),[])
    nave = naves[0]
    pygame.mouse.set_visible(0)
    while jogando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogando = False
                pygame.quit()

        tela.fill((70,70,70))

        draw_bg(cenarios[0],0)
        draw_bg(cenarios[1],0)
        draw_bg(cenarios[2],0)
        draw_bg(cenarios[3],0.3)
        draw_bg(cenarios[4],0)
        draw_bg(cenarios[5],0)
        draw_bg(cenarios[6],0)
        draw_bg(cenarios[7],0)
        draw_bg(cenarios[8],0)
        draw_bg(cenarios[9],0.5)
        draw_bg(cenarios[10],0.7)
        # draw_bg(cenarios[11],0.8)
        draw_bg(cenarios[13],1)
        # scrollInfinito(cenarios[13])

        RemoveElementosTamanhoTela(inimigos,tamanho_tela)
        MovimentoNave(nave,tamanho_tela)

        TiroNave(nave,tempo)
        RemoveTiros(nave[5],tamanho_tela)

        SpawnInimigo(tamanho_tela)
        SpawnChefe(tamanho_tela)

        FogoBoss(chefes)
        FogoInimigo(inimigos)

        DesenhaParticulas()
        

        setTheta()
        setTheta_BOSS()
        # MovimentoInimigo(inimigos)

        for nav in naves:
            pygame.draw.rect(tela,nav[4],(nav[0],nav[1],nav[2],nav[3]))

        #colisão de inimigos com a nave
        RemoveElementosColisao(inimigos,nave,True,False)
       

        #desenhando inimigos na tela
        for inimigo in inimigos:
            MovimentoInimigo(inimigo)
            pygame.draw.rect(tela,inimigo[5],(inimigo[0],inimigo[1],inimigo[2],inimigo[3]))

        #desenhando chefes na tela
        for chefe in chefes:
            MovimentoBoss(chefe, tamanho_tela)
            pygame.draw.rect(tela,chefe[5],(chefe[0],chefe[1],chefe[2],chefe[3]))

        #desenhando tiros de inimigos na tela
        for inimigo in inimigos:
            RemoveTiros(inimigo[9],tamanho_tela)
            RemoveElementosColisao(nave[5],inimigo,True,True)
            RemoveElementosColisao(inimigo[9],nave,True,True)
            for tiro in inimigo[9]:
                tiro[0] += (tiro[5][0] * 10)
                tiro[1] += (tiro[5][1] * 10)
                pygame.draw.rect(tela,tiro[4],(tiro[0],tiro[1],tiro[2],tiro[3]))

        #desenhando tiros de chefes na tela
        for chefe in chefes:
            RemoveTiros(chefe[9],tamanho_tela)
            RemoveElementosColisao(nave[5],chefe,True,True)
            RemoveElementosColisao(chefe[9],nave,True,True)
            for tiro in chefe[9]:
                tiro[0] += (tiro[5][0] * 10)
                tiro[1] += (tiro[5][1] * 10)
                pygame.draw.rect(tela,tiro[4],(tiro[0],tiro[1],tiro[2],tiro[3]))
        
        #desenahndo tiros da nave na tela
        for tiro in nave[5]:
            # print(tiro)
            tiro[0] += (tiro[5][0] * 10)
            tiro[1] += (tiro[5][1] * 10)
            pygame.draw.rect(tela,tiro[4],(tiro[0],tiro[1],tiro[2],tiro[3]))
               
        pygame.display.update()
        
        RemoveElementosTamanhoTela(naves,tamanho_tela)
        relogio.tick(fps)

jogo()