import pygame, sys
from random import choice
from pygame.locals import QUIT, KEYUP, K_ESCAPE, KEYDOWN

'''
# nao funciona
def check_guess(guess):
    if guess == 'a':
        guess = ['a','ã','á','à','â','ä','å','æ','ª']
    elif guess == 'c':
        guess = ['c','ç','ć','č']
    elif guess == 'o':
        guess =  ['o','ò','ô','õ','ó','º','ō','ø','œ','ö']
    elif guess == 'e':
        guess = ['e','è','ê','é','ē','ę','ė','ë']
    elif guess == 'i':
        guess = ['i','ì','î','í','ī','ï','į']
    elif guess == 'u':
        guess = ['u','ú','û','ù','ū','ù','û']
    return guess
'''


pygame.init()

# cores
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#fonte do jogo
font_size = 36
font = pygame.font.Font(None, font_size)

# criando tela
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Jogo da Forca')

# tempo
clock = pygame.time.Clock()

palavra_secreta = ['caracol','espingarda','escola',
'cama','banheiro','celular','parede','cachorro',
'lixo','galinha','ventilador','helicóptero','foguete',
'caderno','teclado','casaco','computador','mulher',
'macaco','zebra','banana','bola','boneco','hospital','escova','boneco','estrela','cometa','carroça','tubarão','televisão',
'abominação','calça','índio','lençol','lápis','pé','ventilação','botão',
'papel','cabeça','xícara','maçã']


used_letters = []
escolhe_palavras = choice(palavra_secreta).lower()

contador_letras_erradas = 0
incorrect_letters = []

palavra_escolhida = escolhe_palavras
hidden_word = ["_"] * len(palavra_escolhida)

running = True
vidas = 6


while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # <ESC> para sair do jogo
        elif event.type == KEYUP:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == KEYDOWN:
            if event.unicode.isalpha():
                guess = event.unicode.lower()

                # verifica se o chute está na palavra
                if guess in palavra_escolhida:
                    for i in range(len(palavra_escolhida)):
                        if palavra_escolhida[i] == guess:
                                hidden_word[i] = guess
                else:
                    contador_letras_erradas += 1
                    incorrect_letters.append(guess)
                    vidas-=1
                used_letters.append(guess)

    # fundo da tela
    screen.fill(BLACK)
    # desenha a forca
    pygame.draw.line(screen, WHITE, [60, 300], [60, 198], 5) #coluna
    pygame.draw.line(screen, WHITE, [60, 200], [120, 200],5) #linha 
    pygame.draw.line(screen, WHITE, [120,198], [120, 210], 2) #gancho
    if vidas < 6:
        pygame.draw.circle(screen, WHITE, [120, 220], 10, 3) #cabeca
        if vidas < 5:
            pygame.draw.line(screen, WHITE, [120, 230], [120, 265], 3) #corpo
            if vidas < 4:
                pygame.draw.line(screen, WHITE, [120, 230], [100, 260], 3) #braco esq
                if vidas < 3:
                    pygame.draw.line(screen, WHITE, [120, 230], [140, 260], 3) #braco dir
                    if vidas < 2:
                        pygame.draw.line(screen, WHITE, [120, 265], [130, 285], 3) #perna dir
                        if vidas < 1:
                            pygame.draw.line(screen, WHITE, [120, 265], [110, 285], 3) #perna esq
  
    # Transforma a palavra escolhida em traços↓
    text_hw = font.render(" ".join(hidden_word), True, WHITE)
    width_hw = (screen_width - text_hw.get_width()) / 4
    height_hw = screen_height - font_size - 80
    screen.blit(text_hw, (width_hw, height_hw))

    # mostra as letras usadas
    text_print_ul = font.render(f"Palavras usadas:", True, WHITE)
    text_ul = font.render(f"{used_letters}", True, WHITE)
    width_ul = 380
    height_ul = 50
    height_txt_ul = 75
    screen.blit(text_print_ul, (width_ul, height_ul))
    screen.blit(text_ul, (width_ul, height_txt_ul))

    # conta quantas tentativas erradas
    text_incorrect_guess = font.render(f"Chutes errados: {contador_letras_erradas}", True, WHITE)
    width_le = 380
    height_le = 200
    screen.blit(text_incorrect_guess, (width_le, height_le))

    # mostra as letras erradas
    text_incorrect_letters = font.render(f"{incorrect_letters}", True, WHITE)
    width_txt_il = 380
    height_txt_il = 240
    screen.blit(text_incorrect_letters, (width_txt_il, height_txt_il))

    # observacao para o jogador
    text_obs = font.render("OBS: Caracteres Especiais devem ser digitados", True, BLUE)
    screen.blit(text_obs, (30, 450))

    # verifica se ganhou ou nao
    if "".join(hidden_word) == palavra_escolhida:
        result_text = font.render("VOCÊ VENCEU!", True, GREEN)
        result_width = (screen_width - result_text.get_width()) / 2
        result_height = 240
        screen.fill(BLACK)
        screen.blit(result_text, (result_width, result_height))
        running = False
    elif vidas == 0:
        result_text = font.render(f"VOCÊ PERDEU! Palavra: {palavra_escolhida}", True, RED)
        result_width = (screen_width - result_text.get_width()) / 10
        result_height = 240
        screen.fill(BLACK)
        screen.blit(result_text, (result_width, result_height))
        running = False


    pygame.display.update()
    clock.tick(2)

  