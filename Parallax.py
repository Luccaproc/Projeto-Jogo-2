import pygame
import os

backgroundImg = pygame.image.load(os.path.join("assets","cenario.png")).convert_alpha()

cenarios = []

qtd_cenarios = 13

altura_img = 512
largura_img = 1024

for i in range(qtd_cenarios):
    
    col = i % 4
    linha = i //4

    corte = backgroundImg.subsurface(i*largura_img,i*altura_img,1024,512)

    cenarios.append(corte)