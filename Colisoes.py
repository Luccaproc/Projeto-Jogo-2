from Particulas import *

mostrar_colisor = False

def colisaoRetangulo(el1,el2):
    if el1[0] < el2[0] + el2[2] and el1[0] + el1[2] > el2[0] and el1[1] < el2[1] + el2[3] and el1[3] + el1[1] > el2[1] :
        return True
    else :
        return False

def colisaoCirculos(el1,el2):
    d = ( (el1[0] - el2[0])**2 + (el1[1] - el2[1])**2 )**0.5
    if d <= el1[2]/2 + el2[2]/2:
        return True
    else:
        return False

def RemoveElementosTamanhoTela(lista,tamanho_tela):
    lista_nova = lista
    for el in lista_nova:
        if mostrar_colisor:
            pygame.draw.rect(pygame.display.get_surface(),(30,255,30),(el[0],el[1],el[2],el[3]),1)
        if el[0] >= tamanho_tela[0] or el[0] <= 0:
            lista_nova.remove(el)
        elif el[1] >= tamanho_tela[1] or el[1] <= 0:
            lista_nova.remove(el)
    


def RemoveElementosColisao(lista,elemento,tipo_lista,tipo_elemento):
    lista_nova = lista
    for el in lista_nova:
        if mostrar_colisor:
            pygame.draw.rect(pygame.display.get_surface(),(30,255,30),(el[0],el[1],el[2],el[3]),1)
            pygame.draw.rect(pygame.display.get_surface(),(30,255,30),(elemento[0],elemento[1],elemento[2],elemento[3]),1)
        if colisaoRetangulo(el,elemento):
            AdicionaParticulas(el[0],el[1])
            lista_nova.remove(el)       
            if tipo_elemento == 'nave' and tipo_lista == 'fire_inimigo':
                elemento[7] -= 10
            if tipo_elemento == 'nave' and tipo_lista == 'inimigos':
                elemento[7] -= 50
            if tipo_elemento == 'nave' and tipo_lista == 'fire_chefe':
                elemento[7] -= 10
            if tipo_elemento == 'nave' and tipo_lista == 'chefes':
                elemento[7] -= 100
            if tipo_elemento == 'inimigo' and tipo_lista == 'fire_nave':
                elemento[12] -= 10
            if tipo_elemento == 'inimigo' and tipo_lista == 'nave':
                elemento[12] -= 100
            if tipo_elemento == 'chefe' and tipo_lista == 'fire_nave':
                elemento[13] -= 10
                print(elemento[13])
            if tipo_elemento == 'chefe' and tipo_lista == 'nave':
                elemento[13] -= 100

# def RemoveElementoColisao(elementoA,elementoB,removerA,removerB):
#     d = ( (elementoA[0] - elementoB[0])**2 + (elementoA[1] - elementoB[1])**2 )**0.5
    # pygame.draw.circle(pygame.display.get_surface(),(30,255,30),(elementoA[0],elementoA[1]),5,1)
#     if d <= elementoA[2]/2 + elementoB[2]/2:
#         AdicionaParticulas(elementoA[0],elementoA[1])
#         if removerA :
#             elementoA[0] = -30
#             elementoA[1] = -30
#         if removerB:
#             elementoB[0] = -30
#             elementoB[1] = -30
            
# def ColisaoBalasNaveInimigo(lista,elemento):
#     for i in range(len(lista)):
        
#         el_lista = lista[i]
        
#         d = ( (el_lista[0] - elemento[0])**2 + (el_lista[1] - elemento[1])**2 )**0.5
#         if d <= el_lista[2]/2 + elemento[2]/2:
#             elemento[12] -= 10
#             if elemento[12] <= 0:
#                 AdicionaParticulas(elemento[0],elemento[1])
#                 elemento[0] = -800
#                 elemento[1] = -800
#             el_lista[0] = -800
#             el_lista[1] = -800

            
# def ColisaoBalasInimigoNave(lista,elemento):
#     for i in range(len(lista)):
        
#         el_lista = lista[i]
        
#         d = ( (el_lista[0] - elemento[0])**2 + (el_lista[1] - elemento[1])**2 )**0.5
        # pygame.draw.circle(pygame.display.get_surface(),(30,255,30),(el_lista[0],el_lista[1]),el_lista[2],1)
#         if d <= el_lista[2]/2 + elemento[2]/2:
#             elemento[7] -= 10
#             print(elemento[7])
#             if elemento[7] <= 0:
#                 AdicionaParticulas(elemento[0],elemento[1])
#                 elemento[0] = -800
#                 elemento[1] = -800
#             lista_del_fire_enemy.append(i)