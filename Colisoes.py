
from Particulas import *

def RemoveElementosTamanhoTela(lista,tamanho_tela):
    for el in lista:
        if el[0] >= tamanho_tela[0] or el[0] <= 0:
            lista.remove(el)
        elif el[1] >= tamanho_tela[1] or el[1] <= 0:
            lista.remove(el)

def RemoveElementosColisao(lista,elemento,removerA,removerB):
    for i in range(len(lista)):
        el_lista = lista[i]
        el = elemento
        d = ( (el_lista[0] - elemento[0])**2 + (el_lista[1] - elemento[1])**2 )**0.5
        if d <= el_lista[2]/2 + elemento[2]/2:
            AdicionaParticulas(el_lista[0],el_lista[1])
            if removerA :
                el_lista[0] = -30
                el_lista[1] = -30
            if removerB:
                elemento[0] = -30
                elemento[1] = -30

def RemoveElementoColisao(elementoA,elementoB,removerA,removerB):
    d = ( (elementoA[0] - elementoB[0])**2 + (elementoA[1] - elementoB[1])**2 )**0.5
    if d <= elementoA[2]/2 + elementoB[2]/2:
        AdicionaParticulas(elementoA[0],elementoA[1])
        if removerA :
            elementoA[0] = -30
            elementoA[1] = -30
        if removerB:
            elementoB[0] = -30
            elementoB[1] = -30