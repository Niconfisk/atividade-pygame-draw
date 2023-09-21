import pygame
from pygame.locals import *
import sys

pygame.init()

larg, altu = 800, 600
screen = pygame.display.set_mode((larg, altu), 0, 32)

branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
azul = (65, 105, 225)
tam = 50
squares = []
rectangles = []
circles = []

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit
            exit()
        keys = pygame.key.get_pressed()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if keys[pygame.K_r]:
                rectangles.append(event.pos)
            elif keys[pygame.K_c]:
                circles.append(event.pos)
            else:
                squares.append(event.pos)

        screen.fill(branco)

        for s in squares:
            pygame.draw.rect(screen, preto, (s[0], s[1], tam, tam))
        for r in rectangles:
            pygame.draw.rect(screen, azul, (r[0], r[1], tam * 2, tam))
        for c in circles:
            pygame.draw.circle(screen, vermelho, c, tam)
        pygame.display.update()
