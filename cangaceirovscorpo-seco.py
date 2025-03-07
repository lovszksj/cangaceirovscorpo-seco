#FEITO POR JULLYANA AZEVEDO E JOÃO VICTOR GOMES

import pygame
from mapas import labirinto 

pygame.init()

#IMAGENS
parede_img = pygame.image.load("parede.jpg")
caminho_img = pygame.image.load("chao.jpg")
armadilha_img = pygame.image.load("armadilha.png")
jogador_img = pygame.image.load("jogador.png")
inimigo_img = pygame.image.load("inimigo.png")

#REDIMENSIONAMOS AS IMAGENS
tamanho_bloco = 20
tamanho_parede = tamanho_bloco *2
parede_img = pygame.transform.scale(parede_img, (tamanho_parede, tamanho_parede))
caminho_img = pygame.transform.scale(caminho_img, (tamanho_bloco, tamanho_bloco))
armadilha_img = pygame.transform.scale(armadilha_img, (tamanho_bloco, tamanho_bloco))
jogador_img = pygame.transform.scale(jogador_img, (tamanho_bloco, tamanho_bloco))
inimigo_img = pygame.transform.scale(inimigo_img, (tamanho_bloco, tamanho_bloco))

#TELA
LARGURA, ALTURA = 1260, 800  
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Cangaceiro vs papangu")
FPS = 15
 
#DIMENSÕES JOGADOR
jogador_x = 150
jogador_y = 150
jogador_altura = 50
jogador_largura = 50

#DIMENSÕES INIMIGO
inimigo_x = 150
inimigo_y = 150
inimigo_altura = 50
inimigo_largura = 50

#DIMENSÃO ARMADILHA
armadilha_x = -1
armadilha_y = -1
tempoParalisado = 0
cooldown = 2000 #2000ms = 2 segundos
paralisado = False

#LOCALIZAÇÃO INICIAL
jogador_x, jogador_y = 1, 2
inimigo_x, inimigo_y = 49, 1
relogio = pygame.time.Clock()

rodando = True

while rodando:

    for linha in range(len(labirinto)):
        for coluna in range(len(labirinto[linha])):
            x = coluna * tamanho_bloco  #CALCULA A POSIÇÃO X
            y = linha * tamanho_bloco   #CALCULA A POSIÇÃO Y

            if labirinto[linha][coluna] == "T":  #CONSTRUÇÃO DA PAREDE
                tela.blit(parede_img, (x, y))
            elif labirinto[linha][coluna] == "O":  #CONSTRUÇÃO DO CAMINHO
                tela.blit(caminho_img, (x, y))
            elif labirinto[linha][coluna] == "A":  #CONSTRUÇÃO DA ARMADILHA
                tela.blit(armadilha_img, (x, y))  

    #DESENHO DOS PERSONAGENS
    tela.blit(jogador_img,(jogador_x*tamanho_bloco, jogador_y*tamanho_bloco))
    tela.blit(inimigo_img,(inimigo_x*tamanho_bloco, inimigo_y*tamanho_bloco))

    #CONDIÇÕES PARA FECHAR O JOGO
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        for dx in range(-2, 3):
            for dy in range(-2, 3):
                if inimigo_x + dx == jogador_x and inimigo_y + dy == jogador_y:
                    rodando = False
                    print("Ah não, você foi pego!")
                    break

    #TECLAS 
    teclas = pygame.key.get_pressed()
    nova_x_jogador, nova_y_jogador = jogador_x, jogador_y

    if teclas[pygame.K_a]:
        nova_x_jogador = jogador_x - 1
    if teclas[pygame.K_d]:
        nova_x_jogador = jogador_x + 1
    if teclas[pygame.K_w]:
        nova_y_jogador = jogador_y - 1
    if teclas[pygame.K_s]:
        nova_y_jogador = jogador_y + 1

    teclas_inimigo = pygame.key.get_pressed()
    nova_x_inimigo, nova_y_inimigo = inimigo_x, inimigo_y 

    if paralisado == False:
        if teclas_inimigo[pygame.K_LEFT]:
            nova_x_inimigo -= 1
        if teclas_inimigo[pygame.K_RIGHT]:
            nova_x_inimigo += 1
        if teclas_inimigo[pygame.K_UP]:
            nova_y_inimigo -= 1
        if teclas_inimigo[pygame.K_DOWN]:
            nova_y_inimigo += 1
    

    #DESENHAR A ARMADILHA (SE EXISTIR)
    desenhar_armadilha = False
    if teclas[pygame.K_SPACE] and not desenhar_armadilha:
        desenhar_armadilha = True
        labirinto[jogador_y][jogador_x] = "A"
        armadilha_x, armadilha_y = jogador_x, jogador_y

    #COLISÃO DO INIMIGO
    if (inimigo_x == armadilha_x and inimigo_y == armadilha_y) and not paralisado:
        paralisado = True
        tempoParalisado = pygame.time.get_ticks()

    #VERIFICAÇÃO DO TEMPO PARALISADO
    if paralisado:
        tempoAtual = pygame.time.get_ticks()
        if tempoAtual - tempoParalisado >= cooldown:
            paralisado = False
            labirinto[armadilha_y][armadilha_x] = 'O'
            armadilha_x, armadilha_y = -1, -1
            desenhar_armadilha = False
            
    #VERIFICAÇÃO DE CAMINHO
    if labirinto[nova_y_jogador][nova_x_jogador] != 'T' :  
        jogador_x, jogador_y = nova_x_jogador, nova_y_jogador

        #VERIFICA SE O JOGADOR SAIU DO LABIRINTO
        if nova_x_jogador < 0 or nova_y_jogador >= 40 or nova_y_jogador < 0 or nova_y_jogador >= 37:
            print("Você encontrou a saída! Parabéns!")
            rodando = False  

    if labirinto[nova_y_inimigo][nova_x_inimigo] != 'T':  
        inimigo_x, inimigo_y = nova_x_inimigo, nova_y_inimigo

    pygame.display.flip()
    relogio.tick(FPS)

pygame.quit()
