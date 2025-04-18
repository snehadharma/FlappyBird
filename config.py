import pygame
import components

win_width = 720
win_height = 550

window = pygame.display.set_mode((720, 550))

ground = components.Ground(720)

pipes = []
