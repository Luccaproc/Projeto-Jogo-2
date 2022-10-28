from random import randint
import pygame

from Player import *
from Tiro import *
from Inimigo import *
from Particulas import *

pygame.init()

fps = 60
tamanho_tela = (1024,512)
background = (0,0,0)

tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption('Synth Invaders')
relogio = pygame.time.Clock()

tempo = pygame.time.get_ticks()

def RemoveElementosTamanhoTela(lista,tamanho_tela):
    for el in lista:
        if el[0] >= tamanho_tela[0] or el[0] <= 0:
            print('removeu')
            lista.remove(el)
        elif el[1] >= tamanho_tela[1] or el[1] <= 0:
            print('removeu')
            lista.remove(el)

def RemoveElementosColisao(lista,elemento):
    for i in range(len(lista)):
        el_lista = lista[i]
        el = elemento
        d = ( (el_lista[0] - elemento[0])**2 + (el_lista[1] - elemento[1])**2 )**0.5
        if d <= el_lista[2]/2 + elemento[2]/2:
            print('colidiu')
            AdicionaParticulas(el_lista[0],el_lista[1])
            el_lista[0] = -30
            el_lista[1] = -30

def jogo():
    jogando = True
    pontos = 0

    AdicionaNave(tamanho_tela[0]/2,tamanho_tela[1]/2,50,25,(255,255,255),[])

    pygame.mouse.set_visible(0)
    while jogando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogando = False
                pygame.quit()

        tela.fill((70,70,70))

        RemoveElementosTamanhoTela(inimigos,tamanho_tela)

        MovimentoNave(naves[0],tamanho_tela)
        TiroNave(naves[0],tempo)
        SpawnInimigo(tamanho_tela)
        FogoInimigo(inimigos)
        DesenhaParticulas()
        RemoveTiros(naves[0][5],tamanho_tela)

        setTheta()
        # MovimentoInimigo(inimigos)

        for nav in naves:
            pygame.draw.rect(tela,nav[4],(nav[0],nav[1],nav[2],nav[3]))

        #colisão de inimigos com a nave
        RemoveElementosColisao(inimigos,naves[0])

        #desenhando inimigos na tela
        for inimigo in inimigos:
            MovimentoInimigo(inimigo)
            pygame.draw.rect(tela,inimigo[5],(inimigo[0],inimigo[1],inimigo[2],inimigo[3]))

        #desenhando tiros de inimigos na tela
        for inimigo in inimigos:
            RemoveTiros(inimigo[9],tamanho_tela)
            for tiro in inimigo[9]:
                tiro[0] += (tiro[5][0] * 10)
                tiro[1] += (tiro[5][1] * 10)
                pygame.draw.rect(tela,tiro[4],(tiro[0],tiro[1],tiro[2],tiro[3]))
        
        #desenahndo tiros da nave na tela
        for tiro in naves[0][5]:
            # print(tiro)
            tiro[0] += (tiro[5][0] * 10)
            tiro[1] += (tiro[5][1] * 10)
            pygame.draw.rect(tela,tiro[4],(tiro[0],tiro[1],tiro[2],tiro[3]))
               
        pygame.display.update()
        
        relogio.tick(fps)

jogo()