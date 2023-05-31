import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

COMPRIMENTOJANELA = 450
ALTURAJANELA = 450

branco = (255, 255, 255)
preto = (0,0,0)

tela = pygame.display.set_mode((COMPRIMENTOJANELA, ALTURAJANELA))

tamanho_das_imagens = (60,60) 
fundo = pygame.image.load(r'imagens\fundo.png')
equis = pygame.image.load(r'imagens\x.png')
bola = pygame.image.load(r'imagens\circulo.png')
fundo = pygame.transform.scale(fundo, tamanho_das_imagens)
equis = pygame.transform.scale(equis, tamanho_das_imagens)
bola = pygame.transform.scale(bola, tamanho_das_imagens)
font = pygame.font.Font('freesansbold.ttf', 32)

def game():

    jogada=1

    while ganhou() == 0:
        exibe(jogada)
        mouse = pygame.mouse.get_pos()
        x = 0
        y = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                jogada +=1
                if(mouse[0] > cord_x[0] and mouse[1] > cord_y[0] and mouse[0] < cord_x[1] and mouse[1] < cord_y[1] ):
                    x=0
                    y=0
                elif(mouse[0] > cord_x[1] and mouse[1] > cord_y[0] and mouse[0] < cord_x[2] and mouse[1] < cord_y[1] ):
                    x=0
                    y=1
                elif(mouse[0] > cord_x[2] and mouse[1] > cord_y[0] and mouse[0] < cord_x[0]+ 200 and mouse[1] < cord_y[1] ):
                    x=0
                    y=2
                elif(mouse[0] > cord_x[0] and mouse[1] > cord_y[1] and mouse[0] < cord_x[1] and mouse[1] < cord_y[2] ):
                    x=1
                    y=0
                elif(mouse[0] > cord_x[1] and mouse[1] > cord_y[1] and mouse[0] < cord_x[2] and mouse[1] < cord_y[2] ):
                    x=1
                    y=1
                elif(mouse[0] > cord_x[2] and mouse[1] > cord_y[1] and mouse[0] < cord_x[0]+ 200 and mouse[1] < cord_y[2] ):
                    x=1
                    y=2
                elif(mouse[0] > cord_x[0] and mouse[1] > cord_y[2] and mouse[0] < cord_x[1] and mouse[1] < cord_y[0]+200 ):
                    x=2
                    y=0
                elif(mouse[0] > cord_x[1] and mouse[1] > cord_y[2] and mouse[0] < cord_x[2] and mouse[1] < cord_y[0] +200):
                    x=2
                    y=1
                elif(mouse[0] > cord_x[2] and mouse[1] > cord_y[2] and mouse[0] < cord_x[0]+ 200 and mouse[1] < cord_y[0] +200 ):
                    x=2
                    y=2
            

                if board[x][y] == 0:
                    if(jogada%2+1)==1:
                        board[x][y]=1
                    else:
                        board[x][y]=-1
                else:
                    print("Nao esta vazio")
                    jogada -=1

            exibe(jogada)
        pygame.display.update()
               
numero_controle=1
def ganhou():
    #checando linhas
    for i in range(3):
        soma = board[i][0]+board[i][1]+board[i][2]
        if soma==3 or soma ==-3:
            return 1

    #checando colunas
    for i in range(3):
        soma = board[0][i]+board[1][i]+board[2][i]
        if soma==3 or soma ==-3:
            return 1

    #checando diagonais
    diagonal1 = board[0][0]+board[1][1]+board[2][2]
    diagonal2 = board[0][2]+board[1][1]+board[2][0]
    if diagonal1==3 or diagonal1==-3 or diagonal2==3 or diagonal2==-3:
        return 1

    return 0

def exibe(jogada):

    #divisas
    pygame.draw.rect(tela, branco, Rect([120, 160], [200, 5]), 15)#x,y
    pygame.draw.rect(tela, branco, Rect([180, 100], [5, 200]), 15)
    pygame.draw.rect(tela, branco, Rect([120, 230], [200, 5]), 15)
    pygame.draw.rect(tela, branco, Rect([250, 100], [5, 200]), 15)
   
        
    

    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                tela.blit(fundo,(cord_x[j],cord_y[i]))
            elif board[i][j] == 1:
                tela.blit(equis,(cord_x[j],cord_y[i]))
            elif board[i][j] == -1:
                tela.blit(bola,(cord_x[j],cord_y[i]))
                
    if ganhou():
        print("Jogador ",jogada%2 + 1," ganhou apos ", jogada-1," rodadas")

        font = pygame.font.Font(None, 36)
        text = font.render("Jogador "+str(jogada%2 + 1)+" ganhou após "+ str(jogada-1)+" rodadas", 1, branco)
        textpos = text.get_rect()
        textpos.left = 25
        textpos.top = 30
        tela.blit(text, textpos)
        
        # text = font.render("Jogador ",jogada%2 + 1," ganhou apos ", jogada-1," rodadas", True, branco)
        # tela.blit(text, (120,60))
        
#Fundo
cord_x = [120,187,257]
cord_y = [100,167,237]

board= [[0,0,0],
        [0,0,0],
        [0,0,0] ]


while True:
    pygame.display.set_caption('Jogo_da_velha')

    tela.fill(preto)
    
    game()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    