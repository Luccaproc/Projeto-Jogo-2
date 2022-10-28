from random import randint
import pygame

from Player import *
from Tiro import *
from Inimigo import *

pygame.init()

fps = 60
tamanho_tela = (1024,512)
background = (0,0,0)

tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption('Synth Invaders')
relogio = pygame.time.Clock()

tempo = pygame.time.get_ticks()
#nave

#inimigos

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

        MovimentoNave(naves[0],tamanho_tela)
        TiroNave(naves[0],tempo)

        SpawnInimigo(tamanho_tela)
        FogoInimigo(inimigos)

        RemoveTiros(naves[0][5],tamanho_tela)

        setTheta()
        # MovimentoInimigo(inimigos)

        for nav in naves:
            pygame.draw.rect(tela,nav[4],(nav[0],nav[1],nav[2],nav[3]))

        # for n in range(10):
        #     rand = randint(0, tamanho_tela[1])
        #     AdicionaInimigo(0,rand,25,25,5,(255,255,255),[-1,0])

        for inimigo in inimigos:
            MovimentoInimigo(inimigo)
            pygame.draw.rect(tela,inimigo[5],(inimigo[0],inimigo[1],inimigo[2],inimigo[3]))

        for inimigo in inimigos:
            for tiro in inimigo[9]:
                tiro[0] += (tiro[5][0] * 10)
                tiro[1] += (tiro[5][1] * 10)
                pygame.draw.rect(tela,tiro[4],(tiro[0],tiro[1],tiro[2],tiro[3]))
        

        for tiro in naves[0][5]:
            # print(tiro)
            tiro[0] += (tiro[5][0] * 10)
            tiro[1] += (tiro[5][1] * 10)
            pygame.draw.rect(tela,tiro[4],(tiro[0],tiro[1],tiro[2],tiro[3]))
               
        
               
            
        
        pygame.display.update()
        
        relogio.tick(fps)

jogo()