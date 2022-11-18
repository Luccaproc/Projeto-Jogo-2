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

alpha_over = 0

tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption('Synth Invaders')
relogio = pygame.time.Clock()
tempo = pygame.time.get_ticks()

aguaviva = pygame.image.load(os.path.join("assets","imagens","aguaviva.png")).convert_alpha()
squid = pygame.image.load(os.path.join("assets","imagens","squid.png")).convert_alpha()
tiro = pygame.image.load(os.path.join("assets","imagens","Tiro.png")).convert_alpha()
buff_tiro = pygame.image.load(os.path.join("assets","imagens","buff_tiro.png")).convert_alpha()

nave_img = pygame.image.load(os.path.join("assets","imagens","nave_sprite.png")).convert_alpha()


caminho_fonte = os.path.join("assets","fonts","04B_30__.TTF")

backgroundImg = pygame.image.load(os.path.join("assets","imagens","cenario.png")).convert_alpha()
backgroundImg2 = pygame.transform.scale(backgroundImg,(4096,2048))

cenarios = []

tiro_sprite = []
sprites_squid = []
boss_sprite = []
buff_sprite = []
nave_sprite = []

pontos = 0
nave = [] 


def criarSprite(img,lista,qtd,linhas,colunas,largura,altura):

    print('---------------------------------')
    for i in range(qtd):
        col = i % colunas
        linha = i // linhas
        print(str(linha)+'|'+str(col))
        corte = (col*largura,linha*altura,largura,altura)
        sprite = img.subsurface(corte).convert_alpha()
        lista.append(sprite)

criarSprite(squid,sprites_squid,9,3,3,70,70)
criarSprite(tiro,tiro_sprite,7,3,3,32,32)
criarSprite(aguaviva,boss_sprite,10,4,4,100,100)
criarSprite(buff_tiro,buff_sprite,12,4,4,32,32)

criarSprite(nave_img,nave_sprite,5,5,5,128,64)


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
    gameObj[7] += 0.2
    if gameObj[7] > 6 :
        gameObj[7] = 0
    tela.blit(gameObj[6][math.ceil(gameObj[7])],posicao)

def desenhaBarraVida(vida,vida_max,vivo):
    if(vivo):
        tamanho_barra = 400
        vida_rating = tamanho_barra/vida_max
        pygame.draw.rect(tela,(255,0,0),(20,20,vida*vida_rating,10))
        pygame.draw.rect(tela,(255,255,255),(20,20,tamanho_barra,10),1)

def desenhaGameOver(nave):
    if not nave[9]:
        global alpha_over
        s = pygame.Surface((1024,512))  # the size of your rect
        s.set_alpha(alpha_over)                # alpha level
        s.fill((0,20,10))           # this fills the entire surface
        tela.blit(s, (0,0))
        alpha_over += 1
        if alpha_over > 200:
            alpha_over = 200
        desenhaTexto("Game over",tela,tamanho_tela[0]/2-135,tamanho_tela[1]/2-100)

def desenhaTexto(texto, tela,xpos,ypos):
    pygame.font.init()
    font = pygame.font.Font(caminho_fonte, 40)
    scoreStr = font.render(texto, True, (255, 255, 255))
    tela.blit(scoreStr,(xpos,ypos))

def desenhaScore(score, tela):
    pygame.font.init()
    font = pygame.font.Font(caminho_fonte, 20)
    scoreStr = font.render(str(score), True, (255, 255, 255))
    tela.blit(scoreStr,(tamanho_tela[0]/2,tamanho_tela[1] -30))

def restart():
    global chefes
    global inimigos
    global buffs
    global naves
    global nave
    global pontos
    global alpha_over
    global tempo
    global cenarios

    chefes.clear()
    naves.clear()
    inimigos.clear()
    buffs.clear()
    cenarios.clear()

    AdicionaNave((tamanho_tela[0]/2 )- 100,(tamanho_tela[1]/2)-50,100,64,nave_sprite,[],1,500,500,0)
    nave = naves[0]   
    pontos = 0
    alpha_over = 0
    tempo = pygame.time.get_ticks()

    qtd_cenarios = 14

    for index in range(qtd_cenarios):
        col = index%4
        linha = index//4
        
        corte = (col*1024,linha*512,1024,512)
        img = backgroundImg2.subsurface(corte).convert_alpha()
        objImg = [img,0,0]
        cenarios.append(objImg)

cenario_width = cenarios[0][0].get_width()
    

