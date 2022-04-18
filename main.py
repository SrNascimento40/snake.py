import random
import pygame
from pygame.locals import *
from sys import exit


def on_grid_randon():
    #geração da posição das maçãs em lugares que a cobra passa
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return (x // 10 * 10, y // 10 * 10)


def collision(c1, c2):
    #colisão
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

def reiniciar_jogo():
    global snake,snake_skin, morreu, apple_pos, apple, pts, my_direction
    snake = [(200, 200), (210, 200), (220, 200)]
    snake_skin = pygame.Surface((10, 10))
    snake_skin.fill((255, 255, 255))
    morreu = False
    apple_pos = on_grid_randon()
    apple = pygame.Surface((10, 10))
    apple.fill((255, 0, 0))
    pts = 0
    my_direction = LEFT



print("\nhello world\n")
pygame.init()
screen = pygame.display.set_mode((600, 600))
# set_mode é para receber uma tela, os (()) existem pois esta funcção recebe uma tupla, tamanho por pixel
pygame.display.set_caption('Snake')
# acima é dado o nome do jogo, que vai ficar no topo da tela

musica = pygame.mixer.music.load('flautinha.wav')
pygame.mixer.music.play(-1)
#só a música de fundo pode ser mp3
colisom = pygame.mixer.Sound('go.wav')
colisom.set_volume(0.08)

moreu = pygame.mixer.Sound('moreu.wav')
moreu.set_volume(0.08)

UP = 0
RIGHT = 1
LEFT = 2
DOWN = 3
snake = [(200, 200), (210, 200), (220, 200)]
# matriz = de cima pra baixo da esquerda pra direita
# (m, n)
# m linha = 210
# n coluna = 200
# cobra foi movida para direita
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))

morreu = False

apple_pos = on_grid_randon()
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))

fonte = pygame.font.SysFont('arial', 20, True, True)
fonte2 = pygame.font.SysFont('arial', 20, True, True)
pts = 0
my_direction = LEFT

clock = pygame.time.Clock()

while True:
    # todo jogo fica dentro de um loop
    clock.tick(20)
    mensagem = f'PTS:   {pts}'
    txt_formated = fonte.render(mensagem, False, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if event.type == KEYDOWN:
        if event.key == K_UP:
            my_direction = UP
        if event.key == K_DOWN:
            my_direction = DOWN
        if event.key == K_LEFT:
            my_direction = LEFT
        if event.key == K_RIGHT:
            my_direction = RIGHT

    if collision(snake[0], apple_pos):
        #colisão
        apple_pos = on_grid_randon()
        snake.append((0, 0))
        pts += 1
        colisom.play()

    if snake.count(snake[0]) > 1 or 0 in snake[0] or 600 in snake[0]:
        morreu = True
        moreu.play()
        while morreu:
            screen.fill((235, 235, 235))
            faleceu = f"E MORREU! PRESS f TO PLAY AGAIN"
            txt_morte= fonte2.render(faleceu, True, (0, 0, 0))
            retexto = txt_morte.get_rect()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_f:
                        reiniciar_jogo()

            retexto.center = (300, 300)
            screen.blit(txt_morte, retexto)
            pygame.display.update()

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    screen.fill((0, 250, 0))
    screen.blit(apple, apple_pos)
    for pos in snake:
        screen.blit(snake_skin, pos)

    screen.blit(txt_formated, (450, 40))
    pygame.display.update()



# TAREFA
# criar sistema de colisão com a parede e consigo mesmo
