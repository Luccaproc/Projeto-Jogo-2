import pygame
import os

from random import randint

from Player import *
from Tiro import *
from Inimigo import *
from Particulas import *
from Colisoes import *
from Chefe import *
from Buff import *
# from Parallax import *

pygame.init()

fps = 60
tamanho_tela = (1024,512)
background = (0,0,0)

tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption('Synth Invaders')
relogio = pygame.time.Clock()
tempo = pygame.time.get_ticks()

squid = pygame.image.load(os.path.join("assets","imagens","squid.png")).convert_alpha()
tiro = pygame.image.load(os.path.join("assets","imagens","Tiro.png")).convert_alpha()
 
backgroundImg = pygame.image.load(os.path.join("assets","imagens","cenario.png")).convert_alpha()
backgroundImg2 = pygame.transform.scale(backgroundImg,(4096,2048))

cenarios = []

tiro_sprite = []
sprites_squid = []

def criarSprite(img,lista,qtd,linhas,colunas,largura,altura):
    for i in range(qtd):
        col = i % colunas
        linha = i // linhas

        corte = (col*largura,linha*altura,largura,altura)
        sprite = img.subsurface(corte).convert_alpha()
        lista.append(sprite)

criarSprite(squid,sprites_squid,9,3,3,70,70)
criarSprite(tiro,tiro_sprite,7,3,3,32,32)


qtd_cenarios = 14

for index in range(qtd_cenarios):
    col = index%4
    linha = index//4
    
    corte = (col*1024,linha*512,1024,512)
    img = backgroundImg2.subsurface(corte).convert_alpha()
    objImg = [img,0,0]
    cenarios.append(objImg)

cenario_width = cenarios[0][0].get_width()

def draw_cenario(img,speed):
    tiles = math.ceil(tamanho_tela[0]/cenario_width)+1
    scrollInfinito(img,speed, tiles)
    scrollReset(img,speed)

def scrollInfinito(img,speed,tiles):
    if speed > 0 :
        for i in range(0, tiles):
            tela.blit(img[0],((i * cenario_width )+ img[1],0))
                # tela.blit(img[0],((i*cenario_width)-(img[1]*speed),0))
    else:
        tela.blit(img[0],(0,0))

def scrollReset(img,speed):
    if speed > 0:
        img[1] -= 5 * speed 
        if abs(img[1]) > cenario_width :
            img[1] = 0 

def adicionaAnimacaoTiro(gameObj, posicao, tempo):
    # segundos = (pygame.time.get_ticks() - tempo) // 1000
    # atirou = True
    # if atirou and segundos < 3:
        # print(segundos)
    gameObj[7] += 0.2
    if gameObj[7] > 6 :
        gameObj[7] = 0
    tela.blit(gameObj[6][math.ceil(gameObj[7])],posicao)
        # atirou = False
        # segundos = 0

def desenhaBarraVida(vida,vida_max,vivo):
    if(vivo):
        pygame.draw.rect(tela,(255,0,0),(20,20,vida,20))
        pygame.draw.rect(tela,(255,255,255),(20,20,vida_max,20),1)

