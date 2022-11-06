
import math


cooldown_tiro = 0
cooldown_tiro_inimigo = 0

def AdicionaTiroNave(xpos,ypos,largura,altura,cor,direcao,cooldown,tiros_list,qtd_poder):
    global cooldown_tiro
    global cooldown_tiro_inimigo
    
    anguloStep = 90//(qtd_poder+1)

    anguloAtual = 45 - anguloStep

    cooldown_maximo = cooldown
    if cooldown_tiro > cooldown_maximo:
        for bullet in range(qtd_poder):

            sen = math.sin((anguloAtual * math.pi)/180)*1
            cos = math.cos((anguloAtual * math.pi)/180)*1

            tiroX = xpos
            tiroY = ypos
           
            tiro_largura = largura
            tiro_altura = altura
            tiro_cor = cor
            tiro_direcao = [direcao[0] + cos,direcao[1] + sen]

            tiros_list.append([tiroX,tiroY,tiro_largura,tiro_altura,tiro_cor,tiro_direcao])

            anguloAtual -= math.ceil(anguloStep)

        cooldown_tiro = 0
    else:
        cooldown_tiro += 1

def RemoveTiros(list_tiros,tamanho_tela):
    for tiro in list_tiros:
        if tiro[0] >= tamanho_tela[0] or tiro[0] <= 0:
            list_tiros.remove(tiro)
        elif tiro[1] >= tamanho_tela[1] or tiro[1] <= 0:
            list_tiros.remove(tiro)

def AdicionaTiroInimigo(xpos,ypos,largura,altura,cor,direcao,cooldown,cool_down_start,tiros_list):

    tiroX = xpos
    tiroY = ypos
    tiro_largura = largura
    tiro_altura = altura
    tiro_cor = cor
    tiro_direcao = direcao
    tiros_list.append([tiroX,tiroY,tiro_largura,tiro_altura,tiro_cor,tiro_direcao])
        
def AdicionaTiroBoss(xpos,ypos,largura,altura,cor,direcao,cooldown,cool_down_start,tiros_list):

    tiroX = xpos
    tiroY = ypos
    tiro_largura = largura
    tiro_altura = altura
    tiro_cor = cor
    tiro_direcao = direcao
    tiros_list.append([tiroX,tiroY,tiro_largura,tiro_altura,tiro_cor,tiro_direcao])
 