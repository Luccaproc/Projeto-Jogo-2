
from random import randint
import pygame

particulas = []

def AdicionaParticulas(xpos,ypos):
    for i in range(0,20):
        radius = randint(4,30)
        direction_x = randint(-2,2)
        direction_y = randint(-2,2)
        particle_circle = [[xpos,ypos],radius,[direction_x,direction_y]]
        particulas.append(particle_circle)

def DeletaParticulas():
    global particulas
    particulas_copia = [particle for particle in particulas if particle[1] > 0]
    particulas = particulas_copia

def DesenhaParticulas():
    if particulas:
        DeletaParticulas()
        for particle in particulas:
            particle[0][0] += particle[2][0]
            particle[0][1] += particle[2][1]
            particle[1] -= 0.5
            pygame.draw.circle(pygame.display.get_surface(),(255,255,255),[int(particle[0][0]),int(particle[0][1])],int(particle[1]))