def jogo():
    jogando = True
    pontos = 0
    
    AdicionaNave(tamanho_tela[0]/2,tamanho_tela[1]/2,50,25,(255,255,255),[],1,200,500)
    nave = naves[0]
    pygame.mouse.set_visible(0)
    while jogando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogando = False
                pygame.quit()

        tela.fill((70,70,70))
        tempo_jogo = (pygame.time.get_ticks() - tempo)//1000

        velocidade = (tempo_jogo * 0.01) 

        draw_cenario(cenarios[0],0)
        draw_cenario(cenarios[1],0)
        draw_cenario(cenarios[2],0)
        draw_cenario(cenarios[3],(0.1*velocidade))
        draw_cenario(cenarios[4],0)
        draw_cenario(cenarios[5],0)
        draw_cenario(cenarios[6],0)
        draw_cenario(cenarios[7],0)
        draw_cenario(cenarios[12],0)
        draw_cenario(cenarios[13],(2*velocidade))

        RemoveElementosTamanhoTela(inimigos,tamanho_tela)
        MovimentoNave(nave,tamanho_tela)
        desenhaBarraVida(nave[7],nave[8],nave[9])
        
        TiroNave(nave,tempo)
        RemoveTiros(nave[5],tamanho_tela)

        SpawnInimigo(tamanho_tela,sprites_squid,velocidade+2)
        SpawnChefe(tamanho_tela,velocidade+2)
        SpawnBuff(tamanho_tela)

        FogoBoss(chefes,tiro_sprite)
        FogoInimigo(inimigos,tiro_sprite)

        DesenhaParticulas()
        drawParticlesPlayer(nave,velocidade)

        setTheta()
        setTheta_BOSS()
        # MovimentoInimigo(inimigos)

        for nav in naves:
            print(nav[7])
            pygame.draw.rect(tela,nav[4],(nav[0],nav[1],nav[2],nav[3]))

        #colisão de inimigos com a nave
        RemoveElementosColisao(inimigos,nave,True,False)
       
        #colisão de nave com buffs
        buffColisao(buffs,nave)

        #desenhando inimigos na tela
        for inimigo in inimigos:
            MovimentoInimigo(inimigo,velocidade)
            inimigo[6] += 0.1
            tela.blit(inimigo[5][math.ceil(inimigo[6])],(inimigo[0]+inimigo[2]/2,inimigo[1]+inimigo[3]/2))
            if inimigo[6] > 3:
                inimigo[6] = 0
                
            # pygame.draw.rect(tela,inimigo[5],(inimigo[0],inimigo[1],inimigo[2],inimigo[3]))

        #desenhando chefes na tela
        for chefe in chefes:
            MovimentoBoss(chefe, tamanho_tela,velocidade)
            pygame.draw.rect(tela,chefe[5],(chefe[0],chefe[1],chefe[2],chefe[3]))

        #desenhando tiros de inimigos na tela
        for inimigo in inimigos:
            RemoveTiros(inimigo[10],tamanho_tela)
            ColisaoBalasNaveInimigo(nave[5],inimigo)
            ColisaoBalasInimigoNave(inimigo[10],nave)
            # RemoveElementosColisao(inimigo[10],nave,True,True)
            for tiro in inimigo[10]:
                tiro[0] += (tiro[5][0] * 7)
                tiro[1] += (tiro[5][1] * 7)
                tiro[7] += 0.3
                if tiro[7] > 6:
                    tiro[7] = 0
                adicionaAnimacaoTiro(tiro,(inimigo[0]-(inimigo[2]//2),inimigo[1]+(inimigo[3]//2)+5),tempo)
                pygame.draw.rect(tela,tiro[4],(tiro[0],tiro[1],tiro[2],tiro[3]))
                atirou = False

        #desenhando tiros de chefes na tela
        for chefe in chefes:
            RemoveTiros(chefe[9],tamanho_tela)
            RemoveElementosColisao(nave[5],chefe,True,True)
            RemoveElementosColisao(chefe[9],nave,True,True)
            for tiro in chefe[9]:
                tiro[0] += (tiro[5][0] * 10)
                tiro[1] += (tiro[5][1] * 10)
                # tela.blit(tiro[6][math.ceil(tiro[7])],(chefe[0]-chefe[2],chefe[1]+(chefe[3]/2)))
                # tiro[7] += 0.1
                # if tiro[7] > 3:
                #     tiro[7] = 0
                pygame.draw.rect(tela,tiro[4],(tiro[0],tiro[1],tiro[2],tiro[3]))
        
        #desenahndo tiros da nave na tela
        for tiro in nave[5]:
            # print(tiro)
            tiro[0] += (tiro[5][0] * 10)
            tiro[1] += (tiro[5][1] * 10)
            pygame.draw.rect(tela,tiro[4],(tiro[0],tiro[1],tiro[2],tiro[3]))
               
        for buff in buffs:
            MovimentoBuff(buff)
            pygame.draw.rect(tela,buff[5],(buff[0],buff[1],buff[2],buff[3]))

        pygame.display.update()
        
        RemoveElementosTamanhoTela(naves,tamanho_tela)
        relogio.tick(fps)

jogo()