def jogo():
    jogando = True
    global pontos
    pontos = 0
    # print(pygame.font.get_fonts())
    AdicionaNave((tamanho_tela[0]/2 )- 100,(tamanho_tela[1]/2)-50,100,64,nave_sprite,[],1,500,500,0)
    global nave
    nave = naves[0]
    print(len(nave_sprite))
    pygame.mouse.set_visible(0)
    while jogando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogando = False
                pygame.quit()
        
        key_event = pygame.key.get_pressed()

        if key_event[pygame.K_INSERT]:
            # jogando = False
            restart()
            # break

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
        
        desenhaScore(pontos,tela)

        RemoveElementosTamanhoTela(inimigos,tamanho_tela)
        RemoveElementosTamanhoTela(nave[5],tamanho_tela)

        RemoveElementosColisao(inimigos,nave,'inimigos','nave')
        RemoveElementosColisao(chefes,nave,'chefes','nave')

        buffColisao(buffs,nave)

        MovimentoNave(nave,tamanho_tela)
        verificaVida(naves,nave)

        desenhaBarraVida(nave[7],nave[8],nave[9])
        
        TiroNave(nave,tempo)

        SpawnInimigo(tamanho_tela,sprites_squid,velocidade+2)
        SpawnChefe(tamanho_tela,boss_sprite,velocidade+2)
        SpawnBuff(tamanho_tela,buff_sprite)

        FogoBoss(chefes,tiro_sprite)
        FogoInimigo(inimigos,tiro_sprite)

        DesenhaParticulas()
        drawParticlesPlayer(nave,velocidade)

        setTheta()
        setTheta_BOSS()

        estabilizaNave(nave)
        #desenhando nave
        # pygame.draw.rect(tela,nave[4],(nave[0],nave[1],nave[2],nave[3]))  
        tela.blit(nave[4][math.ceil(nave[10])],(nave[0],nave[1]))
        
        for tiro in nave[5]:
            tiro[0] += (tiro[5][0] * 10)
            tiro[1] += (tiro[5][1] * 10)
            pygame.draw.rect(tela,tiro[4],(tiro[0],tiro[1],tiro[2],tiro[3]))

        #desenhando inimigos na tela
        for inimigo in inimigos:
            MovimentoInimigo(inimigo,velocidade)
            inimigo[6] += 0.1
            tela.blit(inimigo[5][math.ceil(inimigo[6])],(inimigo[0],inimigo[1]-20))
            RemoveElementosTamanhoTela(inimigo[10],tamanho_tela)
            RemoveElementosColisao(inimigo[10],nave,'fire_inimigo','nave')
            RemoveElementosColisao(nave[5],inimigo,'fire_nave','inimigo')
            if inimigo[12] <= 0:
                inimigo[13] = False
                inimigos.remove(inimigo)
                pontos += 10
            if inimigo[6] > 7:
                inimigo[6] = 0
            for tiro in inimigo[10]:
                tiro[0] += (tiro[5][0] * 7)
                tiro[1] += (tiro[5][1] * 7)
                tiro[7] += 0.3
                if tiro[7] > 6:
                    tiro[7] = 0
                adicionaAnimacaoTiro(tiro,(inimigo[0]-20,inimigo[1]),tempo)
                pygame.draw.rect(tela,tiro[4],(tiro[0],tiro[1],tiro[2],tiro[3]))
                
        #desenhando chefes na tela
        for chefe in chefes:
            MovimentoBoss(chefe, tamanho_tela,velocidade)
            RemoveElementosColisao(nave[5],chefe,'fire_nave','chefe')
            RemoveElementosColisao(chefe[9],nave,'fire_chefe','nave')
            RemoveElementosTamanhoTela(chefe[9],tamanho_tela)
            # pygame.draw.rect(tela,chefe[5],(chefe[0],chefe[1],chefe[2],chefe[3]))
            chefe[15] += 0.25
            if chefe[15] > 8:
                chefe[15] = 0
            if chefe[13] <= 0:
                chefe[14] = False
                chefes.remove(chefe)
                pontos += 100
            for tiro in chefe[9]:
                tiro[0] += (tiro[5][0] * 10)
                tiro[1] += (tiro[5][1] * 10)
                pygame.draw.rect(tela,tiro[4],(tiro[0],tiro[1],tiro[2],tiro[3])) 
                pygame.draw.rect(tela,(255,255,255),(tiro[0],tiro[1],tiro[2],tiro[3]),1) 
            tela.blit(chefe[5][math.ceil(chefe[15])],(chefe[0],chefe[1]-20))
   
        for buff in buffs:
            MovimentoBuff(buff)
            tela.blit(buff[5][math.ceil(buff[7])],(buff[0],buff[1]))
            buff[7] += 0.25
            if buff[7] > 11:
                buff[7] = 0
            # pygame.draw.rect(tela,buff[5],(buff[0],buff[1],buff[2],buff[3]))

        desenhaGameOver(nave)

        pygame.display.update()
        
        relogio.tick(fps)
 
jogo()