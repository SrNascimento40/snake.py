# sprites = imagens que se movem
# pra animar sprite, é só exibir uma sequencia de imagens
# piskel permite criar sprites

import pygame
from pygame.locals import *
from sys import exit


pygame.init()


class Sapo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/attack_1.png'))
        self.sprites.append(pygame.image.load('sprites/attack_2.png'))
        self.sprites.append(pygame.image.load('sprites/attack_3.png'))
        self.sprites.append(pygame.image.load('sprites/attack_4.png'))
        self.sprites.append(pygame.image.load('sprites/attack_5.png'))
        self.sprites.append(pygame.image.load('sprites/attack_8.png'))
        self.sprites.append(pygame.image.load('sprites/attack_6.png'))
        self.sprites.append(pygame.image.load('sprites/attack_7.png'))
        self.sprites.append(pygame.image.load('sprites/attack_9.png'))
        self.sprites.append(pygame.image.load('sprites/attack_10.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (128*5, 64*5))

        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100
        self.animar = False

    def atacar(self):
        self.animar = True
    def update(self):
        if self.animar == True:
            self.atual += 0.5
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (128 * 5, 64 * 5))


all_sprites = pygame.sprite.Group()
sapo = Sapo()
all_sprites.add(sapo)

largura = 600
altura = 500
nego = (0, 0, 0)
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Sprites")

relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill(nego)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            sapo.atacar()

    all_sprites.draw(tela)
    all_sprites.update()
    pygame.display.flip()
