# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pygame
import random

WIDTH = 360  # ширина игрового окна
HEIGHT = 480 # высота игрового окна
FPS = 60 # частота кадров в секунду
# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("123")
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speedx = 0
        self.speedy = 0

    def update(self):
        # self.rect.x += 5
        # self.rect.y += 10
        # if self.rect.left > WIDTH:
        #     self.rect.right = 0
        if self.rect.bottom > HEIGHT:
            self.rect.top = 0
            self.rect.right = 0
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        if keystate[pygame.K_UP]:
            self.speedy = -8
        if keystate[pygame.K_DOWN]:
            self.speedy = 8
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
running = True


while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Обновление
    all_sprites.update()

    # Отрисовка
    screen.fill(BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()
    # Ввод процесса (события)
    # Обновление
    # Визуализация (сборка)

    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.W:
        #     player.rect.y -= 10
        # if event.type == pygame.KEYDOWN:
        #     player.rect.y += 10
        # if event.type == pygame.K_LEFT:
        #     player.rect.x += 5
        # if event.type == pygame.K_RIGHT:
        #     player.rect.x -= 5


pygame.quit()
