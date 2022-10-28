import pygame

pygame.init()

fps = 60
tamanho_tela = (1024,512)
background = (0,0,0)

tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption('Synth Invaders')
relogio = pygame.time.Clock()

tempo = 0

nave = []
tiros_nave = []

def AdicionaTiro(xpos,ypos,largura,altura,cor,direcao):
    tiroX = xpos
    tiroY = ypos
    tiro_largura = largura
    tiro_altura = altura
    tiro_cor = cor
    tiro_direcao = direcao
    tiros_nave.append([tiroX,tiroY,tiro_largura,tiro_altura,tiro_cor,tiro_direcao])

def AdicionaNave(xpos,ypos,largura,altura,cor):
    naveX = xpos + 3
    naveY = ypos + 3
    nave_largura = largura
    nave_altura = altura
    nave_cor = cor
    nave.append([naveX,naveY,nave_largura,nave_altura,nave_cor])

def MovimentoNave(nave):
    velocidade = 5
    
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT]: # We can check if a key is pressed like this
        if(nave[0] >= 0):
            nave[0] = nave[0] - velocidade
        else:
            nave[0] = nave[0]
    if keys[pygame.K_RIGHT]:
        if nave[0] <= tamanho_tela[0] - nave[2]:
            nave[0] = nave[0] + velocidade
        else: 
            nave[0] = tamanho_tela[0] - nave[2]
    if keys[pygame.K_UP]:
        if nave[1] >= 0:
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
        AdicionaTiro(nave[0],nave[1],5,5,(255,255,255),[1,0])
   

def jogo():
    jogando = True
    pontos = 0

    AdicionaNave(tamanho_tela[0]/2,tamanho_tela[1]/2,50,25,(255,255,255))

    pygame.mouse.set_visible(0)
    while jogando:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogando = False
                pygame.quit()

        
        tela.fill((70,70,70))     
        MovimentoNave(nave[0])
        TiroNave(nave[0],tempo)

        for nav in nave:
            pygame.draw.rect(tela,nav[4],(nav[0],nav[1],nav[2],nav[3]))

        for tiro in tiros_nave:
            tiro[0] += (tiro[5][0] * 10)
            tiro[1] += (tiro[5][1] * 10)
            pygame.draw.rect(tela,tiro[4],(tiro[0],tiro[1],tiro[2],tiro[3]))
               
            
        
        pygame.display.update()
        
        relogio.tick(fps)

jogo()